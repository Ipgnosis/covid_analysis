# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def scatter_plot(these_labels, these_results, these_params):

    # define the chart and data
    this_data = plt.scatter(
        these_results['x_axis'], # the x axis values
        these_results['y_axis'], # the y axis values
        s = these_params['area'], # the area
        #c = these_params['colors'], # colors
        #alpha = these_params['alpha'], # transparency of plot markers
        label = these_results['legend_label']
    )

    # set up the labels
    plt.xlabel(these_labels['x_label'])
    plt.ylabel(these_labels['y_label'])
    plt.title(these_labels['title'])

    # set up the axes
    plt.ylim(these_params['y_lim'])

    # display the plot
    plt.legend(handles = [this_data])
    plt.show()


# double matplotlib graph of the results
def subplot_share_axis(these_labels, these_results, these_params):

    # empty canvas
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.5)

    # declare the axis data
    # subplot 1
    ax1.plot(these_results['x_axis'], these_results['yw1_axis'], label = (these_labels['legend_1a']))
    ax1.plot(these_results['x_axis'], these_results['y1_axis'], label = (these_labels['legend_1b']))

    # subplot 2
    ax2.plot(these_results['x_axis'], these_results['yw2_axis'], label = (these_labels['legend_2a']))
    ax2.plot(these_results['x_axis'], these_results['y2_axis'], label = (these_labels['legend_2b']))
    ax2.set_xlabel(these_labels['x_axis_label'], fontsize=10)

    # declare the text data
    fig.suptitle(these_labels['chart_title'], fontsize=10)

    #  format the x axis (date) labels

    # Text in the x axis will be displayed in 'YYYY-mm-dd' format.
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
    ax1.tick_params(labelsize=5)
    ax2.tick_params(labelsize=5)

    # format the legends
    ax1.legend(loc = 0, fontsize=7)
    ax2.legend(loc = 0, fontsize=7)

    # display the plot
    plt.show()
