import unittest
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


class HomePageTest(unittest.TestCase):
    # clase de prueba
    
    def setUp(self):
        # metodo de la clase
        #self.driver = webdriver.Chrome(executable_path = './chromedriver')  # no funciona
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        # le indicamos q espere 15 segundos antes de cerrar la ventana
        driver.implicitly_wait(15)


    def test_search_text_field(self):
        # metodo de la clase
        # metodo de prueba
        # indicar el elemento a buscar
        search_field = self.driver.find_element_by_id("search")


    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")


    def test_search_text_field_by_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")


    def test_search_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")


    def test_count_of_promo_banner_images(self):
        # lista de elementos
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        # validacion para verificar que una condicion se cumple o no
        self.assertEqual(3, len(banners))


    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[3]/a/img')


    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")


    def tearDown(self):
        # metodo de la clase
        # le indicamos al navegador que cierre la ventana o cualquier sesion q tenga iniciada
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity= 2)