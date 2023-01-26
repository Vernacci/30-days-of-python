from matplotlib import pyplot

x_data = [1, 2, 4, 5, 6]
y_data = [5.5, 6.4, 5.3, 4.4, 7.9]

pyplot.scatter(x_data, y_data)
pyplot.savefig('graph.png')
