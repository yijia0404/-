from common.baseObject import BaseObject
from locator.homePageLocator import HomePageLocator
import allure


class HomePage(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)

    def click_baidu_logo(self):
        allure.step("点击百度logo")
        # allure.attach('', name="点击百度logo", attachment_type=allure.attachment_type.TEXT)
        BaseObject(self.driver).click_element(HomePageLocator().baidu_logo)

    @allure.step("搜索框输入{keys}")
    def send_keys_to_input_filed(self, keys):
        # allure.attach('', name=f"搜索框输入{keys}", attachment_type=allure.attachment_type.TEXT)
        BaseObject(self.driver).send_keys_to_element(HomePageLocator().input_filed, keys)

    @allure.step("点击搜索按钮")
    def click_search_button(self):
        # allure.attach('', name="点击搜索按钮", attachment_type=allure.attachment_type.TEXT)
        BaseObject(self.driver).click_element(HomePageLocator().search_button)


if __name__ == '__main__':
    from selenium import webdriver
    import time

    a = webdriver.Chrome(executable_path="/Users/yijia/Downloads/chromedriver")
    a.get("https://www.baidu.com")
    # HomePage(a).click_baidu_logo()
    # time.sleep(10)
    a.execute_script("window.open('', '_blank');")
    a.switch_to.window(a.window_handles[-1])
    a.get("https://www.bilibili.com")
    # time.sleep(10)
    a.close()
    time.sleep(2)
    a.switch_to.window(a.window_handles[0])
