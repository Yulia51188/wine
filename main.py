import datetime

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

FOUNDATION_YEAR = 1920


def correct_years_form(age):
    last_number = int(age) % 10
    if last_number == 1:
        return "год"
    if last_number == 0 or last_number > 4:
        return "лет"    
    return "года"


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

company_age = datetime.date.today().year - FOUNDATION_YEAR

years_form = correct_years_form(company_age)

rendered_page = template.render(
    company_age=company_age,
    years_form=years_form,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
