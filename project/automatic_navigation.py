from time import time
import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# importamos este modulo para incluir pausas, pero no se recomienda hacerlo
# porque las pausas añaden segundos a la ejecucion de la prueba
from time import sleep


class CompareProducts(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 30 segundos antes de cerrar la ventana
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://google.com/")


    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        # enviar el termino a buscar
        search_field.send_keys('platzi')
        search_field.submit()

        # retrocedemos una pagina
        driver.back()
        sleep(3)
        # avanzamos una pagina
        driver.forward()
        sleep(3)
        # refrescamos la pagina actual
        driver.refresh()
        sleep(3)
        # en total se han añadido 9 segundos al tiempo de ejecucion de la prueba


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        # self.driver.quit()
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)