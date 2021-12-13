import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
import os
import shutil


class ExportNewFile(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://qacci.dinersclubperu.pe/interno')

    def test_new_user(self):
        driver =self.driver
        #Find the ACCOUNT button
        
        user=driver.find_element_by_id('exampleEmail')
        
        user.send_keys('cci@dinersclub.pe')
        sleep(30)
        password=driver.find_element_by_id('examplePassword')
        
        password.send_keys('123456')
        sleep(30)
        button=driver.find_element_by_xpath('//*[@id="formLogin"]/div[3]/div/button')
        sleep(10)
        #Click in Log In
        button.click()
        sleep(20)
        export_button=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/a')
        sleep(10)
        export_button.click()
        sleep(10)

  
    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.close()
        date=datetime.today().strftime('%Y-%m-%d')
        archivo_name="Compras refinanciados -"+date+'.xlsx'
        path="C:\\Users\\Lenovo\\Downloads\\"
        ruta_SFTP="C:\\Users\\Lenovo\\Desktop\\DinersClub\\CSI_TO_CCI\\SFTP"
        path="C:\\Users\\Lenovo\\Downloads\\"+archivo_name
        dest=shutil.move(path, ruta_SFTP)


if __name__=="__main__":
    unittest.main(verbosity=2)
    
    



        


