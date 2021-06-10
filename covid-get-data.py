# imports

from datetime import datetime

# set up file paths and other data globals

import config
import modify

# local imports

from covid_package.data_funcs.store_data import read_json_data, convert_owid_data
from covid_package.data_funcs.update_data import check_refresh_data

from covid_package.libs.aggregate_data import fetch_latest_data_date

from covid_package.api.get_country_data import get_l2_date_data

# update data

# check if data up to date; if not, reload
if check_refresh_data():
    # read the updated(?) data file from the data dir
    data = read_json_data(config.DATA_FILE_STR)
    # convert the OWID_ keys
    data = convert_owid_data(data)

    # set the latest data date global
    config.LATEST_DATA_DATE = fetch_latest_data_date(data)

    print("Latest data is:", config.LATEST_DATA_DATE)
    print("Current UTC 0 dateime = {}".format(datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S%z")))
