class DoorState:
    ACTIVE_THREAD = None
    STOP_EVENT = None
    CLOSED_TIME = None
    OPEN_TIME = None
    STATUS = None


class GarageState:
    __instance = None
    DOORS = {'1': DoorState(),
             '2': DoorState()}

    def __init__(self):
        if GarageState.__instance is not None:
            raise Exception
        else:
            GarageState.__instance = self

    def terminate_all_threads(self):
        for key, door in self.DOORS.items():
            door.STOP_EVENT.set()

    @staticmethod
    def get_instance():
        if GarageState.__instance is None:
            GarageState.__instance = GarageState()
        return GarageState.__instance
