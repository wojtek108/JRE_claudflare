from bs4 import BeautifulSoup
from datetime import date
import requests

url = "https://www.jrepodcast.com/"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'}

res = requests.get(url, headers=headers, timeout=30).text

soup = BeautifulSoup(res, 'lxml')
dates = soup.find_all('time', attrs= {'class' : 'entry-date published'})
titles = soup.find_all('h3', attrs= {'class' : 'card__title'})
intro = soup.find_all('div', attrs= {'class' : 'card__excerpt'})

if not (titles and intro and dates):
    raise SystemExit("Scrape failed: no episodes found - site structure changed or bot-blocked. Not writing output.")


with open('scrape.html', 'w') as file:
    file.write("<!DOCTYPE html>\n")
    file.write("<html lang=\"en\">\n")
    file.write("<head>\n")
    file.write("    <meta charset=\"UTF-8\">\n")
    file.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    file.write("    <title>Recent Joe Rogan Experience Episodes</title>\n")
    file.write("    <style>\n")
    file.write("        body {\n")
    file.write("            font-family: Arial, sans-serif;\n")
    file.write("            margin: 20px;\n")
    file.write("        }\n")
    file.write("        h1 {\n")
    file.write("            font-size: 24px;\n")
    file.write("            margin-bottom: 20px;\n")
    file.write("        }\n")
    file.write("        h3.card__title {\n")
    file.write("            margin: 0;\n")
    file.write("            font-size: 20px;\n")
    file.write("        }\n")
    file.write("        .card__excerpt {\n")
    file.write("            margin: 5px 0;\n")
    file.write("        }\n")
    file.write("        time {\n")
    file.write("            color: #999;\n")
    file.write("            font-size: 14px;\n")
    file.write("        }\n")
    file.write("        hr {\n")
    file.write("            margin: 30px 0;\n")
    file.write("        }\n")
    file.write("    </style>\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("    <h1>Recent Joe Rogan Experience Episodes:</h1>\n")
    file.write("    <hr>\n")
    for title, excerpt, date_el in zip(titles, intro, dates):
        file.write(str(title) + '\n')
        file.write(str(excerpt) + '\n')
        file.write(str(date_el) + '\n')
        file.write('<br>')
        file.write('<br>')

today = date.today()
date_format = today.strftime('%Y.%m.%d')

file = open('scrape.html', 'a')
file.write('<hr>')
file.write('\nLast checked: ')
file.write(date_format)
file.write("</body>\n")
file.write("</html>\n")
file.close()


scrape = open('scrape.html', 'r')
scrape_content = scrape.read()
index = open('index.html', 'w+')
index_content = index.read()


if not (bool(scrape_content == index_content)):
    index.write(scrape_content)

index.close()
scrape.close()

