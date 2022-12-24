import time

import allure
import pytest_check

from page.homePage import HomePage
from locator.homePageLocator import HomePageLocator


def test_run(visit_baidu):
    HomePage(visit_baidu).click_baidu_logo()
    HomePage(visit_baidu).switch_to_new_window()
    actual_result = HomePage(visit_baidu).get_attribute_from_element(HomePageLocator().input_filed, "value")
    if not pytest_check.equal(actual_result, "百度", "搜索框内的单词不是百度"):
        screenshot_ap = "".join([HomePage.screenshot_path, str(int(time.time())), ".png"])
        HomePage(visit_baidu).get_screenshot(screenshot_ap)
        allure.attach(open(screenshot_ap, "rb").read(), "搜索框内的单词不是百度",
                      attachment_type=allure.attachment_type.PNG)
    HomePage(visit_baidu).switch_to_original_window()


@allure.suite("xxxxx")
class Test1:
    def test_run1(self, visit_baidu):
        HomePage(visit_baidu).click_baidu_logo()
        HomePage(visit_baidu).switch_to_new_window()
        actual_result = HomePage(visit_baidu).get_attribute_from_element(HomePageLocator().input_filed, "value")
        if not pytest_check.equal(actual_result, "百度", "搜索框内的单词不是百度"):
            screenshot_ap = "".join([HomePage.screenshot_path, str(int(time.time())), ".png"])
            HomePage(visit_baidu).get_screenshot(screenshot_ap)
            allure.attach(open(screenshot_ap, "rb").read(), "搜索框内的单词不是百度",
                          attachment_type=allure.attachment_type.PNG)
        HomePage(visit_baidu).switch_to_original_window()

    def test_run2(self, visit_baidu):
        HomePage(visit_baidu).send_keys_to_input_filed("asdfasdfasdf")
