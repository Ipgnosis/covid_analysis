# output key information on available data by country

from covid_package.libs.aggregate_data import count_daily_records, fetch_date_range


def get_country_records(this_data, list_of_keys):

    return_str = ""

    for iso in list_of_keys:

        this_country = this_data[iso]["location"]

        daily_records = count_daily_records(this_data, iso)

        date_range = fetch_date_range(this_data, iso)

        iso_str = "\n{}: {} = {}; from {} to {}.".format(
            iso, this_country, str(daily_records), str(date_range[0]), str(date_range[1]))

        return_str += iso_str

    return return_str


def main():

    import os
    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\pandas")

    from pathlib import Path
    from covid_package.libs.store_data import read_data
    from covid_package.libs.valid_keys import fetch_l0_keys

    # get data
    CURRENT_DIR = os.path.abspath('')
    sys.path.append(CURRENT_DIR)

    FILE_NAME = 'owid-covid-data.json'
    file_path = os.path.join(CURRENT_DIR, 'data', FILE_NAME)
    DATA_FILE = Path(file_path)

    # read the data file from the data dir
    data = read_data(DATA_FILE)

    key_list = fetch_l0_keys(data)

    print("Testing get_country_records.py")

    # run the function
    print(get_country_records(data, key_list))


# stand alone test run
if __name__ == "__main__":
    main()
