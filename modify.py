# modify the globals

import config
import os, sys
from pathlib import Path

data_file_name = 'owid-covid-data.json'
old_data_file_name = 'owid-covid-data-old.json'
update_file_name = 'update-record.json'
country_file_name = 'country-data.json'

config.CURRENT_DIR_STR = os.path.abspath('')
config.DATA_URL_STR = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.json"
config.UPDATE_DATETIME_STR = "2020-01-01T10:00:00Z"  # this is just a dummy to depict the format: gets reset every program run
config.DATA_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', data_file_name)
config.OLD_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', old_data_file_name)
config.UPDATE_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', update_file_name)
config.COUNTRY_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', country_file_name)
config.COVID_PACKAGE_STR = os.path.join(config.CURRENT_DIR_STR, 'covid_package')
config.DATA_FILE_PATH = Path(config.DATA_FILE_STR)
config.OLD_FILE_PATH = Path(config.OLD_FILE_STR)
config.UPDATE_FILE_PATH = Path(config.UPDATE_FILE_STR)
config.COUNTRY_FILE_PATH = Path(config.COUNTRY_FILE_STR)
config.COVID_PACKAGE_PATH = Path(config.COVID_PACKAGE_STR)
