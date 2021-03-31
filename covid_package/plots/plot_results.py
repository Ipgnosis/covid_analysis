# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt

# simple matplotlib graph of the results


def subplot_share_axis(labels, results):

    #x_label = "Cross wins; mode: {}".format(x_mode)
    #o_label = "Nought wins; mode: {}".format(o_mode)

    ax1 = plt.subplot(211)
    plt.plot(results['x_axis'], results['y1_axis'])
    plt.legend(handles=labels['legend_1'])
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(212, sharex=ax1)
    plt.plot(results['x_axis'], results['y2_axis'])
    plt.legend(handles=labels['legend_2'])
    plt.setp(ax2.get_xticklabels(), fontsize=6)

    plt.title(labels['chart_title'])
    plt.xlabel(labels['x_axis_label'])
    plt.ylabel(labels['y_axis_label'])

    plt.legend()

    plt.show()
