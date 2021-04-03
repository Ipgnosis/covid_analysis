# read covid data and apply small kluge for consistency

# Note that in the OWID data, Kosovo has a special iso_code: OWID_KOS   Kosovo
# So for consistency, per above, Kosovo is being assigned a fake iso_code KOS


import json
import os
import requests
import config, modify

from datetime import date, datetime, timedelta


# convert some of the iso_codes to 3 char codes
def convert_owid_data(this_data):

    # change the iso_code for Kosovo, for consistency
    this_data['KOS'] = this_data['OWID_KOS']
    this_data.pop('OWID_KOS', None)

    # change the iso_code for World, for consistency
    this_data['WRL'] = this_data['OWID_WRL']
    this_data.pop('OWID_WRL', None)

    return this_data


# read a json data file
def read_json_data(fname):

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
        return data
    except OSError as error:
        print(error)
        print("File {} cannot be read".format(fname))
        return False


# write a json data file
def write_json_data(fname, wdata):

    try:
        with open(fname, 'w') as outfile:
            json.dump(wdata, outfile)
        return True
    except OSError as error:
        print(error)
        print("File {} cannot be saved".format(fname))
        return False


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


# download and save new data file version
def refresh_data(source_url, data_file):

    try:
        downloaded_data = requests.get(source_url).json()
    except:
        print("Data cannot be downloaded")
        return False

    if write_json_data(config.DATA_FILE_STR, downloaded_data):
        update_the_update_file(config.UPDATE_DATETIME_STR)
    else:
        return False

    return True


# return a datetime string for the last time the data was updated
def get_last_file_update():

    update_data_file = read_json_data(config.UPDATE_FILE_STR)
    print("get_last_file_update: update_data_file = ", update_data_file)

    last_update_str = update_data_file["last_update"]

    return last_update_str


# append new update time to UPDATE_FILE
def update_the_update_file(new_update_datetime):

    update_data = read_json_data(config.UPDATE_FILE_STR)

    update_data['update_list'].append(update_data['last_update'])

    update_data['last_update'] = new_update_datetime

    if write_json_data(config.UPDATE_FILE_STR, update_data):
        pass
    else:
        print("Error updating UPDATE_FILE")

# do the datetime jiggery-pokery
def convert_datetime_str_to_obj(datetime_str):

    github_format = "%Y-%m-%dT%H:%M:%S%z"

    print("conv_dt_str_obj: datetime_str = ", datetime_str)

    datetime_obj = datetime.strptime(datetime_str, github_format)

    print("conv_dt_str_obj: datetime_obj = ", datetime_obj)

    return datetime_obj
