# needs more work

import os
import sys

from covid_package.data_funcs.store_data import read_json_data
from covid_package.api.get_country_data import get_country_data

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(CURRENT_DIR)

FILE_NAME = 'owid-covid-data.json'
OLD_FILE = 'owid-covid-data-old.json'

DATA_FILE = os.path.join(CURRENT_DIR, 'data', FILE_NAME)
OLD_DATA = os.path.join(CURRENT_DIR, 'data', OLD_FILE)

COVID_PACKAGE = os.path.join(CURRENT_DIR, 'covid_package')
sys.path.append(COVID_PACKAGE)

# read the data file from the data dir
data = read_json_data(DATA_FILE)

test_country = "AFG"

# run the function
print(get_country_data(data, test_country))
