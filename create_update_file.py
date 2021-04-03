
from covid_package.data_funcs.store_data import write_json_data

# create update file

def create_update_file(update_file):

    #from covid_package.data_funcs.store_data import write_json_data

    # first data update was 2021-04-01T14:40:33Z
    # latest data update was 2021-04-02T09:11:58Z

    first_update = "2021-04-01T14:40:33Z"
    #second_update = "2021-04-02T09:11:58Z"

    update_json = {
        'last_update': first_update,
        'update_list': []
    }

    write_json_data(update_file, update_json)

    print('Complete')


# test function

def main():

    import os
    import sys
    import json

    from pathlib import Path

    CURRENT_DIR = os.path.abspath('')
    sys.path.append(CURRENT_DIR)
    data_path = "C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\data"
    package_path = "C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package"
    sys.path.append(data_path)
    sys.path.append(package_path)

    update_file = 'update-data.json'
    UPDATE_DATA = Path(os.path.join(data_path, update_file))

    # write the update data file
    create_update_file(UPDATE_DATA)

# stand alone test run
if __name__ == "__main__":
    main()
