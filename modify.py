# modify the globals

import config
import os, sys
from pathlib import Path

data_file_name = 'owid-covid-data.json'
old_data_file_name = 'owid-covid-data-old.json'
update_file_name = 'update-data.json'

CURRENT_DIR_STR = os.path.abspath('')
DATA_URL_STR = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.json"
UPDATE_DATETIME_STR = "2020-01-01T10:00:00Z"
DATA_FILE_STR = os.path.join(CURRENT_DIR_STR, 'data', data_file_name)
OLD_FILE_STR = os.path.join(CURRENT_DIR_STR, 'data', old_data_file_name)
UPDATE_FILE_STR = os.path.join(CURRENT_DIR_STR, 'data', update_file_name)
COVID_PACKAGE_STR = os.path.join(CURRENT_DIR_STR, 'covid_package')
DATA_FILE_PATH = Path(DATA_FILE_STR)
OLD_FILE_PATH = Path(OLD_FILE_STR)
UPDATE_FILE_PATH = Path(UPDATE_FILE_STR)
COVID_PACKAGE_PATH = Path(COVID_PACKAGE_STR)
