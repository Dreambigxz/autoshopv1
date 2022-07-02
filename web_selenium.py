from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

browser = webdriver.Firefox(executable_path="geckodriver-v0.31.0-linux32/geckodriver")
