import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class Typos(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Typos').click()


    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
        # extraemos el texto para no hacer referencia a la etiqueta, sino al texto q hay en ella
        text_to_check = paragraph_to_check.text
        # mostramos en pantalla para validar q este correcto
        print(text_to_check)

        # definimos variables de control
        tries = 1 # numero de intentos hasta encontrar el texto correcto
        found = False # variable para definir si lo encontramos o no
        correct_text = "Sometimes you'll see a typo, other times you won't."

        # cada vez q el texto a verificar sea diferente al texto correcto, cargara nuevamente el navegador, 
        # evitando tomar el texto equivocado
        while text_to_check != correct_text:
            # reasignamos lo valores para continuar con las validaciones
            paragraph_to_check = driver.find_element_by_css_selector('#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            tries += 1
            driver.refresh()

        # indicamos q mientras la variable found se mantenga en falso, estaremos refrescando la pagina para
        # encontrar el texto correcto
        while not found:
            if text_to_check == correct_text:
                driver.refresh
                found = True

        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo') 


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    # unittest.main(verbosity= 2)
    unittest.main()