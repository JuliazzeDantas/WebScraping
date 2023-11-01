from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from xpath_site import Amazon

url_t = 'https://www.amazon.com.br/s?k=frigideira&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2AVD4M4EFDU6X&sprefix=frigideira%2Caps%2C201&ref=nb_sb_noss_1'

amazon = Amazon()
 
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service)

item_body1 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div'
item_body2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div'

item_name1 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2'
item_name2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[6]/div/div/div/div/div/div/div[2]/div[1]/h2'
   
item_price1 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/a/span/span[1]'
item_price2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[29]/div/div/div/div/div[2]/div[3]/div'
item_price3 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[25]/div/div/div/div/div/div/div[2]/div[2]/div/div[1]/a/span/span[1]'
    
item_frete1 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div/div[2]/span/span'
item_frete2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[31]/div/div/div/div/div[2]/div[4]/div/div[2]/span/span'
    
item_dead_line1 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div/div[1]/span/span[2]'
item_dead_line2 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[31]/div/div/div/div/div[2]/div[4]/div/div[1]/span'
item_dead_line3 = '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[30]/div/div/div/div/div[2]/div[4]/div/div[1]/span/span[2]'

driver.get(url_t)

item_name = ''
item_price = ''
item_frete = ''

item_bric = []
final_list = []

texto = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[10]/div').text
for count in range(3,50):
    print(f'CONTADOR {count}')
    item_box = driver.find_element(By.XPATH, f'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div').text
    attribute_list = item_box.split('\n')
    print(attribute_list)
    
    initial_count = 0
    
    if (attribute_list[initial_count] == 'Patrocinado') or (attribute_list[initial_count] == 'Escolha da Amazon') or (attribute_list[initial_count] == 'Mais vendido'):
        item_name = attribute_list[initial_count]
    else:
        item_name = attribute_list[initial_count] 
        
    for item_count in range(initial_count + 1,len(attribute_list)):
        if ('R$' in attribute_list[item_count]) == True and (',' in attribute_list[item_count]) == False:
            item_price = attribute_list[item_count] + ',' + attribute_list[item_count  + 1][:2]

        
    print("NOME: " + item_name)
    print("PRICE: " + item_price)

    print("#######################\n")