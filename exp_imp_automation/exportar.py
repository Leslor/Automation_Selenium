#from io import DEFAULT_BUFFER_SIZE
import unittest
import configparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
#from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
import shutil
import os


class ExportFile(unittest.TestCase):


    def setUp(self):
        configuracion=configparser.ConfigParser()
        configuracion.read('configuracion.ini')
        configuracion.sections()
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        driver=self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        self.page=configuracion['Paginas']['page']
        driver.get(self.page)
        self.password=configuracion['Credentials']['password']
        self.email=configuracion['Credentials']['email']
        self.file_name=configuracion['File_dowloaded']['name']
        self.path=configuracion['sftp']['path']
    
        
    def test_exportProcess(self):

        #LogIn Process

        user=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,'exampleEmail' )))
        user.send_keys(self.email)
            
        password=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'examplePassword')))
        password.send_keys(self.password)

        sleep(2)
        enter_button=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="formLogin"]/div[3]/div/button')))
        enter_button.click()
               
        sleep(5)

        #Proceso Exportación:

        export_button=self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/a')
        export_button.click()
        sleep(4)


    def tearDown(self):
        
        self.driver.close()

    def  test_leaveSFTPrute(self):

        #Cambiar Shutil por os
        archivo=self.file_name+"B_Descarga.xlsx"
        shutil.move(archivo,self.path)


if __name__=="__main__":
    unittest.main(verbosity=2)



        


