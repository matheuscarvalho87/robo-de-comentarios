from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random 

class InstagramBot:
  def __init__(self,username,password):
    self.username = username
    self.password = password
    self.driver = webdriver.Firefox(executable_path='C:/Users/usuario/Desktop/geckodriver-v0.29.0-win64/geckodriver.exe')

  def login(self):
    driver=self.driver
    driver.get('https://www.instagram.com')
    time.sleep(5)
    campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
    campo_usuario.click()
    campo_usuario.clear()
    campo_usuario.send_keys(self.username)
    
    campo_password = driver.find_element_by_xpath("//input[@name='password']")
    campo_password.click()
    campo_password.clear()
    campo_password.send_keys(self.password)
    campo_password.send_keys(Keys.RETURN)
    time.sleep(8)

    self.comente_nas_fotos('sorteio')
  
  @staticmethod
  def digite_como_uma_pessoa(frase,onde_digitar):
    for letra in frase:
      onde_digitar.send_keys(letra)
      time.sleep(random.randint(1,5)/30)

  def comente_nas_fotos(self,hashtag):
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
    for i in range(1,3):
      driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
      time.sleep(5)
    
    hrefs = driver.find_elements_by_tag_name('a')
    pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
    [href for href in pic_hrefs if hashtag in href]
    print(hashtag + ' fotos ' + str(len(pic_hrefs)))

    for pic_href in pic_hrefs:
      driver.get(pic_href)
      driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
      try:
        comentarios =["@silveirajv_","@djalexreisoficial"]
        driver.find_element_by_class_name('Ypffh').click()
        campo_comentario=driver.find_element_by_class_name('Ypffh')
        time.sleep(random.randint(2,5))
        for coment in comentarios:
          self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
          time.sleep(random.randint(2,5))
          driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
          time.sleep(5)
      except Exception as e:
        print(e)
        time.sleep(3)



instaBot = InstagramBot('#coloca a conta aqui#','#coloca as senha aqui#')
instaBot.login()