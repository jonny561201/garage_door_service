import logging

from svc.constants.garage_state import GarageState
from svc.controllers.door_status_controller import create_status_app

logging.basicConfig(filename='garageDoorStatus.log', level=logging.DEBUG)

try:
    logging.info('Application started!')
    create_status_app()
except KeyboardInterrupt:
    state = GarageState.get_instance()
    state.terminate_thread()
    logging.error('Application interrupted by user')
