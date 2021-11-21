# modules to check for expiry, read, download/write and delete covid data

from urllib.request import urlopen
import config

from covid_package.data_funcs.store_data import delete_file, rename_file, refresh_data, get_last_file_update
from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj

# check that the data is up to date; if not, refresh data from github
def check_refresh_data():

    print('Checking that data is up to date')
    if expired_data():

        # rename data file to a temp for safety
        if rename_file(config.DATA_FILE_STR, config.OLD_FILE_STR):
            # the file rename succeeded
            pass
        else:
            # the file rename failed
            print("File '{}' rename failed".format(config.DATA_FILE_STR))
            # delete the old data so we don't get an overwrite problem
            delete_file(config.DATA_FILE_STR)

        # try to get an updated copy of the data and store it
        if refresh_data(config.DATA_URL_STR, config.BACKUP_DATA_URL_STR, config.DATA_FILE_STR):
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
        print("Data file up to date: last updated at:", config.UPDATE_DATETIME_STR)
        return True

# check latest data to see if expired
def expired_data():

    # uncomment this for local testing
    #from covid_package.libs.aggregate_data import fetch_latest_data_date

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
        print("Expired data file: current file = {}, latest update = {}".format(config.UPDATE_DATETIME_STR, owid_updatetime))
        # update the global to reflect the new update time
        config.UPDATE_DATETIME_STR = owid_updatetime
        return True

    else:
        # Data file up to date
        return False

# fetches the update time string from OWID
# returns a validated datetime string
def get_update_time_fm_owid():

    timestamp_url = "https://covid.ourworldindata.org/data/owid-covid-data-last-updated-timestamp.txt"

    # get the timestamp
    timestamp_page = urlopen(timestamp_url)
    timestamp_str = str(timestamp_page.read(), 'utf-8')

    # add the timezone to ensure correct format for convert_datetime_str_to_obj
    updatetime_str = timestamp_str + "Z"

    # validate and return the timestamp
    # note we are returning the string, not the object in order not to break later logic
    if convert_datetime_str_to_obj(updatetime_str, 'datetime'):
        return updatetime_str
    else:
        print("Error: updatetime_str =", updatetime_str)
        return False  # this will signal that the timestamp fetch has broken

# test function
def main():

    import os
    import sys
    import json

    from pathlib import Path

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis"
    package_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package"
    sys.path.append(proj_loc)

    import config
    import modify

    sys.path.append(package_loc)

    from covid_package.libs.aggregate_data import fetch_latest_data_date
    from covid_package.data_funcs.store_data import read_json_data, write_json_data, delete_file, rename_file, refresh_data, convert_owid_data, get_last_file_update
    from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj
    from covid_package.libs.valid_keys import fetch_l0_keys


    # get data

    if check_refresh_data():
        # read the updated(?) data file from the data dir
        data = read_json_data(config.DATA_FILE_STR)
        # repopulate the keys
        #key_list = fetch_l0_keys(data)
        # need this?
        #country_list = fetch_countries(data)

    print("After update:", fetch_latest_data_date(data))

    #get_update_time_fm_owid()

# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
