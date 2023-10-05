import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# Function for start parse data from table from page and open
# new window with table preview
def start_parse(url):
    result = requests.get(url)
    if result.status_code == 200:
        parse_res_content(data=result.text)


# Function for read content
def parse_res_content(data):
    soup = bs(data, "html.parser")
    title_page = soup.title.string
    all_page_table = soup.find_all("table", {"class": "wikitable"})
    # for index in range(0, len(all_page_table)):
    #     df = pd.read_html(str(all_page_table[index]))
    #     print(df)
    test = re.sub(r'<.*?>', lambda g: g.group(0).upper(), data)
    df = pd.read_html(str(test), header=0, parse_dates=True)
    print(df)
    # print(all_page_table)
