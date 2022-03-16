# modify the globals

import os
import sys

from pathlib import Path

import config

# file names
data_file_name = 'owid-covid-data.json'
old_data_file_name = 'owid-covid-data-old.json'
update_file_name = 'update-record.json'
country_file_name = 'country-data.json'

# url for covid data file
# this url was confirmed on 3/16/22
config.DATA_URL_STR = "https://covid.ourworldindata.org/data/owid-covid-data.json"

# set up the project paths

# the top level location of the project code
config.CURRENT_DIR_STR = os.path.abspath('')
sys.path.append(config.CURRENT_DIR_STR)


# the package for the libraries which will ultimately be installed in the app and the api
config.COVID_PACKAGE_STR = os.path.join(config.CURRENT_DIR_STR, 'covid_package')
sys.path.append(config.COVID_PACKAGE_STR)

# set up the file paths

# data folder path
config.DATA_FOLDER_PATH = os.path.join(config.CURRENT_DIR_STR, 'data')
sys.path.append(config.DATA_FOLDER_PATH)

# the data file
config.DATA_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', data_file_name)

# the old (backup) file saved for recovery of failures in the update operation
config.OLD_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', old_data_file_name)

# the update file
config.UPDATE_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', update_file_name)

# the country file
config.COUNTRY_FILE_STR = os.path.join(config.CURRENT_DIR_STR, 'data', country_file_name)
config.COUNTRY_FILE_PATH = Path(config.COUNTRY_FILE_STR)
# sys.path.append(config.COUNTRY_FILE_PATH)

# important datetimes
# the update datetime of the current data file
# this is just a dummy to initialize the variable: gets reset every program run
config.UPDATE_DATETIME_STR = "2019-01-01T10:00:00Z"
# the date of the earliest valid data in the data set
config.DATA_START_DATE = "2020-01-01"  # may change this later
# the date of the most recent valid data in the data set
# this is just a dummy to initialize the variable: gets reset every program run
config.LATEST_DATA_DATE = "2018-01-01"
