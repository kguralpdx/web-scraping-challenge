from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "../../../../chromedriver_win32/chromedriver.exe'"}
    return Browser("chrome", **executable_path, headless=False)