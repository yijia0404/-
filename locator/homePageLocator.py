class HomePageLocator:
    def __init__(self):
        self.__baidu_logo = '//div[@id="lg"]'
        self.__input_filed = '//input[@id="kw"]'
        self.__search_button = '//input[@id="su"]'

    @property
    def baidu_logo(self):
        return self.__baidu_logo

    # @baidu_logo.setter
    # def baidu_logo(self, x):
    #     self.__baidu_logo = x
    #     return self.__baidu_logo

    @property
    def input_filed(self):
        return self.__input_filed

    @property
    def search_button(self):
        return self.__search_button


if __name__ == '__main__':
    pass
    # a = HomePageLoactor()
    # print(a.baidu_logo)
    # a.baidu_logo = 234
    # print(a.baidu_logo)
