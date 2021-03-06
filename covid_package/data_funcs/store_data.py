# utility functions for managing data

# convert the 'OWID_' iso_codes to 3 char codes or remove
def convert_owid_data(this_data):
    """ Takes the OWID json as an input and returns a converted json as an output.
        Removes all isos starting with 'OWID_'. Some are removed as they are just aggregates of the
        country data.  Some are converted as they are actually countries whose existence is
        challenged by other countries (e.g. Kosovo)  OWID_WRL is convered to WRL, a synthetic
        'country' as it contains the aggregated data for the world that is used by other functions.
    """

    # the list(s) of OWID_ data that we are going to remove for consistency

    # don't pop the INT data
    # owid_list = ['OWID_AFR', 'OWID_ASI', 'OWID_EUR', 'OWID_EUN', 'OWID_HIC', 'OWID_LIC', 'OWID_LMC', 'OWID_NAM', 'OWID_OCE', 'OWID_SAM', 'OWID_UMC']

    # pop the iso_code for International, for consistency
    # this data causes bugs since it is missing key resources, e.g. population
    # exclusion may cause minor inconsistencies because it includes a small number of
    # cases that are not attributable to a country (e.g. cases at sea)

    # pop the INT data
    owid_list = ['OWID_INT', 'OWID_AFR', 'OWID_ASI', 'OWID_EUR', 'OWID_EUN', 'OWID_HIC', 'OWID_LIC', 'OWID_LMC', 'OWID_NAM', 'OWID_OCE', 'OWID_SAM', 'OWID_UMC']

    # clear out the unneeded 'OWID_' entries
    [this_data.pop(i) for i in owid_list]

    # change the iso_code for Northern Cyprus, for consistency
    this_data['CYN'] = this_data.pop('OWID_CYN')

    # change the iso_code for Kosovo, for consistency
    this_data['KOS'] = this_data.pop('OWID_KOS')

    # change the iso_code for the World aggregation, for consistency
    this_data['WRL'] = this_data.pop('OWID_WRL')

    # trap new OWID codes
    {print(f"New OWID_ key: {key}") for key in this_data if len(key) > 3}

    return this_data


# output the contents of update-record.json
def print_update_record():
    """Output the contents of update-record.json"""

    updata = read_json_data(config.UPDATE_FILE_STR)

    print("Last update =", updata["last_update"])
    print("Earliest update =", updata["earliest_update"])

    for u, val in enumerate(updata["update_list"]):
        print(f"Update {u + 1} = {val}")


# read a json data file
def read_json_data(fname):
    """Read a json data file string/path"""

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
        return data
    except OSError as error:
        print(error)
        print("File {fname} cannot be read")
        return False


# write a json data file
def write_json_data(fname, wdata):
    """Write a json data file"""

    try:
        with open(fname, 'w', encoding='utf-8') as outfile:
            json.dump(wdata, outfile, indent=4)
        return True
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be saved")
        return False


# delete the old data
def delete_file(fname):
    """Delete the param file string/path"""

    try:
        os.remove(fname)
        return True
    except OSError as error:
        print(error)
        print(f"File {fname} cannot be removed")
        return False


# rename a file
def rename_file(fromf, tof):
    """Rename a file string/path"""

    try:
        os.rename(fromf, tof)
        return True
    except OSError as error:
        print(f"File {fromf} cannot be renamed: {error}")
        return False


# download and save new data file version
# data went missing from Github in Jan, 2022
def refresh_data():
    """Download and save new data file version.  Data went missing from GitHub in Jan 2022."""

    # get the json data from github
    try:
        downloaded_data = requests.get(config.DATA_URL_STR).json()
    except requests.exceptions.RequestException as err:
        print(f"Data download error: {err}")
        return False

    # if we updated the data without error
    if write_json_data(config.DATA_FILE_STR, downloaded_data):
        update_the_update_file()  # update the record of updates
    else:
        return False

    return True


# return a datetime string for the last time the data was updated
def get_last_file_update():
    """Return a dateime string for the last time the data was updated."""

    update_data_file = read_json_data(config.UPDATE_FILE_STR)

    last_update_str = update_data_file["last_update"]

    return last_update_str


# append new update time to UPDATE_FILE
def update_the_update_file():
    """Append the new update time to UPDATE_FILE"""

    # get the update file
    update_data = read_json_data(config.UPDATE_FILE_STR)

    # store the new update datetime
    update_data['last_update'] = config.UPDATE_DATETIME_STR
    # also push this update onto the historical record - slightly redundant but
    # this is a change as of 4/14/21 to enable easier analysis of the update times
    update_data['update_list'].append(config.UPDATE_DATETIME_STR)

    # keep a record of the earliest time that the file was updated
    # we'll need this later, but building the record for now
    # extract 2 time objects for comparison
    earliest_update = convert_datetime_str_to_obj(update_data['earliest_update'], 'time')
    this_update = convert_datetime_str_to_obj(config.UPDATE_DATETIME_STR, 'time')

    # update the earliest update time as necessary
    # don't forget that this is a datetime string
    # this will need to be reconverted later once needed
    if this_update < earliest_update:
        update_data['earliest_update'] = config.UPDATE_DATETIME_STR

    # write the updated update file
    if write_json_data(config.UPDATE_FILE_STR, update_data):
        pass
    else:
        print("Error updating UPDATE_FILE")

# test function


def main():
    """Test function"""

    print("sys.path =", sys.path)
    # to test, comment out the local imports at the top
    import config
    import modify

    # update_data = read_json_data(config.UPDATE_FILE_STR)

    # print(update_data)

    # write_json_data(config.UPDATE_FILE_STR, update_data)

    print(get_last_file_update())

    """
    dtstr = "2021-04-04T08:02:44Z"
    #dtstr = "blah-04-04T08:02:44Z"  # bad dateime string


    print_update_record()

    print("datetime =", convert_datetime_str_to_obj(dtstr, 'datetime'))

    print("date =", convert_datetime_str_to_obj(dtstr, 'date'))

    print("time =", convert_datetime_str_to_obj(dtstr, 'time'))
    """


# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":

    import sys
    proj_loc = "C:\\Users\\russe\\Documents\\Repos\\Github\\covid_analysis"
    package_loc = "C:\\Users\\russe\\Documents\\Repos\\Github\\covid_analysis\\covid_package"
    sys.path.append(proj_loc)
    sys.path.append(package_loc)

    main()

else:  # get the module imports
    import json
    import os
    import requests

    import config

    from covid_package.data_funcs.datetime_funcs import convert_datetime_str_to_obj
