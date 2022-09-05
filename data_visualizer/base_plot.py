import numpy as np
import matplotlib.pyplot as plt
from model import mongo_client


def plot(item_name):
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

    y_mean = [np.mean(y)] * len(x)
    ax.plot(x, y_mean, label='Mean', linestyle='--')

    values = np.polyfit(regression_x, regression_y, 1)
    trend = np.poly1d(values)
    ax.plot(x, trend(x), label='Regression')

    ax.set_xlabel('score')
    ax.set_ylabel('predictions correct (percentage)')
    ax.legend(loc='upper right')

    plt.show()
