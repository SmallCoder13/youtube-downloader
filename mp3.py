from time import sleep
from selenium import webdriver
from tkinter import simpledialog
from selenium.webdriver.common.by import By

class Youtube_To_Mp3:

    def __init__(self):

        users_url = simpledialog.askstring(title="Youtube URL", prompt="Please enter the youtube video you want to download below:")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://ytmp3.nu/hfJ2/")

        url_input = driver.find_element(By.ID, value="url")
        url_input.send_keys(users_url)
        url_input.submit()

        print("sleeping for 20 seconds")
        sleep(20)
        print("done sleeping")

        download_button = driver.find_element(by=By.LINK_TEXT, value="Download")
        download_button.click()

        driver.switch_to.new_window('tab')

        driver.get("http://127.0.0.1:3000/youtube-downloader/index.html")