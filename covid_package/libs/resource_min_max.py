# get the min and max values of a given resource

def get_min_max(this_data, level, min_max, res, count):

    temp_dict = dict()

    if level == 'l1':
        for key, val in this_data.items():
            val_max = -1
            val_min = 999999999999
            if res in val.keys():
                if min_max == 'max':
                    if val[res] > val_max:
                        val_max = val[res]
                else:
                    if val[res] < val_min:
                        val_min = val[res]

            if min_max == 'max':
                temp_dict[key] = val_max
            else:
                temp_dict[key] = val_min

    elif level == 'l2':
        for key, val in this_data.items():
            val_max = -1
            val_min = 999999999999
            for day in val['data']:
                if res in day.keys():
                    if min_max == 'max':
                        if day[res] > val_max:
                            val_max = day[res]
                    else:
                        if day[res] < val_min:
                            val_min = day[res]

            if min_max == 'max':
                temp_dict[key] = val_max
            else:
                temp_dict[key] = val_min

    if min_max == 'max':
        return_dict = sorted(temp_dict.items(), key = lambda kv:(-kv[1], kv[0]))
    else:
        return_dict = sorted(temp_dict.items(), key = lambda kv:(kv[1], kv[0]))

    return_dict = return_dict[0: count]

    return return_dict

# test function
def main():

    agg_test_data = {
        "CAN": {"median_age": 50.0, "population": 500000.0, "gdp_per_capita": 50000.0,
                "data": [{"date": "2020-11-01", "new_cases": 50, "new_deaths": 5}, {"date": "2020-11-02", "new_cases": 56, "new_deaths": 6}, {"date": "2020-11-03","new_cases": 54, "new_deaths": 4}]
                },
        "AFG": {"median_age": 30.0, "population": 300000.0, "gdp_per_capita": 30000.0,
                "data": [{"date": "2020-11-01", "new_cases": 33, "new_deaths": 3}, {"date": "2020-11-02", "new_cases": 39, "new_deaths": 9}, {"date": "2020-11-03","new_cases": 36, "new_deaths": 6}]
                },
        "BEL": {"median_age": 60.0, "population": 600000.0, "gdp_per_capita": 60000.0,
                "data": [{"date": "2020-11-01", "new_cases": 84, "new_deaths": 4}, {"date": "2020-11-02", "new_cases": 82, "new_deaths": 2}, {"date": "2020-11-03","new_cases": 88, "new_deaths": 8}]
                },
        "VAT": {"median_age": 40.0, "population": 400000.0, "gdp_per_capita": 40000.0,
                "data": [{"date": "2020-11-01", "new_cases": 45, "new_deaths": 5}, {"date": "2020-11-02", "new_cases": 43, "new_deaths": 3}, {"date": "2020-11-03","new_cases": 47, "new_deaths": 7}]
                }
    }

    lvl = 'l1'
    resrce = 'population'
    #resrce = 'new_cases'
    min_or_max = 'max'
    cnt = 2

    print(get_min_max(agg_test_data, lvl, min_or_max, resrce, cnt))

if __name__ == "__main__":
    main()
