import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# de la libreria ddt extraemos los submodulos ddt, data, unpack
# q nos permiten utilizar ddt con datos q vamos a designar y desempaquetarlos
# de las tuplas donde estan
from ddt import ddt, data, unpack


# usamos el decorador ddt
@ddt
class SearchDDT(unittest.TestCase):
    # clase de prueba

    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    # decoradores
    # data va a incluir tuplas con los terminos a buscar y la cantidad de 
    # elementos q esperamos como resultado
    # (elemento a buscar, cantidad de elementos esperados como resultado)
    @data(('dress', 5), ('music', 5))
    # usamos el decorador unpack para desempaquetar las tuplas incluidas en 
    # data y asi poder consultarlas de forma individual
    @unpack

    def test_search_ddt(self, search_value, expected_count):
        # search_value = valor de la busqueda
        # expected_count = cantidad de resultados q esperamos encontrar
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear() # limpiamos la barra de busqueda en caso de q tenga algo escrito
        search_field.send_keys(search_value) # simulamos el ingreso de datos por teclado, enviando los valores almacenados en la variable
        search_field.submit() # enviamos para q aparezca los resultados de busqueda

        # identificamos donde estan los productos
        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        # validar q este correcto
        print(f'Found {len(products)} products')

        # imprimimos el nombre de cada uno de los productos, para estar seguros
        for product in products:
            print(product.text)

        # indicamos q es lo q esperabamos encontrar
        self.assertEqual(expected_count, len(products))


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main()