#crear el archvio .ini desde un .py

import configparser
"""
Parsear una configuracion para despues grabarla en un archivo 
en el que le daremos la extencion que se desee
"""
configuracion=configparser.ConfigParser()

configuracion['General']={'chrome':'C:\\Users\\Lenovo\\Documents\\testing_with_Selenium\\exp_imp_automation\\chromedriver.exe'}
configuracion['Paginas']={'page':'https://pagewithoutacces.com'}
configuracion['Credentials']={'email':'mail@example.com' ,'password':'1@******'}
configuracion['File_dowloaded']={'name':'C:\\Users\\Lenovo\\Downloads\\'}
configuracion['sftp']={'path':'C:\\Users\\Lenovo\\Desktop\\SFTP\\'}


with open('configuracion.ini','w') as archivoconfig:
    configuracion.write(archivoconfig)

