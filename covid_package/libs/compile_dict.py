from covid_package.api.get_stdev_data import get_stdevs


# collate all the relevant data for the analysis in question
# return a dict containing the data with WRL and standard deviation separated out
def collate_data(this_country_date_data):
    """ Collates the data for a specific pair of L2 attributes and returns a dict
    containing that data for World, the Std Dev values and the data for all countries
    and all available dates.
    """
    # cycle through each day's collections of new cases and new deaths
    data_dict = dict()

    for day, vals in this_country_date_data.items():

        # print(day)

        # calculate the values for World
        wrl_val_1 = vals['WRL'][0]
        wrl_val_2 = vals['WRL'][1]

        # pop the wrl vals out of the structure
        # so they don't screw up the stdev calculation
        vals.pop('WRL')

        # calculate the std dev for the day
        mean_stdev = get_stdevs(vals)

        # populate the date dict for this day
        data_dict[day] = {
            "wrl_val_1": wrl_val_1,
            "wrl_val_2": wrl_val_2,
            "stdev_upper_val_1": wrl_val_1 + mean_stdev[0],
            "stdev_lower_val_1": max(wrl_val_1 - mean_stdev[0], 0),
            "stdev_upper_val_2": wrl_val_2 + mean_stdev[1],
            "stdev_lower_val_2": max(wrl_val_2 - mean_stdev[1], 0),
            "country_vals": vals
        }

    print("data_dict compiled")

    return data_dict


# collate all the relevant data for the analysis in question
# return a dict containing the data with WRL and standard deviation separated out
def collate_print_data(isos, all_country_res_data):
    """ Collates the data for and returns a dict containing that data for World,
    the Std Dev values and the data for all countries and all available dates.
    """

    # declare the vars
    print_dict = dict()
    x_axis = country_val1 = country_val2 = []
    yw1_axis = yw1_upper = yw1_lower = []
    yw2_axis = yw2_upper = yw2_lower = []

    # cycle through each day's collections of values
    for key, vals in all_country_res_data.items():

        # print(key)
        x_axis.append(key)

        # store the value for World
        wrl_val_0 = vals['WRL'][0]
        wrl_val_1 = vals['WRL'][1]

        # collate the values for World
        yw1_axis.append(vals['WRL'][0])
        yw2_axis.append(vals['WRL'][1])

        # pop the wrl vals out of the structure
        # so they don't screw up the stdev calculation
        vals.pop('WRL')

        # calculate the std dev for the day
        mean_stdev = get_stdevs(vals)

        # collate the WRL values for the two plots
        yw1_upper.append(wrl_val_0 + mean_stdev[0])
        yw1_lower.append(max(wrl_val_0 - mean_stdev[0], 0))
        yw2_upper.append(wrl_val_1 + mean_stdev[1])
        yw2_lower.append(max(wrl_val_1 - mean_stdev[1], 0))

        # trim down the country_data_data to the target isos
        for i in range(len(isos)):
            country_val1.append(vals[isos[i]][0])
            country_val2.append(vals[isos[i]][1])

    # print(x_axis)
    # populate the print dict
    print_dict["x_axis"] = x_axis
    print_dict["yw1_axis"] = yw1_axis
    print_dict["yw2_axis"] = yw2_axis
    print_dict["yw1_upper"] = yw1_upper
    print_dict["yw1_lower"] = yw1_lower
    print_dict["yw2_upper"] = yw2_upper
    print_dict["yw2_lower"] = yw2_lower
    print_dict["country_val1"] = country_val1
    print_dict["county_val2"] = country_val2

    print("print_dict compiled")

    return print_dict
