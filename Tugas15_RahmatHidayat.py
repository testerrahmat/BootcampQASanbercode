import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# variable
url = "http://barru.pythonanywhere.com/daftar"
nama_daftar = "Rahmat Hidayat"
email_daftar = "testerrahmat31@gmail.com"
email_daftar2 = "testerrahmat2@gmail.com"
email_daftar3 = "testerrahmat@gmail.com"
password_daftar = "test123"


class TestDaftar(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # test case pertama
    def test_daftar_lengkap(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(5)
        driver.find_element(By.ID, "name_register").send_keys(
            nama_daftar)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "email_register").send_keys(
            email_daftar)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "password_register").send_keys(
            password_daftar)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')

        # step terakhir
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(8)

    # test case kedua

    def test_daftar_namakosong(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(5)
        driver.find_element(By.ID, "email_register").send_keys(
            email_daftar2)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "password_register").send_keys(
            password_daftar)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertIn(
            'Email/Username/Password tidak boleh kosong', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

        # step terakhir
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(8)

    # test case ketiga
    def test_daftar_terdaftar(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "signUp").click()
        time.sleep(5)
        driver.find_element(By.ID, "name_register").send_keys(
            nama_daftar)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "email_register").send_keys(
            email_daftar3)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "password_register").send_keys(
            password_daftar)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signup_register").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertIn(
            'Email sudah terdaftar, gunakan Email lain', response_data)
        self.assertEqual(response_message, 'Gagal Registrasi')

        # step terakhir
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(8)

    # test case keempat
    def test_login_berhasil(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "email").send_keys(
            email_daftar)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            password_daftar)  # isi password
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertIn(
            'Welcome', response_data)
        self.assertEqual(response_message, 'Anda Berhasil Login')

        # step terakhir
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(8)

    # test case kelima
    def test_login_passwordkosong(self):

        driver = self.driver
        driver.get(url)  # buka situs
        time.sleep(5)
        driver.find_element(By.ID, "email").send_keys(
            email_daftar)  # isi email
        time.sleep(1)
        driver.find_element(By.ID, "signin_login").click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(By.ID, "swal2-title").text
        response_message = driver.find_element(By.ID, "swal2-content").text

        self.assertIn(
            'not found', response_data)
        self.assertEqual(response_message, 'Email atau Password Anda Salah')

        # step terakhir
        driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div[3]/button[1]").click()
        time.sleep(8)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
