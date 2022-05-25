import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


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

        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            text_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]').text
            sleep(2) # segundos de pausa para poder notar las vece que se recarga la pagina y contar los intentos como comprobacion manual.

            if text_to_check != correct_text: # este 'if' me permite sumar solo en caso de que no exista coincidencia y solo entonces recarga.
                driver.refresh()
                tries += 1
            
        print(f"It took {tries} tries to find the typo")


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    # unittest.main(verbosity= 2)
    unittest.main()