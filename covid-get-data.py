# imports

from datetime import datetime

# set up file paths and other data globals

import config
import modify

# local imports

from covid_package.data_funcs.store_data import read_json_data
from covid_package.data_funcs.store_data import convert_owid_data
from covid_package.data_funcs.update_data import check_refresh_data

from covid_package.libs.aggregate_data import fetch_latest_data_date

# update data

# check if data up to date; if not, reload
if check_refresh_data():
    # read the updated(?) data file from the data dir
    data = read_json_data(config.DATA_FILE_STR)

    # convert the OWID_ data so that we don't trip up fetch_latest_data_date
    data = convert_owid_data(data)

    # set the latest data date global
    config.LATEST_DATA_DATE = fetch_latest_data_date(data)

    print("Latest data is:", config.LATEST_DATA_DATE)
    utc0_dt = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S%z")
    print("Current UTC 0 dateime = {}".format(utc0_dt))
