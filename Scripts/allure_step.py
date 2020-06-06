import  allure

class Test001:
    @allure.step("实测文件")
    def test_001(self):
        print("/n--->test_001")

    @allure.step("实测文件2")
    def test_002(self):
        print("/n--->test_002")
        assert False