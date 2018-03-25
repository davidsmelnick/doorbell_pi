import RPi.GPIO as GPIO
import time
import makeDestinations
import sendEmail

destinations = makeDestinations.f()
server = sendEmail.login()


GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def handle(pin):
    emailAddress = '921WinonaDoorbell@gmail.com'
    msg = 'Someone at the door!!'
    if pin == 17:
        floor = '1'
    elif pin == 23:
        floor = '2'
    else:
        floor = 'unassigned'
            
##    server.sendmail(emailAddress,destinations[floor],msg)
    print('sending text to ' + floor)
    
GPIO.add_event_detect(17, GPIO.FALLING, handle, bouncetime=300)
GPIO.add_event_detect(23, GPIO.FALLING, handle, bouncetime=300)
GPIO.add_event_detect(24, GPIO.FALLING, handle, bouncetime=300)
GPIO.add_event_detect(25, GPIO.FALLING, handle, bouncetime=300)

while True:
    time.sleep(1e6)