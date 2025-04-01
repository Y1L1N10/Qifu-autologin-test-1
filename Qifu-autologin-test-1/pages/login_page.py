from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver import ActionChains

class LoginPage(BasePage):
    # 页面元素定位器
    USERNAME_INPUT = (By.ID, 'form_item_username')
    PASSWORD_INPUT = (By.ID, 'form_item_password')
    SLIDER_BUTTON = (By.CLASS_NAME, 'dv_handler')
    CHECKBOX = (By.CLASS_NAME, 'ant-checkbox-input')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.ant-btn.ant-btn-primary.ant-btn-lg.ant-btn-block.login-btn')
    CONFIRM_BUTTON = (By.CSS_SELECTOR, '.ant-modal-confirm-btns .ant-btn-primary')
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://2.test.qifu.com/login"
    
    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self
    
    def input_credentials(self, username, password):
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        return self
    
    def slide_verification(self):
        slider = self.find_clickable_element(self.SLIDER_BUTTON)
        track_width = self.execute_js("return document.getElementsByClassName('dv_text')[0].offsetWidth;")
        
        actions = ActionChains(self.driver)
        actions.move_to_element(slider)
        actions.click_and_hold(slider)
        actions.move_by_offset(track_width, 0)
        actions.release()
        actions.perform()
        return self
    
    def check_agreement(self):
        checkbox = self.find_element(self.CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
        return self
    
    def click_login(self):
        self.click_element(self.LOGIN_BUTTON)
        return self
    
    def handle_force_logout(self):
        self.click_element(self.CONFIRM_BUTTON)
        return self 