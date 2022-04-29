# Con unittest nos podemos traer todas nuestras pruebas
import unittest
# Ayuda a orquestar cada una de las pruebas que estaremos ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner
# Para comunicarnos con el navegador usamos webdriver
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class HelloWorld(unittest.TestCase):
    # Realiza todo lo necesario antes de empezar la prueba
    
    @classmethod # Decorador para que las distintas paginas corran en una sola pestaña
    def setUpClass(cls):
    # def setUp(self): # sin decorador
        # ejecuta todo lo necesario antes de hacer una prueba, 
        # va a preparar el entorno de la prueba misma

        # indicamos que es lo q se va a hacer
        # ruta del driver
        # self se usa sin decorador, con decorador se usa cls
        #self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(executable_path = '/Users/macbook/Documents/CURSOS/Desarrollo Backend con Python y Django/10 Curso de Introducción a Selenium con Python/project/chromedriver')
        # en windows
        # self.driver = webdriver.Chrome(executable_path = r' ruta completa de chromedriver')
        #indicamos q la variable driver es igual a self.driver para no estar escribiendo esta ultima todo el tiempo
        driver = cls.driver
        # se indica al driver q espere implicitamente hasta 10 segundos antes de realizar la sigte acción
        driver.implicitly_wait(10)


    def test_hello_world(self):
        # realiza una serie de acciones para que el navegador las automatice
        
        driver = self.driver
        driver.get('https://www.platzi.com')


    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')


    @classmethod
    def tearDown(cls):
        # acciones para finalizar, por lo gral cerrar la ventana del navegador 
        # y evitar fuga de recursos y q el equipo se pueda poner lento
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2, testRunner= HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))