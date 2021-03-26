#  generates list of keys at all 3 levels

from datetime import datetime

#  compiles a list of distinct country keys, excluding aggregations


def fetch_l0_keys(this_data):

    key_list = []

    for key in this_data.keys():
        if str(key)[0:3] != "OWI":
            key_list.append(key)

    return key_list


# compile the exhaustive list of level 1 keys (less 'data')
def fetch_l1_keys(this_data, these_keys):

    l1_keys_list = []

    for iso in these_keys:
        l1_keys = this_data[iso].keys()
        for l1_key in l1_keys:
            if l1_key != 'data' and l1_key not in l1_keys_list:
                l1_keys_list.append(l1_key)

    return l1_keys_list

# compile the exhaustive list of level2 keys


def fetch_l2_keys(this_data, these_keys):

    l2_keys_list = []

    for iso in these_keys:
        l2_objs_list = this_data[iso]['data']
        for l2_obj in l2_objs_list:
            for obj_key in l2_obj.keys():
                if obj_key not in l2_keys_list:
                    l2_keys_list.append(obj_key)

    return l2_keys_list


# validate fields against keys list
def valid_fields(these_fields, these_keys):

    for field in these_fields:
        if field not in these_keys:
            return False

    return True


# validate a date
def valid_date(this_date):

    format = '%Y-%m-%d'
    try:
        datetime.strptime(this_date, format)
        return True
    except:
        return False

# convert a date string to a datetime


def strptime_date(this_date_str):

    format = '%Y-%m-%d'

    return datetime.strptime(this_date_str, format)


# convert a strptime to a strftime


def strftime_date(this_date):

    format = '%Y-%m-%d'
    return datetime.strftime(this_date, format)
