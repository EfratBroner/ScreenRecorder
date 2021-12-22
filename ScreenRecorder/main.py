import cv2
import numpy as np
import os
import pyautogui
import webbrowser
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def make_video(index):
    output = "videoThursday19" + ".mp4"
    img = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    # get info from img
    height, width, channels = img.shape
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))
    acts = ActionChains(driver)

    for i in range(5*6*60):
        try:
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            StopIteration(0.5)
        except KeyboardInterrupt:
            break

    print("finished")
    out.release()
    cv2.destroyAllWindows()


driver = webdriver.Firefox(executable_path='C:/Users/sbroner/Downloads/geckodriver-v0.29.0-win64/geckodriver.exe')
driver.get("https://www.iroads.co.il/%D7%AA%D7%99%D7%A7%D7%99%D7%99%D7%AA-%D7%9E%D7%A6%D7%9C%D7%9E%D7%95%D7%AA/")

li = driver.find_elements_by_class_name("searchInput")
inputElement = li[1]
print(li)
inputElement.send_keys('ברנר')
time.sleep(5)
camera = driver.find_element_by_class_name("imgWrap").click()
time.sleep(5)
videoCamera = driver.find_element_by_id("iRoadsPlayer467-347")
videoCamera.send_keys("F")


for i in range(1):
    make_video(str(i))
