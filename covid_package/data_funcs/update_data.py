# modules to check for expiry, read, download/write and delete covid data

import config, modify
import requests
from bs4 import BeautifulSoup as bSoup

# comment this out for local testing
from covid_package.libs.aggregate_data import fetch_latest_data_date
from covid_package.data_funcs.store_data import read_json_data, write_json_data, delete_file, rename_file, refresh_data, convert_owid_data, get_last_file_update, convert_datetime_str_to_obj


# check data up to date
def check_refresh_data():

    if expired_data():

        # rename data file
        if rename_file(config.DATA_FILE_STR, config.OLD_FILE_STR):
            # the file rename succeeded
            pass
        else:
            # the file rename failed
            print("File '{}' rename failed".format(config.DATA_FILE_STR))
            # delete the old data so we don't get an overwrite problem
            delete_file(config.DATA_FILE_STR)

        # try to get an updated copy of the data
        if refresh_data(config.DATA_URL_STR, config.DATA_FILE_STR):
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
        return True

# check latest data to see if expired


def expired_data():

    # uncomment this for local testing
    #from covid_package.libs.aggregate_data import fetch_latest_data_date

    # first data update was 2021-04-01T14:40:33Z
    # latest data update was 2021-04-02T09:11:58Z

    # check last update datetime of current data file
    config.UPDATE_DATETIME_STR = get_last_file_update()
    last_updatetime_obj = convert_datetime_str_to_obj(config.UPDATE_DATETIME_STR)

    # get latest update datetime of owid data
    owid_updatetime = get_update_time_fm_owid()
    owid_updatetime_obj = convert_datetime_str_to_obj(owid_updatetime)

    # calculate if data in need of update
    if owid_updatetime_obj > last_updatetime_obj:  # we should reload the data file
        print("Expired data file")
        # update the global to reflect the new update time
        config.UPDATE_DATETIME_STR = owid_updatetime
        return True

    else:
        print("Data file up to date")
        return False



# takes a github page url and scrapes a file update time string
# returns a datetime string
# see https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
# this is very brittle...

def get_update_time_fm_owid():

    # define some brittle values
    page_url = "https://github.com/owid/covid-19-data/tree/master/public/data"
    this_href = "/owid/covid-19-data/blob/master/public/data/owid-covid-data.json"
    class_descr = 'Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item'

    # get the page content
    req = requests.get(page_url)

    ### let the beautifulsoup jiggery-pokery commence ###
    # html parsing
    page_soup = bSoup(req.content, 'html5lib')

    # get the list of divs to search
    code_rows = page_soup.find_all('div', attrs = {'class': class_descr})

    # search the divs list for a div containing this_href
    for row in code_rows:
        if row.find_all(href = this_href):
            target_row = row

    # find the correct div
    target_div = target_row.find('div', attrs = {'class': 'color-text-tertiary text-right'})

    # locate the user-defined tag 'time-ago'
    timeago = target_div.find('time-ago')

    # grab the string value in 'datetime'
    updatetime_str = timeago.get('datetime')

    # debug output
    #print("get_update_time_fm_owid: updatetime_str = ", updatetime_str)

    return updatetime_str


# test function

def main():

    import os
    import sys
    import json

    from pathlib import Path

    import config, modify

    config.CURRENT_DIR_STR = os.path.abspath('')
    sys.path.append(config.CURRENT_DIR_STR)
    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package")

    from covid_package.libs.aggregate_data import fetch_latest_data_date
    from covid_package.data_funcs.store_data import read_json_data
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data

    if check_refresh_data():
        # read the updated(?) data file from the data dir
        data = read_json_data(config.DATA_FILE_STR)
        # repopulate the keys
        key_list = fetch_l0_keys(data)
        # need this?
        #country_list = fetch_countries(data)

    print("After update:", fetch_latest_data_date(data, key_list))

# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
