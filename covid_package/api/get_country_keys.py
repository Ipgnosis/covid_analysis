#  outputs list of distinct country key mappings

from typing import get_type_hints


def get_country_key_mappings(this_data):

    keys_locations = this_data.items()

    return_str = {str(key): str(value["location"])
                  for key, value in keys_locations if str(key)[0:3] != "OWI"}

    return return_str

#################################
# fix this below
#################################
def main():

    #from covid_package.libs.store_data import read_json_data

    # read the data file from the data dir
    #data = read_json_data()

    # run the function
    #print(get_country_key_mappings(data))
    pass


# stand alone test run
if __name__ == "__main__":
    main()
