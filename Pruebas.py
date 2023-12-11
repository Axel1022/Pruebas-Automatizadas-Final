import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from Utils import Utils
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUserCRUD:
    @pytest.fixture

    def setup(self):
        url = "http://localhost/Atlantis-System-main//login.php"
        path_driver = os.chdir(r"C:\chrome")
        chrome_options = Options()
        chrome_options.add_argument("C:\\path\\to\\chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)

        yield

        self.driver.quit()

    def InicioSeccion(self):

        Element_Btn_Usuario = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[2]/input'))
        )
        Utils.escribir(Element_Btn_Usuario, "G_Campusano")

        Element_TB_COntraceña = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[2]/input'))
        )
        Utils.escribir(Element_TB_COntraceña, "123456789")

        Element_Btn_Acceder = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/button')
        Element_Btn_Acceder.click()
    def InicioSeccionF(self):

        Element_Btn_Usuario = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[2]/input'))
        )
        Utils.escribir(Element_Btn_Usuario, "G_Campusano Fail User")

        Element_TB_COntraceña = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[2]/input'))
        )
        Utils.escribir(Element_TB_COntraceña, "123456789")

        Element_Btn_Acceder = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/button')
        Element_Btn_Acceder.click()
    def InicioSeccionR(self):

        Element_Btn_Usuario = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[1]/div[2]/input'))
        )
        Element_Btn_Usuario.send_keys("G_Campusano")

        Element_TB_COntraceña = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div[2]/input'))
        )
        Element_TB_COntraceña.send_keys("123456789")

        Element_Btn_Acceder = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/button')
        Element_Btn_Acceder.click()



    def test_Login(self, setup):
       self.InicioSeccion()

    def test_Login_Feil(self, setup):
       self.InicioSeccionF()

    def test_NewCita(self, setup):

        self.InicioSeccion()

        #lateral
        #/html/body/div[1]/div[1]/div/button[1]

        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/appointment.php"
        self.driver.get(AgregarCitasURl)

        #Boton Nuevo
        #/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/a

        self.driver.find_element(By.LINK_TEXT, "Nuevo").click()

        #
        dates_input = WebDriverWait(self.driver, 10).until(

            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[1]/div/input'))
        )
        dates_input.send_keys("12/12/2023")
        hora_input = WebDriverWait(self.driver, 10).until(

            EC.element_to_be_clickable((By.NAME, "hour"))
        )
        hora_input.send_keys("15/54")

        self.driver.find_element(By.ID, "paciente").click()
        dropdown = self.driver.find_element(By.ID, "paciente")
        dropdown.find_element(By.XPATH, "//*[@id='paciente']/option[2]").click()

        self.driver.find_element(By.ID, "continentes").click()
        dropdown = self.driver.find_element(By.ID, "continentes")
        dropdown.find_element(By.XPATH, "//*[@id='continentes']/option[4]").click()

        self.driver.find_element(By.ID, "paises").click()
        dropdown = self.driver.find_element(By.ID, "paises")
        dropdown.find_element(By.XPATH, "//*[@id='paises']/option[2]").click()
        self.driver.find_element(By.NAME, "agregar").click()

    def test_NewCita_Fail(self, setup):

        self.InicioSeccion()

        #lateral
        #/html/body/div[1]/div[1]/div/button[1]

        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/appointment.php"
        self.driver.get(AgregarCitasURl)

        #Boton Nuevo
        #/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/a

        self.driver.find_element(By.LINK_TEXT, "Nuevo").click()

        #
        dates_input = WebDriverWait(self.driver, 10).until(

            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[1]/div/input'))
        )
        dates_input.send_keys("12/12/2023")
        hora_input = WebDriverWait(self.driver, 10).until(

            EC.element_to_be_clickable((By.NAME, "hour"))
        )
        hora_input.send_keys("")

        self.driver.find_element(By.ID, "paciente").click()
        dropdown = self.driver.find_element(By.ID, "paciente")
        dropdown.find_element(By.XPATH, "//*[@id='paciente']/option[2]").click()

        self.driver.find_element(By.ID, "continentes").click()
        dropdown = self.driver.find_element(By.ID, "continentes")
        dropdown.find_element(By.XPATH, "//*[@id='continentes']/option[4]").click()

        self.driver.find_element(By.ID, "paises").click()
        dropdown = self.driver.find_element(By.ID, "paises")
        dropdown.find_element(By.XPATH, "//*[@id='paises']/option[2]").click()
        self.driver.find_element(By.NAME, "agregar").click()


    def test_agregarPaciente(self, setup):
        self.InicioSeccionR()
        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/customers.php"
        self.driver.get(AgregarCitasURl)

        self.driver.find_element(By.LINK_TEXT, "Nuevo").click()

        #DNI
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/form/div/div[1]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "010203")
        #NOMBRE
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[2]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "Gary Alexander")
        #Apellido
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[3]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "Campusano Paredes")
        #Telefono
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[5]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "8090000000")
        #User
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[7]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "User Nuevo")
        #Pass
        elemento_user = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[1]/div/form/div/div[8]/div/input'))
        )
        elemento_user.click()
        Utils.escribir(elemento_user, "123456789")

        #Guardar
        #//*[@id="addRowModal"]/div/div/div[2]/div[2]/button[2]

        Element_Btn_Crear = self.driver.find_element(By.XPATH, '//*[@id="addRowModal"]/div/div/div[2]/div[2]/button[2]')
        Element_Btn_Crear.click()

    def test_CambiarStadoCita(self, setup):

        self.InicioSeccionR()

        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/appointment.php"
        self.driver.get(AgregarCitasURl)

        time.sleep(5)

        Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[4]/div[2]/div/table/tbody/tr/td[7]/form/button')

        #/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[13]/div[2]/div/table/tbody/tr[4]/td[7]/form/button
        #/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div[16]/div[2]/div/table/tbody/tr[5]/td[7]/form/button
        Element_Btn_SwEstado.click() 

    def test_DesactivarPaciente(self, setup):

            self.InicioSeccionR()

            AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/customers.php"
            self.driver.get(AgregarCitasURl)

            time.sleep(5)

            Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[6]/form/button')
            Element_Btn_SwEstado.click()
    def test_ActivarPaciente(self, setup):

            self.InicioSeccionR()

            AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/customers.php"
            self.driver.get(AgregarCitasURl)

            time.sleep(5)

            Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[6]/form/button')
            Element_Btn_SwEstado.click()


    def test_DesCargarPDF(self, setup):

        self.InicioSeccionR()

        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/specialty.php"
        self.driver.get(AgregarCitasURl)

        time.sleep(5)

        Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[2]/a')
        Element_Btn_SwEstado.click()


    def test_NewAreaMedica(self, setup):

        self.InicioSeccionR()

        AgregarCitasURl = "http://localhost/Atlantis-System-main//folder/specialty.php"
        self.driver.get(AgregarCitasURl)

        Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/a')
        Element_Btn_SwEstado.click()

        elemento_Nombre = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/form/div[1]/div/div/input'))
        )
        elemento_Nombre.click()

        Utils.escribir(elemento_Nombre ,"Neurocirugía" )

        Element_Btn_SwEstado = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/form/button')
        Element_Btn_SwEstado.click()



if __name__ == "__main__":
    pytest.main(args=["-v", "Pruebas.py", "--html=report.html"])
