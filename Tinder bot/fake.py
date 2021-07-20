from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

FB_EMAIL = "Your facebook email"
FB_PASSWORD = "Your facebook password"
driver = webdriver.Chrome()

driver.get("http://www.tinder.com")

sleep(1)
login_button = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
login_button.click()

sleep(1)
login_button = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[2]/div/div/div[1]/button')
login_button.click()

sleep(1)
login_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/button')
login_button.click()
# try:
#     pass
# except NoSuchElementException:
#     driver.refresh()
# finally:
#     driver.refresh()
#     driver.get("http://www.tinder.com")
#     sleep(1)
#     login_button = driver.find_element_by_xpath('//*[@id="q633216204"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
#     login_button.click()
#     sleep(1)
#     login_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/button')
#     login_button.click()

sleep(1)
fb_login = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

sleep(1)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)
#
# sleep(2)
# login_button = driver.find_element_by_xpath ('//*[@id="u_0_4_56"]/div[2]/div[1]/div[2]/div[1]/button')
# login_button.click()

sleep(100)
allow_location_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="q-1095164872"]/div/div/div/div/div[3]/button[1]')
notifications_button.click()
# cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
# cookies.click()
sleep(5)
for n in range(100):
    try:
        if driver.find_element_by_css_selector("#q-1095164872 > div > div"):
            exidd_button = driver.find_element_by_xpath('''//*[@id="q-1095164872"]/div/div/div[2]/button[2]''')
            exidd_button.click()
            sleep(3)
    except NoSuchElementException:
        sleep(2)

    try:
        for n in range(100):
            print("like")
            like_button = driver.find_element_by_css_selector('#q633216204 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-like-green\) > button')
            like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector("#q963587405 > div > div > div.CenterAlign.M\(a\).Expand.Pos\(r\).Fx\(\$flx1\) > div > div.Mt\(40px\).Pos\(r\).Trsdu\(\$slow\).D\(f\).Fx\(\$flx1\).Ai\(c\).Pe\(n\) > div > div")
            exit_button = driver.find_element_by_xpath('''//*[@id="q963587405"]/div/div/div[1]/div/div[4]/button''')
            exit_button.click()

        except NoSuchElementException:
            sleep(2)
driver.quit()