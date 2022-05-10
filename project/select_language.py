import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
#submodulo  para usar el dropdown
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        # le indicamos q espere 30 segundos antes de cerrar la ventana
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("http://demo-store.seleniumacademy.com/")


    def test_select_language(self):
        # creamos una lista con las opciones del select, el orden respeta como aparecen en la página
        exposed_options = ['English', 'French', 'German']
        # creamos una lista vacia, para almacenar las opciones que elijamos
        active_options = []

        #acceder a las opciones del dropdown
        select_language = Select(self.driver.find_element_by_id('select-language'))

        # validar q el dorpdown realmente tenga las tres opciones, 
        # para comprobar que si esté la cantidad de  opciones correcta 
        # 'options' permite ingresar directamente a las opciones del dropdown
        self.assertEqual(3, len(select_language.options))

        # iteramos por cada opcion q tiene el dropdown
        for option in select_language.options:
            active_options.append(option.text)

        # verificamos q la lista de las opciones expuestas y la activa sean las mismas
        self.assertListEqual(exposed_options, active_options)

        # seleccionar uno de los idiomas
        #verificamos q la palabra English sea la primera opcion q parece en el dropdown
        self.assertEqual('English', select_language.first_selected_option.text)

        # indicamos a selenium q ahora seleccione el idioma aleman
        select_language.select_by_visible_text('German')

        # verificamos q realmente este en aleman
        self.assertTrue('store=german' in self.driver.current_url)

        # otra opcion para elegir un idioma (a traves del indice)
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity= 2)