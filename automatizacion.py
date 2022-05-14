from lib2to3.pgen2 import driver
from selenium  import webdriver

sitioweb = "https://dimayor.com.co/liga-betplay-dimayor/"
 
ruta = "C:\msedgedriver.exe"

driver = webdriver.Edge(ruta)
driver.get(sitioweb)

clubesBoton = driver.find_element_by_css_selector("#menu-item-1414 >a")
clubesBoton.click()

clubesLiga = driver.find_element_by_css_selector("#menu-item-1427 >a")
clubesLiga.click()

BotonAlianzaPetrolera = driver.find_element_by_css_selector("#esg-grid-4-1>div>ul>li.filterall.filter-liga-aguila.filter-2019-2.filter-daniel-villa-zapata.eg-washington-wrapper.eg-post-id-1556.tp-esg-item.itemtoshow.loadedmedia.isvisiblenow>div>div.esg-entry-cover")
BotonAlianzaPetrolera.click()

BtnPresidente =  driver.find_element_by_xpath('//*[@id="tab-ada5427d-dcd9-7789f-cbc586cf-1729"]/div/div[1]/div/div/div[1]/div/h3[1]')
print('el presidente del Alianza pretrolera es: '+ BtnPresidente.text)

