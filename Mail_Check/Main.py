'''This automation helps you to automatically sign in to yahoo mail
without a single mouse/keyboard stroke. To run this piece of code successfully,
you need to have an existing yahoo account'''
from selenium import webdriver
import time
from Configure import Configure

def if_exists(idstr):
    try:
        elem = browser.find_element_by_class_name(idstr)
        elem = elem.find_element_by_class_name('username')
        elem.click()
        flag = 1
    except Exception as e:
        flag = -1
    return flag
try:
    c = Configure()
    chk = c.check()
    if chk == -1:
        chk = c.create()
        if chk == 1:
            print('Please logout from all of your account while configuring...')
            time.sleep(3)
            c.configure()
    fp = open(r'config.dat', 'r')
    [username, password] = fp.readline().split(',')
    browser = webdriver.Edge()
    browser.get(r'yahoo.co.in')
    time.sleep(2)
    elem = browser.find_element_by_id('uh-mail-link')
    elem.click()
    time.sleep(10)
    chk = if_exists('account-card loggedOut')
    time.sleep(5)
    elem = browser.find_element_by_id('login-username')
    elem.clear()
    elem.send_keys(username)
    elem = browser.find_element_by_id('login-signin')
    elem.click()
    time.sleep(5)
    elem = browser.find_element_by_id('login-passwd')
    elem.send_keys(password)
    elem = browser.find_element_by_id('login-signin')
    elem.submit()

except Exception as e:
    print(str(e))



