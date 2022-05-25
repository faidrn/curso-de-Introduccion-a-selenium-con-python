import csv, unittest
from email import message
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# de la libreria ddt extraemos los submodulos ddt, data, unpack
# q nos permiten utilizar ddt con datos q vamos a designar y desempaquetarlos
# de las tuplas donde estan
from ddt import ddt, data, unpack


# funcion para consultar el archivo csv
def get_data(file_name):
    rows = []  # lista para indicar el numero de filas q hay
    # indicamos q se va a abrir el archivo en modo lectura ('r')
    data_file = open(file_name, 'r')
    # leemos los datos del archivo
    reader = csv.reader(data_file)
    # con el metodo next indicamos q pase a la siguiente fila de datos, ya 
    # q se omite la cabecera
    next(reader, None)

    # indicamos q la fila en reader se va a agregar a una lista en filas
    for row in reader:
        rows.append(row)

    # retornamos el valor de rows
    return rows


# usamos el decorador ddt
@ddt
class SearchCsvDDT(unittest.TestCase):
    # clase de prueba

    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")

    # decoradores
    # data va a incluir como argumento la funcion q lee el archivo csv
    @data(*get_data('testdata.csv'))
    # usamos el decorador unpack obtener la informacion q se esta extrayendo del archivo csv
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
        
        # convertimos los datos de la variable a enteros, para evitar conflictos
        expected_count = int(expected_count)

        # verificamos q expected_count sea mayor a 0 antes de mostrar los resultados
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            # verificamos q no hay productos
            self.assertEqual('Your search returns no results.', message)

        print(f'Found {len(products)} products')


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main()