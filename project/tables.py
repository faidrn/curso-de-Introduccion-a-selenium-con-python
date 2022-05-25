import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
# librearia para ver tablas en consola
from prettytable import PrettyTable


class Tables(unittest.TestCase):
    # clase de prueba

    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com/")
        driver.find_element_by_link_text('Sortable Data Tables').click()


    def test_sort_tables(self):
        driver = self.driver
        rows = []
        pretty_table = PrettyTable()

        # iteramos por cada uno de la headers y por cada uno de los datos
        # ciclo q recorre las columnas
        for i in range(5): 
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')

            # ciclo q recorre las filas (usamos 4 porque hay 4 filas)
            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                # agregamos el dato obtenido con row_data a la lista 
                rows.append(row_data.text)
                
            pretty_table.add_column(header.text, rows)
            rows.clear()
            
        # imprimimos la tabla
        print(pretty_table)


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    unittest.main()