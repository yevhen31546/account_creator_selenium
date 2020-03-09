from selenium import webdriver
import time
import random
import names
import string
import datetime
import csv

# Catch the forms
first_name_form = '//*[@id="create-account"]/label[1]/div/input'
last_name_form = '//*[@id="create-account"]/label[2]/div/input'
email_form = '//*[@id="create-account"]/label[3]/div/input'
password_form = '//*[@id="create-account"]/div[2]/div/label/div/input'
signup_button = '//*[@id="create-account"]/button'

# random names and email address
length = 4
delay = 3
temp = 2
site_url = 'https://shop.nordstrom.com/'
signup_path = 'https://secure.nordstrom.com/signup?origin=tab&ReturnURL=https%3A%2F%2Fshop.nordstrom.com%2F'
lower_letters = string.ascii_lowercase
uppercase_digit = string.ascii_uppercase + string.digits
lowercase = ''.join(random.choice(lower_letters) for _ in range(length))
chars = ''.join(random.choice(uppercase_digit) for _ in range(length))
domainList = ["bgrknyc.com", "srfcavity.com"]
randomDomain = random.choice(domainList)

accounts = []
header = []
header.append('firstName')
header.append('lastName')
header.append('emailAddress')
header.append('password')
accounts.append(header)

times = int(input("Enter Number of Loops: "))
for i in range(times):
    firstName = names.get_first_name()
    lastName = names.get_first_name()
    emailAddress = lastName + chars + '@' + randomDomain
    password = ''.join(random.choice(uppercase_digit) for _ in range(10)) + lowercase

    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.get(site_url)
    driver.refresh()
    time.sleep(temp)
    driver.get(signup_path)
    time.sleep(delay)
    driver.find_element_by_xpath(first_name_form).send_keys(firstName)
    time.sleep(temp)
    driver.find_element_by_xpath(last_name_form).send_keys(lastName)
    time.sleep(temp)
    driver.find_element_by_xpath(email_form).send_keys(emailAddress)
    time.sleep(temp)
    driver.find_element_by_xpath(password_form).send_keys(password)
    time.sleep(delay)
    driver.find_element_by_xpath(signup_button).click()
    time.sleep(delay)

    account = []
    account.append(firstName)
    account.append(lastName)
    account.append(emailAddress)
    account.append(password)
    accounts.append(account)
    time.sleep(delay)

print('Done!!!')

currentDT = datetime.datetime.now()
filename = 'accounts_' + str(currentDT.microsecond) + '.csv'
with open(filename, "w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(accounts)
