import smtplib
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import clipboard

for i in range(10):
    opt=Options()
    opt.add_argument('--disable-blink-features=AutomationControlled')
    opt.add_argument('--start-maximized')

# Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1
    })
    driver = webdriver.Chrome(options=opt, executable_path=r"C:\Program Files (x86)\chromedriver.exe")

    driver.maximize_window()
    driver.get('https://meet.vdotok.com/?t=1654156110537')
    driver.implicitly_wait(5)

    name = driver.find_element(By.XPATH, "//input[@id='username']")
    name.send_keys("Nimra")
    btnclik = driver.find_element(By.XPATH , "//button[normalize-space()='Join room']")
    btnclik.click()

    time.sleep(3)
    copy_url = driver.find_element(By.XPATH, "//button[normalize-space()='Copy Room URL']")
    copy_url.click()
    time.sleep(4)

    new_URL = clipboard.paste()

    try:
        # Create your SMTP session
        smtp = smtplib.SMTP('smtp.gmail.com', 587)

        # Use TLS to add security
        smtp.starttls()

        # User Authentication
        smtp.login("nimranasir301@gmail.com", "bpcqslovwihohelm")

        # Defining The Message
        message = new_URL

        # Sending the Email
        smtp.sendmail("nimranasir301@gmail.com", "nimranasir254@gmail.com", message)

        # Terminating the session
        smtp.quit()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....", ex)

#New Browser open(Firefox)
    options = webdriver.FirefoxOptions()
    options.set_preference("media.navigator.permission.disabled", True)
    driver1 = webdriver.Firefox(options=options,executable_path=r"C:\Program Files (x86)\geckodriver.exe")
    driver1.get(new_URL)
    time.sleep(4)

    name1 = driver1.find_element(By.XPATH, "//input[@id='username']")
    name1.send_keys("Nimra1")
    time.sleep(1)
    btnclik1 = driver1.find_element(By.XPATH , "//button[normalize-space()='Join room']")
    btnclik1.click()
    time.sleep(5)

    chat1 = driver1.find_element(By.XPATH, "//img[@class='responseButtonImg AnalyticsReturnToChat']")
    chat1.click()
    entertext = driver1.find_element(By.XPATH, "//input[@placeholder='Type to reply..']")
    entertext.send_keys("hi")
    send = driver1.find_element(By.XPATH, "//div[@class='col-sm-8 rightSide']//div[2]//img[1]")
    send.click()
    for i in range(10):
        pyautogui.press("enter")
        pyautogui.press("h")
        pyautogui.press("i")

        pyautogui.press("enter")
        pyautogui.press("H")
        pyautogui.press("o")
        pyautogui.press("w")
        pyautogui.press(" ")
        pyautogui.press("a")
        pyautogui.press("r")
        pyautogui.press("e")
        pyautogui.press(" ")
        pyautogui.press("y")
        pyautogui.press("o")
        pyautogui.press("u")
        pyautogui.press("?")
        handles = driver.window_handles
        for i in handles:
            driver.switch_to.window(i)
            chat2 = driver.find_element(By.XPATH, "//img[@class='responseButtonImg AnalyticsReturnToChat']")
            chat2.click()

        entertext = driver.find_element(By.XPATH, "//input[@placeholder='Type to reply..']")
        entertext.send_keys("hi")
        send = driver.find_element(By.XPATH, "//div[@class='col-sm-8 rightSide']//div[2]//img[1]")
        send.click()

        returncal = driver.find_element(By.XPATH, "//div[@class='AnalyticsReturnToCall']")
        returncal.click()

for i in range(10):
        pyautogui.press("enter")
        pyautogui.press("h")
        pyautogui.press("i")

        pyautogui.press("enter")
        pyautogui.press("H")
        pyautogui.press("o")
        pyautogui.press("w")
        pyautogui.press(" ")
        pyautogui.press("a")
        pyautogui.press("r")
        pyautogui.press("e")
        pyautogui.press(" ")
        pyautogui.press("y")
        pyautogui.press("o")
        pyautogui.press("u")
        pyautogui.press("?")
        pyautogui.press("enter")
        time.sleep(20)
