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

    count = 0
    for key in deep_analysis[item_name]:
        count += 1
        x.append(int(key))
        y.append(int(deep_analysis[item_name][key]["percentage"]))
        area.append(int(deep_analysis[item_name][key]["total"]))

    colors = np.random.rand(count)

    fig, ax = plt.subplots()

    ax.scatter(x, y, s=area, c=colors, alpha=0.5, label='Data')

    y_mean = [np.mean(y)] * len(x)
    ax.plot(x, y_mean, label='Mean', linestyle='--')

    values = np.polyfit(x, y, 1)
    trendpoly = np.poly1d(values)
    ax.plot(x, trendpoly(x), label='Regression')

    ax.set_xlabel('score')
    ax.set_ylabel('predictions correct (percentage)')
    ax.legend(loc='upper right')

    plt.show()
