
from datetime import datetime


# do the datetime jiggery-pokery
def convert_datetime_str_to_obj(datetime_str, resolution):

    github_format = "%Y-%m-%dT%H:%M:%S%z"

    datetime_obj = datetime.strptime(datetime_str, github_format)

    if resolution == 'datetime':  # returns type datetime
        return_obj = datetime_obj

    elif resolution == 'date':  # returns type date
        return_obj = datetime.date(datetime_obj)

    elif resolution == 'time':  # returns type time
        return_obj = datetime.time(datetime_obj)

    elif resolution == 'hour':  # returns type str
        return_obj = datetime.time(datetime_obj).strftime('%H')

    elif resolution == 'minute':  # returns type str
        return_obj = datetime.time(datetime_obj).strftime('%M')

    elif resolution == 'day_num':  # returns type int
        # 1 = Monday, 7 = Sunday
        return_obj = datetime.date(datetime_obj).isoweekday()

    elif resolution == 'day':  # returns type str
        # 1 = Monday, 7 = Sunday
        return_obj = datetime.date(datetime_obj).strftime('%A')

    else:
        return False  # incorrect parameter

    return return_obj


# test function

def main():

    import sys
    # import json
    # from pathlib import Path

    # from datetime import date

    proj_loc = "c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis"

    sys.path.append(proj_loc)

    import config
    import modify

    from covid_package.data_funcs.store_data import print_update_record

    dtstr = "2021-04-04T08:02:44Z"
    # dtstr = "blah-04-04T08:02:44Z"  # bad dateime string

    print("time now =", dtstr)

    # print_update_record()

    print("datetime =", convert_datetime_str_to_obj(dtstr, 'datetime'))

    print("date =", convert_datetime_str_to_obj(dtstr, 'date'))

    print("time =", convert_datetime_str_to_obj(dtstr, 'time'))

    print("hour =", convert_datetime_str_to_obj(dtstr, 'hour'))

    print("minute =", convert_datetime_str_to_obj(dtstr, 'minute'))

    print("day_num =", convert_datetime_str_to_obj(dtstr, 'day_num'))

    print("day =", convert_datetime_str_to_obj(dtstr, 'day'))


# stand alone test run
# don't forget to flip the import statements
if __name__ == "__main__":
    main()
