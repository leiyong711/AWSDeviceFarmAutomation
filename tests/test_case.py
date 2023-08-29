# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: insta-page-load-automation
# author: "Lei Yong"
# creation time: 2023/8/25 10:39
# Email: leiyong711@163.com

import time
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        'appPackage': 'ai.instameta.android',
        'appActivity': 'android.base.app.mvp.ui.activity.SplashActivity',
        'platformName': 'Android',
        'deviceName': 'Android Emulator'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    yield driver
    driver.quit()


class TestAppium:

    def wait_for_element(self, driver, locator, interval=1, timeout=10):
        """
        wait for element to appear
        :param driver: WebDriver instance
        :param locator: element locator, which can be any positioning method in the MobileBy class
        :param interval: The interval between checking elements, the default is 1 second
        :param timeout: timeout, the default is 10 seconds
        :return: WebElement object, representing the found element
        """
        wait = WebDriverWait(driver, timeout, interval)
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            return element
        except NoSuchElementException:
            print(f"element_not_found: {locator}")
            return False
        except TimeoutError:
            print(f"element_not_found: {locator}")
            return False

    def test_01_front_page_youmaylike(self, driver):

        # wait for the homepage to appear
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/item_name'), timeout=20)

        if not element:
            raise Exception("test_01_front_page_youmaylike DID NOT ENTER THE HOME PAGE")
        # home vertical slide load youmaylike
        for i in range(15):
            driver.swipe(500, 900, 500, 200, 200)
            time.sleep(1)

    def test_02_dp_youmaylike(self, driver):
        # enter the product details page from youmaylike
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/cm_item_price'), timeout=5)
        if not element:
            raise Exception("test_02_dp_youmaylike NO CLICKABLE ITEMS FOUND")
        element.click()

        # judging whether it is an ordinary commodity
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/btn_shoppingcart_home'), timeout=5)
        if not element:

            # enter the product details page from the feed card
            element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/cm_item_name'), timeout=3)
            if element:
                element.click()

            element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/btn_shoppingcart_home'), timeout=5)
            if not element:
                raise Exception("test_02_dp_youmaylike NOT FOUND")

        # home vertical slide load youmaylike
        for i in range(20):
            driver.swipe(500, 900, 500, 200, 200)
            time.sleep(1)

        # RETURN HOME
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/btn_shoppingcart_home'), timeout=5)
        if element:
            element.click()

    def test_03_insta(self, driver):
        # wait for the homepage to appear
        element = self.wait_for_element(driver, (MobileBy.XPATH, '//*[@text="Insta"]'), timeout=20)
        if not element:
            raise Exception("test_03_insta INSTA NOT FOUND")

        # switch to insta
        element.click()

        # insta beginner s guide 1
        element = self.wait_for_element(driver, (MobileBy.XPATH, '//*[@resource-id="ai.instameta.android:id/bg_guide_step1"]'), timeout=5)
        if element:

            # next
            element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/tv2_guide_step1'), timeout=5)
            element.click()

        # insta beginner s guide 2
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/bg_guide_step2'), timeout=5)
        if element:

            # next
            element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/tv2_guide_step2'), timeout=5)
            element.click()

        # insta beginner s guide 3
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/tv_guide_step2'), timeout=10)
        if element:

            # complete
            element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/tv_guide_step2'), timeout=10)
            element.click()

        # did you successfully enter insta
        element = self.wait_for_element(driver, (MobileBy.ID, 'ai.instameta.android:id/avatar_insta_author'), timeout=10)
        if element:
            # vertical swipe load post
            for i in range(15):
                driver.swipe(500, 900, 500, 200, 100)
                time.sleep(1)


if __name__ == '__main__':
    pytest.main(['-s', 'test_appium.py'])
