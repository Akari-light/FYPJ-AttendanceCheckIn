from cryptography.fernet import Fernet
from twilio.rest import Client
from selenium import webdriver
from time import sleep, ctime
from random import randint
from json import dumps, loads
from pathlib import Path
import cryptography, datetime, os

class SetUp:
    def __init__(self):
        self.file_path = Path(__file__)
        self.current_dir = self.file_path.parent.absolute()
        self.retriveCredentials()

    # Retrive user creds
    def retriveCredentials(self):
        reset_msg = "username     : username\npassword     : password\naccount_sid  : account_sid\nauth_token   : auth_token\ntwilio_phone : twilio_phone\nusr_phone    : usr_phone"
        self.credentials = {}
        with open(str(self.current_dir)+'\credentials.txt', 'r') as f:
            creds_list= f.read().split('\n')
            for i in creds_list:
                self.credentials[i.split(":")[0].strip(' ')] = i.split(":")[1].strip(' ')

        # Reset credentials.txt
        with open(str(self.current_dir)+'\credentials.txt', 'w') as f:
            f.write(reset_msg)
   
    def encryption(self):
        plaintext = dumps(self.credentials).encode('utf-8')
        key = Fernet.generate_key()

        self.token = Fernet(key)
        self.credentials = self.token.encrypt(plaintext)

    def getCredentials(self):
        plaintext = loads(self.token.decrypt(self.credentials).decode('utf-8'))
        return plaintext

class Attendance_System:
    def __init__(self, username, password, account_sid, auth_token, twilio_phone, usr_phone):
        self.username = username
        self.password = password
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_phone = twilio_phone
        self.usr_phone = usr_phone
    
    def notification(self, msg):
        Twilio_SID = self.account_sid
        Auth_Token = self.auth_token
        client = Client(Twilio_SID, Auth_Token)

        message = client.messages \
                        .create(
                            body = msg,
                            from_ = self.twilio_phone,
                            to = self.usr_phone
                        )

    def automation(self):
        # Go to FYPJ 2.0 Website
        driver = webdriver.Chrome()
        driver.get('https://fypj.sit.nyp.edu.sg/')
        driver.implicitly_wait(10)

        # Enter Username
        driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[2]/input').send_keys(self.username)
        # Enter Password
        driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[3]/input').send_keys(self.password)
        driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[6]/input[2]').click()

        # Click on Student Dropdown Button
        driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/a').click()
        # Click on Sign In/Out
        driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/ul/li[1]/a').click()

        '''
        # Check In/Out of the system
        driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[5]/div/div/div[4]/div[3]/input').click()
        # Confirmation
        driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[8]/div/div/div[3]/button').click()
        '''

        # Check In Notificaton
        if datetime.time(8,25,0) <= datetime.datetime.now().time() <= datetime.time(8,30,59):
            self.notification("You have Successfully Checked Into the FYPJ System at " + ctime())
        # Check Out Notificaton
        elif datetime.time(5,59,59) <= datetime.datetime.now().time() <= datetime.time(6,6,0):
            self.notification("You have Successfully Checked Out of the FYPJ System at " + ctime())
        
        # '''
        self.notification("Test Run - script is working as of " + ctime())
        # '''

        # return driver
        return driver


def debug():
    #Setup for script
    user_instance = SetUp()
    user_instance.encryption()
    credentials = user_instance.getCredentials()
    system_instance = Attendance_System(credentials["username"], credentials["password"],credentials["account_sid"],credentials["auth_token"],credentials["twilio_phone"],credentials["usr_phone"])

if __name__ == '__main__':
    #Setup for script
    user_instance = SetUp()
    user_instance.encryption()
    credentials = user_instance.getCredentials()
    system_instance = Attendance_System(credentials["username"], credentials["password"],credentials["account_sid"],credentials["auth_token"],credentials["twilio_phone"],credentials["usr_phone"])

    # '''
    while True:
        current_time = datetime.datetime.now()

        # Check if today is Monday - Friday
        if current_time.isoweekday() in range(1, 6):
            # Trigger Function at 8.20 am
            if datetime.time(8,20,0) <= datetime.datetime.now().time() <= datetime.time(8,30,59):
                # Emulate human's randomness (Up to 4mins)  
                sleep(randint(1,240))
                try:
                    driver = system_instance.automation() 
                except:
                    system_instance.notification("You have Failed to Check In of the FYPJ System at " + ctime())

                # sleep(21600)
            # Trigger Function at 6:00 pm
            elif datetime.time(18,0,0) <= datetime.datetime.now().time() <= datetime.time(6,6,0):
                # Emulate human's randomness (Up to 4mins)  
                sleep(randint(1,240))
                try:
                    driver = system_instance.automation() 
                except:
                    system_instance.notification("You have Failed to Check Out of the FYPJ System at " + ctime())

                # sleep(21600)
            # Stop the script for 5 mins
            else:
                sleep(300)     
        # Stop Running the code on Saturday and Sunday by pausing the code for 6 hours:
        else:
            sleep(21600)
            continue
    # '''