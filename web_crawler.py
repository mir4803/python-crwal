from flask import Flask, request, render_template, redirect, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    # Render the index page with an empty form
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def crawl():
    url = "https://news.naver.com/section/100"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []
    for item in soup.select('div.sa_text'):
        title_tag = item.find('a', class_='sa_text_title')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            articles.append({'title': title, 'link': link})

    # Redirect to the index page with articles
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
