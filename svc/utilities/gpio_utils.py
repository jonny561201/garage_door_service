# import RPi.GPIO as GPIO

FIRST_GARAGE_STATUS_PIN = 11
SECOND_GARAGE_STATUS_PIN = 12


# GPIO.cleanup()
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(FIRST_GARAGE_STATUS_PIN, GPIO.IN, GPIO.PUD_UP)
# GPIO.setup(SECOND_GARAGE_STATUS_PIN, GPIO.IN, GPIO.PUD_UP)


# assumes connection to output pin and ground with GPIO.PUD_UP
def is_garage_open(garage_id):
    return True
    # status_pin = FIRST_GARAGE_STATUS_PIN if garage_id == '1' else SECOND_GARAGE_STATUS_PIN
    # status = GPIO.input(status_pin)
    # return True if status == 1 else False