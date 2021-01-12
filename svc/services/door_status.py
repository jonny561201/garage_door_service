from datetime import datetime

import pytz

from svc.constants.garage_state import GarageState
from svc.constants.home_automation import Automation
from svc.utlities.gpio_utils import is_garage_open
from svc.utlities.file_utils import write_status_to_file


def monitor_status():
    state = GarageState.get_instance()
    first_open = is_garage_open('1')
    second_open = is_garage_open('2')

    __update_door_status(state.DOORS.get('1'), first_open, '1')
    __update_door_status(state.DOORS.get('2'), second_open, '2')


def __update_door_status(door_state, is_open, door_num):
    now = datetime.now(pytz.utc)
    if is_open and door_state.OPEN_TIME is None:
        door_state.STATUS = Automation.GARAGE.OPEN
        door_state.OPEN_TIME = now
        door_state.CLOSED_TIME = None
        write_status_to_file(door_num, now)
    if not is_open and door_state.CLOSED_TIME is None:
        door_state.STATUS = Automation.GARAGE.CLOSED
        door_state.CLOSED_TIME = now
        door_state.OPEN_TIME = None
        write_status_to_file(door_num, now)
