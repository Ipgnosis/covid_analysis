# modules to check for expiry, read, download/write and delete covid data

import os
import requests
import json
from datetime import date, datetime, timedelta

from covid_package.libs.aggregate_data import fetch_latest_data_date

# check data up to date


def check_refresh_data(this_data, iso_list, data_file, old_data, source_url):
    if expired_data(this_data, iso_list):

        # rename data file
        if rename_file(data_file, old_data):
            # print("Data reloaded")
            pass
        else:
            print("File '{}' rename failed".format(data_file))
            # delete the old data so we don't get an overwrite problem
            delete(data_file)

        # try to get an updated copy of the data
        if refresh_data(source_url, data_file):
            # safe to delete the old data file
            delete(old_data)
        else:  # un-rename data file
            if rename_file(old_data, data_file):
                print("Old data restored")
            else:
                print("Data restore failed")

            return False

        return True

# check latest data to see if expired


def expired_data(this_data, iso_codes):

    format = "%Y-%m-%d"

    # check date of current data file
    latest_data_str = fetch_latest_data_date(this_data, iso_codes)
    latest_date_iso = datetime.strptime(latest_data_str, format)
    latest_date_obj = date(latest_date_iso.year,
                           latest_date_iso.month, latest_date_iso.day)
    # print("latest_date_obj:", latest_date_obj)

    # determine expected date of most up to date data
    today_iso = datetime.now()
    today_obj = date(today_iso.year, today_iso.month, today_iso.day)
    # print("today_obj:", today_obj)

    yesterday = today_obj - timedelta(days=1)
    # print("Yesterday:", yesterday)

    # calculate if data in need of update
    if yesterday > latest_date_obj:  # reload the data file
        print("Expired data file")
        return True

    else:
        print("Data file up to date")
        return False

# download and save new data file version


def refresh_data(source_url, data_file):

    try:
        try:
            data = requests.get(source_url).json()
        except:
            print("File cannot be downloaded")
            return False

        with open(data_file, 'w') as outfile:
            json.dump(data, outfile)
            return True

    except OSError as error:
        print(error)
        print("File cannot be saved - reverting to old file")

        return False


# delete the old data


def delete(fname):

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


"""
def main():

    CURRENT_DIR = os.path.dirname(__file__)
    COVID_PACKAGE = os.path.join(CURRENT_DIR, '..\\covid_package')
    sys.path.append(COVID_PACKAGE)
    DATA_DIR = os.path.join(CURRENT_DIR, '..\\data')
    DATA_FILE = os.path.join(DATA_DIR, "owid-covid-data.json")
    OLD_DATA = os.path.join(DATA_DIR, "owid-covid-data-old.json")
    SOURCE_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.json'

    data = read_data(DATA_FILE)
    key_list = covid_package.libs.fetch_keys(data)
    # print(key_list)
    if check_refresh_data(data, key_list, DATA_FILE, OLD_DATA, SOURCE_URL):
        print("Success - all operations compete")
    else:
        print("ERROR - check data file integrity")


    # stand alone test run
if __name__ == "__main__":
    main()
"""
