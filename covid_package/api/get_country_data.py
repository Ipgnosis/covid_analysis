#  outputs data for a country, based on a country key

import json

# the country api


def get_country_data(this_data, this_country):

    country_data = json.dumps(
        this_data[this_country], indent=4, skipkeys=False)

    return country_data

# the level 1 api


def get_level_1_data(this_data, these_keys, req_keys):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        for req_key in req_keys:
            if req_key in this_data[iso].keys():
                country_dict[req_key] = this_data[iso][req_key]
        return_dict[iso] = country_dict

    return return_dict

# the level 2 key api
# req_keys is a list of level 2 keys


def get_l2_keys_data(this_data, these_keys, req_keys):

    return_dict = dict()

    for iso in these_keys:

        country_dict = dict()
        data_list = []

        # traverse the list of day dicts
        for day in range(len(this_data[iso]['data'])):

            day_data = False  # we haven't found any data yet
            day_dict = dict()

            # traverse the dict of key:vals looking for the required data
            for req_key in range(len(req_keys)):
                # locate the required data in the dict
                if req_keys[req_key] in this_data[iso]['data'][day].keys():
                    day_data = True  # we have now found data
                    # write the key:val
                    day_dict[req_keys[req_key]
                             ] = this_data[iso]['data'][day][req_keys[req_key]]

            # only append the day_dict to the list if we have found data
            if day_data:
                # only add the date key_val if we have found data
                day_dict['date'] = this_data[iso]['data'][day]['date']
                data_list.append(day_dict)

        # add the country data to the return data
        return_dict[iso] = data_list

    return return_dict

# the level 2 date api


def get_l2_date_data(this_data, these_keys, this_date):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        country_list = []
        for day in range(len(this_data[iso]['data'])):
            if this_data[iso]['data'][day]['date'] == this_date:
                country_list.append(this_data[iso]['data'][day])

            country_dict['data'] = country_list

        return_dict[iso] = country_dict

    return return_dict


def main():

    import os
    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis")

    from pathlib import Path
    from covid_package.libs.store_data import read_data
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data
    CURRENT_DIR = os.path.abspath('')
    sys.path.append(CURRENT_DIR)

    FILE_NAME = 'owid-covid-data.json'
    file_path = os.path.join(CURRENT_DIR, 'data', FILE_NAME)
    DATA_FILE = Path(file_path)

    # read the data file from the data dir
    data = read_data(DATA_FILE)

    key_list = fetch_l0_keys(data)

    print("Testing get_l2_keys_data.py")

    required_data = ['new_cases_per_million', 'new_deaths_per_million']

    # run the function
    print(get_l2_keys_data(data, key_list, required_data))


# stand alone test run
if __name__ == "__main__":
    main()
