import time
import datetime
from threading import Thread
from mapadroid.utils.logging import logger


class Event(object):
    def __init__(self, args, dbwrapper):
        self.args = args
        self._dbwrapper = dbwrapper
        self._event_id: int = 1
        self._lure_duration: int = 30

    def event_checker(self):
        while True:
            self._event_id, self._lure_duration = self._dbwrapper.get_current_event()
            self._dbwrapper.set_event_id(self._event_id)
            self._dbwrapper.set_event_lure_duration(self._lure_duration)
            time.sleep(60)

    def start_event_checker(self):
        if not self.args.no_event_checker:
            t = Thread(target=self.event_checker, name='event_checker')
            t.daemon = True
            t.start()

    def get_current_event_id(self):
        return self._event_id

    def get_current_lure_duration(self):
        return self._lure_duration
