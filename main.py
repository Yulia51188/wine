import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

import pandas as pd
from pprint import pprint

FOUNDATION_YEAR = 1920
WINE_FILENAME = 'wine2.xlsx'


def correct_years_form(age):
    last_number = int(age) % 10
    if last_number == 1:
        return "год"
    if last_number == 0 or last_number > 4:
        return "лет"    
    return "года"


def get_wine_record(df, groupby_column):
    cutted_df = df.drop(groupby_column, 1).fillna(value='')
    return cutted_df.to_dict(orient='records')


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

company_age = datetime.date.today().year - FOUNDATION_YEAR
years_form = correct_years_form(company_age)
wine_df = pd.read_excel('wine.xlsx', sheet_name='Лист1')

wine2_df = pd.read_excel('wine2.xlsx', sheet_name='Лист1', na_values='',
    keep_default_na=False)
groupby_column = wine2_df.columns[0]
# print(wine2_df)
wine2_groups = wine2_df.groupby(by=groupby_column).apply(
    lambda x: get_wine_record(x, groupby_column)).to_dict()
# pprint(wine2_groups)

rendered_page = template.render(
    company_age=company_age,
    years_form=years_form,
    # wines=wine_df.to_dict(orient='records')
    wines=wine2_groups
)


with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
