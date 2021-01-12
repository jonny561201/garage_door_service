from threading import Event

import mock

from svc.constants.garage_state import GarageState


def test_terminate_thread__should_cancel_all_threads():
    test_event = mock.create_autospec(Event)
    state = GarageState.get_instance()
    state.STOP_EVENT = test_event
    state.terminate_thread()

    test_event.set.assert_called()
