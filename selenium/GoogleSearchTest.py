from selenium import webdriver

def testReadFile():
    file = open("testData/target.txt ", "r")
    dataT = file.readline()
    if dataT.__eq__(''):
        dataT = "Gmail"
    print(dataT)
    return dataT


driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://www.google.com/")

# TODO : get [send_keys] from file
dataT = testReadFile()

# driver.find_element_by_name("q").send_keys("selenium python")
driver.find_element_by_name("q").send_keys(dataT)

driver.find_element_by_name("btnK").click()

# driver.save_screenshot('capture_GoogleSearchTest.png')
driver.save_screenshot('testResult/capture_GoogleSearchTest.png')

driver.close()

driver.quit()

print("Test automate!!!")



