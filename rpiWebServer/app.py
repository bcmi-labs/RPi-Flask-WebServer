'''
    Portenta-X8 GPIO Status and Control
'''
#import RPi.GPIO as GPIO
import gpio as GPIO
from flask import Flask, render_template, request

app = Flask(__name__)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)

#define sensors GPIOs
button1 = 163
button2 = 164

#define actuators GPIOs
gpio0 = 160
gpio1 = 161
gpio2 = 162

#initialize GPIO status variables
button1Sts = 0
button2Sts = 0
gpio0Sts = 0
gpio1Sts = 0
gpio2Sts = 0

# Define button1 and button2 pins as an input
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

# Define gpio pins as output
GPIO.setup(gpio0, GPIO.OUT)
GPIO.setup(gpio1, GPIO.OUT)
GPIO.setup(gpio2, GPIO.OUT)

# turn gpios OFF
GPIO.output(gpio0, GPIO.LOW)
GPIO.output(gpio1, GPIO.LOW)
GPIO.output(gpio2, GPIO.LOW)

@app.route("/")
def index():
    # Read GPIO Status
    button1Sts = GPIO.input(button1)
    button2Sts = GPIO.input(button2)
    gpio0Sts = GPIO.input(gpio0)
    gpio1Sts = GPIO.input(gpio1)
    gpio2Sts = GPIO.input(gpio2)

    templateData = {
        'button1' : button1Sts,
        'button2' : button2Sts,
        'gpio0'   : gpio0Sts,
        'gpio1'   : gpio1Sts,
        'gpio2'   : gpio2Sts,
    }
    return render_template('index.html', **templateData)

# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'gpio0':
        actuator = gpio0
    if deviceName == 'gpio1':
        actuator = gpio1
    if deviceName == 'gpio2':
        actuator = gpio2

    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    button1Sts = GPIO.input(button1)
    button2Sts = GPIO.input(button2)
    gpio0Sts = GPIO.input(gpio0)
    gpio1Sts = GPIO.input(gpio1)
    gpio2Sts = GPIO.input(gpio2)

    templateData = {
        'button1' : button1Sts,
        'button2' : button2Sts,
        'gpio0'   : gpio0Sts,
        'gpio1'   : gpio1Sts,
        'gpio2'   : gpio2Sts,
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
