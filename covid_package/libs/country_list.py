# extract country keys and country names from json

# compiles a list of distinct countries, excluding aggregations


def fetch_countries(this_data):

    temp_country_list = []

    for key, country in this_data.items():
        if str(key)[0:3] != "OWI":
            temp_country_list.append(country["location"])

    return temp_country_list


def main():

    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\ipgn_covid")

    from covid_package.libs.valid_keys import fetch_l0_keys

    country_test_data = {
        "AFG": {"location": "Afghanistan"},
        "OWID_WRL": {"location": "World"},
        "BEL": {"location": "Belgium"},
        "CAN": {"location": "Canada"}
    }

    print("Testing get_country_list.py:")

    country_keys = fetch_l0_keys(country_test_data)

    print("Key list = ", country_keys)

    country_list = fetch_countries(country_test_data)

    print("Country list = ", country_list)


# stand alone test run
if __name__ == "__main__":
    main()
