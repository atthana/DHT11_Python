import RPi.GPIO as GPIO
import dht11
import time
import datetime
import smtplib

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()


Atthana = 'atthana.p@scale360solutions.com'
Q_hotmail = 'q_electronics@hotmail.com'
Yoh = 'ekkachai.n@scale360solutiions.com'
Oh =  'kanokwan.n@scale360solutions.com'
Nut = 'nutcha.c@scale360solutions.com'
Uli = 'ulrich@scale360solutions.com'
Sabari = 'sabarimanoj.t@scale360solutions.com'
Nat = 'natthapong.i@scale360solutions.com'

#list_mails = [Atthana, Q_hotmail, Uli, Nut, Yoh, Oh, Sabari]
list_mails = [Atthana, Q_hotmail, Nat]

instance = dht11.DHT11(40)
subject = '''Send room temperature from sensor in Q's table'''

def temperature_print():
    print("Last valid input: " + str(datetime.datetime.now()))
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    return  f'''
        Last valid input:  + {str(datetime.datetime.now())}
        Temperature: {result.temperature} C
        Humidity: {result.humidity} %
    '''

msg = 'This email was sent automatically by Python script krub'
#msg = temperature_print()


def send_email(mailto, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        
        sender_email = 'atthana.p@scale360solutions.com'
        sender_password = 'diebold123456'
        
        server.login(sender_email, sender_password)
        
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(sender_email, mailto, message)
        
        server.quit()
        print('Success: Email sent')
    except:
        print('Email failed to send.')



while True:
    result = instance.read()
    if result.is_valid():
        temperature_print()
        msg2 = temperature_print() 
        send_email(list_mails, subject, msg2)

    time.sleep(3)
    
