from threading import Event

import mock

from svc.constants.garage_state import GarageState


def test_terminate_all_threads__should_cancel_all_threads():
    test_event_one = mock.create_autospec(Event)
    test_event_two = mock.create_autospec(Event)
    state = GarageState.get_instance()
    state.DOORS.get('1').STOP_EVENT = test_event_one
    state.DOORS.get('2').STOP_EVENT = test_event_two
    state.terminate_all_threads()

    test_event_one.set.assert_called()
    test_event_two.set.assert_called()