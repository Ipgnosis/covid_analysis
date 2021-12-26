from covid_package.api.get_stdev_data import get_stdevs


# collate all the relevant data for the analysis in question
# return a dict containing the data
def collate_data(country_date_data):
    """ Collates the data for a specific pair of L2 attributes and returns a dict
    containing that data for World, the Std Dev values and foat data for all countries
    and all available dates.
    """
    # cycle through each day's collections of new cases and new deaths
    data_dict = dict()
    for day in country_date_data:

        # print(country_date_data[day])

        # calculate the 1st value for World
        if country_date_data[day]['WRL'][0]:
            wrl_val_1 = country_date_data[day]['WRL'][0]
        else:
            wrl_val_1 = 0

        # calculate the 2nd value for World
        if country_date_data[day]['WRL'][1]:
            wrl_val_2 = country_date_data[day]['WRL'][1]
        else:
            wrl_val_2 = 0

        # pop the wrl vals out of the structure
        # so they don't screw up the stdev calculation
        country_date_data[day].pop('WRL')

        # calculate the std dev for the day
        mean_stdev = get_stdevs(country_date_data[day])

        # populate the date dict for this day
        data_dict[day] = {
            "wrl_val_1": wrl_val_1,
            "wrl_val_2": wrl_val_2,
            "stdev_upper_val_1": wrl_val_1 + mean_stdev[0],
            "stdev_lower_val_1": max(wrl_val_1 - mean_stdev[0], 0),
            "stdev_upper_val_2": wrl_val_2 + mean_stdev[1],
            "stdev_lower_val_2": max(wrl_val_2 - mean_stdev[1], 0),
            "country_vals": country_date_data[day]
        }

    print("date_dict compiled")

    return data_dict
