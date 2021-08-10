from scraper import get_web_data, write_to_json_file

if __name__ == '__main__':
    web_data = get_web_data()
    write_to_json_file(web_data)
