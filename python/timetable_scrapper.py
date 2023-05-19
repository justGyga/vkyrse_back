from my_json_lib import *
from my_urls_lib import *
from my_timetables_lib import *
from constants import *
from parser_news import *

if __name__ == '__main__':
    urls = get_all_urls()
    update_file(filename_urls, urls)
    print("All urls was scrapped")
    scrappers = timetables_scrapper(filename_urls)
    update_file(filename_timetables, scrappers)
    print("All tables was scrapped")