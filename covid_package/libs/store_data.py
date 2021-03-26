# read covid data and apply small kluge for consistency

# Note that in the OWID data, Kosovo has a special iso_code: OWID_KOS   Kosovo
# So for consistency, per above, Kosovo is being assigned a fake iso_code KOS


import json


def read_data(fname):

    with open(fname) as json_file:
        this_data = json.load(json_file)

    # change the iso_code for Kosovo, for consistency
    this_data['KOS'] = this_data['OWID_KOS']
    this_data.pop('OWID_KOS', None)

    return this_data
