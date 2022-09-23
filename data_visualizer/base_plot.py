import numpy as np
from numpy import arange
import matplotlib.pyplot as plt
from model import mongo_client
from scipy.optimize import curve_fit


def objective(x, a, b, c):
    return a * x + b * x ** 2 + c


def objective_5d(x, a, b, c, d, e, f):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f


def plot_regression(ax, reg_x, reg_y, base_x):
    values = np.polyfit(reg_x, reg_y, 1)
    trend = np.poly1d(values)
    ax.plot(base_x, trend(base_x), label='Regression')


def plot_2d_poly_regression(ax, reg_x, reg_y, base_x):
    popt, _ = curve_fit(objective, reg_x, reg_y)
    a, b, c = popt
    x_line = arange(min(base_x), max(base_x), 0.01)
    y_line = objective(x_line, a, b, c)
    ax.plot(x_line, y_line, '--', color='red', label='2nd Degree Poly')


def plot_5d_poly_regression(ax, reg_x, reg_y, base_x):
    popt, _ = curve_fit(objective_5d, reg_x, reg_y)
    a, b, c, d, e, f = popt
    x_line = arange(min(base_x), max(base_x), 0.01)
    y_line = objective_5d(x_line, a, b, c, d, e, f)
    ax.plot(x_line, y_line, '--', color='orange', label='5th Degree Poly')


def label_plot(ax):
    ax.set_xlabel('score')
    ax.set_ylabel('won match (percentage)')
    ax.legend(loc='best')


def annotate_plot(x, y):
    plotted_xs = []
    plotted_ys = []
    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    min_y = min(y)
    for x, y in zip(x, y):
        label = f"({round(x, 1)},{int(y)}%)"

        step_x = (max_x - min_x) / 20
        step_y = (max_y - min_y) / 20

        skip = False
        for x_item in plotted_xs:
            if abs(x - x_item) < step_x:
                for y_item in plotted_ys:
                    if abs(y - y_item) < step_y:
                        skip = True
                        break
                if skip:
                    break

        if skip:
            continue

        plotted_xs.append(x)
        plotted_ys.append(y)

        plt.annotate(label,  # this is the text
                     (x, y),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center


def plot_poly(item_name):
    client = mongo_client.MongoClient()
    deep_analysis_doc = client.get_deep_analysis_document()

    deep_analysis = deep_analysis_doc.find_one({})

    x = []
    y = []
    area = []

    regression_x = []
    regression_y = []

    count = 0
    for key in deep_analysis[item_name]:
        count += 1
        x.append(float(key))
        y.append(float(deep_analysis[item_name][key]["percentage"]))
        area.append(float(deep_analysis[item_name][key]["total"]))

        # account for duplicates for regression line data
        for num in range(deep_analysis[item_name][key]["total"]):
            regression_x.append(float(key))
            regression_y.append(float(deep_analysis[item_name][key]["percentage"]))

    colors = np.random.rand(count)

    fig, ax = plt.subplots()
    ax.scatter(x, y, s=area, c=colors, alpha=0.5, label=item_name)

    plot_regression(ax, regression_x, regression_y, x)
    plot_2d_poly_regression(ax, regression_x, regression_y, x)
    plot_5d_poly_regression(ax, regression_x, regression_y, x)

    label_plot(ax)
    annotate_plot(x, y)

    plt.show()
