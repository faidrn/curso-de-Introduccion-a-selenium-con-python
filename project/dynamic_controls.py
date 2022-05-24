import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class AddRemoveElements(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Dynamic Controls').click()


    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element_by_css_selector('#checkbox > input[type=checkbox]')
        # hacemos clic en el checkbox para q se active
        checkbox.click()

        # usamos el selector de css porque es mas legible la lectura del codigo 
        # y tambien hace q el codigo sea prolijo
        remove_add_button = driver.find_element_by_css_selector('#checkbox-example > button')
        # hacemos q desaparezca el checkbox
        remove_add_button.click()

        # usamos una condicion esperada (expected conditions)
        # le decimos al driver q espere un maximo de 15 segundos hasta que la condicion esperada 
        # sea q el elemento pueda ser cliqueable, debemos indicar cual es dicho elemento, lo indicamos
        # por su selector de css
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        # despues de esperar, hacemos clic en el boton para q aparezca el checkbos nuevamente
        remove_add_button.click()

        enable_disble_bnutton = driver.find_element_by_css_selector('#input-example > button')
        enable_disble_bnutton.click()
        # esperamos a q cargue para q habilite el textarea
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        # identificamos el textarea
        text_area = driver.find_element_by_css_selector('#input-example > input[type=text]')
        text_area.send_keys('platzi')

        # nuevamente hacemos clic en el boton de habilitar / deshabilitar textarea para q lo deshabilite
        enable_disble_bnutton.click()


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    # unittest.main(verbosity= 2)
    unittest.main()