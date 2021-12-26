import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime


# get the plot for one county
def one_plot(chart_data, this_dict):
    # declare the axis vars
    x_axis = []
    yw1_axis = []
    yw1_upper = []
    yw1_lower = []
    y1_axis = []
    yw2_axis = []
    yw2_upper = []
    yw2_lower = []
    y2_axis = []

    # load the axis data lists
    for key, val in this_dict.items():

        # list of dates for x axis
        x_axis.append(datetime.strptime(key, "%Y-%m-%d"))

        # lists of values_1 for y1 axis
        yw1_axis.append(val["wrl_val_1"])
        yw1_upper.append(val["stdev_upper_val_1"])
        yw1_lower.append(val["stdev_lower_val_1"])
        y1_axis.append(val['country_vals'][chart_data['y_iso']][0])

        # lists of values_2 for y2 axis
        yw2_axis.append(val["wrl_val_2"])
        yw2_upper.append(val["stdev_upper_val_2"])
        yw2_lower.append(val["stdev_lower_val_2"])
        y2_axis.append(val['country_vals'][chart_data['y_iso']][1])

    ###########################################################
    # package up the matplotlib data for a single country chart
    ###########################################################

    # create the labels
    chart_title_str = "{}: {} data".format(chart_data['y_axis_label'], chart_data['expl_str'])
    # x_axis_label_str = "Date"

    yw1_axis_legend_str = "Global mean"
    yw1_stdev_legend_str = "Global std dev"
    y1_axis_legend_str = "{}".format(chart_data['y_axis_label'])

    yw2_axis_legend_str = "Global mean"
    yw2_stdev_legend_str = "Global std dev"
    y2_axis_legend_str = "{}".format(chart_data['y_axis_label'])

    # define empty canvas
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(chart_data['width'], chart_data['height']))
    fig.subplots_adjust(hspace=0.5)

    # declare the axis data
    # subplot 1
    ax1.set_title(chart_data['descr_str_1'], fontsize=chart_data['fsize'])
    ax1.plot(x_axis, yw1_axis, label=yw1_axis_legend_str, color='red')
    ax1.grid()
    ax1.fill_between(x_axis, yw1_upper, yw1_lower, label=yw1_stdev_legend_str, color='orange', alpha=0.5)
    ax1.plot(x_axis, y1_axis, label=y1_axis_legend_str, color='blue')

    # subplot 2
    ax2.set_title(chart_data['descr_str_2'], fontsize=chart_data['fsize'])
    ax2.plot(x_axis, yw2_axis, label=yw2_axis_legend_str, color='red')
    ax2.grid()
    ax2.fill_between(x_axis, yw2_upper, yw2_lower, label=yw2_stdev_legend_str, color='orange', alpha=0.5)
    ax2.plot(x_axis, y2_axis, label=y2_axis_legend_str, color='blue')

    # ax2.set_xlabel(x_axis_label_str, fontsize=10)

    # declare the text data
    fig.suptitle(chart_title_str, fontsize=chart_data['tsize'])

    # format the x axis (date) labels
    # text in the x axis will be displayed in 'YYYY-mm-dd' format.
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # major ticks every 3 months.
    fmt_qtr_year = mdates.MonthLocator(interval=3)
    ax2.xaxis.set_major_locator(fmt_qtr_year)

    # minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax2.xaxis.set_minor_locator(fmt_month)

    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()

    # changing the fontsize of ticks
    ax1.tick_params(labelsize=chart_data['lsize'])
    ax2.tick_params(labelsize=chart_data['lsize'])

    # format the legends
    ax1.legend(loc=0, fontsize=chart_data['fsize'])
    ax2.legend(loc=0, fontsize=chart_data['fsize'])

    # display the plot
    plt.show()
