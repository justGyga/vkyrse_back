from my_json_lib import *
from my_urls_lib import *
from my_timetables_lib import *
from constants import *

_all_urls = get_all_urls()
update_file(filename_urls, _all_urls)
print("All urls was scrapped")
_all_scrappers = timetables_scrapper(filename_timetables)
update_file(filename_timetables, _all_scrappers)
print("All tables was scrapped")