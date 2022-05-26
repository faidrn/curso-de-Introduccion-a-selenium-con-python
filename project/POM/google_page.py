from selenium import webdriver 
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage(object):
    # inicializamos la clase (constructor)
    def __init__(self, driver):
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'  # barra de busqueda


    # propiedades
    @property  #decorador
    def is_loaded(self):
        # metodo para verificar q el sitio web ha cargado correctamente

        # espera explicita, donde el driver espera 10 segundos hasta que la condicion esperada se
        # cumpla, en este caso sera la presencia del elemento ubicado por su nombre que es 'q'
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

        return True # indica q la carga del sitio ha sido verdadera


    @property
    def keyword(self):
        # ubicamos el campo de busqueda
        input_field = self._driver.find_element_by_name('q')

        return input_field.get_attribute('value')


    def open(self):
        # metodo para ingresar a la url
        self._driver.get(self._url)


    def type_search(self, keyword):
        # metodo para buscar terminos
        input_field = self._driver.find_element_by_name('q')
        input_field.send_keys(keyword)

    
    def click_submit(self):
        # metodo q hace el envio del termino de busqueda
        
        input_field = self._driver.find_element_by_name('q')
        input_field.submit()


    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit