import time
import requests
import json

from threading import Thread
from metaflow.sidecar import MessageTypes, Message
from metaflow.metaflow_config import SERVICE_HEADERS
from metaflow.exception import MetaflowException

HB_URL_KEY = "hb_url"


class HeartBeatException(MetaflowException):
    headline = "Metaflow heart beat error"

    def __init__(self, msg):
        super(HeartBeatException, self).__init__(msg)


class MetadataHeartBeat(object):
    def __init__(self):
        self.headers = SERVICE_HEADERS
        self.req_thread = Thread(target=self._ping)
        self.req_thread.daemon = True
        self.default_frequency_secs = 10
        self.hb_url = None

    def process_message(self, msg):
        # type: (Message) -> None
        if msg.msg_type == MessageTypes.SHUTDOWN:
            self._shutdown()
        if not self.req_thread.is_alive():
            # set post url
            self.hb_url = msg.payload[HB_URL_KEY]
            # start thread
            self.req_thread.start()

    @classmethod
    def get_worker(cls):
        return cls

    def _ping(self):
        retry_counter = 0
        while True:
            try:
                frequency_secs = self._heartbeat()

                if frequency_secs is None or frequency_secs <= 0:
                    frequency_secs = self.default_frequency_secs

                time.sleep(frequency_secs)
                retry_counter = 0
            except HeartBeatException as e:
                retry_counter = retry_counter + 1
                time.sleep(4**retry_counter)

    def _heartbeat(self):
        if self.hb_url is not None:
            response = requests.post(url=self.hb_url, data="{}", headers=self.headers)
            # Unfortunately, response.json() returns a string that we need
            # to cast to json; however when the request encounters an error
            # the return type is a json blob :/
            if response.status_code == 200:
                return json.loads(response.json()).get("wait_time_in_seconds")
            else:
                raise HeartBeatException(
                    "HeartBeat request (%s) failed"
                    " (code %s): %s"
                    % (self.hb_url, response.status_code, response.text)
                )
        return None

    def _shutdown(self):
        # attempts sending one last heartbeat
        self._heartbeat()
