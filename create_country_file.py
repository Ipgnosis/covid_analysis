# create country attributes file

import os
import sys
import json

from pathlib import Path
from datetime import datetime

import config, modify

from covid_package.data_funcs.store_data import read_json_data, write_json_data, rename_file, convert_owid_data

def islands(iso):

    islands = ['AIA', 'ATG', 'ABW', 'AUS', 'BHR', 'BHS', 'BRB', 'BMU', 'CYM', 'COM', 'CPV', 'CUB', 'CUW', 'CYP', 'CYN', 'DMA', 'FRO', 'FLK', 'FJI', 'FSM', 'GGY', 'GRL', 'GBR', 'GRD', 'IMN', 'IDN', 'IRL', 'ISL', 'JAM', 'JPN', 'JEY', 'KNA', 'KOR', 'LCA', 'LKA', 'MDG', 'MDV', 'MHL', 'MLT', 'MUS', 'MSR', 'NRU', 'NZL', 'PHL', 'PNG', 'SGP', 'SHN', 'SLB', 'STP', 'SYC', 'TON', 'TTO', 'TCA', 'TWN', 'VCT', 'VUT', 'WSM']

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


# is this very interesting??
def e_w_hemis(iso):

    east = []
    west = []

    if iso in east:
        return 'E'
    elif iso in west:
        return 'W'
    else:
        return None

def nat_area(pop, dens):

    # check_exists returns 0 for pop_density for countries that have no value
    # avoid the 'divide by zero' error
    if dens == 0:
        return 0

    # return calculated area in sq. km.
    return round(pop/dens, 1)

def time_zone(iso):

    return None

def politics(iso):

    return None

def culture(iso):

    return None

def check_exists(this_val, res, this_type):

    if res in this_val.keys():
        return this_val[res]
    else:
        if this_type == 's':
            return None
        elif this_type == 'i':
            return 0
        elif this_type == 'f':
            return 0.0
        else:
            return None

def create_country_file():

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
            'continent': check_exists(val, 'continent', 's'),
            'location': check_exists(val, 'location', 's'),
            'population': check_exists(val, 'population', 'i'),
            'population_density': check_exists(val, 'population_density', 'f'),
            'area': nat_area(check_exists(val, 'population', 'i'), check_exists(val, 'population_density', 'f')),
            'island': islands(key),
            'gdp_per_capita': check_exists(val, 'gdp_per_capita', 'f'),
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

def list_complete(iso, this_list):

    sorted_iso = sorted(iso, key=lambda i: i)
    sorted_this_list = sorted(this_list, key=lambda l: l)


    if sorted_iso != sorted_this_list:

        print("iso len = ", len(sorted_iso))
        print("list len = ", len(sorted_this_list))

        max_len = max(sorted_iso, sorted_this_list, key = len)

        i = 0

        while i < max_len:

            print('sorted iso = ', sorted_iso[i])

            print('sorted_list =', sorted_this_list[i])

            i += 1

        for country1 in sorted_iso:
            if country1 not in sorted_this_list:
                print(country1, "not in this_list")

        for country2 in sorted_this_list:
            if country2 not in sorted_iso:
                print(country2, "not in key_list")

        return False
    else:
        return True

# driver function

