import os
import sys
import json

import config, modify

from covid_package.data_funcs.store_data import write_json_data, rename_file

# create update file

def create_update_file(update_file): # don't run this, it may delete all the current data

    # do we need to make a backup of an existing update file?
    if os.path.exists(config.UPDATE_FILE_STR):
        old_update_file_name = 'update-record-old.json'
        old_update_file_str = os.path.join(config.CURRENT_DIR_STR, 'data', old_update_file_name)
        rename_file(config.COUNTRY_FILE_STR, old_update_file_str)

    first_update = "2021-04-01T14:40:33Z"
    second_update = "2021-04-02T09:11:58Z"

    update_json = {
        'last_update': first_update,
        'earliest_update': second_update,
        'update_list': [first_update, second_update]
    }

    write_json_data(update_file, update_json)

    print('Complete')


# test function

def main():

    from pathlib import Path

    CURRENT_DIR = os.path.abspath('')
    sys.path.append(CURRENT_DIR)
    data_path = "C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\data"
    package_path = "C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package"
    sys.path.append(data_path)
    sys.path.append(package_path)

    update_file = 'update-data.json'
    update_data = Path(os.path.join(data_path, update_file))

    # write the update data file
    print(update_data) # gets rid of 'unused variable' problem
    #create_update_file(update_data)  # don't run this or risk deleting data

# stand alone test run
if __name__ == "__main__":
    main()
