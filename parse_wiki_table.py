import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

# Import our layout
from res.layout.tablet_layout import TabletViewWindow


# Function for start parse data from table from page and open
# new window with table preview
def start_parse(url, window):
    result = requests.get(url)
    if result.status_code == 200:
        tables_list = parse_res_content(data=result.text)
        if not tables_list:
            show_tablet_view(window=window, data= tables_list)


# Function for read content
def parse_res_content(data):
    soup = bs(data, "html.parser")
    title_page = soup.title.string
    all_page_table = soup.find_all("table", {"class": "wikitable"})
    table_data_frames_list = []
    if len(all_page_table) > 1:
        for index in range(0, len(all_page_table)):
            text_table = all_page_table[index]
            text_table.text.replace(r"\[.*\]", "")
            if len(text_table.text.strip()) == 0:
                continue

            df = pd.read_html(str(all_page_table[index]))
            df = df[0].dropna(axis=1, how="all")
            table_data_frames_list.append(df)
        # for element in table_data_frames_list:
        #     print("*******")
        #     print(element)

    elif len(all_page_table) == 1:
        df = pd.read_html(str(all_page_table[0]))
        df = df[0].dropna(axis=1, how="all")
        table_data_frames_list.append(df)


    # Function for view tablet save page
def show_tablet_view(window, data):
    if window.isVisible():
        window.hide()
    else:
        window.show()
        window.view_tabel(tabel_list=data)