def main():

    """
    from covid_package.libs.valid_keys import fetch_l0_keys
    from covid_package.data_funcs.update_data import check_refresh_data
    # get data

    # get the data and massage
    data = read_json_data(config.DATA_FILE_STR)
    # convert the OWID_ keys
    data = convert_owid_data(data)
    # also pop the INT and WRL records: not needed
    #data.pop('INT')
    data.pop('WRL')
    # get the iso keys
    key_list = fetch_l0_keys(data)


    islands = ['AIA', 'ATG', 'ABW', 'AUS', 'BHR', 'BHS', 'BRB', 'BMU', 'CYM', 'COM', 'CPV', 'CUB', 'CUW', 'CYP', 'CYN', 'DMA', 'FRO', 'FLK', 'FJI', 'FSM', 'GGY', 'GRL', 'GBR', 'GRD', 'IMN', 'IDN', 'IRL', 'ISL', 'JAM', 'JPN', 'JEY', 'KNA', 'KOR', 'LCA', 'LKA', 'MDG', 'MDV', 'MHL', 'MLT', 'MUS', 'MSR', 'NRU', 'NZL', 'PHL', 'PNG', 'SGP', 'SHN', 'SLB', 'STP', 'SYC', 'TON', 'TTO', 'TCA', 'TWN', 'VCT', 'VUT', 'WSM']
    not_islands = ['AFG', 'ALB', 'DZA', 'AND', 'AGO', 'ARG', 'ARM', 'AUT', 'AZE', 'BGD', 'BEL', 'BLR', 'BLZ', 'BEN', 'BTN', 'BOL', 'BIH', 'BWA', 'BRA', 'BRN', 'BGR', 'BFA', 'BDI',
    'KHM', 'CMR', 'CAN', 'CAF', 'TCD', 'CHL', 'CHN', 'COL', 'COG', 'CRI', 'CIV', 'HRV', 'CZE', 'COD', 'DNK', 'DJI', 'DOM', 'ECU', 'EGY', 'SLV', 'GNQ', 'ERI', 'EST', 'SWZ', 'ETH',
    'FIN', 'FRA', 'GAB', 'GMB', 'GEO', 'DEU', 'GHA', 'GIB', 'GRC', 'GTM', 'GIN', 'GNB', 'GUY', 'HTI', 'HND', 'HKG', 'HUN', 'IND', 'IRN', 'IRQ', 'ISR', 'ITA', 'JOR', 'KAZ', 'KEN', 'KWT', 'KGZ', 'LAO', 'LVA', 'LBN', 'LSO', 'LBR', 'LBY', 'LIE', 'LTU', 'LUX', 'MAC', 'MWI', 'MYS', 'MLI', 'MRT', 'MEX', 'MDA', 'MCO', 'MNG', 'MNE', 'MAR', 'MOZ', 'MMR', 'NAM', 'NPL', 'NLD', 'NIC', 'NER', 'NGA', 'MKD',
    'NOR', 'OMN', 'PAK', 'PSE', 'PAN', 'PRY', 'PER', 'POL', 'PRT', 'QAT', 'ROU', 'RUS', 'RWA', 'SMR', 'SAU', 'SEN', 'SRB', 'SLE', 'SVK', 'SVN', 'SOM', 'ZAF', 'SSD', 'ESP', 'SDN', 'SUR', 'SWE', 'CHE', 'SYR', 'TJK', 'TZA', 'THA', 'TLS', 'TGO', 'TUN', 'TUR', 'UGA', 'UKR', 'ARE', 'USA', 'URY', 'UZB', 'VAT', 'VEN', 'VNM', 'YEM', 'ZMB', 'ZWE', 'KOS']


    north = ['AFG', 'ALB', 'DZA', 'AND', 'ARM', 'AUT', 'AZE', 'BHS', 'BHR', 'BGD', 'BLR', 'BEL', 'BMU', 'BTN', 'BIH', 'BGR', 'CAN', 'CHN', 'HRV', 'CYP', 'CZE', 'CYN', 'DNK', 'EGY', 'EST', 'FIN', 'FRA', 'FRO', 'GEO', 'DEU', 'GIB', 'GRC', 'GRL', 'GGY', 'HUN', 'ISL', 'IMN', 'IRN', 'IRQ', 'IRL', 'ISR', 'ITA', 'JEY', 'JPN', 'JOR', 'KAZ', 'KOS', 'KWT', 'KGZ', 'LVA', 'LBN', 'LBY', 'LIE', 'LTU', 'LUX', 'MLT', 'MDA', 'MCO', 'MNG', 'MSR', 'MNE', 'MAR', 'NPL', 'NLD', 'MKD', 'NOR', 'PAK', 'PSE', 'POL', 'PRT', 'QAT', 'ROU', 'RUS', 'SMR', 'SAU', 'SRB', 'SVK', 'SVN', 'KOR', 'ESP', 'SWE', 'CHE', 'SYR', 'TWN', 'TJK', 'TUN', 'TUR', 'UKR', 'GBR', 'USA', 'UZB', 'VAT']
    tropics = ['AGO', 'AIA', 'ABW', 'ARE', 'ATG', 'BDI', 'BEN', 'BFA', 'BLZ', 'BOL', 'BRA', 'BRB', 'BRN', 'BWA', 'CYM', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'DJI', 'DMA', 'DOM', 'ECU', 'ERI', 'ETH', 'FJI', 'FSM', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'GRD', 'GTM', 'GUY', 'HKG', 'HND', 'HTI', 'IDN', 'IND', 'JAM', 'KEN', 'KHM', 'KNA', 'LAO', 'LBR', 'LCA', 'LKA', 'MAC', 'MDG', 'MDV', 'MEX', 'MHL', 'MLI', 'MMR', 'NRU', 'MOZ', 'MRT', 'MUS', 'MWI', 'MYS', 'NER', 'NGA', 'NIC', 'OMN', 'PAN', 'PER', 'PHL', 'PNG', 'PRY', 'RWA', 'SHN', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV', 'SOM', 'SSD', 'STP', 'SUR', 'SYC', 'TCD', 'TGO', 'TON', 'THA', 'TLS', 'TTO', 'TZA', 'TCA', 'UGA', 'VCT', 'VEN', 'VNM', 'VUT', 'WSM', 'YEM', 'ZMB', 'ZWE']
    south = ['ARG', 'AUS', 'CHL', 'FLK', 'SWZ', 'LSO', 'NAM', 'NZL', 'ZAF', 'URY']

    island_list = islands + not_islands

    hemis1 = north + tropics + south


    print("Islands = ", list_complete(key_list, island_list))
    print("hemis1 = ", list_complete(key_list, hemis1))
    """
    # write the country data file
    create_country_file()



# stand alone test run
if __name__ == "__main__":
    main()
