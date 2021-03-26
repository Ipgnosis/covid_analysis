#  outputs data for a country, based on a country key

import json

# the country api


def get_country_data(this_data, this_country):

    country_data = json.dumps(
        this_data[this_country], indent=4, skipkeys=False)

    return country_data

# the level 1 api


def get_level_1_data(this_data, these_keys, req_keys):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        for req_key in req_keys:
            if req_key in this_data[iso].keys():
                country_dict[req_key] = this_data[iso][req_key]
        return_dict[iso] = country_dict

    return return_dict

# the level 2 key api


def get_l2_keys_data(this_data, these_keys, req_keys):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        country_list = []
        day_data = False
        for day in range(len(this_data[iso]['data'])):
            day_dict = dict()
            day_dict['date'] = this_data[iso]['data'][day]['date']
            for req_key in req_keys:
                if req_key in this_data[iso]['data'][day].keys():
                    day_data = True
                    day_dict[req_key] = this_data[iso]['data'][day][req_key]
            if day_data:  # only write the day
                country_list.append(day_dict)
            country_dict['data'] = country_list
        return_dict[iso] = country_dict

    return return_dict

# the level 2 date api


def get_l2_date_data(this_data, these_keys, this_date):

    return_dict = dict()

    for iso in these_keys:
        country_dict = dict()
        country_list = []
        for day in range(len(this_data[iso]['data'])):
            if this_data[iso]['data'][day]['date'] == this_date:
                country_list.append(this_data[iso]['data'][day])

            country_dict['data'] = country_list

        return_dict[iso] = country_dict

    return return_dict
