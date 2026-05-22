import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginAutomationTest(unittest.TestCase):

    def setUp(self):
        # Setup browser sebelum setiap test case berjalan
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
        # Otomatis membuat folder 'screenshots' jika belum ada di PC kamu
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

    def test_01_login_sukses(self):
        """
        GHERKIN SYNTAX:
        Given the user navigates to the login page "https://the-internet.herokuapp.com/login"
        When the user enters username "tomsmith" and password "SuperSecretPassword!"
        And the user clicks the login button
        Then the user should see a success message containing "You logged into a secure area!"
        """
        driver = self.driver
        
        # GIVEN: Membuka halaman login
        driver.get("https://the-internet.herokuapp.com/login")
        
        # WHEN: Mengisi username dan password yang benar
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        
        # AND: Mengklik tombol login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # THEN: Memvalidasi pesan sukses (bar hijau) yang muncul
        # Menunggu maksimal 10 detik sampai elemen pesan muncul
        flash_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        # Memastikan teks "You logged into a secure area!" ada di dalam pesan tersebut
        self.assertIn("You logged into a secure area!", flash_message.text)
        
        # Mengambil screenshot hasil test case 1
        driver.save_screenshot("screenshots/01_login_sukses.png")

    def test_02_login_gagal(self):
        """
        GHERKIN SYNTAX:
        Given the user navigates to the login page "https://the-internet.herokuapp.com/login"
        When the user enters username "tomsmith" and password "WrongPassword123"
        And the user clicks the login button
        Then the user should see an error message containing "Your password is invalid!"
        """
        driver = self.driver
        
        # GIVEN: Membuka halaman login
        driver.get("https://the-internet.herokuapp.com/login")
        
        # WHEN: Mengisi username benar tapi password salah
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("WrongPassword123")
        
        # AND: Mengklik tombol login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # THEN: Memvalidasi pesan error (bar merah) yang muncul
        flash_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "flash"))
        )
        
        # Memastikan teks "Your password is invalid!" ada di dalam pesan tersebut
        self.assertIn("Your password is invalid!", flash_message.text)
        
        # Mengambil screenshot hasil test case 2
        driver.save_screenshot("screenshots/02_login_gagal.png")

    def tearDown(self):
        # Menutup browser secara otomatis setelah setiap test case selesai
        self.driver.quit()

if __name__ == "__main__":
    # Menjalankan test dengan verbositas tinggi agar laporan di terminal detail
    unittest.main(verbosity=2)