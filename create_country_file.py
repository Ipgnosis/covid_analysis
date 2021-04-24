# create country attributes file

import os
import sys
import json

from pathlib import Path

import config, modify

from covid_package.data_funcs.store_data import read_json_data, write_json_data, rename_file, convert_owid_data

def islands(iso):

    islands = []

    if iso in islands:
        return True
    else:
        return None # False

def no_tr_so(iso):

    north = []
    tropics = []
    south = []

    if iso in north:
        return 'N'
    elif iso in tropics:
        return 'T'
    elif iso in south:
        return 'S'
    else:
        return None

def e_w_hemis(iso):

    east = []
    west = []

    if iso in east:
        return 'E'
    elif iso in west:
        return 'W'
    else:
        return None

def nat_area(iso):

    return None

def time_zone(iso):

    return None

def politics(iso):

    return None

def culture(iso):

    return None



def create_country_file(country_file):

    # get the data and massage
    data = read_json_data(config.DATA_FILE_STR)
    # convert the OWID_ keys
    data = convert_owid_data(data)
    # also pop the INT and WRL records: not needed
    #data.pop('INT')
    data.pop('WRL')

    # do we need to make a backup of an existing country file?
    if os.path.exists(config.COUNTRY_FILE_STR):
        old_country_file_name = 'country-data-old.json'
        old_country_file_str = os.path.join(config.CURRENT_DIR_STR, 'data', old_country_file_name)
        rename_file(config.COUNTRY_FILE_STR, old_country_file_str)

    country_json = dict()

    #for key, val in data.items():
    for key in data.keys():
        country_json['iso_code'] = key

        for val in data[key].values():

            country_json[key]['continent'] = val['continent']
            country_json[key]['location'] = val['location']
            country_json[key]['population'] = val['population']
            country_json[key]['population_density'] = val['population_density']
            country_json[key]['area'] = nat_area(key)
            country_json[key]['island'] = islands(key)
            country_json[key]['gdp_per_capita'] = val['gdp_per_capita']
            country_json[key]['no_tr_so_hemis'] = no_tr_so(key)
            country_json[key]['e_w_hemis'] = e_w_hemis(key)
            country_json[key]['time_zone'] = time_zone(key)
            country_json[key]['politics'] = politics(key)
            country_json[key]['culture'] = culture(key)
            #country_json[key][''] = data[key]['']


    write_json_data(config.COUNTRY_FILE_STR, country_json)

    print('Complete')


# driver function

def main():

    sys.path.append(config.CURRENT_DIR_STR)

    # write the update data file
    create_country_file(config.COUNTRY_FILE_STR)

# stand alone test run
if __name__ == "__main__":
    main()
