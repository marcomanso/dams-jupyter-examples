import time
import common


import matplotlib.pyplot as plt


def test_run(operation, endpoint, token, data):
    time_start = time.time()
    if operation == "DELETE":
        (result, data) = common.delete_data(endpoint, token, data)
    elif operation == "PUT":
        (result, data) = common.put_data(endpoint, token, data)
    elif operation == "POST":
        (result, data) = common.post_data(endpoint, token, data)
    else: # assumes GET
        (result, data) = common.get_data(endpoint, token, data)
    time_end = time.time()
    return (result, operation, endpoint, time_start, time_end, data)


def pretty_show_test(result, show_data = None):
    if show_data == True:
        print(f"{result[0]} \t {result[1]} \t {result[2]} \t {(result[4]-result[3])*1000}ms \t {result[5]}")
    else:
        print(f"{result[0]} \t {result[1]} \t {result[2]} \t {(result[4]-result[3])*1000}ms")



def chart_nested_stats(title, data_stats):
    #
    if data_stats and "count" in data_stats["value"]:
        x_values=list(data_stats["value"]["count"].keys())
        count_values=list(data_stats["value"]["count"].values())
        plt.subplot(1,2,1)
        plt.plot(x_values, count_values)
        plt.title(title+" COUNT")
        plt.xticks(rotation=70)
        plt.tight_layout()
        plt.show()
    #    
    if data_stats and "avg" in data_stats["value"]:    
        x_values=list(data_stats["value"]["avg"].keys())
        avg_values=list(data_stats["value"]["avg"].values())
        max_values=list(data_stats["value"]["max"].values())
        min_values=list(data_stats["value"]["min"].values())
        plt.subplot(1,2,2)
        plt.plot(x_values, avg_values)
        plt.plot(x_values, min_values)
        plt.plot(x_values, max_values)
        plt.title(title+" STATS")
        plt.xticks(rotation=70)

    plt.tight_layout()
    plt.show()


