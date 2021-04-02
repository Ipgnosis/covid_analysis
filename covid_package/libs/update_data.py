# modules to check for expiry, read, download/write and delete covid data

import os
import requests
import json
from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup as bSoup

from covid_package.libs.aggregate_data import fetch_latest_data_date


# takes a github url and scrapes a file update time string and returns
# see https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/

def get_update_time_fm_owid():

    page_url = "https://github.com/owid/covid-19-data/tree/master/public/data"
    this_href = "/owid/covid-19-data/blob/master/public/data/owid-covid-data.json"
    class_descr = 'Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item'

    # get page
    req = requests.get(page_url)

    # html parsing
    page_soup = bSoup(req.content, 'html5lib')

    code_rows = page_soup.find_all('div', attrs = {'class': class_descr})

    for row in code_rows:
        if row.find_all(href = this_href):
            target_row = row

    target_div = target_row.find('div', attrs = {'class': 'color-text-tertiary text-right'})

    timeago = target_div.find('time-ago')

    updatetime = timeago.get('datetime')

    return updatetime

# check data up to date


def check_refresh_data(this_data, iso_list, data_file, old_data, source_url):

    if expired_data(this_data, iso_list):

        # rename data file
        if rename_file(data_file, old_data):
            # the file rename succeeded
            pass
        else:
            # the file rename failed
            print("File '{}' rename failed".format(data_file))
            # delete the old data so we don't get an overwrite problem
            delete_file(data_file)

        # try to get an updated copy of the data
        if refresh_data(source_url, data_file):
            # safe to delete the old data file
            delete_file(old_data)
            print("Data updated")
        else:  # un-rename data file
            if rename_file(old_data, data_file):
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


def expired_data(this_data, iso_codes):

    iso_format = "%Y-%m-%d"
    github_format = "%Y-%m-%dT%H:%M:%S%z"

    # check latest data date of current data file
    latest_data_str = fetch_latest_data_date(this_data, iso_codes)
    latest_date_iso = datetime.strptime(latest_data_str, iso_format)
    print("latest data = ", latest_date_iso)
    latest_date_plus_1 = latest_date_iso + timedelta(days=1)
    print("latest data plus 1:", latest_date_plus_1)
    latest_date_obj = date(latest_date_plus_1.year,
                           latest_date_plus_1.month, latest_date_plus_1.day)

    # determine expected date of most up to date data
    owid_file_update_str = get_update_time_fm_owid()

    owid_datetime = datetime.strptime(owid_file_update_str, github_format)
    owid_date_obj = date(owid_datetime.year,
                           owid_datetime.month, owid_datetime.day)


    # calculate if data in need of update
    if owid_date_obj > latest_date_obj:  # reload the data file
        print("Expired data file")
        return True

    else:
        print("Data file up to date")
        return False

# download and save new data file version


def refresh_data(source_url, data_file):

    try:
        data = requests.get(source_url).json()
    except:
        print("Data cannot be downloaded")
        return False

    try:
        with open(data_file, 'w') as outfile:
            json.dump(data, outfile)
    except OSError as error:
        print(error)
        print("File cannot be saved - reverting to old file")
        return False

    return True

# read data file


def read_data(fname):

    with open(fname) as json_file:
        data = json.load(json_file)

    return data

# delete the old data


def delete_file(fname):

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(error)
        print("File {} cannot be removed".format(fname))
        return False

# rename a file


def rename_file(fromf, tof):

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(error)
        return False


# test function

def main():

    import os
    import sys
    import json

    from pathlib import Path

    CURRENT_DIR = os.path.abspath('')
    sys.path.append(CURRENT_DIR)
    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package")

    from covid_package.libs.aggregate_data import fetch_latest_data_date
    from covid_package.libs.store_data import read_data
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data

    FILE_NAME = 'owid-covid-data.json'
    OLD_DATA = 'owid-covid-data-old.json'
    file_path = os.path.join(CURRENT_DIR, 'data', FILE_NAME)
    old_path = os.path.join(CURRENT_DIR, 'data', OLD_DATA)
    DATA_FILE = Path(file_path)
    OLD_FILE = Path(old_path)

    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.json"

    # read the data file from the data dir
    data = read_data(DATA_FILE)
    # get the iso_code keys
    key_list = fetch_l0_keys(data)

    print("Before update:", fetch_latest_data_date(data, key_list))


    print(expired_data(data, key_list))

    check_refresh_data(data, key_list, DATA_FILE, OLD_FILE, url)

    # read the data file from the data dir
    data = read_data(DATA_FILE)
    # get the iso_code keys
    key_list = fetch_l0_keys(data)

    print("After update:", fetch_latest_data_date(data, key_list))

# stand alone test run
if __name__ == "__main__":
    main()
