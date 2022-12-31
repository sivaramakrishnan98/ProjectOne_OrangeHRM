from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


class Project_second():
    def testcase1(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        # find the xpath to login the page

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # click on admin Tab
        clcik_on_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        driver.find_element(By.XPATH, clcik_on_admin).click()
        driver.implicitly_wait(3)

        # select menu options are displaying on Admin page
        element = driver.find_element(By.XPATH, '//nav[@aria-label="Sidepanel"]')
        print(element.is_displayed())
        time.sleep(3)

        # select search box is displaying on Admin page
        result_validation = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        print(result_validation.is_displayed())
        time.sleep(3)

        #  Xpath for search button
        xpath_for_search_button = '//input[@placeholder="Search"]'
        search_option = driver.find_element(By.XPATH, xpath_for_search_button)

        # Using for loop to search in upper
        list_1 = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory",
                  "Maintenance", "Buzz"]

        for a in list_1:
            search_option.send_keys(a.upper())
            time.sleep(1)
            # Clearing text
            search_option.send_keys(Keys.CONTROL, 'a')
            search_option.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        # Using for loop to search in upper
        for a in list_1:
            search_option.send_keys(a.lower())
            time.sleep(1)
            # Clearing existing text
            search_option.send_keys(Keys.CONTROL, 'a')
            search_option.send_keys(Keys.BACKSPACE)
            time.sleep(1)
        print("Individual Tab name are displayed under search box")

        time.sleep(4)
        driver.quit()


    def testcase2(self):

        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.maximize_window()
        # find the xpath to login the page

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # click on admin Tab
        clcik_on_admin = '//a[@href="/web/index.php/admin/viewAdminModule"]'
        driver.find_element(By.XPATH, clcik_on_admin).click()
        driver.implicitly_wait(3)

        # select on user role

        select_the_use_role = "//label[text()='User Role']/following::div[1]"
        select_the_use_role1 = driver.find_element(By.XPATH, select_the_use_role).click()
        time.sleep(4)

        # drop down to admin
        drop_down_for_admmin = '//div[@role="option"]/span[text()="Admin"]'
        drop_down_for_admmin1 = driver.find_element(By.XPATH, drop_down_for_admmin).click()
        time.sleep(5)

        # select the status option
        select_the_status = "//label[text()='Status']/following::div[1]"
        select_the_status1 = driver.find_element(By.XPATH, select_the_status).click()
        time.sleep(4)

        drop_down_for_enable = '//div[@role="option"]/span[text()="Enabled"]'
        drop_down_for_enable1 = driver.find_element(By.XPATH, drop_down_for_enable).click()
        time.sleep(5)

        # select on user role On ESS path

        select_the_ESS = "//label[text()='User Role']/following::div[1]"
        select_the_ESS1 = driver.find_element(By.XPATH, select_the_ESS).click()
        time.sleep(4)

        # drop down to admin
        drop_down_for_ESS = '//div[@role="option"]/span[text()="ESS"]'
        drop_down_for_ESS1 = driver.find_element(By.XPATH, drop_down_for_ESS).click()
        time.sleep(5)

        # select the status option
        select_the_status_on_disable = "//label[text()='Status']/following::div[1]"
        select_the_status_on_disable1 = driver.find_element(By.XPATH, select_the_status_on_disable).click()
        time.sleep(4)

        drop_down_for_disabled = '//div[@role="option"]/span[text()="Disabled"]'
        drop_down_for_disabled1 = driver.find_element(By.XPATH, drop_down_for_disabled).click()

        time.sleep(5)
        print("Drop Down successfully it done on Admin and Enabled")
        print("Drop Down successfully it done on ESS and Disabled")

        driver.quit()

    def testcase3(self):
        # open the browser on firefox or chrome
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(url)
        driver.implicitly_wait(3)
        # find the xpath to login the page

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # click on add button by xpath
        driver.implicitly_wait(2)
        xpath_add_person = "//button[@type='button'][@class='oxd-button oxd-button--medium oxd-button--secondary']"
        driver.find_element(By.XPATH, xpath_add_person).click()
        driver.implicitly_wait(3)

        # add a image
        xpath_image = "//i[@class='oxd-icon bi-plus']"
        image = driver.find_element(By.XPATH, xpath_image)

        # add a person detail in employee path
        xpath_of_first_name = "//input[@name='firstName']"
        driver.find_element(By.XPATH, xpath_of_first_name).send_keys("Siva")
        driver.implicitly_wait(3)

        xpath_of_middle_name = "//input[@name='middleName']"
        driver.find_element(By.XPATH, xpath_of_middle_name).send_keys("rama")
        driver.implicitly_wait(3)

        xpath_of_last_name = "//input[@name='lastName']"
        driver.find_element(By.XPATH, xpath_of_last_name).send_keys("krishnan")
        driver.implicitly_wait(3)
        time.sleep(4)

        # add a employee id xpath
        xpath_of_id = "//label[text()='Employee Id']//following::input[1]"
        driver.find_element(By.XPATH, xpath_of_id).send_keys("26532")

        # Xpath for submit button
        #xpath_of_submit = '//button[@type="submit"]'
        time.sleep(3)

        click_on_Create_Login_Details = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
        driver.find_element(By.XPATH,click_on_Create_Login_Details).click()
        time.sleep(5)
        # click on the username by an Xpath
        driver.implicitly_wait(6)
        add_on_username = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH,add_on_username).send_keys("Siva2798")

        time.sleep(2)
        # enable the select which by an Xpath
        click_on_enable = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span"
        driver.find_element(By.XPATH,click_on_enable).click()
        time.sleep(4)

        # type on the password Xpath
        select_the_password = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input"
        driver.find_element(By.XPATH, select_the_password).send_keys("SivaGuvi98$")
        driver.implicitly_wait(3)

        # confire the password
        confire_the_password = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input"
        driver.find_element(By.XPATH,confire_the_password).send_keys("SivaGuvi98$")
        time.sleep(4)

        # click on save button
        click_on_save = '//button[@type="submit"]'
        driver.find_element(By.XPATH,click_on_save).click()
        time.sleep(3)
        print("successfully Employee name as be created")

        driver.quit()

    def testcase4(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # xpath for personal details tab
        personal_xpath = "//a[text()='Personal Details']"
        print(driver.find_element(By.XPATH,personal_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for contact details tab
        contact_details_xpath = "//a[text()='Contact Details']"
        print(driver.find_element(By.XPATH,contact_details_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for emergency contacts tab
        emergency_contacts_xpath = "//a[text()='Emergency Contacts']"
        print(driver.find_element(By.XPATH,emergency_contacts_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for dependents tab
        dependents_xpath = "//a[text()='Dependents']"
        print(driver.find_element(By.XPATH,dependents_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for Immigration tab
        Immigration_xpath = "//a[text()='Immigration']"
        print(driver.find_element(By.XPATH, Immigration_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for Job tab
        Job_xpath = "//a[text()='Job']"
        print(driver.find_element(By.XPATH,Job_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for salary tab
        salary_xpath = "//a[text()='Salary']"
        print(driver.find_element(By.XPATH,salary_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for tax exemptions tab
        exemptions_xpath = "//a[text()='Tax Exemptions']"
        print(driver.find_element(By.XPATH,exemptions_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath for Report to tab
        Report_to_xpath = "//a[text()='Report-to']"
        print(driver.find_element(By.XPATH,Report_to_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath to qualifications tab
        qualifications_xpath = "//a[text()='Qualifications']"
        print(driver.find_element(By.XPATH, qualifications_xpath).accessible_name)
        driver.implicitly_wait(3)

        # xpath to memberships tab
        memberships_xpath = "//a[text()='Memberships']"
        print(driver.find_element(By.XPATH,memberships_xpath).accessible_name)
        driver.implicitly_wait(3)
        time.sleep(7)

        driver.quit()

    def testcase5(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        driver.implicitly_wait(4)
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH,search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH,search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH,my_ID).click()
        driver.implicitly_wait(3)
        time.sleep(3)

        # click on nick name
        select_nick_name = "//label[text()='Nickname']/following::input[1]"
        driver.find_element(By.XPATH,select_nick_name).send_keys("SRK")
        time.sleep(3)

        # enter the other id
        enter_the_name = "//label[text()='Other Id']/following::input[1]"
        driver.find_element(By.XPATH, enter_the_name).send_keys("349270")
        time.sleep(3)

        # entering the driver license number
        time.sleep(3)
        enter_the_licence_name = """//label[contains(text(),"Driver's License Number")]/following::input[1]"""
        driver.find_element(By.XPATH,enter_the_licence_name).send_keys("TN 18Tn875524231")
        time.sleep(3)

        # entering the license expiry date
        entering_the_license_expiry = "//label[text()='License Expiry Date']/following::input[1]"
        driver.find_element(By.XPATH,entering_the_license_expiry).send_keys("2022-12-30")
        time.sleep(3)

        # entering the SSN number
        entering_the_ssn_number = "//label[text()='SSN Number']/following::input[1]"
        driver.find_element(By.XPATH,entering_the_ssn_number).send_keys("9087557846")
        time.sleep(3)

        # entering the SSN number2
        entering_the_ssn_number1 = "//label[text()='SSN Number']/following::input[2]"
        driver.find_element(By.XPATH,entering_the_ssn_number1).send_keys("9087557846")
        time.sleep(3)

        # select the Nationality option
        select_the_nation = "//label[text()='Nationality']/following::div[1]"
        select_the_nation1 = driver.find_element(By.XPATH,select_the_nation).click()
        time.sleep(4)
        # select the indain option on dropdown
        select_the_option_indain = "//div[@role='option']/span[text()='Indian']"
        select_the_option_indain1 = driver.find_element(By.XPATH,select_the_option_indain).click()
        driver.implicitly_wait(2)

        # select Marital Status
        select_the_Marital_Status = "//label[text()='Marital Status']/following::div[1]"
        select_the_Marital_Status1 = driver.find_element(By.XPATH,select_the_Marital_Status).click()
        driver.implicitly_wait(2)
        # drop down option to select the single
        drop_the_Marital_Status = '//div[@role="option"]/span[text()="Single"]'
        drop_the_Marital_Status1 = driver.find_element(By.XPATH,drop_the_Marital_Status).click()
        driver.implicitly_wait(2)

        #Select_the_D.O.B

        select_the_DOB = '//label[text()="Date of Birth"]/following::div[3]/input'
        driver.find_element(By.XPATH, select_the_DOB).send_keys("1998-11-27")
        time.sleep(4)

        # click on male option
        select_the_male = '//label[text()="Gender"]/following::div[2]/div[2]'
        driver.find_element(By.XPATH, select_the_male).click()

        # enetring the Military option as No
        Military = '//label[text()="Military Service"]/following::input[1]'
        driver.find_element(By.XPATH, Military).send_keys("NO")
        time.sleep(3)

        # click on save button
        enter_the_save = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button"
        driver.find_element(By.XPATH, enter_the_save).send_keys(Keys.ENTER)
        time.sleep(6)

        # select the blood group
        time.sleep(4)
        select_the_blood = '//label[text()="Blood Type"]/following::div[1]'
        select_the_xpath = driver.find_element(By.XPATH,select_the_blood).click()
        driver.implicitly_wait(3)
        # drop down blood group
        driver.implicitly_wait(5)
        select_the_drop_down = '//div[@role="option"]/span[text()="O+"]'
        select_the_drop_down1 = driver.find_element(By.XPATH,select_the_drop_down).click()
        time.sleep(2)

        # web page save in person detail
        save_the_person_detail = "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button"
        driver.find_element(By.XPATH,save_the_person_detail).click()

        print("successfully Personal Details as be saved")
        time.sleep(3)
        driver.quit()

    def testcase6(self):

        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on contact details
        time.sleep(5)
        click_on_contact_detail = "//a[text()='Contact Details']"
        driver.find_element(By.XPATH,click_on_contact_detail).click()
        driver.implicitly_wait(3)

        # select the address 1 and 2 and 3
        time.sleep(5)
        entering_the_street1  = "//h6[text()='Address']/following::input[1]"
        driver.find_element(By.XPATH,entering_the_street1).send_keys("No:3 lakshmi Amman koil")
        driver.implicitly_wait(3)

        # street 2
        time.sleep(3)
        entering_the_street2 = "//h6[text()='Address']/following::input[2]"
        driver.find_element(By.XPATH, entering_the_street2).send_keys("2nd cross street puzhal")
        driver.implicitly_wait(3)

        # street 3
        time.sleep(3)
        entering_the_street3 = "//h6[text()='Address']/following::input[3]"
        driver.find_element(By.XPATH, entering_the_street3).send_keys("Chennai")
        driver.implicitly_wait(3)

        # state option
        entering_the_state = "//h6[text()='Address']/following::input[4]"
        driver.find_element(By.XPATH, entering_the_state).send_keys("Tamil Nadu")
        driver.implicitly_wait(3)

        # Zip code option
        entering_the_Zipcode = "//h6[text()='Address']/following::input[5]"
        driver.find_element(By.XPATH, entering_the_Zipcode).send_keys("600066")
        driver.implicitly_wait(3)

        # select the country
        select_the_country = "//label[text()='Country']/following::div[1]"
        select_the_country1 = driver.find_element(By.XPATH,select_the_country).click()
        driver.implicitly_wait(3)

        drop_down = '//div[@role="option"]/span[text()="India"]'
        drop_down1 = driver.find_element(By.XPATH,drop_down).click()

        # Home option
        entering_the_home_option = "//h6[text()='Address']/following::input[6]"
        driver.find_element(By.XPATH, entering_the_home_option).send_keys("272829")
        driver.implicitly_wait(3)

        # Mobile option
        entering_the_moblie_number = "//h6[text()='Address']/following::input[7]"
        driver.find_element(By.XPATH, entering_the_moblie_number).send_keys("9087558951")
        driver.implicitly_wait(3)

        # Work option
        entering_the_work_option = "//h6[text()='Address']/following::input[8]"
        driver.find_element(By.XPATH, entering_the_work_option).send_keys("242625")
        driver.implicitly_wait(3)

        # work Email option
        entering_the_work_Email = "//h6[text()='Address']/following::input[9]"
        driver.find_element(By.XPATH, entering_the_work_Email).send_keys("sivarama409@gmail.com")
        driver.implicitly_wait(3)

        # Email option
        entering_the_Email_option = "//h6[text()='Address']/following::input[10]"
        driver.find_element(By.XPATH, entering_the_Email_option).send_keys("sivarama48@gmail.com")
        driver.implicitly_wait(3)

        # save the option
        click_on_save_button_for_contact = '//button[@type="submit"]'
        driver.find_element(By.XPATH,click_on_save_button_for_contact).click()

        time.sleep(2)

        # print the output statement
        print("successfully filled the contact details")

        # browser will be closed
        driver.quit()

    def testcase7(self):

        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on the Emergency Contacts

        click_on_the_emergency = '//a[text()="Emergency Contacts"]'
        driver.find_element(By.XPATH,click_on_the_emergency).click()
        time.sleep(2)

        # click on the add button Assigned Emergenc

        click_on_add_Assigned_Emergenc = '//h6[text()="Assigned Emergency Contacts"]/following::button[1]'
        driver.find_element(By.XPATH,click_on_add_Assigned_Emergenc).click()
        driver.implicitly_wait(2)

        # save option name
        entering_the_AE_name = '//label[text()="Name"]/following::input[1]'
        driver.find_element(By.XPATH,entering_the_AE_name).send_keys("Gunasekar")
        driver.implicitly_wait(3)

        # save option Relationship

        entering_the_AE_relationship = '//label[text()="Name"]/following::input[2]'
        driver.find_element(By.XPATH, entering_the_AE_relationship).send_keys("Father")
        driver.implicitly_wait(3)

        # save option Home Telephone

        entering_the_AE_home_number = '//label[text()="Name"]/following::input[3]'
        driver.find_element(By.XPATH, entering_the_AE_home_number).send_keys("004-82484848")
        driver.implicitly_wait(3)

        # save option moblie Telephone

        entering_the_AE_moblie_number = '//label[text()="Name"]/following::input[4]'
        driver.find_element(By.XPATH, entering_the_AE_moblie_number).send_keys("8248489099")
        driver.implicitly_wait(3)

        # save option Work Telephone

        entering_the_AE_Work_Telephone = '//label[text()="Name"]/following::input[5]'
        driver.find_element(By.XPATH,entering_the_AE_Work_Telephone).send_keys("004-90985598")
        driver.implicitly_wait(3)

        # save the option button
        save_on_button = '//label[text()="Work Telephone"]/following::button[2]'
        driver.find_element(By.XPATH,save_on_button).click()
        driver.implicitly_wait(3)

        # print the statement
        print("successfully filled the Emergency Contacts")
        time.sleep(6)

        driver.quit()

    def testcase8(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on Dependents tab
        clcik_on_dependents = "//a[text()='Dependents']"
        driver.find_element(By.XPATH,clcik_on_dependents).click()
        driver.implicitly_wait(4)

        # click_on_add_button

        click_on_add_button = "//h6[text()='Assigned Dependents']/following::button[1]"
        driver.find_element(By.XPATH,click_on_add_button).click()
        time.sleep(3)

        # enter the name

        enter_the_name = "//label[text()='Name']/following::input[1]"
        driver.find_element(By.XPATH,enter_the_name).send_keys("Gunasekar")

        # select the Relationship
        selct_the_relationship = "//label[text()='Name']/following::div[5]"
        driver.find_element(By.XPATH,selct_the_relationship).click()
        driver.implicitly_wait(4)
        drop_down_for_RS = '//div[@role="option"]/span[text()="Other"]'
        driver.find_element(By.XPATH,drop_down_for_RS).click()

        # enter the Please Specify
        enter_the_please_specify = "//label[text()='Name']/following::input[2]"
        driver.find_element(By.XPATH,enter_the_please_specify).send_keys("Father")

        # enter the DOB
        enter_the_DOB = "//label[text()='Name']/following::input[3]"
        driver.find_element(By.XPATH,enter_the_DOB).send_keys("1972-05-05")

        # save the button
        save_the_button_on_D = "//label[text()='Date of Birth']/following::button[2]"
        driver.find_element(By.XPATH,save_the_button_on_D).click()

        time.sleep(5)

        print("successfully filled the Dependents")

        driver.quit()

    def testcase9(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on Job tab

        click_on_option = "//a[text()='Job']"
        driver.find_element(By.XPATH,click_on_option).click()

        # select the join date
        time.sleep(7)
        join_date = "//label[text()='Joined Date']/following::input[1]"
        driver.find_element(By.XPATH,join_date).send_keys("2019-06-26")

        # select the jon title
        job_title = "//label[text()='Joined Date']/following::div[7]"
        job_title1 = driver.find_element(By.XPATH,job_title).click()
        driver.implicitly_wait(3)

        # drop down the job title
        job_drop_down = "//div[@role='option']/span[text()='Software Engineer']"
        job_drop_down1 = driver.find_element(By.XPATH, job_drop_down).click()

        # select the Job Category

        category_select= "//label[text()='Job Category']/following::div[1]"
        category_select1 = driver.find_element(By.XPATH,category_select).click()

        # drop dowm job category

        category_drop_down = "//div[@role='option']/span[text()='Technicians']"
        category_drop_down1 = driver.find_element(By.XPATH, category_drop_down).click()

        # select Sub Unit

        sub_unit_select = "//label[text()='Sub Unit']/following::div[1]"
        sub_unit_select1 = driver.find_element(By.XPATH, sub_unit_select).click()

        # drop dowm job category

        driver.implicitly_wait(6)
        sub_drop_down = "//div[@role='option']/span[text()='Quality Assurance']"
        sub_drop_down1 = driver.find_element(By.XPATH,sub_drop_down).click()

        # select Location

        select_location = "//label[text()='Location']/following::div[1]"
        select_location1 = driver.find_element(By.XPATH, select_location).click()

        # drop dowm location

        driver.implicitly_wait(3)
        location_drop_down = "//div[@role='option']/span[text()='New York Sales Office']"
        location_drop_down1 = driver.find_element(By.XPATH,location_drop_down).click()

        # select Employment Status

        select_employee = "//label[text()='Employment Status']/following::div[1]"
        select_employee1 = driver.find_element(By.XPATH,select_employee).click()

        # drop dowm Employment Status

        driver.implicitly_wait(6)
        employee_drop_down = "//div[@role='option']/span[text()='Full-Time Permanent']"
        employee_drop_down1 = driver.find_element(By.XPATH,employee_drop_down).click()

        # click on Include Employment Contract Details
        click_on_include_EMP_CD = "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']"
        driver.find_element(By.XPATH,click_on_include_EMP_CD).click()
        driver.implicitly_wait(3)

        # enter the contract start date
        entering_the_start_date = "//p[text()='Include Employment Contract Details']/following::input[2]"
        driver.find_element(By.XPATH,entering_the_start_date).send_keys("2019-06-26")
        driver.implicitly_wait(3)

        # enter the contract END date
        entering_the_end_date = "//p[text()='Include Employment Contract Details']/following::input[3]"
        driver.find_element(By.XPATH, entering_the_end_date).send_keys("2022-11-12")
        driver.implicitly_wait(3)
        time.sleep(4)

        # enter the contract details.
        enter_the_upload = "//div[@class='oxd-file-div oxd-file-div--active']"
        enter_the_upload1 = driver.find_element(By.XPATH,enter_the_upload)
        #enter_the_upload1.send_keys("C://Learing/Automation/Selenium/Sivaramakrishnan Resume.pdf")
        # for uploading in Orange HRM site its not taking the upload selecting
        time.sleep(4)

        # click on save button on JOB tab
        click_on_save = "//button[@type='submit']"
        driver.find_element(By.XPATH,click_on_save).click()

        print("successfully Job Detail as be saved")
        time.sleep(4)

        driver.quit()

    def testcase10(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on Job tab

        click_on_option = "//a[text()='Job']"
        driver.find_element(By.XPATH,click_on_option).click()
        time.sleep(3)

        # click on Terminate Employment
        time.sleep(5)
        driver.implicitly_wait(7)
        click_on_terminate_EMP = "//h6[text()='Employee Termination / Activiation']/following::button[1]"
        driver.find_element(By.XPATH,click_on_terminate_EMP).click()
        driver.implicitly_wait(4)
        time.sleep(3)


        # enter on Terminate Employment tab frame

        enter_the_date_TM = "//label[normalize-space()='Termination Date']/following::input[1]"
        driver.find_element(By.XPATH,enter_the_date_TM).send_keys("2020-12-01")
        driver.implicitly_wait(3)

        # enter the Termination Reason
        enter_the_termian_reaseon ="//label[normalize-space()='Termination Date']/following::div[7]"
        driver.find_element(By.XPATH, enter_the_termian_reaseon).click()
        driver.implicitly_wait(3)

        # drop dowm for Termination Reason
        drop_dowm_for_termination_Reason = "//div[@role='option']/span[text()='Resigned - Self Proposed']"
        driver.find_element(By.XPATH,drop_dowm_for_termination_Reason).click()
        time.sleep(4)

        # enter the note list

        entering_the_note = "//label[text()='Note']/following::textarea[1]"
        entering_the_note1= driver.find_element(By.XPATH,entering_the_note)
        entering_the_note1.send_keys("due to Night shift and health issue are there")

        # enter the save
        save_the_button = "//label[text()='Note']/following::button[2]"
        driver.find_element(By.XPATH,save_the_button).click()

        print(driver.find_element(By.XPATH,'//h6[text()="Employee Termination / Activiation"]/following::p[1]').text)

        print(driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button').text)

        time.sleep(4)

        driver.quit()

    def testcase11(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on Job tab

        click_on_option = "//a[text()='Job']"
        driver.find_element(By.XPATH, click_on_option).click()
        time.sleep(3)

        # click on Terminate Employment Activatied
        time.sleep(5)
        driver.implicitly_wait(7)
        click_on_terminate_EMP = "//h6[text()='Employee Termination / Activiation']/following::button[1]"
        driver.find_element(By.XPATH, click_on_terminate_EMP).click()
        driver.implicitly_wait(4)
        print("Employee Job Activated")
        time.sleep(4)
        driver.quit()


    def testcase12(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on salary
        click_on_salary_tab = "//a[text()='Salary']"
        driver.find_element(By.XPATH,click_on_salary_tab).click()
        driver.implicitly_wait(3)

        # click on Assigned Salary Components
        time.sleep(5)
        click_on_add_button = "//h6[text()='Assigned Salary Components']/following::button[1]"
        driver.find_element(By.XPATH,click_on_add_button).click()
        driver.implicitly_wait(3)

        # enter the Salary Component
        entering_the_salary = "//label[text()='Salary Component']/following::input[1]"
        driver.find_element(By.XPATH,entering_the_salary).send_keys("600000")
        driver.implicitly_wait(3)

        # enter the Pay Grade

        select_the_grade = "//label[text()='Salary Component']/following::div[5]"
        driver.find_element(By.XPATH,select_the_grade).click()
        driver.implicitly_wait(3)

        # select the dropdown
        select_the_drop_down = '//div[@role="option"]/span[text()="Grade 2"]'
        driver.find_element(By.XPATH,select_the_drop_down).click()
        driver.implicitly_wait(3)

        # enter the Pay Frequency

        select_the_frequency = "//label[text()='Pay Frequency']/following::div[3]"
        driver.find_element(By.XPATH, select_the_frequency).click()
        driver.implicitly_wait(3)

        # select the dropdown
        select_pay_the_drop_down = '//div[@role="option"]/span[text()="Monthly"]'
        driver.find_element(By.XPATH, select_pay_the_drop_down).click()
        driver.implicitly_wait(3)

        # enter the Currency

        select_the_currency = "//label[text()='Currency']/following::div[3]"
        driver.find_element(By.XPATH, select_the_currency).click()
        driver.implicitly_wait(3)

        # select the dropdown Currency
        select_currency_the_drop_down = '//div[@role="option"]/span[text()="United States Dollar"]'
        driver.implicitly_wait(8)
        driver.find_element(By.XPATH, select_currency_the_drop_down).click()
        driver.implicitly_wait(3)
        time.sleep(3)

        # select_the_amount_comment

        select_the_amount = "//label[text()='Currency']/following::input[1]"
        driver.find_element(By.XPATH, select_the_amount).send_keys("50000")
        driver.implicitly_wait(4)

        # enter the Comments option
        enter_the_comments = "//label[text()='Currency']/following::textarea[1]"
        enter_the_comments1 = driver.find_element(By.XPATH,enter_the_comments)
        enter_the_comments1.send_keys("My salary expectations for this position are between $85,000 and $95,000. I feel this is a fair salary range given my experience, knowledge of the industry, and skills.")
        time.sleep(5)

        # click on Include Direct Deposit Details

        click_on_include_DDD = "//p[text()='Include Direct Deposit Details']/following::span[1]"
        driver.find_element(By.XPATH,click_on_include_DDD).click()
        driver.implicitly_wait(3)

        # enter the account number
        enter_account_number = "//p[text()='Include Direct Deposit Details']/following::input[2]"
        driver.find_element(By.XPATH,enter_account_number).send_keys("0112345678")
        driver.implicitly_wait(3)

        # account type
        select_the_account_type = "//label[text()='Account Type']/following::div[1]"
        driver.find_element(By.XPATH,select_the_account_type).click()
        driver.implicitly_wait(3)

        # drop dowm for account type

        drop_dowm_for_account ='//div[@role="listbox"]//span[text()="Savings"]'
        driver.find_element(By.XPATH, drop_dowm_for_account).click()
        time.sleep(4)

        # enter the Routing Number
        enter_the_rount_number = "//label[text()='Account Type']/following::input[1]"
        driver.find_element(By.XPATH, enter_the_rount_number).send_keys("271183701")
        time.sleep(4)

        # enter the Amount
        enter_the_amount = "//label[text()='Account Type']/following::input[2]"
        driver.find_element(By.XPATH, enter_the_amount).send_keys("10000")
        time.sleep(4)

        # save the option
        save_the_option = '//button[@type="submit"]'
        driver.find_element(By.XPATH,save_the_option).click()
        time.sleep(8)
        print("successfully filled salary detail")
        driver.quit()


    def testcase13(self):
        driver = webdriver.Chrome()
        # Page will be maximize window
        driver.maximize_window()
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        # get the orange HRM login page to
        driver.get(url)
        driver.implicitly_wait(3)

        # Xpath for username
        xpath_username = "//input[@name='username']"
        username = driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.implicitly_wait(2)

        # Xpath for password
        xpath_password = "//input[@name='password']"
        password = driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        driver.implicitly_wait(3)

        # xpath for login button
        xpath_login_button = "//button[@type='submit']"
        login_button = driver.find_element(By.XPATH, xpath_login_button).click()
        driver.implicitly_wait(2)

        # open the HRM Page
        # click on pim tab menu by xpath
        xpath_pim = "//a[@href='/web/index.php/pim/viewPimModule']"
        driver.find_element(By.XPATH, xpath_pim).click()
        driver.implicitly_wait(2)

        # search the create on exiting account on search option
        time.sleep(6)
        search_box = "//label[text()='Employee Name']/following::input[1]"
        driver.find_element(By.XPATH, search_box).send_keys("Siva rama krishnan")
        driver.implicitly_wait(3)

        # clcik on serch button
        search_button = "//button[@type='submit']"
        driver.find_element(By.XPATH, search_button).click()
        driver.implicitly_wait(3)

        # record found to search option
        my_ID = "//i[@class='oxd-icon bi-pencil-fill']"
        driver.find_element(By.XPATH, my_ID).click()
        driver.implicitly_wait(3)

        # click on Tax Exemptions Teb
        click_on_tax = "//a[text()='Tax Exemptions']"
        driver.find_element(By.XPATH,click_on_tax).click()
        driver.implicitly_wait(3)

        # enter the Status option

        select_the_status = "//h6[text()='Federal Income Tax']/following::div[7]"
        driver.find_element(By.XPATH,select_the_status).click()
        driver.implicitly_wait(3)

        drop_down_for_status = '//div[@role="option"]/span[text()="Single"]'
        driver.find_element(By.XPATH,drop_down_for_status).click()
        driver.implicitly_wait(3)

        # enter the Exemptions

        select_the_exemptions = "//h6[text()='Federal Income Tax']/following::input[1]"
        driver.find_element(By.XPATH, select_the_exemptions).send_keys("8000CC")
        driver.implicitly_wait(3)

        # enter the State option

        select_the_state = "//h6[text()='State Income Tax']/following::div[7]"
        driver.find_element(By.XPATH, select_the_state).click()
        driver.implicitly_wait(3)

        drop_down_for_state = '//div[@role="option"]/span[text()="Arkansas"]'
        driver.find_element(By.XPATH, drop_down_for_state).click()
        driver.implicitly_wait(3)

        # enter the Statusone option

        select_the_statusone = "//label[text()='State']/following::div[9]"
        driver.find_element(By.XPATH, select_the_statusone).click()
        driver.implicitly_wait(3)

        drop_down_for_statusone = '//div[@role="option"]/span[text()="Single"]'
        driver.find_element(By.XPATH, drop_down_for_statusone).click()
        driver.implicitly_wait(3)

        # enter theExemptionsone option

        select_the_exemptionsone = "//label[text()='State']/following::input[1]"
        driver.find_element(By.XPATH, select_the_exemptionsone).send_keys("8000CC")
        driver.implicitly_wait(3)

        # enter the Unemployment State

        select_the_unemployment = "//label[text()='Unemployment State']/following::div[1]"
        driver.find_element(By.XPATH,select_the_unemployment).click()
        driver.implicitly_wait(3)

        drop_down_for_unemploy = '//div[@role="option"]/span[text()="Armed Forces Europe"]'
        driver.find_element(By.XPATH,drop_down_for_unemploy).click()
        driver.implicitly_wait(3)

        # enter the Work State

        select_the_work_state = "//label[text()='Work State']/following::div[1]"
        driver.find_element(By.XPATH, select_the_work_state).click()
        driver.implicitly_wait(3)

        drop_down_for_work_state = '//div[@role="option"]/span[text()="Armed Forces Europe"]'
        driver.find_element(By.XPATH,drop_down_for_work_state).click()
        driver.implicitly_wait(3)

        # save the option
        save_the_option = "//label[text()='Work State']/following::button[1]"
        driver.find_element(By.XPATH,save_the_option).click()
        driver.implicitly_wait(3)
        time.sleep(5)

        print("successfully saved the Tax Exemptions")
        driver.quit()

Sivaramakrishnan = Project_second()
Sivaramakrishnan.testcase1() # Done
Sivaramakrishnan.testcase2() # Done
Sivaramakrishnan.testcase3() # Done
Sivaramakrishnan.testcase4() # Done
Sivaramakrishnan.testcase5() # Done
Sivaramakrishnan.testcase6() # Done
Sivaramakrishnan.testcase7() # Done
Sivaramakrishnan.testcase8() # Done
Sivaramakrishnan.testcase9() # Done
Sivaramakrishnan.testcase10() # Done
#Sivaramakrishnan.testcase11() # Done If we get the Error mean please run it again
Sivaramakrishnan.testcase12() #Done
Sivaramakrishnan.testcase13() #Done