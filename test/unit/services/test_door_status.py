from datetime import datetime, timedelta

import pytz
from mock import patch

from svc.constants.garage_state import GarageState
from svc.constants.home_automation import Automation
from svc.services.door_status import monitor_status


@patch('svc.services.door_status.datetime')
@patch('svc.services.door_status.is_garage_open')
class TestGarageService:

    DOOR_ONE = '1'
    DOOR_TWO = '2'
    DATE = datetime.now(pytz.utc)
    STATE = GarageState.get_instance()

    def setup_method(self):
        self.STATE.DOORS[self.DOOR_ONE].CLOSED_TIME = None
        self.STATE.DOORS[self.DOOR_ONE].OPEN_TIME = None
        self.STATE.DOORS[self.DOOR_ONE].STATUS = None
        self.STATE.DOORS[self.DOOR_TWO].CLOSED_TIME = None
        self.STATE.DOORS[self.DOOR_TWO].OPEN_TIME = None
        self.STATE.DOORS[self.DOOR_TWO].STATUS = None

    def test_monitor_status__should_call_is_garage_open_for_first_door(self, mock_status, mock_date):
        monitor_status()

        mock_status.assert_any_call(self.DOOR_ONE)

    def test_monitor_status__should_set_status_to_open_when_garage_open_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = True

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].STATUS == Automation.GARAGE.OPEN

    def test_monitor_status__should_set_open_time_when_garage_open_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = True
        mock_date.now.return_value = self.DATE

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].OPEN_TIME == self.DATE

    def test_monitor_status__should_set_status_to_closed_when_garage_door_closed_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = False

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].STATUS == Automation.GARAGE.CLOSED

    def test_monitor_status__should_set_closed_time_when_garage_closed_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = False
        mock_date.now.return_value = self.DATE

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].CLOSED_TIME == self.DATE

    def test_monitor_status__should_nullify_open_date_when_closed_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = False

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].OPEN_TIME is None

    def test_monitor_status__should_nullify_closed_date_when_opened_for_first_door(self, mock_status, mock_date):
        mock_status.return_value = True

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].CLOSED_TIME is None

    def test_monitor_status__should_not_reset_open_date_when_already_open_for_first_door(self, mock_status, mock_date):
        older_date = datetime.now() - timedelta(days=1)
        mock_status.return_value = True
        mock_date.now.return_value = self.DATE
        self.STATE.DOORS[self.DOOR_ONE].OPEN_TIME = older_date

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].OPEN_TIME == older_date

    def test_monitor_status__should_not_reset_closed_date_when_already_closed_for_first_door(self, mock_status, mock_date):
        older_date = datetime.now() - timedelta(days=1)
        mock_status.return_value = False
        mock_date.now.return_value = self.DATE
        self.STATE.DOORS[self.DOOR_ONE].CLOSED_TIME = older_date

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_ONE].CLOSED_TIME == older_date

    def test_monitor_status__should_call_is_garage_open_for_second_door(self, mock_status, mock_date):
        monitor_status()

        mock_status.assert_any_call(self.DOOR_TWO)

    def test_monitor_status__should_set_status_to_open_when_garage_open_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = True

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].STATUS == Automation.GARAGE.OPEN

    def test_monitor_status__should_set_open_time_when_garage_open_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = True
        mock_date.now.side_effect = [self.DATE, self.DATE]

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].OPEN_TIME == self.DATE

    def test_monitor_status__should_set_status_to_closed_when_garage_door_closed_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = False

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].STATUS == Automation.GARAGE.CLOSED

    def test_monitor_status__should_set_closed_time_when_garage_closed_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = False
        mock_date.now.return_value = self.DATE

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].CLOSED_TIME == self.DATE

    def test_monitor_status__should_nullify_open_date_when_closed_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = False

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].OPEN_TIME is None

    def test_monitor_status__should_nullify_closed_date_when_opened_for_second_door(self, mock_status, mock_date):
        mock_status.return_value = True

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].CLOSED_TIME is None

    def test_monitor_status__should_not_reset_open_date_when_already_open_for_second_door(self, mock_status, mock_date):
        older_date = datetime.now() - timedelta(days=1)
        mock_status.return_value = True
        mock_date.now.return_value = self.DATE
        self.STATE.DOORS[self.DOOR_TWO].OPEN_TIME = older_date

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].OPEN_TIME == older_date

    def test_monitor_status__should_not_reset_closed_date_when_already_closed_for_second_door(self, mock_status, mock_date):
        older_date = datetime.now() - timedelta(days=1)
        mock_status.return_value = False
        mock_date.now.return_value = self.DATE
        self.STATE.DOORS[self.DOOR_TWO].CLOSED_TIME = older_date

        monitor_status()

        assert self.STATE.DOORS[self.DOOR_TWO].CLOSED_TIME == older_date
