from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os
import random as rd

chrome_driver_path = "C:/Selenium/chromedriver.exe"
URL = "https://tinder.com/"

driver = webdriver.Chrome(service=Service(chrome_driver_path))
driver.get(URL)
driver.maximize_window()
time.sleep(1)

# open login page

log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()

# click login to facebook
time.sleep(1.5)

fb_login_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Login with Facebook']")

fb_login_button.click()

# switching windows
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)
print(driver.title)  # verify we are on the facebook window
time.sleep(3)

# allow cookies
allow_e_cookies_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Only allow essential cookies')]")
allow_e_cookies_button.click()

# find the login and password field
email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")

# enter login details

fb_login = os.environ["fb_login"]
fb_password = os.environ["fb_password"]

email_field.send_keys(fb_login)
password_field.send_keys(fb_password)

# hit enter
password_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(5)
allow_location = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Allow']")
allow_location.click()

time.sleep(3)
disallow_notifications = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Not interested']")
disallow_notifications.click()

time.sleep(1)
allow_cookies = driver.find_element(By.CSS_SELECTOR, "button[data-testid='privacyPreferencesAccept']")
allow_cookies.click()

time.sleep(1)

swipe_right = driver.find_element(By.CSS_SELECTOR, "button[data-testid='gamepadLike']")
swipe_left = driver.find_element(By.CSS_SELECTOR, "button[data-testid='gamepadDislike']")

for _ in range(10):
    random_sleep_time = rd.uniform(2.5, 3.5)
    time.sleep(random_sleep_time)

    try:
        swipe_left.click()

    except ElementClickInterceptedException:  # if something pops up
        try:  # if it's a match that pops up, this should deal with it
            # the line below to be updated after I see a match
            match_popup = driver.find_element(By.LINK_TEXT, "BACK TO TINDER")
            match_popup.click()
        except NoSuchElementException:  # if not
            try:  # it might be "would you like to add tinder to your home screen
                not_interested = driver.find_element(By.CSS_SELECTOR, "button[data-testid='cancel']")
                not_interested.click()
            except NoSuchElementException:
                time.sleep(2)
