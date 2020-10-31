import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  title = 'Brand List'
  theme_array = []

  # Set theme 
  theme = request.args.get('theme', '')
  url = '< SET_URL >' + theme

  resp = requests.get(url)
  content = resp.content

  # Get elements from html data
  soup = BeautifulSoup(content, "lxml")

  # Search and retrieve HTML elements
  td_find = soup.find_all('< SET_HTML_TAGS >')

  # Put the elements taken from the HTML into Company_list and array them.
  for company_list in td_find:
    data_list = []
    theme_array.append(company_list.getText())

  # Arrayed data to the HTML side 
  return render_template('index.html',title = title, theme_array = theme_array) 

if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port='5000')
