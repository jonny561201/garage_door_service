import logging

from svc.constants.garage_state import GarageState
from svc.controllers.door_status_controller import create_status_app

logging.basicConfig(filename='sumpPump.log', level=logging.DEBUG)

try:
    logging.info('Application started!')
    create_status_app()
except KeyboardInterrupt:
    state = GarageState.get_instance()
    state.terminate_all_threads()
    logging.error('Application interrupted by user')
