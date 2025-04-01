from selenium import webdriver
from pages.login_page import LoginPage
from time import sleep
from config.Login  import Userinfor
def test_login():
    try:
        # 初始化driver
        driver = webdriver.Chrome()
        
        # 创建登录页面对象并执行登录流程
        login_page = LoginPage(driver)
        login_page.open() \
            .input_credentials(Userinfor.username, Userinfor.password)\
            .slide_verification()\
            .check_agreement()\
            .click_login()\
            .handle_force_logout()
        
        sleep(10)
    except Exception as e:
        print(f"登录过程出现错误: {str(e)}")
        raise e
    finally:
        driver.quit()

if __name__ == "__main__":
    test_login() 