import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class SearchTests(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 15 segundos antes de cerrar la ventana
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_search_tee(self):
        # metodo de la clase
        # metodo de prueba
        # indicar el elemento a buscar
        driver = self.driver
        search_field = driver.find_element_by_name("q")
        # metodo que limpia el campo de busqueda en caso de q haya texto
        search_field.clear()

        # enviamos una serie de teclas, e este caso, se simula el escrito 
        # por teclado de tee (camisa)
        search_field.send_keys('tee')
        # enviar datos
        search_field.submit()


    def test_search_salt_shaker(self):
        # metodo para buscar un salero
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(products))


    def tearDown(self):
        # metodo de la clase
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2)