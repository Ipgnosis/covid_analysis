# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# double matplotlib graph of the results
def subplot_share_axis(these_labels, these_results):

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.5)

    ax1.plot(these_results['x_axis'], these_results['y1_axis'])
    ax1.set_xlabel(these_labels['x_axis_label'])
    ax1.set_ylabel(these_labels['y1_axis_label'])

    ax2.plot(these_results['x_axis'], these_results['y2_axis'])
    ax2.set_ylabel(these_labels['y2_axis_label'])

    fig.set_title(these_labels['chart_title'])

    # display the plot
    plt.legend()
    plt.show()


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


def line_plot(these_labels, these_results, these_params):

    # empty canvas
    fig = plt.figure()

    # add axes
    #ax = fig.add_axes(these_params['axis_settings'])
    ax = fig.add_axes([0, 0, 1, 1])

    # plot 2 lines with common x axis
    ax.plot(these_results['x_axis'], these_results['y_axis'], 'b-')
    ax.plot(these_results['x_axis'], these_results['y1_axis'], 'r-')

    # Text in the x axis will be displayed in 'YYYY-mm-dd' format.
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # major ticks every 3 months.
    fmt_qtr_year = mdates.MonthLocator(interval=3)
    ax.xaxis.set_major_locator(fmt_qtr_year)

    # minor ticks every month.
    fmt_month = mdates.MonthLocator()
    ax.xaxis.set_minor_locator(fmt_month)

    # Rotates and right aligns the x labels, and moves the bottom of the
    # axes up to make room for them.
    fig.autofmt_xdate()

    # set labels
    ax.set_title(these_labels['chart_title'])
    ax.set_xlabel(these_labels['x_axis_label'])
    ax.set_ylabel(these_labels['y_axis_label'])
    ax.legend(labels = (these_labels['legend_1'], these_labels['legend_2']), loc = 0)

    plt.show()
