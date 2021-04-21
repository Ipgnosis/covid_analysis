# takes output from get_l2_keys_data (params = ['new_cases_per_million', 'new_deaths_per_million'])
# outputs global standard deviation for that day

import numpy as np

# calculating the standard deviations for cases and deaths for a given date
# return a tuple with values for a given date: (case_std, death_std)

def get_case_death_stdev(day_dict):

    case_list_pm = []
    death_list_pm = []

    # iterate across the day_dict:
    for country in day_dict:

        case_list_pm.append(day_dict[country][0])
        death_list_pm.append(day_dict[country][1])

    case_pm_std = np.std(case_list_pm)
    death_pm_std = np.std(death_list_pm)

    #print("gcdstd: case_std = ", case_pm_std)
    #print("gcdstd: death_std = ", death_pm_std)

    return (round(case_pm_std, 3), round(death_pm_std, 3))


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

    #all_dates = ["2020-09-01", "2020-09-02", "2020-09-03"]

    print("\nTesting get_case_death_mean_std.py:")

    #print("all_dates =", all_dates)

    # fix this                         VVVV
    resuwt = get_case_death_stdev(agg_test_data)

    print(resuwt['2020-09-02'])


# stand alone test run
if __name__ == "__main__":
    main()
