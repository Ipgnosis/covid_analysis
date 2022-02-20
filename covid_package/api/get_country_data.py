#  outputs data for a country, based on a country key

import json

# the country (level 0) api
# returns all the data for a country

def get_l0_data(this_data, this_country):

    country_data = json.dumps(
        this_data[this_country], indent=4, skipkeys=False)

    return country_data

# the level 1 api
# req_keys is a list of level 1 keys
# returns a dict containing all the required resources from level 1
def get_l1_data(this_data, req_keys):

    return_dict = dict()

    for iso, country in this_data.items():

        country_dict = dict()
        for req_key in req_keys:

            if req_key in country.keys():
                country_dict[req_key] = country[req_key]
        return_dict[iso] = country_dict

    return return_dict

# the level 2 key api
# req_keys is a list of level 2 keys
# for returns a dict with key = iso, values = list of dicts containing only the required resources
def get_l2_iso_data(this_data, req_keys):

    return_dict = dict()

    for iso, val in this_data.items():

        data_list = []

        # traverse the list of day objects
        for day in val['data']:

            day_data = False  # we haven't found any data yet
            day_dict = dict()

            # traverse the day object looking for the required key:vals
            for req_key in req_keys:
                # locate the required data in the day dict
                if req_key in day.keys():
                    day_data = True  # we have now found data
                    # write the key:val
                    day_dict[req_key] = day[req_key]

            # only append the day_dict to the list if we have found data
            if day_data:
                # only add the date key_val if we have found data
                day_dict['date'] = day['date']
                data_list.append(day_dict)

        # add the country data to the return data
        return_dict[iso] = data_list

    return return_dict


# the level 2 date api
# req_res is a list of level 2 keys
# for returns a dict with key = date, values = list of resource values
# each dict is has a key = iso, value is a list containing only the required resources
def get_l2_date_data(this_data, these_dates, req_res):

    return_dict = dict()

    # initialize a resource list with zeros so we have an exhaustive set of values
    # zero_list = [0] * len(req_res)

    # iterate over the date list - note that we might be working with a subset of dates
    for this_date in these_dates:
        date_dict = dict()

        # iterate over the countries
        for iso, val in this_data.items():

            # initialize the country list with the resource values set to 0
            # country_list = zero_list.copy()
            # country_list = []
            country_list = [0] * len(req_res)

            # iterate over the country's date dictionaries
            for day in val['data']:

                # verify that the date is the one we are looking for
                # note that countries don't always report every day
                if this_date == day['date']:

                    # iterate over the resources being collated
                    # note that countries don't report all values on all days

                    for r, res in enumerate(req_res):
                        # locate the required data in the day dict
                        if res in day:
                            # store the req_res value
                            country_list[r] = day[res]

                    # let's get fancy and use a list comprehension instead of the code block above
                    # country_list = [day[res] if res in day.keys() else 0 for res in enumerate(req_res)]

            date_dict[iso] = country_list

        return_dict[this_date] = date_dict

    return return_dict


# stand alone test code
def main():

    import os
    import sys

    from pathlib import Path

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis"
    sys.path.append(proj_loc)

    from covid_package.data_funcs.store_data import read_json_data, convert_owid_data
    from covid_package.libs.aggregate_data import fetch_date_list
    import config
    import modify
    # from covid_package.libs.valid_keys import fetch_l0_keys

    # define data path
    FILE_NAME = 'owid-covid-data.json'
    file_path = os.path.join(proj_loc, 'data', FILE_NAME)
    DATA_FILE = Path(file_path)

    # read the data file from the data dir
    data = read_json_data(DATA_FILE)
    data = convert_owid_data(data)

    # key_list = fetch_l0_keys(data)
    # key_list = ['WRL', 'USA']

    print("Testing...")

    start_date = config.DATA_START_DATE
    end_date = config.LATEST_DATA_DATE
    date_list = ['2021-01-01', '2021-01-02', '2021-01-03']
    #date_list = fetch_date_list(data, start_date=start_date, end_date=end_date)
    print(date_list)
    # req_l1_data = ['population', 'gdp_per_capita']
    req_l2_data = ['new_cases_per_million', 'new_deaths_per_million']

    # run the functions
    # print(get_l0_data(data, req_country))

    print(get_l2_date_data(data, date_list, req_l2_data))

    # print(get_l2_iso_data(data, resources))

    # print(get_l2_date_data(data, date_list, resources))


# stand alone test run
if __name__ == "__main__":
    main()
