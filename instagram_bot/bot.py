from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def create_account(self, email, fullname, username, password):
        try:
            logging.info("Navigating to Instagram signup page.")
            self.driver.get("https://www.instagram.com/accounts/emailsignup/")
            wait = WebDriverWait(self.driver, 10)

            logging.info(f"Entering account details for {username}.")
            email_input = wait.until(EC.presence_of_element_located((By.NAME, "emailOrPhone")))
            email_input.send_keys(email)

            fullname_input = self.driver.find_element(By.NAME, "fullName")
            fullname_input.send_keys(fullname)

            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys(username)

            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(password)

            signup_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign up')]")))
            signup_button.click()

            logging.info("Handling birthday selection.")
            month_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@title='Month:']")))
            month_select.click()
            self.driver.find_element(By.XPATH, "//option[text()='January']").click()

            day_select = self.driver.find_element(By.XPATH, "//select[@title='Day:']")
            day_select.click()
            self.driver.find_element(By.XPATH, "//option[text()='1']").click()

            year_select = self.driver.find_element(By.XPATH, "//select[@title='Year:']")
            year_select.click()
            self.driver.find_element(By.XPATH, "//option[text()='1990']").click()

            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
            next_button.click()

            logging.info(f"Account for {username} created successfully (pending verification).")
            time.sleep(10)

        except TimeoutException as e:
            logging.error(f"A timeout occurred while creating account for {username}: {e}")
            raise e
        except Exception as e:
            logging.error(f"An unexpected error occurred while creating account for {username}: {e}")
            raise e

    def close_browser(self):
        self.driver.quit()

if __name__ == '__main__':
    # This is for testing purposes
    bot = InstagramBot()
    bot.create_account("test@example.com", "Test User", "testuser12345", "testpassword")
    bot.close_browser()
