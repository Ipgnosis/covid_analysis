#  output parameterized data for a country

from covid_package.libs.aggregate_data import fetch_latest_data_date


def get_data_items(this_data, iso_list, param_list):

    # get the last date that data is available
    this_date = fetch_latest_data_date(this_data, iso_list)

    return_str = ""

    for iso in iso_list:

        for item in param_list:
            return_str += "\n {}".format(this_data[iso][this_date][item])

    return return_str


def main():

    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\ipgn_covid")

    from covid_package.libs.store_data import read_data

    # read the data file from the data dir
    data = read_data()

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
