from mock import patch, ANY

from svc.constants.garage_state import GarageState
from svc.controllers.door_status_controller import create_status_app


@patch('svc.controllers.door_status_controller.create_thread')
def test_create_status_app__should_create_first_thread_when_doesnt_exist(mock_thread):
    create_status_app()
    door_one_state = GarageState.get_instance().DOORS['1']

    mock_thread.assert_called_with(door_one_state, ANY)


@patch('svc.controllers.door_status_controller.create_thread')
def test_create_status_app__should_not_create_first_thread_when_already_exists(mock_thread):
    create_status_app()
    GarageState.get_instance().DOORS['1'] = {}

    mock_thread.assert_not_called()
