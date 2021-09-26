import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class HomePageTests(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        driver=self.driver
        driver.get('https://qaclubcare.dinersclubperu.pe/')
        driver.maximize_window() 
    
    #probar buscador
    #def test_search_text_field_by_name(self):
    #    search_field=self.driver.find_elements_by_name("buscador")
    #probar boton VerPlanes
    def test_verplanes_button_enabled(self):
        button=self.driver.find_element_by_class_name("btnPlanes")
    #Validar n° de seguros
    def test_count_of_insurance_nav(self):
        insurance_list=self.driver.find_element_by_class_name("boxMenuPC")
        insurance=insurance_list.find_elements_by_tag_name('li')
        self.assertEqual(16,len(insurance))

    def tearDown(self):
       self.driver.quit()
       

if __name__=="__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes',report_name='find-element-report'))
