from twilio.rest import Client
from selenium import webdriver
from time import sleep, ctime
from random import randint
import cryptography
import datetime

def notification(Twilio_SID, Auth_Token, msg, twilioPhone, phone):
    account_sid = Twilio_SID
    auth_token = Auth_Token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=msg,
                        from_='+' + twilioPhone,
                        to='+' + phone
                    )

def main(username, password):
    # # Go to FYPJ 2.0 Website
    # driver = webdriver.Chrome()
    # driver.get('https://fypj.sit.nyp.edu.sg/')
    # driver.implicitly_wait(10)

    # # Enter Username
    # driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[2]/input').send_keys(username)
    # # Enter Password
    # driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[3]/input').send_keys(password)
    # driver.find_element('xpath','/html/body/div/div/div/div/div[2]/form/fieldset/div[6]/input[2]').click()

    # # Click on Student Dropdown Button
    # driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/a').click()
    # # Click on Sign In/Out
    # driver.find_element('xpath', '/html/body/form/div[3]/nav/div/div[2]/ul[1]/li[1]/ul/li[1]/a').click()

    # # Check In/Out of the system
    # driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[5]/div/div/div[4]/div[3]/input').click()
    # # Confirmation
    # driver.find_element('xpath', '/html/body/form/div[3]/div[2]/div[8]/div/div/div[3]/button').click()

    # Check In Notificaton
    if datetime.time(8,24,0) <= datetime.datetime.now().time() <= datetime.time(8,30,59):
        notification("You have Successfully Checked Into the FYPJ System at " + ctime())
    elif datetime.time(5,59,59) <= datetime.datetime.now().time() <= datetime.time(6,6,0):
        notification("You have Successfully Checked Out of the FYPJ System at " + ctime())

    # return driver
    return 'pog'

if __name__ == '__main__':


    
        


    # Emulate human's randomness (Up to 4mins)
    # sleep(randint(1,240))
    # try:
    #     driver = main()
    # except:
    #     notification("You have Failed to Check In/Out of the FYPJ System at " + ctime())
        
