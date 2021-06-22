# output key information on available data by country

def get_country_records(this_data):

    return_str = ""

    for country, info in this_data.items():

        iso_str = "\n{}: {} = {}; from {} to {}.".format(
            country, info["location"], str(len(info['data'])), str(info['data'][0]['date']), str(info['data'][-1]['date']))

        return_str += iso_str

    return return_str


def main():

    import sys
    """
    sys.path.append("C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\covid_package\\data_funcs")
    sys.path.append("C:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis\\data")

    #from store_data import read_json_data, convert_owid_data

    # get data
    data = read_json_data('owid-covid-data.json')
    data = convert_owid_data(data)


    print("Testing get_country_records.py")

    # run the function
    print(get_country_records(data))
    """

# stand alone test run
if __name__ == "__main__":
    main()
