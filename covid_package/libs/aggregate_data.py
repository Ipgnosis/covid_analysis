# functions to return data from the json structure

import config

from covid_package.api.get_country_data import get_l2_iso_data

# return all data for a specific country
def fetch_country_data(this_data, this_country):

    return this_data[this_country]

# return specific items from the top level data


def fetch_top_level_data(this_data, this_country, this_key):

    # print(this_key)

    if this_key in this_data[this_country].keys():
        # print(this_data[this_country].keys())
        return this_data[this_country][this_key]
    else:
        return None

# return the number of day records for a country


def count_daily_records(this_data, this_country):

    return len(this_data[this_country]["data"])

# return the date range of the daily records for a country

def fetch_date_range(this_data, this_country):

    start_date = this_data[this_country]["data"][0]["date"]
    end_index = len(this_data[this_country]["data"]) - 1
    end_date = this_data[this_country]["data"][end_index]["date"]

    return start_date, end_date


# return an ordered list of distinct dates contained in the data
def fetch_date_list(this_data, **kwargs):

    date_list = []

    if kwargs:
        this_start_date = kwargs['start_date']
        this_end_date = kwargs['end_date']
    else:
        this_start_date = config.DATA_START_DATE
        this_end_date = config.LATEST_DATA_DATE

    for this_country in this_data.keys():
        for day_obj in this_data[this_country]['data']:
            if (day_obj['date'] >= this_start_date) and (day_obj['date'] <= this_end_date) and (day_obj['date'] not in set(date_list)):
                date_list.append(day_obj['date'])

    sorted_dates = sorted(date_list, key=lambda x: x)

    return sorted_dates

# return the date of the latest data

def fetch_latest_data_date(this_data):

    latest_date = "2020-01-01"
    idx = -1

    while idx >= -5:
        if this_data['WRL']["data"][idx]["new_cases"] > 0:
            latest_date = this_data['WRL']["data"][idx]["date"]
            break
        idx -= 1

    # store this in global
    config.LATEST_DATA_DATE = latest_date

    if latest_date == "2020-01-01":
        latest_date = "ERROR"

    return latest_date

# aggregate the values from a specific country and second level resource
def aggregate_second_level_data(this_data, this_country, this_key):

    temp_data = 0

    for day in this_data[this_country]["data"]:
        temp_data += day[this_key]

    return round(temp_data, 3)


# get the top/bottom N counties and instances of a specific value
def get_min_max_data(main_data, iso_list, res_list, enn):

    # initialize two dicts of variable length to store the result
    tops = dict()
    bottoms = dict()
    for res in res_list:
        tops[res] = [0]
        bottoms[res] = [999999999]


    iso_data = get_l2_iso_data(main_data, iso_list, res_list)

    for iso in iso_data:
        for day in iso:
            for res in res_list:
                tops[res].append({iso: day[res]})
                bottoms[res].append({iso: day[res]})
                pass



"""
def get_country_summary(this_data, this_country):
    ###################################################
    pass
"""


def main():

    import os
    import sys

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis"

    sys.path.append(proj_loc)

    import config
    import modify

    from pathlib import Path
    from covid_package.data_funcs.store_data import read_json_data
    from covid_package.data_funcs.store_data import convert_owid_data
    from covid_package.libs.valid_keys import fetch_l0_keys
    from covid_package.api.get_country_data import get_l2_iso_data

    # get data

    FILE_NAME = 'owid-covid-data.json'
    file_path = os.path.join(proj_loc, 'data', FILE_NAME)
    DATA_FILE = Path(file_path)

    # read the data file from the data dir
    data = read_json_data(DATA_FILE)

    print("Testing...")

    #key_list = fetch_l0_keys(data)

    data = convert_owid_data(data)

    print("Dates of data are:", fetch_date_range(data, 'WRL'))


    """
    agg_test_data = {
        "CAN": {"median_age": 41.4,
                "data": [{"date": "2020-11-01", "new_deaths": 1}, {"date": "2020-11-02", "new_deaths": 2}, {"date": "2020-11-03", "new_deaths": 3}]
                },
        "AFG": {"population": 38928341.0,
                "data": [{"date": "2020-09-01", "new_cases": 1}, {"date": "2020-09-02", "new_cases": 1}, {"date": "2020-09-03", "new_cases": 1}]
                },
        "BEL": {"gdp_per_capita": 42658.576,
                "data": [{"date": "2020-10-01", "new_cases_per_million": 0.1}, {"date": "2020-10-02", "new_cases_per_million": 0.1}, {"date": "2020-10-03", "new_cases_per_million": 0.1}]
                },
        "VAT": {"median_age": 21000,
                "data": [{"date": "2020-12-01", "new_cases_per_million": 0.1}, {"date": "2020-12-02", "new_cases_per_million": 0.1}, {"date": "2020-12-03", "new_cases_per_million": 0.1}]
                }
    }

    agg_country_keys = ["AFG", "BEL", "CAN", "VAT"]

    print("\nTesting aggregate_data.py:")

    print(fetch_date_list(agg_test_data, agg_country_keys))

    print("count_daily_records (ans = 3):",
          count_daily_records(agg_test_data, "AFG"))
    print("get_date_range AFG (ans = ('2020-09-01', '2020-09-03')):",
          fetch_date_range(agg_test_data, "AFG"))

    print("Latest data date:", fetch_latest_data_date(
        agg_test_data, agg_country_keys))

    print("Testing get_top_level_data():")

    print("'AFG': 'population' = ", fetch_top_level_data(
        agg_test_data, "AFG", "population"))

    print("'BEL': 'gdp_per_capita' = ", fetch_top_level_data(
        agg_test_data, "BEL", "gdp_per_capita"))

    print("'CAN': 'median_age' = ", fetch_top_level_data(
        agg_test_data, "CAN", "median_age"))

    print("'VAT': 'gdp_per_capita' = ", fetch_top_level_data(
        agg_test_data, "VAT", "gdp_per_capita"))

    print("Testing aggregate_second_level_data():")

    print("'AFG': new_cases (ans = 3)", aggregate_second_level_data(
        agg_test_data, "AFG", "new_cases"))
    print("'BEL': new_cases_per_million (ans = 0.3)", aggregate_second_level_data(
        agg_test_data, "BEL", "new_cases_per_million"))
    print("'CAN': new_deaths (ans = 6)", aggregate_second_level_data(
        agg_test_data, "CAN", "new_deaths"))
    """

# stand alone test run
if __name__ == "__main__":
    main()
