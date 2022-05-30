from time import sleep
import unittest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class TestingMercadoLibre(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("https://www.mercadolibre.com/")
        driver.maximize_window


    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()

        search_field = driver.find_element_by_name('as_word')
        search_field.click()  # hacemos clic en la barra de busqueda para ubicarnos en ella
        search_field.clear()  # limpiamos cualquier texto q pueda haber en la barra de busqueda
        search_field.send_keys('playstation 4')  # enviamos el texto de busqueda
        search_field.submit()  # usamos submit para hacer la busqueda
        sleep(3)  # pausa de 3 segundos

        location = driver.find_element_by_partial_link_text('Bogotá D.C')
        #location.click()
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        #condition.click()
        driver.execute_script("arguments[0].click();", condition)
        sleep(3)

        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()  # hacemos clic para q despliegue las opciones
        higher_price = driver.find_element_by_css_selector('#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        #higher_price.click()
        driver.execute_script("arguments[0].click();", higher_price)
        sleep(3)

        # listas vacias en las cuales se almacenara la informacion
        articles = []
        prices = []

        for i in range(5):
            # interamos en un rango de 5 elementos, xq solo nos interesa la informacion de 5 elementos
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles, prices)


    def tearDown(self):
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.close()


if __name__ == "__main__":
    # unittest.main(verbosity= 2)
    unittest.main()