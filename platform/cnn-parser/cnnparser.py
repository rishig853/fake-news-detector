import requests
from bs4 import BeautifulSoup

valid = False
while valid == False:
    URL = input('Enter a valid CNN article URL: ')
    try:
        URL.index('https://')
    except ValueError:
        URL = 'https://' + URL
    try:
        URL.index('cnn.com')
    except ValueError:
        print('Not a valid link.')
        continue

        page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        title = soup.find('h1', class_='pg-headline').text
        content = soup.find_all(class_='zn-body__paragraph')
        valid = True
    except:
        print('Not a valid article.')


text = ''
for paragraph in content:
    text+=paragraph.text


print(title)
print(text)


