# modules to check for expiry, read, download/write and delete covid data

# from urllib.request import urlopen
import requests

import config

# local imports - uncomment these if being imported externally
from covid_package.data_funcs.store_data import delete_file, rename_file, refresh_data, get_last_file_update
from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj


# check that the data is up to date; if not, refresh data from github
def check_refresh_data():
    """Check that data is up to date.  If not, refresh data from GitHub.
        Returns True if data was updated, or is already up to date.
        Returns False if data failed to renew."""

    print('Checking that data is up to date')
    # bypass expired_data() for now... they keep changing the file name and location
    if True:
    # if expired_data():

        # rename data file to a temp for safety
        if rename_file(config.DATA_FILE_STR, config.OLD_FILE_STR):
            # the file rename succeeded
            pass
        else:
            # the file rename failed
            print(f"File '{config.DATA_FILE_STR}' rename failed")
            # delete the old data so we don't get an overwrite problem
            delete_file(config.DATA_FILE_STR)

        # try to get an updated copy of the data and store it
        if refresh_data():
            # safe to delete the old data file
            delete_file(config.OLD_FILE_STR)

            print("Data updated")
        else:  # un-rename data file
            if rename_file(config.OLD_FILE_STR, config.DATA_FILE_STR):
                print("Old data restored")
            else:
                print("Data restore failed - check data integrity")
                # failed to update the data and the restoration of the old data also failed
                return False
        # the data was expired but the update operations succeeded or failed back, so we are good

        return True
    else:
        # the data wasn't expired, so we are good
        print(f"Data file up to date: last updated at: {config.UPDATE_DATETIME_STR}")
        return True


# check latest data to see if expired
def expired_data():
    """ Check latest data to see if expired.
        Returns True if there is a file newer than the currently stored version.
        Returns False if the data is up to date."""

    # uncomment this for local testing
    # from covid_package.libs.aggregate_data import fetch_latest_data_date

    # first data update was 2021-04-01T14:40:33Z
    # latest data update was 2021-04-02T09:11:58Z

    # check last update datetime of current data file
    config.UPDATE_DATETIME_STR = get_last_file_update()  # set the global to the datetime in the update-record
    last_updatetime_obj = convert_datetime_str_to_obj(config.UPDATE_DATETIME_STR, 'datetime')

    # get latest update datetime of owid data from github
    owid_updatetime = get_update_time_fm_owid()
    owid_updatetime_obj = convert_datetime_str_to_obj(owid_updatetime, 'datetime')

    # calculate if data in need of update
    if owid_updatetime_obj > last_updatetime_obj:  # we should reload the data file
        print(f"Expired data file: current file = {config.UPDATE_DATETIME_STR}, latest update = {owid_updatetime}")
        # update the global to reflect the new update time
        config.UPDATE_DATETIME_STR = owid_updatetime
        return True

    else:
        # Data file up to date
        return False


# fetches the update time string from OWID
# returns a validated datetime string
def get_update_time_fm_owid():
    """ Fetches the update time string from OWID.
        Returns a validated datetime string."""

    # uncomment for local testing
    # from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj

    # old timestamp
    # timestamp_url = "https://covid.ourworldindata.org/data/owid-covid-data-last-updated-timestamp.txt"
    # new new timestamp
    timestamp_url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/internal/timestamp/owid-covid-data-last-updated-timestamp.txt"

    # get the timestamp
    try:
        timestamp_file = requests.get(timestamp_url)
        # print(timestamp_file.text)
        # print(type(timestamp_file.text))

    except requests.exceptions.RequestException as err:
        print(f"Data download error: {err}")
        return False  # this will signal that the timestamp fetch has broken


    # add the timezone to ensure correct format for convert_datetime_str_to_obj
    updatetime_str = timestamp_file.text + "Z"

    # validate and return the timestamp
    # note we are returning the string, not the object in order not to break later logic
    if convert_datetime_str_to_obj(updatetime_str, 'datetime'):
        return updatetime_str
    else:
        print(f"Error: updatetime_str = {updatetime_str}")
        return False  # this will signal that the timestamp fetch has broken


# test function
def main():

    import os
    import sys
    import json

    proj_loc = "C:\\Users\\russe\\Documents\\Repos\\GitHub\\covid_analysis"
    sys.path.append(proj_loc)

    # to test, comment out the local imports at the top
    #import config
    #import modify

    package_loc = "C:\\Users\\russe\\Documents\\Repos\\GitHub\\covid_analysis\\covid_package"
    sys.path.append(package_loc)
    """
    from covid_package.libs.aggregate_data import fetch_latest_data_date
    from covid_package.data_funcs.store_data import read_json_data
    from covid_package.data_funcs.store_data import write_json_data
    from covid_package.data_funcs.store_data import delete_file
    from covid_package.data_funcs.store_data import rename_file
    from covid_package.data_funcs.store_data import refresh_data
    from covid_package.data_funcs.store_data import convert_owid_data
    from covid_package.data_funcs.store_data import get_last_file_update

    from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data
    if check_refresh_data():
        # read the updated(?) data file from the data dir
        data = read_json_data(config.DATA_FILE_STR)
        # repopulate the keys
        # key_list = fetch_l0_keys(data)
        # need this?
        # country_list = fetch_countries(data)

    print("After update:", fetch_latest_data_date(data))
"""

    print(get_update_time_fm_owid())


# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
