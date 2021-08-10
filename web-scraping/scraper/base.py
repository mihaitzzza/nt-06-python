import requests
from bs4 import BeautifulSoup


def get_page_data():
    server_response = requests.get('https://caen.ro/')
    return server_response.content


def get_category_data(category_string):
    category_data = category_string.find('a').text.split(' - ')
    code = category_data[0]
    name = category_data[1]
    return code, name


def get_recursive_subcategories(div_element):
    result = []

    top_levels = div_element.find_all('p', class_='lead', recursive=False)
    for index, top_level in enumerate(top_levels):
        code, name = get_category_data(top_level)
        current_level = {
            'code': code,
            'name': name,
        }

        next_div = top_level.find_next_sibling('div')

        if next_div is None:
            current_level['categories'] = []
        else:
            current_level['categories'] = get_recursive_subcategories(next_div)
        result.append(current_level)

    return result


def get_web_data():
    page_data = get_page_data()
    soup = BeautifulSoup(page_data, features='html.parser')

    div_sections = soup.find(id='sections')
    result = get_recursive_subcategories(div_sections)

    return result
