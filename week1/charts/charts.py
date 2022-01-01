""" script shows us the different graphs for current_price column of the crypto api.
     to visualize the data using matplotlib library"""

# importing different libraries
import pandas as pd
import matplotlib.pyplot as plt
import logging

logging.basicConfig(filename='logging_stat.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')

PATH = 'C:/Users/HP/PycharmProjects/pandas_study/week1/'
CSV_FILE = 'cypto_csv.csv'

try:
    # reading Crypto Csv File to dataframe
    df = pd.read_csv(PATH + CSV_FILE)

    # sorting the values in ascending order
    df_sort = df.sort_values('current_price')

    # create histogram for numeric data
    df['current_price'][:100].hist()
    plt.xlabel("Current Price")
    plt.ylabel("Frequency")
    plt.title('Histogram for Crypto Prices ')
    plt.show()
    logging.info("program is running smooth, Histogram is loaded")

    # create pie chart for IDs & crypto Prices
    data = df_sort['current_price'][:10]
    plt.pie(data, labels=df_sort['id'][:10], autopct='%1.0f%%')
    plt.title("Pie chart for crypto prices")
    plt.legend(loc='best')
    plt.show()

    # scatter plot between id and crypto prices
    plt.scatter(df_sort['id'][:10], df_sort['current_price'][:10])
    plt.xlabel("Crypto IDs")
    plt.ylabel("Current Price")
    plt.title('scatter plot for Crypto Prices ')
    plt.xticks(rotation=70)
    plt.show()

    # creating Bar chart
    plt.bar(df_sort['id'][:10], df_sort['current_price'][:10])
    plt.xlabel("Crypto IDs")
    plt.ylabel("Current Price")
    plt.title(' Bar Graph for Crypto Prices ')
    plt.xticks(rotation=70)
    plt.legend(loc='upper right')
    plt.show()

    # creating box plot
    lst1 = df_sort['current_price'][:10]
    lst2 = df_sort['current_price'][10:20]
    list_1 = [lst1, lst2]
    plt.boxplot(list_1)
    plt.xlabel('Current Price')
    plt.title(' Box plot for Crypto Prices ')
    plt.show()

    # creating line chart
    line1 = df_sort[:10].plot.line(x='id', y='current_price', label="Crypto Prices")
    plt.title("line chart for Crypto Prices")
    plt.ylabel('Current Price')
    plt.xlabel('Relevant Ids')
    plt.show()


except FileNotFoundError as e:
    logging.error(e)
    print(" Exception occurred", e)

except Exception as e:
    logging.error(msg='Some other errors: {}'.format(e))
