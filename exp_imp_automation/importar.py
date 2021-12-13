import unittest
import configparser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
#from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException
import shutil
class ImportNewFile(unittest.TestCase):

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
        
    def test_cargar_archivo(self):
        
        #LogIn Process
        user=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID,'exampleEmail' )))
        user.send_keys(self.email)
            
        password=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,'examplePassword')))
        password.send_keys(self.password)

        sleep(2)
        enter_button=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="formLogin"]/div[3]/div/button')))
        enter_button.click()
               
        sleep(5)

        #Import Process
        """Consideraciones:
            1. Usar explicity Explicity_Wait
            2. Usar try Expecto para el manejo de Errores de cada boton
            3. Cambiar XPATH por id, solicitar los cambios
        """
        import_button=self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/a')
        import_button.click()
        sleep(4)
        archivo_name=self.file_name+"B_Carga.xlsx"
        archivo="C:\\Users\\Lenovo\\Desktop\\DinersClub\\CSI_TO_CCI\\SFTP\\"+archivo_name
        select_file=self.driver.find_element_by_xpath('//*[@id="fileExcel"]').send_keys(archivo)
        sleep(3)
        save_button=self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        save_button.click()
        sleep(3)
        #Está seguro de crear este registro de excel?
        ok1_button=self.driver.find_element_by_xpath('/html/body/div[5]/div/div[4]/div[2]/button')
        ok1_button.click()
        sleep(3)
        #Porque hacer un Try, si este boton nos da la confirmacion de uqe todo se ha subido 
        try:
            ok2_button=self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/button')
            ok2_button.click()
        except NoSuchElementException:
            print("The file has not finished uploading, please check the system")


        def tearDown(self):
            self.driver.close()

if __name__=='__main__':
    unittest.main()


