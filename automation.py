from twilio.rest import Client
from selenium import webdriver
from time import sleep, ctime
from random import randint
from RSA_encryption import SetUp
import cryptography, datetime


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

        # Check In/Out of the system
        driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[5]/div/div/div[4]/div[3]/input').click()
        # Confirmation
        # driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[8]/div/div/div[3]/button').click()

        # Check In Notificaton
        if datetime.time(8,25,0) <= datetime.datetime.now().time() <= datetime.time(8,30,59):
            self.notification("You have Successfully Checked Into the FYPJ System at " + ctime())
        # Check Out Notificaton
        elif datetime.time(5,59,59) <= datetime.datetime.now().time() <= datetime.time(6,6,0):
            self.notification("You have Successfully Checked Out of the FYPJ System at " + ctime())
        
        # self.msg = "Test Run - script is working as of " + ctime()
        # self.notification()

        # return driver
        return driver


if __name__ == '__main__':
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
                    driver = Attendance_System().automation() 
                except:
                    Attendance_System.notification("You have Failed to Check In of the FYPJ System at " + ctime())

                sleep(21600)
            # Trigger Function at 6:00 pm
            elif datetime.time(18,0,0) <= datetime.datetime.now().time() <= datetime.time(6,6,0):
                # Emulate human's randomness (Up to 4mins)  
                sleep(randint(1,240))
                try:
                    driver = Attendance_System().automation() 
                except:
                    Attendance_System.notification("You have Failed to Check Out of the FYPJ System at " + ctime())

                sleep(21600)
            # Stop the script for 5 mins
            else:
                sleep(300)     
        # Stop Running the code on Saturday and Sunday by pausing the code for 6 hours:
        else:
            sleep(21600)
            continue

    # '''

