import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure


class BaseObject:
    screenshot_path = "/Users/yijia/PycharmProjects/pythonProject3/screenshot/"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    @allure.attach("{locator}", name=f"点击元素xpath", attachment_type=allure.attachment_type.TEXT)
    def click_element(self, locator):
        # allure.attach(locator, name=f"点击元素xpath", attachment_type=allure.attachment_type.TEXT)
        self.driver.find_element(By.XPATH, locator).click()
        time.sleep(2)

    def send_keys_to_element(self, locator, keys):
        allure.attach(f"xpath: {locator}\ndata: {keys}", name=f"向元素xpath输入数据",
                      attachment_type=allure.attachment_type.TEXT)
        self.driver.find_element(By.XPATH, locator).send_keys(keys)

    def swipup_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    def swipdown_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView(false);", locator)

    def get_screenshot(self, file_ap):
        self.driver.get_screenshot_as_file(file_ap)

    def get_attribute_from_element(self, locator, attribute):
        return self.driver.find_element(By.XPATH, locator).get_attribute(attribute)

    def get_text_from_element(self, locator):
        return self.driver.find_element(By.XPATH, locator).text

    def is_exist_element(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator)
            return True
        except:
            return False

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def switch_to_original_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def close_page(self):
        self.driver.close()
        time.sleep(2)

    def quite_driver(self):
        self.driver.quit()


if __name__ == '__main__':
    print("".join(["1", "2", "3"]))
