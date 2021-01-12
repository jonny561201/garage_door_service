from svc.constants.garage_state import GarageState
from svc.services.door_status import monitor_status
from svc.utlities.event_utils import create_thread


def create_status_app():
    door_one_id = '1'
    door_one_state = GarageState.get_instance().DOORS[door_one_id]
    if door_one_state.ACTIVE_THREAD is None:
        create_thread(door_one_state, lambda: monitor_status(door_one_state, door_one_id))