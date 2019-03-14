from selenium import webdriver
# from yundama.dama import indetify
import requests
from selenium.webdriver import ActionChains
import time

driver =webdriver.Firefox()
#driver = webdriver.Chrome()
resp = driver.get('http://pub.alimama.com/')
#resp = driver.get('https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&from=alimama&redirectURL=http%3A%2F%2Flogin.taobao.com%2Fmember%2Ftaobaoke%2Flogin.htm%3Fis_login%3d1&full_redirect=true&disableQuickLogin=true')

time.sleep(10)
driver.switch_to.frame("taobaoLoginIfr")


#切换成淘宝密码登入
driver.find_element_by_xpath('//i[@class="iconfont static"]').click()
driver.find_element_by_name('TPL_username').send_keys('友人智创科技')

driver.find_element_by_id('TPL_password_1').send_keys('youren158')
#第一次点击登入触发滑块事件
driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]').click()


try:
    fuck = driver.find_element_by_xpath('//*[@class="nc_iconfont btn_slide"]')
    action = ActionChains(driver)
    action.click_and_hold(fuck)
    time.sleep(4)
    action.move_by_offset(250,0).perform()

    action.release().perform()
except Exception as e:
    #driver.find_element_by_id('TPL_password_1').send_keys('wjw1314520')
    driver.find_element_by_id('TPL_password_1').send_keys('youren158')
    driver.find_element_by_xpath('//button[@id="J_SubmitStatic"]').click()
    print(e)
# action.move_by_offset(151,0).perform()






#driver.find_element_by_id('codeid').click()
#img = driver.find_element_by_xpath('//span[@class="cell-wrap"]/img').get_attribute('src')
#print(img)
#response = requests.get(img)
#ret =indetify(response.content)

# time.sleep(5)
# driver.find_element_by_name('captcha').send_keys(ret)
# driver.find_element_by_name('submit').click()

