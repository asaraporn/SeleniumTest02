from selenium import webdriver

def testInput():
    name = str(input("Enter your data: "))
    if name:
        print("Hello " + str(name))
    else:
        name = "Hadsai"
        print("Hello " + str(name))
    return name


# driver = webdriver.Chrome(executable_path='C:\Project\Selenium_Project02\drivers\chromedriver.exe')
driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')


driver.implicitly_wait(10)
driver.maximize_window()

# TODO : key in your information
name = testInput()

driver.get("https://www.facebook.com/login/identify?ctx=recover")
driver.find_element_by_css_selector("a[href=\"https://www.facebook.com/\"]").click()

# print(pageTitle)
# if(driver.getTitle().equals("Facebook - log in or sign up")):
#     print("We are back at Facebook's homepage")
# else :
#     print("We are NOT in Facebook's homepage")

driver.save_screenshot('/reports/capture.png')

driver.close()
driver.quit()
print("complete!!!")






