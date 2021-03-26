# plot the results of a multi-game run
# written by Russell on 5/4/20
# modified on 6/28 to integrate agent modes into legend

import matplotlib.pyplot as plt

# simple matplotlib graph of the results


def results_plot(plot_title, x_label, y_label, x_mode, o_mode, results):

    agentX_x_axis = results[0]
    agentX_y_axis = results[1]

    agentO_x_axis = results[2]
    agentO_y_axis = results[3]

    draw_x_axis = results[4]
    draw_y_axis = results[5]

    #x_label = "Cross wins; mode: {}".format(x_mode)
    #o_label = "Nought wins; mode: {}".format(o_mode)

    plt.subplot(1, 1, 1)
    plt.plot(agentX_x_axis, agentX_y_axis, label=x_label)
    plt.plot(agentO_x_axis, agentO_y_axis, label=y_label)

    plt.plot(draw_x_axis, draw_y_axis, label='Drawn games')

    plt.title(plot_title)
    plt.xlabel("Games")
    plt.ylabel("Score")
    plt.legend()

    plt.show()
