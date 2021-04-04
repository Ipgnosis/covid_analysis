# takes output from get_l2_keys_data (params = ['new_cases_per_million', 'new_deaths_per_million'])
# outputs a global mean and standard deviation for each date

import numpy as np

# return a json containing key:value = date_string:tuple,
# format = {'date_string': (case_mean, case_std, death_mean, death_std)}

##################################################
# need to weight the country numbers by population
##################################################
def get_case_death_mean_std(this_data, these_keys, these_dates):

    date_obj = dict()

    res_list = ["new_cases_per_million", "new_deaths_per_million"]

    # a bunch of json manipulation here

    for this_date in range(len(these_dates)):
        obj_date = these_dates[this_date]
        case_list = []
        death_list = []
        for key in range(len(these_keys)):
            country = these_keys[key]
            for date_data in range(len(this_data[country]['data'])):
                #print("date_data:", this_data[country]['data'][date_data])
                #print("obj_date =", obj_date)
                if obj_date == this_data[country]['data'][date_data]['date']:

                    if res_list[0] in this_data[country]['data'][date_data]:
                        #####################################
                        case_list.append(
                            this_data[country]['data'][date_data][res_list[0]])

                    if res_list[1] in this_data[country]['data'][date_data]:
                        #####################################
                        death_list.append(
                            this_data[country]['data'][date_data][res_list[1]])
        #print("case_list =", case_list)
        #print("death_list = ", death_list)

        if len(case_list) > 0 and len(death_list) > 0:
            case_mean = np.mean(case_list)
            case_std = np.std(case_list)
            death_mean = np.mean(death_list)
            death_std = np.std(death_list)
        else:
            case_mean = 0
            case_std = 0
            death_mean = 0
            death_std = 0

        date_obj[obj_date] = (case_mean, case_std, death_mean, death_std)

    return date_obj


def main():

    import sys

    sys.path.append("c:\\Users\\Ipgnosis\\Documents\\Github\\covid_analysis")

    agg_test_data = {
        "AFG": {"population": 38928341.0,
                "data": [{"date": "2020-09-01", "new_cases_per_million": 1, "new_deaths_per_million": 1},
                         {"date": "2020-09-02", "new_cases_per_million": 2},
                         {"date": "2020-09-03", "new_cases_per_million": 1}]
                },
        "BEL": {"gdp_per_capita": 42658.576,
                "data": [{"date": "2020-09-01", "new_cases_per_million": 1, "new_deaths_per_million": 1},
                         {"date": "2020-09-02", "new_cases_per_million": 2},
                         {"date": "2020-10-03", "new_cases_per_million": 3}]
                },
        "CAN": {"median_age": 41.4,
                "data": [{"date": "2020-09-01", "new_cases_per_million": 1, "new_deaths_per_million": 1},
                         {"date": "2020-09-02", "new_cases_per_million": 2,
                             "new_deaths_per_million": 2},
                         {"date": "2020-09-03", "new_cases_per_million": 3}]
                },
        "VAT": {"median_age": 21000,
                "data": [{"date": "2020-09-01", "new_cases_per_million": 1, "new_deaths_per_million": 1},
                         {"date": "2020-09-02", "new_cases_per_million": 2},
                         {"date": "2020-09-03", "new_cases_per_million": 3}]
                }
    }

    agg_country_keys = ["AFG", "BEL", "CAN", "VAT"]

    all_dates = ["2020-09-01", "2020-09-02", "2020-09-03"]

    print("\nTesting get_case_death_mean_std.py:")

    #print("all_dates =", all_dates)

    resuwt = get_case_death_mean_std(
        agg_test_data, agg_country_keys, all_dates)

    print(resuwt['2020-09-02'])


# stand alone test run
if __name__ == "__main__":
    main()
