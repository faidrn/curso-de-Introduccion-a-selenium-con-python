import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class RegisterNewUser(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 30 segundos antes de cerrar la ventana
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_new_user(self):
        driver = self.driver
        # hacemos click en el menu Account para q se despliegue
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        # le indicamos al driver q encuentre un elemento por el texto q esta en su enlace (respetando mayusculas y minusculas)
        # lo cual abre la ventana de log in
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        # validamos q el boton este habilitado, usando un assertion.
        # validando q este tanto visible para el usuario como el hecho de q pueda interactuar con él
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        # hacemos clic ene l boton
        create_account_button.click()

        # verificamos si estamos en el sitio de creacion de cuentas, a través del titulo de la pagina
        self.assertEqual('Create New Customer Account', driver.title)

        # identificacion de los elementos del form para interactuar
        #creación de variables con el nombre del selector correspondiente
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')

        # verificamos q los elementos del form esten habilitados
        self.assertTrue(first_name.is_enabled() 
        and middle_name.is_enabled() 
        and last_name.is_enabled() 
        and email_address.is_enabled() 
        and news_letter_subscription.is_enabled() 
        and password.is_enabled() 
        and confirm_password.is_enabled() 
        and submit_button.is_enabled())

        # enviar datos al form usando las variables
        first_name.send_keys('Tony')
        driver.implicitly_wait(1)
        middle_name.send_keys('Montague')
        driver.implicitly_wait(1)
        last_name.send_keys('Grenfell')
        driver.implicitly_wait(1)
        email_address.send_keys('tgrenfell0@sohu.com')
        driver.implicitly_wait(1)
        # news_letter_subscription.send_keys()
        password.send_keys('FuokHdCEKM')
        driver.implicitly_wait(1)
        confirm_password.send_keys('FuokHdCEKM')
        driver.implicitly_wait(1)
        submit_button.click()


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity= 2)