# IMPORTING LIBRARIES
import requests
import pandas as pd
import logging

logging.basicConfig(filename='logging_statements.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')

# Requesting crypto API to fetch information
URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1" \
      "&sparkline=false&price_change_percentage=1h,24h "
PATH = 'C:/Users/HP/PycharmProjects/pandas_study/week1/'
CSV_FILE = 'crypto_csv.csv'
PATH_WITH_CSV_FILE = PATH + CSV_FILE
userdata = []

try:
    # Requesting crypto API to fetch information
    my_req = requests.get(url=URL)
    logging.debug(my_req)
    var = my_req.json()
    # for every item in json data appending to an empty list
    for item in var:
        userdata.append(item)
    df = pd.DataFrame(userdata)  # Converting the list into pandas dataframe
    # Creating CSV from dataframe
    df.to_csv(CSV_FILE, index=False)
    logging.debug('CSV File has been Generated : Path - {}'.format(PATH_WITH_CSV_FILE))

except requests.exceptions.HTTPError as e:
    logging.error(e)
    print(" Exception occurred", e)
except requests.exceptions.ConnectionError as e:
    logging.error(e)
except Exception as e:
    logging.error(msg='Some other errors: {}'.format(e))
