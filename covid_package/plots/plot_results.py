# plot the results
# written by Russell on 3/30/21

import matplotlib.pyplot as plt

# simple matplotlib graph of the results


def subplot_share_axis(labels, results):

    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
    fig.subplots_adjust(hspace=0.5)

    ax1.plot(results['x_axis'], results['y1_axis'])
    ax1.set_xlabel(labels['x_axis_label'])
    ax1.set_ylabel(labels['y1_axis_label'])

    ax2.plot(results['x_axis'], results['y2_axis'])
    ax2.set_ylabel(labels['y2_axis_label'])

    fig.set_title(labels['chart_title'])
    plt.legend()
    plt.show()
