from threading import Event

import mock

from svc.constants.garage_state import GarageState
from svc.utilities.event_utils import MyThread


def test_terminate_thread__should_cancel_all_threads():
    mock_thread = mock.create_autospec(MyThread)
    mock_event = mock.create_autospec(Event)
    mock_thread.stopped = mock_event
    state = GarageState.get_instance()
    state.ACTIVE_THREAD = mock_thread
    state.terminate_thread()

    mock_thread.stopped.set.assert_called()
