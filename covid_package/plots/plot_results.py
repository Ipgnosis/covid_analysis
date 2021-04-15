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
    plt.scatter(these_results['x_axis'], these_results['y_axis'], s = these_params['area'], c = these_params['colors'], alpha = these_params['alpha'])

    # set up the labels
    plt.xlabel(these_labels['x_label'])
    plt.ylabel(these_labels['y_label'])
    plt.title(these_labels['title'])

    # display the plot
    #plt.legend()
    plt.show()
