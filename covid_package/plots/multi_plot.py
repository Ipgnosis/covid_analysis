import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import datetime


# get the plot for two countries
def multi_plots(label_dict, data_dict):

    # declare the plot colors
    mean_color = 'saddlebrown'
    stdev_color = 'yellow'
    line_color = ['blue', 'green', 'grey', 'orange', 'red', 'purple', 'black']

    # create the labels
    chart_title_str = "{} data for:".format(label_dict['expl_str'])
    # chart_title_string is enhanced below
    yw1_axis_legend_str = yw2_axis_legend_str = "Global mean"
    yw1_stdev_legend_str = yw2_stdev_legend_str = "Global std dev"

    # define empty canvas
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(label_dict['width'], label_dict['height']))
    fig.subplots_adjust(hspace=0.5)

    # declare the axis data
    # subplot 1
    ax1.set_title(label_dict['descr_str_1'], fontsize=label_dict['fsize'])
    ax1.plot(data_dict['x_axis'], data_dict['yw1_axis'], label=yw1_axis_legend_str, color=mean_color)
    ax1.grid()
    ax1.fill_between(data_dict['x_axis'], data_dict['yw1_upper'], data_dict['yw1_lower'], label=yw1_stdev_legend_str, color=stdev_color, alpha=0.5)

    # subplot 2
    ax2.set_title(label_dict['descr_str_2'], fontsize=label_dict['fsize'])
    ax2.plot(data_dict['x_axis'], data_dict['yw2_axis'], label=yw2_axis_legend_str, color=mean_color)
    ax2.grid()
    ax2.fill_between(data_dict['x_axis'], data_dict['yw2_upper'], data_dict['yw2_lower'], label=yw2_stdev_legend_str, color=stdev_color, alpha=0.5)

    # for each plot, create a plot line for each country
    for idx, iso in enumerate(label_dict['y_isos']):
        chart_title_str += iso + " "
        ax1.plot(data_dict['x_axis'], data_dict['country_val1'][iso], label=label_dict['y_axis_labels'][idx], color=line_color[idx])
        ax2.plot(data_dict['x_axis'], data_dict['country_val2'][iso], label=label_dict['y_axis_labels'][idx], color=line_color[idx])

    # ax2.set_xlabel(x_axis_label_str, fontsize=10)

    # declare the text data
    fig.suptitle(chart_title_str, fontsize=label_dict['tsize'])

    # format the x axis (date) labels
    # text in the x axis will be displayed in 'YYYY-mm-dd' format.
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # major ticks every 3 months.
    fmt_qtr_year = mdates.MonthLocator(interval=3)
    ax1.xaxis.set_major_locator(fmt_qtr_year)
    ax2.xaxis.set_major_locator(fmt_qtr_year)

    # minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax1.xaxis.set_minor_locator(fmt_month)
    ax2.xaxis.set_minor_locator(fmt_month)

    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()

    # changing the fontsize of ticks
    ax1.tick_params(labelsize=label_dict['lsize'])
    ax2.tick_params(labelsize=label_dict['lsize'])

    # format the legends
    ax1.legend(loc=0, fontsize=label_dict['fsize'])
    ax2.legend(loc=0, fontsize=label_dict['fsize'])

    # display the plot
    plt.show()
