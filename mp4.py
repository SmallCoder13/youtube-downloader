import subprocess
from time import sleep
from selenium import webdriver
from tkinter import messagebox
from tkinter import simpledialog
from selenium.webdriver.common.by import By

class Youtube_To_Mp4:
    def __init__(self):
        users_url = simpledialog.askstring(title="Youtube URL", prompt="Please enter the youtube video you want to download below:")

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(name="detach", value=True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://wave.video/convert/youtube-to-mp4-65")

        url_input = driver.find_element(By.CLASS_NAME, value="sc-8b4b6g-0")
        url_input.send_keys(users_url)

        print("sleeping for 5 seconds")
        sleep(5)
        print("done sleeping")

        decline_cookies = driver.find_element(by=By.CLASS_NAME, value="t-acceptAllButton")
        decline_cookies.click()

        print("sleeping for 10 seconds")
        sleep(10)
        print("done sleeping")

        start_button = driver.find_element(by=By.CLASS_NAME, value="dkrhAU")
        start_button.click()

        driver.switch_to.new_window('tab')

        driver.get("http://127.0.0.1:3000/youtube-downloader/index.html")

        install = messagebox.askyesno(title="Install?", message="Do you want to install the needed codecs to play the downloaded video?")


        if install:
            from subprocess import call

            pwd = simpledialog.askstring(title="Password", prompt="What is your password?")
            cmd = 'apt install ubuntu-restricted-extras -y > ~/decoder_output.txt'  # install ubuntu-restricted-extras

            status = call('echo {} | sudo -S {}'.format(pwd, cmd), shell=True)

            message = "WARNING: apt does not have a stable CLI interface. Use with caution in scripts."

            if status == 0:

                messagebox.showinfo(title="OK?",
                                    message="It looks like the needed decoders are installed. However, please open the text file named 'decoder_output.txt' in your home folder to be sure")
            else:
                messagebox.showerror(title="Oh No!", message=f"An error ocurrer while install the needed decoders. \n\nThe error is: {subprocess.getoutput(cmd).replace(message, '')}")

        else:
            messagebox.showinfo(title="", message="OK. Goodbye")
