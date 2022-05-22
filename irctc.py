from selenium import webdriver

driver = webdriver.Chrome(executable_path="/home/in520/Downloads/chromedriver")


def lets_open_site():
    driver.maximize_window()
    driver.get("https://www.irctc.co.in/nget/train-search")
    elem1 = driver.find_element_by_xpath(
        "/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button")
    elem1.click()
    elem2 = driver.find_element_by_xpath(
        "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[1]/p-autocomplete/span/input")
    elem2.send_keys("MANKAPUR JN - MUR")
    elem3 = driver.find_element_by_xpath(
        "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[1]/div[2]/p-autocomplete/span/input")
    elem3.send_keys("GHAZIABAD - GZB")
    elem4 = driver.find_element_by_xpath(
        "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[2]/div[2]/div[1]/p-calendar/span/input")
    elem4.click()
    # elem4.send_keys("18/05/2022")
    elem6 = driver.find_element_by_xpath(
        "//*[@id='jDate']/span/div/div/div[2]/table/tbody/tr[3]/td[4]")
    elem6.click()
    elem5 = driver.find_element_by_xpath(
        "/html/body/app-root/app-home/div[3]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button")
    elem5.click()
    elem7 = driver.find_element_by_xpath(
        "//*[@id='divMain']/div/app-train-list/div[4]/div/div[5]/div[4]/div[1]/app-train-avl-enq/div[1]/div[7]/div[1]/div[3]/table/tr/td[2]/div")
    elem7.click()
    elem8 = driver.find_element_by_xpath(
        "//*[@id='divMain']/div/app-train-list/div[4]/div/div[5]/div[4]/div[1]/app-train-avl-enq/div[2]/div/span/span[1]/button")
    elem8.click()
    elem9 = driver.find_element_by_xpath(
        "//*[@id='divMain']/div/app-train-list/p-confirmdialog[1]/div/div/div[3]/button[1]/span[2]")
    elem9.click()
    elem10 = driver.find_element_by_xpath("//*[@id='3021056']")
    elem10.send_keys("SHASHWATTRIPATHI")
    elem11 = driver.find_element_by_xpath("//*[@id='9616900']")
    elem11.send_keys("Pathi9198")


lets_open_site()
