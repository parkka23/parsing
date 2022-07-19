import requests
from bs4 import BeautifulSoup
from save_data import write_to_csv

MAIN_URL='https://www.kivano.kg/noutbuki'
PAGES=10
IMAGE_LINK='https://www.kivano.kg'

# запрос 
def open_page(url):
    response = requests.get(url)
    return response.text

# принять код страници, анализировать и подготавливать к парсингу
def analyze_page_content(page_content):
    soup=BeautifulSoup(page_content, 'lxml')
    return soup

# обработка супа
# div - tag
def get_product_cards(soup):
    listing=soup.find('div',id='w0')
    product_cards=listing.find_all('div',class_='item product_listbox oh')
    return product_cards

def get_data_from_card(card):
    title=card.find('div',class_='listbox_title').find('a').text
    describtion=card.find('div',class_='product_text').text.replace(title,'')
    price=card.find('div',class_='listbox_price').find('strong').text
    image=f"{IMAGE_LINK}{card.find('img').get('src')}"
    return {
        'title':title,
        'describtion':describtion,
        'price':price,
        'image':image
    }

def parse():
    total_product_cards=[]
    for page in range(1,PAGES+1):
        page_url=f'{MAIN_URL}?page={page}'
        content=open_page(page_url)
        soup=analyze_page_content(content)
        product_cards=get_product_cards(soup)
        total_product_cards.extend(product_cards)

    data=[]
    for card in total_product_cards:
        data.append(get_data_from_card(card))
        #print(data)

    write_to_csv(data)

    #print(len(data))

if __name__=='__main__':
    parse()


# TODO: написать функцию для нахождения последней страницы


