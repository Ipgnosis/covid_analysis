#  outputs list of country keys and locations, excluding the OWID_ keys

#from typing import get_type_hints


def get_country_key_mappings(this_data):

    # note that the OWID_ exclusion has been replaced by libs/convert_owid_data
    # however, when run stand-alone, those keys still exist
    return {str(key): str(value["location"])
                  for key, value in this_data.items() if str(key)[0:5] != "OWID_"}



def main():

    import os
    import sys

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis"

    sys.path.append(proj_loc)

    from pathlib import Path
    from covid_package.data_funcs.store_data import read_json_data
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data

    FILE_NAME = 'owid-covid-data.json'
    file_path = os.path.join(proj_loc, 'data', FILE_NAME)
    DATA_FILE = Path(file_path)

    # read the data file from the data dir
    data = read_json_data(DATA_FILE)

    print("Testing...")

    # run the function

    test_result = get_country_key_mappings(data)

    for key, value in test_result.items():
        print("iso =", key, "location = ", value)


# stand alone test run
if __name__ == "__main__":
    main()
