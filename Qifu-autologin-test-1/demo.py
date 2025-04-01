from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import config


# 实例化 WebDriver
driver = webdriver.Chrome()

# 设置浏览器窗口大小  driver.set_window_size(1920, 1080)
driver.maximize_window()

# 打开网页
driver.get("http://2.test.qifu.com/login")

# 输入账号
driver.find_element(By.ID, 'form_item_username').send_keys(config.Userinfor.username)

# 输入密码
driver.find_element(By.ID, 'form_item_password').send_keys(config.Userinfor.password)

'''WebDriverWait:这是 Selenium 提供的一个显式等待机制，用于等待某个条件成立后再继续执行代码。
WebDriverWait(driver, 10) 表示最多等待 10 秒，直到某个条件成立。
如果 10 秒内条件未成立，会抛出 TimeoutException。

EC.element_to_be_clickable:
这是一个条件判断函数，用于检查某个元素是否可被点击。
参数是一个元组，包含定位方式和定位值。这里使用了 By.CLASS_NAME，表示通过类名定位元素。

By.CLASS_NAME, "dv_handler" 表示查找类名为 dv_handler 的元素，这是滑块按钮的类名。'''
slider_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "dv_handler"))  # 极验滑块的经典类名
)
#slider_button = WebDriverWait()

'''计算滑动距离 这是 Selenium 提供的一个方法，用于执行 JavaScript 脚本。
document.getElementsByClassName('dv_text') 获取所有类名为 dv_text 的元素。
[0] 表示取第一个元素。
.offsetWidth 获取该元素的宽度（包括内边距、边框和滚动条，但不包括外边距）。'''

track_background_width = driver.execute_script(
    "return document.getElementsByClassName('dv_text')[0].offsetWidth;"
)
print(track_background_width)
slide_button_width = slider_button.size['width']
print(slide_button_width)

# 构造拖动动作（模拟人类操作）
'''
ActionChains:
这是 Selenium 提供的一个类，用于模拟用户的一系列动作（如鼠标移动、点击、拖动等）。

move_to_element:
这个方法用于将鼠标移动到指定元素上。
参数是目标元素对象。

click_and_hold:
这个方法用于模拟鼠标按下并按住某个元素。
参数是目标元素对象。
'''
actions = ActionChains(driver)
actions.move_to_element(slider_button)
actions.click_and_hold(slider_button)

# 最终移动 + 松开
actions.move_by_offset(track_background_width, 0)
actions.release()
actions.perform()



'''勾选用户协议,class = ant-checkbox-input'''
try:
    # 等待用户协议复选框加载完成
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ant-checkbox-input"))
    )
    # 勾选用户协议
    if not checkbox.is_selected():  # 检查是否已经被勾选
        checkbox.click()
    print("用户协议已勾选")
    # 这里可以继续后续操作，例如提交表单等
except Exception as e:
    print("勾选用户协议失败，请检查定位方式或页面元素是否正确")
    raise e

# 等待登录按钮可点击
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.ant-btn.ant-btn-primary.ant-btn-lg.ant-btn-block.login-btn'))
    )
    print("登录按钮已找到且可点击")
    login_button.click()
    print("登录按钮已点击")
except Exception as e:
    print("登录按钮未找到或不可点击，请检查登录按钮的定位方式是否正确")
    driver.quit()
    raise e
sleep(3)

#强制踢出
# 等待并点击“确定”按钮
confirm_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-modal-confirm-btns .ant-btn-primary"))
)
confirm_button.click()

sleep(10)
driver.quit()