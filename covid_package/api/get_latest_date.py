# gets data of latest data
# small hack to check the data update service

from covid_package.libs.aggregate_data import fetch_latest_data_date


def get_latest_date(this_data, these_keys):

    return fetch_latest_data_date(this_data, these_keys)
