import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class CompareProducts(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 30 segundos antes de cerrar la ventana
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # como buena practica limpiamos el texto q hay en la barra de busqueda
        search_field.clear()

        # escribimos en la barra de busqueda el termino q queremos encontrar
        search_field.send_keys('tee')
        # enviamos el texto a traves del formulario
        search_field.submit()

        # identificar el elemento q hace la comparacion y hacemos clic en el
        driver.find_element_by_class_name('link-compare').click()

        # hacemos clic en el enlace q elimina la lista de comparacion
        # buscamos el elemento por el texto del enlace, se debe respetar
        # mayusculas y minusculas
        driver.find_element_by_link_text('Clear All').click()

        # lo anterior dispara un alert en pantalla, interactuamos con el 
        # pidiendole al driver q haga un cambio del focus al alert
        alert = driver.switch_to.alert
        # extraemos el texto q muestra el alert
        alert_text = alert.text
        
        #validamos si el texto q muestra el alert es el q queremos
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        # si el texto es identico simulamos un clic en el boton aceptar
        alert.accept()
        

    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity= 2)