import imp
from optparse import Option
import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class AddRemoveElements(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Disappearing Elements').click()


    def test_name_elements(self):
        driver = self.driver

        # declaracion de variables
        options = [] # lista en la cual se agregaran las opciones q aparecen en el menu
        menu = 5
        tries = 1 # variable q contara los intentos le toman a selenium

        while len(options) < 5:
            # limpiamos lo valores q hay en options
            options.clear()

            # iteramos a traves de la opciones
            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    # agregamos el nombre del elemento a la lista de opciones
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f'Option number {i + 1} is NOT FOUND')
                    tries += 1
                    # refrescamos el navegador
                    driver.refresh()

        print(f'Finished in {tries} tries')


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)