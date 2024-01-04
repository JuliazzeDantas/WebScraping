from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import xpath_site
import json
import time

url_t = 'https://www.amazon.com.br/s?k=tablet+samaung+fe+lil%C3%A1s&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3JXWQC5DSOIG5&sprefix=tablet+samaung+fe+lil%C3%A1%2Caps%2C240&ref=nb_sb_noss'

#amazon = Amazon()
 
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = service)
wait = WebDriverWait(driver, 10)

driver.get(url_t)

item_name = ''
item_price = ''
item_shipping = ''
item_date = ''
item_url = ''

final_list = []

def get_name(attribute_list, initial_count):
    if (attribute_list[initial_count] == 'Patrocinado') or (attribute_list[initial_count] == 'Escolha da Amazon') or (attribute_list[initial_count] == 'Mais vendido') or (attribute_list[initial_count] == 'Pesquisas relacionadas') or (attribute_list[initial_count] == 'Mais vendido'):
        item_name = attribute_list[initial_count + 1]
    else:
        item_name = attribute_list[initial_count] 
    
    return item_name


def get_shipping(item_box):
    return item_box.find_element(By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'frete')]").text


def get_url(item_box):
    return item_box.find_element(By.TAG_NAME, 'a').get_attribute('href')


def get_price(initial_count, attribute_list):
    for item_count in range(initial_count + 1,len(attribute_list)):
        if ('R$' in attribute_list[item_count]) == True and (',' in attribute_list[item_count]) == False:
            item_price = attribute_list[item_count] + '.' + attribute_list[item_count  + 1][:2]
            item_price = item_price.replace("R$", '')

    return item_price


def get_date(initial_count,attribute_list):
    for item_count in range(initial_count + 1,len(attribute_list)):
        if ('RECEBA' in attribute_list[item_count].upper()):
            item_date = attribute_list[item_count].upper()
            item_date = item_date.replace('RECEBA ATÉ ', '').replace('RECEBA ', '')

def return_list_itens(attribute_list, item_box):
    global final_list

    initial_count = 0

    item_name = get_name(attribute_list, initial_count)   
    item_price = get_price(initial_count, attribute_list)

    item_date = get_date(initial_count,attribute_list)
        
    item_shipping = get_shipping(item_box)
    item_url = get_url(item_box)

    if (item_name == '*******************************') or (item_price == '*******************************') or (item_date == '*******************************') or (item_shipping == '*******************************') or (item_url == '*******************************'):
        print("RASPAGEM COM DEFEITO")

        print(attribute_list)
    if (item_name != '') or (item_price != '') or (item_date != '') or (item_shipping != '') or (item_url != ''):
        item_key = {'name' : item_name, 'price' : item_price, 'date' : item_date, 'shipping' : item_shipping, 'url' : item_url, 'page' : 'Amazon'}
    
    return item_key

def search_itens(first_page):
    
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div')))
    for count in range(3,62):

        item_name = '*******************************'
        item_price = '*******************************'
        item_date = '*******************************'
        item_shipping = '*******************************'
        item_url = '*******************************'

        print(f'Item {count}')
        
        path = f'/html/body/div[1]/div[1]/div[1]/div[1]/div/span[1]/div[1]/div[{count}]/div'

        item_box = driver.find_element(By.XPATH, path)
  
        attribute_list = item_box.text.split('\n')
        if ('Não disponível.' in attribute_list) or ('Nenhuma opção de compra em destaque' in attribute_list):
            print("PRODUTO NÃO DISPONÍVEL OU INVÁLIDO")
        else:
            try:
                item_key = return_list_itens(attribute_list, item_box)
                final_list.append(item_key)
                print(item_key['name'])
            except Exception:
                print(attribute_list)
                print(Exception)
                while True:
                    x = 1

def verify_button_next_page():
    wait.until(EC.presence_of_element_located((By.XPATH, "//*[text() = 'Próximo']")))
    if driver.find_element(By.XPATH, "//*[text() = 'Próximo']").get_attribute('aria-disabled'):
        print("Não há mais páginas")
        return 0
    else:
        driver.find_element(By.XPATH, "//*[text() = 'Próximo']").click()
        print("Indo para a próxima página")
        return 1

def main():
    global final_list
    flag = True
    while True:
        search_itens(flag)
        if verify_button_next_page() == 0:
            break
        flag = False

    print(json.dumps(final_list))


main()
