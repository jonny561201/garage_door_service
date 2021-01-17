from svc.constants.garage_state import GarageState
from svc.services.door_status import monitor_status
from svc.utilities.event_utils import create_thread


def create_status_app():
    state = GarageState.get_instance()
    if state.ACTIVE_THREAD is None:
        state.ACTIVE_THREAD = create_thread(state, monitor_status)
        state.ACTIVE_THREAD.start()
