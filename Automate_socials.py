from selenium import webdriver

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to Instagram's login page
driver.get("https://www.instagram.com/accounts/login/")

# Find the username and password input fields and enter the login credentials
username_input = driver.find_element_by_name("username")
username_input.send_keys("your_username")
password_input = driver.find_element_by_name("password")
password_input.send_keys("your_password")

# Find the login button and click it
login_button = driver.find_element_by_css_selector("button[type='submit']")
login_button.click()

# Navigate to a user's profile
driver.get("https://www.instagram.com/user_to_follow/")

# Find the follow button and click it
follow_button = driver.find_element_by_css_selector("button[type='button']")
follow_button.click()

# Close the webdriver
driver.close()
