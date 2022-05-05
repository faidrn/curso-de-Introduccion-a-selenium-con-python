# Archivo donde estara el test suite(agrupacion de los archivos de pruebass)
from unittest import TestLoader, TestSuite
# para generar el reporte
from pyunitreport import HTMLTestRunner
# llamar archivos de prueba y las clases de prueba
from assertions import AssertionsTest
from search_tests_assertions import SearchTests

# variables con las cuales se cargan los casos de prueba
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# construir la suite de pruebas a traves del codigo
# Como parametro se pasa la lista de las variables donde se cargaron las pruebas
smoke_test = TestSuite([assertions_test, search_test])

# parametros para generar el reporte (a traves de un diccionario)
kwargs = {
    "output": 'smoke-report'
}

# variable a la que se le pasa el test runner con los argumentos para que se genere el reporte
runner = HTMLTestRunner(**kwargs)
# corremos el runner llamando a la suite de testing
runner.run(smoke_test)
