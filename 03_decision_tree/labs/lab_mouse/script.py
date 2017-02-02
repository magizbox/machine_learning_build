import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.widgets import RadioButtons, Button

points = []
LIMIT = 10
# data point size
SIZE = 100
# data point marker
# either: o, v, ^, <, >, 8, s, p, *, h, H, D, d
# visit https://goo.gl/VI2CyP to see how marker works
MARKER = 'x'

fig, ax = plt.subplots()
ax.set_title("Dataset Generator")
plt.subplots_adjust(bottom=0.2, left=0.18)
plot = ax.scatter([], [])
select_color_ax = plt.axes([0.01, 0.4, 0.1, 0.15])
select_color_widget = RadioButtons(select_color_ax, ('Blue', 'Red'), active=0, activecolor='black')
save_ax = plt.axes([0.8, 0.05, 0.1, 0.075])
save_widget = Button(save_ax, 'Save')

undo_ax = plt.axes([0.18, 0.05, 0.1, 0.075])
undo_widget = Button(undo_ax, 'Undo')

ax.set_xlim(-LIMIT, LIMIT)
ax.set_ylim(-LIMIT, LIMIT)


def undo(event):
    global points
    ax.clear()
    ax.set_title("Dataset Generator")
    ax.set_xlim(-LIMIT, LIMIT)
    ax.set_ylim(-LIMIT, LIMIT)
    points = points[:-1]
    x1 = [point.x1 for point in points]
    x2 = [point.x2 for point in points]
    color = [point.label for point in points]
    ax.scatter(x1, x2, color=color, s=SIZE, marker=MARKER)
    return True


def save_data(event):
    global points
    data = [point.__dict__ for point in points]
    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)
    print "Save %s points" % len(points)


class Point:
    def __init__(self, x1, x2, label):
        self.x1 = x1
        self.x2 = x2
        self.label = label

    def __str__(self):
        return "(%s, %s, %s)" % (self.x1, self.x2, self.label)


def add_point(event):
    global points
    x1, x2 = event.xdata, event.ydata
    if event.inaxes in [select_color_ax, save_ax, undo_ax]:
        return
    if not (x1 and x2):
        return
    current_color = select_color_widget.value_selected
    point = Point(x1, x2, label=current_color)
    points.append(point)
    # add the points to the plot
    ax.scatter(point.x1, point.x2, color=current_color, s=SIZE, marker=MARKER)
    fig.canvas.draw()


fig.canvas.callbacks.connect('button_press_event', add_point)
undo_widget.on_clicked(undo)
save_widget.on_clicked(save_data)
plt.show()
