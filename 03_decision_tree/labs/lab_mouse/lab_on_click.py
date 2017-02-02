import matplotlib.pyplot as plt
def on_click(event):
    xmouse, ymouse = event.xdata, event.ydata
    if not (xmouse and ymouse):
        print 'Out of range'
    else:
        print 'x, y of mouse: {:.2f},{:.2f}'.format(xmouse, ymouse)

fig, ax = plt.subplots()

tolerance = 10
ax.plot(range(10), 'ro-', picker=tolerance)

fig.canvas.callbacks.connect('button_press_event', on_click)

plt.show()
