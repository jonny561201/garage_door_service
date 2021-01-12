from datetime import datetime

import pytz

from svc.constants.garage_state import GarageState
from svc.constants.home_automation import Automation
from svc.utlities.gpio_utils import is_garage_open


def monitor_status():
    state = GarageState.get_instance()
    first_status = is_garage_open('1')
    second_status = is_garage_open('2')

    __update_door_status(state.DOORS.get('1'), first_status)
    __update_door_status(state.DOORS.get('2'), second_status)


def __update_door_status(door, status):
    if status and door.OPEN_TIME is None:
        door.STATUS = Automation.GARAGE.OPEN
        door.OPEN_TIME = datetime.now(pytz.utc)
        door.CLOSED_TIME = None
    if not status and door.CLOSED_TIME is None:
        door.STATUS = Automation.GARAGE.CLOSED
        door.CLOSED_TIME = datetime.now(pytz.utc)
        door.OPEN_TIME = None
