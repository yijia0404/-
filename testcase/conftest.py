import os
import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def delete_cache():
    os.system("rm -rf /Users/yijia/PycharmProjects/pythonProject3/screenshot/*")
    os.system("rm -rf /Users/yijia/PycharmProjects/pythonProject3/report/*")
    os.system("rm -rf /Users/yijia/PycharmProjects/pythonProject3/alluretemp/*")
    allure.attach(body="这是一段文本,setUp", name="test文本01", attachment_type=allure.attachment_type.TEXT)


@pytest.fixture(scope="function", autouse=True)
def visit_baidu():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome = webdriver.Chrome(executable_path="/Users/yijia/Downloads/chromedriver", options=chrome_options)
    chrome.maximize_window()
    chrome.get("https://www.baidu.com")
    yield chrome
    chrome.quit()
