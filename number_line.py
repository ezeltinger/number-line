import os
import matplotlib.pyplot as plt
from datetime import datetime


def number_line(format="png", filename=datetime.now().strftime("num_line_%d-%m-%Y_%H-%M-%S")):
    fig, ax = plt.subplots()
    # Set size of plot, make bigger than numbers you intend to show
    ax.set_xlim(-7, 7)
    # Set ticks on number line
    tick_positions = range(-5, 6, 1)

    # Remove y-axis
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    # Make arrows on number line
    ax.arrow(-6, 0, 12, 0, head_width=0.5, head_length=1, fc='k', ec='k')
    ax.arrow(6, 0, -12, 0, head_width=0.5, head_length=1, fc='k', ec='k')

    # Remove unnecessary spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax.set_xticklabels([])  # Remove the tick labels
    ax.tick_params(
        axis='x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom=False,      # ticks along the bottom edge are off
        top=False,         # ticks along the top edge are off
        labelbottom=False) # labels along the bottom edge are off

    # Draw tick lines manually so that they are centered on the x-axis
    for tick_position in tick_positions:
        ax.axvline(x=tick_position, color='black', linewidth=1)
        ax.text(tick_position, -1.2, str(tick_position), ha='center', va='bottom')

    if not os.path.exists("images"):
        os.mkdir("images")
    plt.savefig(f"images/{filename}.{format}", bbox_inches='tight', dpi=200)
    plt.show()


if __name__ == "__main__":
    number_line()
