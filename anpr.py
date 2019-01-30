from openalpr import Alpr
from picamera import PiCamera
from time import sleep
import pushover

# Pushover settings
PUSHOVER_USER_KEY = "<REPLACE WITH USER KEY>"
PUSHOVER_APP_TOKEN = "<REPLACE WITH APP TOKEN>"

# 'gb' means we want to recognise UK plates, many others are available
alpr = Alpr("gb", "/etc/openalpr/openalpr.conf",
            "/usr/share/openalpr/runtime_data")
camera = PiCamera()
pushover.init(PUSHOVER_APP_TOKEN)
last_seen = None

try:
    # Let's loop forever:
    while True:

        # Take a photo
        print('Taking a photo')
        camera.capture('/home/pi/latest.jpg')

        # Ask OpenALPR what it thinks
        analysis = alpr.recognize_file("/home/pi/latest.jpg")

        # If no results, no car!
        if len(analysis['results']) == 0:
            print('No number plate detected')

            # Has a car left?
            if last_seen is not None:
                pushover.Client(PUSHOVER_USER_KEY).send_message(
                    last_seen + " left",
                    title="Driveway")

            last_seen = None

        else:
            number_plate = analysis['results'][0]['plate']
            print('Number plate detected: ' + number_plate)

            # Has there been a change?
            if last_seen is None:
                pushover.Client(PUSHOVER_USER_KEY).send_message(
                    number_plate + " has arrived", title="Driveway")
            elif number_plate != last_seen:
                pushover.Client(PUSHOVER_USER_KEY).send_message(
                    number_plate + " arrived  and " + last_seen + " left",
                    title="Driveway")

            last_seen = number_plate

        # Wait for five seconds
        sleep(5)

except KeyboardInterrupt:
    print('Shutting down')
    alpr.unload()
