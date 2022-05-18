import imp
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
        driver.find_element_by_link_text('Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver

        # elementos q vamos a agregar
        elements_added = int(input('How many elements will you add?: '))
        # elementos q vamos a remover
        elements_removed = int(input('How many elements will you remove?: '))
        total_elements = elements_added - elements_removed

        # agregamos los elementos de acuerdo a la cantidad indicada
        for i in range(elements_added):
            driver.execute_script("addElement()")
        
        # agregamos una espera en segundos para q el script se detenga un momento antes de continuar
        sleep(3)

        # removemos la cantidad de elementos indicados
        for i in range(elements_removed):
            # usamos un try y un except para evitar errores por eliminar mas elementos de los q tenemos
            try:
                driver.execute_script("deleteElement()")
            except:
                print("You're triying delete more elements than the existents")
                break
        
        # agregamos una espera en segundos para q el script se detenga un momento antes de continuar
        sleep(3)

        # mostramos en consola lo q ocurrio al final
        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print('There are 0 elements on screen')

        # agregamos una pausa de 3 segundos para ver lo q ocurre
        sleep(3)


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity= 2)