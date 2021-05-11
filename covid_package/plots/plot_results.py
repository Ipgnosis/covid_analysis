# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt

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
