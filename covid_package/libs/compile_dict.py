from covid_package.api.get_stdev_data import get_stdevs
from datetime import datetime


### OLD VERSION - retained for backwards compat - see below for new version ###
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
    """ Collates the data for a specific pair of L2 attributes and returns a dict
    containing that data for World, the Std Dev values and the data for all countries
    and all available dates.
    """

    # declare the vars
    print_dict = dict()
    print_dict["x_axis"] = []
    print_dict["yw1_axis"] = []
    print_dict["yw2_axis"] = []
    print_dict["yw1_upper"] = []
    print_dict["yw1_lower"] = []
    print_dict["yw2_upper"] = []
    print_dict["yw2_lower"] = []
    print_dict["ax1_vals"] = []
    print_dict["ax2_vals"] = []

    # dynamically create 2 y-axis lists for each iso
    for iso in isos:
        locals()['ax1_' + iso] = []
        locals()['ax2_' + iso] = []

    # cycle through each day's collections of values
    for key, vals in all_country_res_data.items():

        print_dict["x_axis"].append(datetime.strptime(key, "%Y-%m-%d"))

        # store the value for World
        wrl_val_0 = vals['WRL'][0]
        wrl_val_1 = vals['WRL'][1]

        # collate the values for World
        print_dict["yw1_axis"].append(vals['WRL'][0])
        print_dict["yw2_axis"].append(vals['WRL'][1])

        # pop the wrl vals out of the structure
        # so they don't screw up the stdev calculation
        stdev_vals = vals.copy()
        stdev_vals.pop('WRL')

        # calculate the std dev for the day
        mean_stdev = get_stdevs(stdev_vals)

        # collate the WRL values for the two plots
        print_dict["yw1_upper"].append(wrl_val_0 + mean_stdev[0])
        print_dict["yw1_lower"].append(max(wrl_val_0 - mean_stdev[0], 0))
        print_dict["yw2_upper"].append(wrl_val_1 + mean_stdev[1])
        print_dict["yw2_lower"].append(max(wrl_val_1 - mean_stdev[1], 0))

        # trim down the country_data_data to the target isos
        # append the ax1 and ax1 y-axis plot values to the respective lists
        for iso in isos:
            locals()['ax1_' + iso].append(vals[iso][0])
            locals()['ax2_' + iso].append(vals[iso][1])

    # dynamically append the 2 y-axis lists to the plot lists
    for iso in isos:
        print_dict["ax1_vals"].append(locals()['ax1_' + iso])
        print_dict["ax2_vals"].append(locals()['ax2_' + iso])

    # print("print_dict compiled")

    return print_dict
