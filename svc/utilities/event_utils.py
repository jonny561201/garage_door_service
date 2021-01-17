from threading import Thread, Event

from svc.constants.home_automation import Automation


class MyThread(Thread):
    def __init__(self, event, sched_function, function_interval):
        Thread.__init__(self)
        self.stopped = event
        self.function = sched_function
        self.interval = function_interval

    def run(self):
        while not self.stopped.wait(self.interval):
            self.function()


# stop_event.set() will kill the process
def create_thread(fn, delay=Automation.TIMING.THIRTY_SECONDS):
    stop_event = Event()
    fn()
    return MyThread(stop_event, fn, delay)
