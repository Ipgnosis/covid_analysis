# imports

from datetime import datetime, timedelta
# set up file paths and other data globals

import config
import modify

# local imports

from covid_package.data_funcs.store_data import read_json_data, convert_owid_data

from covid_package.libs.aggregate_data import fetch_latest_data_date, fetch_date_list
from covid_package.libs.compile_dict import collate_print_data

from covid_package.api.get_country_data import get_l2_date_data

from covid_package.plots.multi_plot import multi_plots

print("Imports complete")

# read the updated(?) data file from the data dir
data = read_json_data(config.DATA_FILE_STR)

# convert the OWID_ data so that we don't trip up fetch_latest_data_date
data = convert_owid_data(data)

print("Data read")

# set the latest data date global
config.LATEST_DATA_DATE = fetch_latest_data_date(data)

start_date = config.DATA_START_DATE
end_date = config.LATEST_DATA_DATE

date_list = fetch_date_list(data)

# set up chart_labels dict

chart_labels = dict()

# define plot values
chart_labels['width'] = 15
chart_labels['height'] = 10
chart_labels['tsize'] = 16
chart_labels['fsize'] = 12
chart_labels['lsize'] = 10
chart_labels['y_isos'] = []
chart_labels['y_axis_labels'] = []


# define the list of required resources
res = ['new_cases_smoothed_per_million', 'new_deaths_smoothed_per_million']

chart_labels['expl_str'] = "New case/death"
chart_labels['descr_str_1'] = res[0].replace('_', ' ').capitalize()
chart_labels['descr_str_2'] = res[1].replace('_', ' ').capitalize()

# returns a dict with key = date, values = dict of isos
# the value of each iso key is a list of the required resources
country_date_data = get_l2_date_data(data, date_list, res)

print("get_l2_date_data complete")

# chart_labels['y_isos'] = ['USA', 'GBR']
chart_labels['y_isos'] = ['AUT', 'GBR', 'DEU', 'FRA']

print_data = collate_print_data(chart_labels['y_isos'], country_date_data)

print("collate_print_data complete")

# assemble the locations list
for iso in chart_labels['y_isos']:
    chart_labels['y_axis_labels'].append(data[iso]['location'])


# call multi_plots
multi_plots(chart_labels, print_data)
