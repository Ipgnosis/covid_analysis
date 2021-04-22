# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt

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

    case_mean = ax.plot(these_results['x_axis'], these_results['y_axis'])
    iso_1 = ax.plot(these_results['x_axis'], these_results['y1_axis'])

    # set labels
    ax.set_title(these_labels['chart_title'])
    ax.set_xlabel(these_labels['x_axis_label'])
    ax.set_ylabel(these_labels['y_axis_label'])

    plt.show()
