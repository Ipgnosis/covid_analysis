# utility functions for managing data


import json
import os
import requests
import config, modify

from datetime import date, datetime

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

    # get the json data from github
    try:
        downloaded_data = requests.get(source_url).json()
    except:
        print("Data cannot be downloaded")
        return False

    # if we updated the data without error
    if write_json_data(config.DATA_FILE_STR, downloaded_data):
        update_the_update_file() # update the record of updates
    else:
        return False

    return True


# return a datetime string for the last time the data was updated
def get_last_file_update():

    update_data_file = read_json_data(config.UPDATE_FILE_STR)

    last_update_str = update_data_file["last_update"]

    return last_update_str


# append new update time to UPDATE_FILE
def update_the_update_file():

    # get the update file
    update_data = read_json_data(config.UPDATE_FILE_STR)

    # push the last update onto the historical record
    update_data['update_list'].append(update_data['last_update'])

    # store the new update datetime
    update_data['last_update'] = config.UPDATE_DATETIME_STR

    # keep a record of the earliest time that the file was updated
    # we'll need this later, but building the record for now
    # extract 2 time objects for comparison
    earliest_update = convert_datetime_str_to_obj(update_data['earliest_update'], 'time')
    this_update = convert_datetime_str_to_obj(config.UPDATE_DATETIME_STR, 'time')

    # update the earliest update time as necessary
    # don't forget that this is a datetime string - this will need to be reconverted later once needed
    if this_update < earliest_update:
        update_data['earliest_update'] = config.UPDATE_DATETIME_STR

    # write the updated update file
    if write_json_data(config.UPDATE_FILE_STR, update_data):
        pass
    else:
        print("Error updating UPDATE_FILE")


# do the datetime jiggery-pokery
def convert_datetime_str_to_obj(datetime_str, resolution):

    github_format = "%Y-%m-%dT%H:%M:%S%z"

    datetime_obj = datetime.strptime(datetime_str, github_format)

    if resolution == 'datetime':
            return_obj = datetime_obj

    elif resolution == 'date':
            return_obj = datetime.date(datetime_obj)

    elif resolution == 'time':
            return_obj = datetime.time(datetime_obj)
    else:
        return False # incorrect parameter

    return return_obj


# test function

def main():

    #import os
    #import sys
    #import json
    #from pathlib import Path

    #import config, modify # need to fix the path for this

    dtstr = "2021-04-04T08:02:44Z"

    print("datetime =", convert_datetime_str_to_obj(dtstr, 'datetime'))

    print("date =", convert_datetime_str_to_obj(dtstr, 'date'))

    print("time =", convert_datetime_str_to_obj(dtstr, 'time'))

# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
