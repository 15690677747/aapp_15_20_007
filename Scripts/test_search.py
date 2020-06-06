from Base.page import Page
from Base.driver import Driver
import pytest


class TestSearch:

    def setup_class(self):
        """点击搜索按钮"""
        Page.get_setting().click_search_btn()

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.mark.parametrize("search_text, search_exp", [("1", "休眠"), ("i", "IP地址"), ("m", "MAC地址")])
    def test_search(self, search_text, search_exp):
        """
        搜索内容测试
        :param search_text: 搜索内容
        :param search_exp: 搜索预期结果
        :return:
        """
        # 搜索
        result = Page.get_search().get_search_result(search_text)
        # 断言
        assert search_exp in result
