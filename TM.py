from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests

# Setup for Chrome WebDriver (Headless)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run browser in background
service = Service('path_to_chromedriver')  # Make sure you have ChromeDriver installed
driver = webdriver.Chrome(service=service, options=chrome_options)

# 1. Country Selection (UK/USA)
def select_country(country):
    if country == "UK":
        # Implement logic specific to UK account creation
        print("Proceeding with UK account creation")
    elif country == "USA":
        # Implement logic specific to USA account creation
        print("Proceeding with USA account creation")
    else:
        print("Invalid country selection")

# 2. Fill Date of Birth
def enter_date_of_birth(dob):
    dob_field = driver.find_element(By.ID, "dob")  # Example field ID
    dob_field.send_keys(dob)

# 3. Temporary Email Generation (Mail.tm API)
def get_temp_email():
    response = requests.get("https://api.mail.tm/domains")
    email_data = response.json()
    return email_data['address']  # Assuming the API returns a temporary email address

# 4. Password Generation (Auto-Generated or Custom)
def generate_password(custom=False, password=""):
    if custom:
        return password
    else:
        # Auto-generate a strong password
        import random
        import string
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        return password

# 5. CAPTCHA Solving (2Captcha API Example)
def solve_captcha(image_url):
    api_key = "YOUR_2CAPTCHA_API_KEY"
    response = requests.post('http://2captcha.com/in.php', data={
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': 'GOOGLE_SITE_KEY',
        'pageurl': image_url
    })
    result = response.text.split('|')
    if result[0] == 'OK':
        return result[1]  # CAPTCHA solved ID
    return None

# 6. Account Creation Process
def create_account():
    # Open sign-up page
    driver.get("https://example.com/signup")

    # Fill out form
    first_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")
    confirm_password = driver.find_element(By.ID, "confirmPassword")

    first_name.send_keys("John")
    last_name.send_keys("Doe")
    email.send_keys(get_temp_email())  # Use temporary email API
    user_password = generate_password(custom=False)
    password.send_keys(user_password)
    confirm_password.send_keys(user_password)

    # Solve CAPTCHA if detected
    captcha_image = driver.find_elements(By.TAG_NAME, 'img')
    if captcha_image:
        captcha_id = solve_captcha(captcha_image[0].get_attribute('src'))
        if captcha_id:
            driver.find_element(By.ID, 'captcha-response').send_keys(captcha_id)

    # Submit the form
    confirm_password.send_keys(Keys.RETURN)

    print("Account creation in progress...")
    time.sleep(5)

    # Final success message
    print(f"Account created successfully. Username: JohnDoe, Password: {user_password}")

if __name__ == "__main__":
    # Example of country selection and workflow
    country = input("Choose country (1. UK, 2. USA): ")
    select_country("UK" if country == "1" else "USA")

    dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
    enter_date_of_birth(dob)

    create_account()

    driver.quit()
