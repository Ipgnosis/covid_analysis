# functions to return data from the json structure

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


def fetch_date_list(this_data, country_keys):

    date_list = []

    for this_country in country_keys:
        for date in range(len(this_data[this_country]['data'])):
            this_date = this_data[this_country]['data'][date]['date']
            if this_date not in set(date_list):
                date_list.append(this_date)

    date_list_sorted = sorted(date_list, key=lambda x: x)

    return date_list_sorted


# return the date of the latest data

def fetch_latest_data_date(this_data, country_keys):

    latest_date = "2020-01-01"

    for this_country in range(len(country_keys)):
        last_date = this_data[country_keys[this_country]]["data"][-1]["date"]
        if last_date > latest_date:
            latest_date = last_date

    return latest_date


# aggregate the values from a specific item in the second level data
def aggregate_second_level_data(this_data, this_country, this_key):

    temp_data = 0

    for day in this_data[this_country]["data"]:
        temp_data += day[this_key]

    return round(temp_data, 3)


"""
def get_max_data(this_data, max_date, this_country):

    data_list = ["total_cases", "total_deaths"]


def get_country_summary(this_data, this_country):
    ###################################################
    pass
"""


def main():

    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis")

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


# stand alone test run
if __name__ == "__main__":
    main()
