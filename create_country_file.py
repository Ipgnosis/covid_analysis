# create country attributes file

import os
import sys
import json

from pathlib import Path
from datetime import datetime

import config, modify

from covid_package.data_funcs.store_data import read_json_data, write_json_data, rename_file, convert_owid_data

def islands(iso):

    islands = ['ATG', 'AUS', 'BHR', 'BHS', 'BRB', 'COM', 'CPV', 'CUB', 'CYP', 'CYN', 'DOM', 'FJI', 'FSM', 'GBR', 'GRD', 'IDN', 'IRL', 'ISL', 'JAM', 'JPN', 'KNA', 'KOR', 'LCA', 'LKA', 'MDG', 'MDV', 'MHL', 'MLT', 'MUS', 'NZL', 'PHL', 'SGP', 'SLB', 'STP', 'SYC', 'TTO', 'TWN', 'VCT', 'VUT', 'WSM']

    if iso in islands:
        return True
    else:
        return False

def no_tr_so(iso):

    north = ['AFG', 'ALB', 'DZA', 'AND', 'ARM', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BLR', 'BEL', 'BMU', 'BTN', 'BIH', 'BGR', 'CAN', 'CHN', 'HRV', 'CYP', 'CZE', 'CYN', 'DNK', 'EGY', 'EST', 'FIN', 'FRA', 'FRO', 'GEO', 'DEU', 'GIB', 'GRC', 'GRL', 'GGY', 'HUN', 'ISL', 'IMN', 'IRN', 'IRQ', 'IRL', 'ISR', 'ITA', 'JEY', 'JPN', 'JOR', 'KAZ', 'KOS', 'KWT', 'KGZ', 'LVA', 'LBN', 'LBY', 'LIE', 'LTU', 'LUX', 'MLT', 'MDA', 'MCO', 'MNG', 'MSR', 'MNE', 'MAR', 'NPL', 'NLD', 'MKD', 'NOR', 'PAK', 'PSE', 'POL', 'PRT', 'QAT', 'ROU', 'RUS', 'SMR', 'SAU', 'SRB', 'SVK', 'SVN', 'KOR', 'ESP', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK', 'TUN', 'TUR', 'UKR', 'GBR', 'USA', 'UZB', 'VAT']
    tropics = ['AGO', 'AIA', 'ABW', 'ARE', 'ATG', 'BDI', 'BEN', 'BFA', 'BLZ', 'BOL', 'BRA', 'BRB', 'BRN', 'BWA', 'CYM', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'DJI', 'DMA', 'DOM', 'ECU', 'ERI', 'ETH', 'FJI', 'FSM', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRD', 'GTM', 'GUY', 'HKG', 'HND', 'HTI', 'IDN', 'IND', 'JAM', 'KEN', 'KHM', 'KNA', 'LAO', 'LBR', 'LCA', 'LKA', 'MAC', 'MDG', 'MDV', 'MEX', 'MHL', 'MLI', 'MMR', 'NRU', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYS', 'NER', 'NGA', 'NIC', 'OMN', 'PAN', 'PER', 'PHL', 'PNG', 'PRY', 'RWA', 'SHN', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SOM', 'SSD', 'STP', 'SUR', 'SYC', 'TCD', 'TGO', 'TON', 'THA', 'TLS', 'TTO', 'TZA', 'TCA', 'UGA', 'VCT', 'VEN', 'VNM', 'VUT', 'WSM', 'YEM', 'ZMB', 'ZWE']
    south = ['ARG', 'AUS', 'CHL', 'FLK', 'SWZ', 'LSO', 'NAM', 'NZL', 'ZAF', 'URY']

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

def check_exists(this_val, res):

    if res in this_val.keys():
        return this_val[res]
    else:
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
        date_time = datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S%z")
        old_country_file_name = 'country-data-' + date_time + '.json'
        old_country_file_str = os.path.join(config.CURRENT_DIR_STR, 'data', old_country_file_name)
        rename_file(config.COUNTRY_FILE_STR, old_country_file_str)

    global_json = dict()

    #for key, val in data.items():
    for key, val in data.items():

        country_json = dict()

        country_json = {
            'continent': check_exists(val, 'continent'),
            'location': check_exists(val, 'location'),
            'population': check_exists(val, 'population'),
            'population_density': check_exists(val, 'population_density'),
            'area': nat_area(key),
            'island': islands(key),
            'gdp_per_capita': check_exists(val, 'gdp_per_capita'),
            'no_tr_so_hemis': no_tr_so(key),
            'e_w_hemis': e_w_hemis(key),
            'time_zone': time_zone(key),
            'politics': politics(key),
            'culture': culture(key)
            #country_json[key][''] = data[key]['']
        }

        global_json[key] = country_json

    write_json_data(config.COUNTRY_FILE_STR, global_json)

    print('Complete')


# driver function

def main():

    sys.path.append(config.CURRENT_DIR_STR)

    # write the update data file
    create_country_file(config.COUNTRY_FILE_STR)

# stand alone test run
if __name__ == "__main__":
    main()
