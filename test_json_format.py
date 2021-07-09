import os
import sys
import config
import modify

from covid_package.data_funcs.store_data import read_json_data, write_json_data

update_data = read_json_data(config.UPDATE_FILE_STR)

print(update_data)

write_json_data(config.UPDATE_FILE_STR, update_data)
