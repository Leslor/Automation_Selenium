import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from selenium.webdriver.common.by import By
import time

class ImportNewFile(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        driver=self.driver
        driver.implicitly_wait(30)
        
    def test_cargar_archivo(self):
        
        self.driver.get('https://qacci.dinersclubperu.pe/interno')
        time.sleep(4)

        #LogIn Process
        user=self.driver.find_element_by_id('exampleEmail')
        user.send_keys('cci@dinersclub.pe')
        time.sleep(4)

        password=self.driver.find_element_by_id('examplePassword')
        password.send_keys('123456')
        time.sleep(4)

        button=self.driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/button')
        button.click()
        time.sleep(4)

        #Import Process
        import_button=self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/a')
        import_button.click()
        time.sleep(4)
        date=datetime.today().strftime('%Y-%m-%d')
        archivo_name="Compras refinanciados import -"+date+'.xlsx'
        archivo="C:\\Users\\Lenovo\\Desktop\\DinersClub\\CSI_TO_CCI\\SFTP\\"+archivo_name
        select_file=self.driver.find_element_by_xpath('//*[@id="fileExcel"]').send_keys(archivo)
        time.sleep(5)
        save_button=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        save_button.click()
        time.sleep(5)
        ok1_button=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div[2]/button')
        ok1_button.click()
        time.sleep(5)
        ok2_button=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/button')
        ok2_button.click()


        def tearDown(self):
            self.driver.close()

if __name__=='__main__':
    unittest.main()


