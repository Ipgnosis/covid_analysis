#  output parameterized data for a country

from covid_package.libs.aggregate_data import fetch_latest_data_date



# gets the latest level 1 string value for a given resource
def get_data_items(this_data, iso_list, param_list):

    # get the last date that data is available
    this_date = fetch_latest_data_date(this_data, iso_list)

    return_str = ""

    for iso in iso_list:

        for item in param_list:
            return_str += "\n {}".format(this_data[iso][this_date][item])

    return return_str


def main():

    import os
    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis")
    import config, modify


    from covid_package.data_funcs.store_data import read_json_data
    from covid_package.libs.valid_keys import fetch_l0_keys
    import config, modify


    # read the data file from the data dir
    data = read_json_data(config.DATA_FILE_STR)

    #key_list = fetch_l0_keys(data)

    test_country = "USA"
    items_list = ['gdp_per_capita',
                  'total_cases_per_million', 'total_deaths_per_million']

    # run the function
    print(get_data_items(data, test_country, items_list))

    # 3 items: gdp_per_capita, total_cases_per_million, total_deaths_per_million

    """
    {
        "AFG": {"gdp_per_capita": 1234, "total_cases_per_million": 12345, "total_deaths_per_million": 1234},
        "USA": {"gdp_per_capita": 12345, "total_cases_per_million": 54321, "total_deaths_per_million": 4321}
    }
    """


# stand alone test run
if __name__ == "__main__":
    main()
