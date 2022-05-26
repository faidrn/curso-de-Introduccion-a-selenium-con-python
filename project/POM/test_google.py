import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# importamos google_page y le decimos q use la clase GooglePage
from google_page import GooglePage


class GoogleTest(unittest.TestCase):
    # clase de prueba

    @classmethod  # decorador
    def setUp(cls):
        # metodo de la clase
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        #cls.driver = webdriver.Chrome(executable_path = './chromedriver')  # no funciona

    
    def test_search(self):
        google = GooglePage(self.driver)
        # usamos el metodo open de google_page para q reqlice todas las acciones indicadas
        google.open() 
        google.search('Platzi')  # usamos el metodo search de google_page para hacer una busqueda

        # verificamos el keyword q estamos utilizando, lo comparamos con google.keyword
        self.assertEqual('Platzi', google.keyword)


    @classmethod
    def tearDown(cls):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()