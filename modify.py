# modify the globals

import config
import os, sys
from pathlib import Path

# file names
data_file_name = 'owid-covid-data.json'
old_data_file_name = 'owid-covid-data-old.json'
update_file_name = 'update-record.json'
country_file_name = 'country-data.json'

# urls for covid data file
config.DATA_URL_STR = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.json"
config.BACKUP_DATA_URL_STR = "https://covid.ourworldindata.org/data/owid-covid-data.json"

# set up the project paths

# the top level location of the project code
config.CURRENT_DIR_STR = os.path.abspath('')
config.CURRENT_DIR_PATH = Path(config.CURRENT_DIR_STR)
sys.path.append(config.CURRENT_DIR_PATH)

# the package for the libraries which will ultimately be installed in the app and the api
config.COVID_PACKAGE_STR = os.path.join(config.CURRENT_DIR_STR, 'covid_package')
config.COVID_PACKAGE_PATH = Path(config.COVID_PACKAGE_STR)
sys.path.append(config.COVID_PACKAGE_PATH)

# set up the file paths

# the data file
config.DATA_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', data_file_name)
config.DATA_FILE_PATH = Path(config.DATA_FILE_STR)
sys.path.append(config.DATA_FILE_PATH)

# the old (backup) file saved for recovery of failures in the update operation
config.OLD_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', old_data_file_name)
config.OLD_FILE_PATH = Path(config.OLD_FILE_STR)
sys.path.append(config.OLD_FILE_PATH)

# the update file
config.UPDATE_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', update_file_name)
config.UPDATE_FILE_PATH = Path(config.UPDATE_FILE_STR)
sys.path.append(config.UPDATE_FILE_PATH)

# the country file
config.COUNTRY_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', country_file_name)
config.COUNTRY_FILE_PATH = Path(config.COUNTRY_FILE_STR)
sys.path.append(config.COUNTRY_FILE_PATH)

# the update datetime of the current data file
config.UPDATE_DATETIME_STR = "2019-01-01T10:00:00Z"  # this is just a dummy to initialize the variable: gets reset every program run
config.LATEST_DATA_DATE = "2018-01-01"  # this is just a dummy to initialize the variable: gets reset every program run
