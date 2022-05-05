import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
#sirve como excepción para los assertions cuando queremos
#validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
#submodulo que ayuda a llamar a las excepciones q queremos crear
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 30 segundos antes de cerrar la ventana
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_search_field(self):
        # Validar que el elementoeste presente
        self.assertTrue(self.is_element_present(By.NAME, 'q'))


    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()


    def is_element_present(self, how, what):
        # funcion de utilidad para identificar cuando un elemento esta presente,
        # de acuerdo a los parametros: 
        # how: indica el tipo de selector
        # what: indica el valor que tiene 
        try:
            # buscar a traves del driver el elemento con los parametros indicados
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity= 2)