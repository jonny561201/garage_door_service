from mock import patch, ANY

from svc.constants.garage_state import GarageState
from svc.controllers.door_status_controller import create_status_app
from svc.services.door_status import monitor_status


@patch('svc.controllers.door_status_controller.create_thread')
def test_create_status_app__should_create_first_thread_when_doesnt_exist(mock_thread):
    state = GarageState.get_instance()
    state.ACTIVE_THREAD = None
    create_status_app()

    mock_thread.assert_called_with(state, monitor_status)


@patch('svc.controllers.door_status_controller.create_thread')
def test_create_status_app__should_not_create_first_thread_when_already_exists(mock_thread):
    GarageState.get_instance().ACTIVE_THREAD = {}
    create_status_app()

    mock_thread.assert_not_called()
