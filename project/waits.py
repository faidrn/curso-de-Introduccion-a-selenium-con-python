import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# By: nos ayuda a hacer referencia a un elemento del sitio web a traves de 
# sus selectores, no para identificarlos, sino para interactuar destinto de 
# lo que lo hace drive
from selenium.webdriver.common.by import By
# WebDriverWait: nos permite hacer uso de las expected conditions junto con 
# las esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
# esperas explicitas, pero se importan como EC para no escribir su nombre 
# completo cada vez q las llamemos
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTests(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_account_link(self):
        # metodo de prueba q hace referencia al enlace que nos lleva 
        # a las cuentas del sitio

        # WebDriverWait hara referencia a self.friver y esperara maximo 10 segundos
        # hasta q se cumpla la condicion esperada (usaremos una funcion lambda, a la q llamaremos s
        # y la usaremos para encontrar el selector de idiomas, despues obtenemos su atributo (get_attribute), 
        # en este caso la longitud (el nuumero de elementos q hay) lo igualamos a 3 para identificarlo, ya q
        # hay 3 idiomas)
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')

        # hacemos referencia al enlace donde estan las cuentas.
        # WebDriverWait hara referencia a self.friver y esperara maximo 10 segundos
        # hasta q se cumpla la condicion esperada, la cual llamaremos con EC(expected_conditions) haciendo referencia 
        # a la visibilidad del elementos q se esta ubicando. Para hacer refencia al elemento, lo hacemos a traves del 
        # texto q hay en el enlace, para lo cual usamos By
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        # le decimos a selenium q haga clic en el enlace
        account.click()


    def test_create_new_customer(self):
        # metodo que lleva al enlace para la creacion de un nuevo usuario
        
        # le decimos self.driver q encuentre el elemento por el texto q hay en el enlace, para despues hace clic y entrar al menu de cuentas
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        # WebDriverWait hara referencia a self.friver y esperara maximo 20 segundos hasta q se cumpla la condicion esperada, 
        # la cual llamaremos con EC(expected_conditions) q un elemento pueda ser clickeable (q se pueda hacer clic en el mismo, 
        # no solamente q sea visible) y lo identificaremos por el enlace del texto
        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        # por ultimo, esperaremos a q se cumpla otra condicion esperada: 
        # va a verificar q el sitio web en su titulo tenga el texto indicado
        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)