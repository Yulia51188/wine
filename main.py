import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas as pd
from jinja2 import Environment, FileSystemLoader, select_autoescape

FOUNDATION_YEAR = 1920
WINE_FILENAME = 'file_sample.xlsx'


def correct_years_form(age):
    last_number = int(age) % 10
    if last_number == 1:
        return "год"
    if last_number == 0 or last_number > 4:
        return "лет"    
    return "года"


def get_wine_records(df, groupby_column):
    cutted_df = df.drop(groupby_column, axis=1)
    return cutted_df.to_dict(orient='records')


def load_wine_records(filename=WINE_FILENAME):
    wine_df = pd.read_excel(filename, sheet_name='Лист1').fillna(value='')
    groupby_column = wine_df.columns[0]
    wine_groups = wine_df.groupby(by=groupby_column).apply(
        lambda x: get_wine_records(x, groupby_column)).to_dict()
    return wine_groups


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    
    company_age = datetime.date.today().year - FOUNDATION_YEAR
    years_form = correct_years_form(company_age)
    wine_groups = load_wine_records()
    
    rendered_page = template.render(
        company_age=company_age,
        years_form=years_form,
        wine_collections=wine_groups
    )
    
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
