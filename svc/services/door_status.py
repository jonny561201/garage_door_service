from datetime import datetime

import pytz

from svc.constants.garage_state import GarageState
from svc.constants.home_automation import Automation
from svc.utlities.gpio_utils import is_garage_open


def monitor_status():
    state = GarageState.get_instance()
    first_status = is_garage_open('1')
    second_status = is_garage_open('2')

    first_door = state.DOORS.get('1')
    second_door = state.DOORS.get('2')
    if first_status and first_door.OPEN_TIME is None:
        first_door.STATUS = Automation.GARAGE.OPEN
        first_door.OPEN_TIME = datetime.now(pytz.utc)
        first_door.CLOSED_TIME = None
    if not first_status and first_door.CLOSED_TIME is None:
        first_door.STATUS = Automation.GARAGE.CLOSED
        first_door.CLOSED_TIME = datetime.now(pytz.utc)
        first_door.OPEN_TIME = None
    if second_status and second_door.OPEN_TIME is None:
        second_door.STATUS = Automation.GARAGE.OPEN
        second_door.OPEN_TIME = datetime.now(pytz.utc)
        second_door.CLOSED_TIME = None
    if not second_status and second_door.CLOSED_TIME is None:
        second_door.STATUS = Automation.GARAGE.CLOSED
        second_door.CLOSED_TIME = datetime.now(pytz.utc)
        second_door.OPEN_TIME = None
