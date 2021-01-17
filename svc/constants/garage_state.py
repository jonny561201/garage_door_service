class DoorState:
    CLOSED_TIME = None
    OPEN_TIME = None
    STATUS = None


class GarageState:
    __instance = None
    ACTIVE_THREAD = None
    DOORS = {'1': DoorState(),
             '2': DoorState()}

    def __init__(self):
        if GarageState.__instance is not None:
            raise Exception
        else:
            GarageState.__instance = self

    def terminate_thread(self):
        self.ACTIVE_THREAD.stopped.set()

    @staticmethod
    def get_instance():
        if GarageState.__instance is None:
            GarageState.__instance = GarageState()
        return GarageState.__instance
