""" The script fetches crypto API information and creates CSV,Excel, XML and HTML document
    with the response received from the server
    Author - Priyanka Sirohiya
"""
import json
import requests
import pandas as pd
import pdfkit
import logging

logging.basicConfig(filename='logging_stat.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='w')


def json_to_csv(json_data, file_name):
    """
    Creates CSV with the json object received
    :param json_data: JSON Object
    :param file_name: CSV file has to be created
    :return: dataframe containing normalized CSV data
    """
    try:
        df = pd.json_normalize(json_data)
        df.to_csv(file_name, index=False)
        logging.info('CSV File has been Generated : FILENAME - {}'.format(file_name))
        return df
    except KeyError as ke:
        logging.error('Key error has generated {}'.format(ke))


def to_excel(csv_df, file_name):
    """
    Creates excel with the json object received
    :param csv_df: dataframe containing CSV data
    :param file_name: Excel file to be created
    :return: Null
    """
    try:
        ew = pd.ExcelWriter(file_name)
        csv_df.to_excel(ew, index=False)
        ew.save()
        logging.info('Excel file has been generated : Filename - {}'.format(file_name))
    except ValueError as ve:
        logging.error('Got value Error while trying to write Excel File {}'.format(ve))
    except PermissionError as pe:
        logging.error('Got Permission Error while trying to write Excel File {}'.format(pe))


def to_html(csv_df, file_name):
    """
    Creates html with the json object received
    :param csv_df: dataframe containing CSV data
    :param file_name: HTML file to be created
    :return: Null
    """
    try:
        csv_df.to_html(file_name, escape=False)
        logging.info('HTML is generated from CSV : Filename - {}'.format(file_name))
    except ValueError as ve:
        logging.error('Got value Error while trying to write HTML File {}'.format(ve))
    except PermissionError as pe:
        logging.error('Got Permission Error while trying to write HTML File {}'.format(pe))


def to_xml(csv_df, file_name):
    """
    Creates XML with the json object received
    :param csv_df: dataframe containing CSV data
    :param file_name: XML file to be created
    :return: Null
    """
    try:
        csv_df.to_xml(file_name)
        logging.info('XML file has been generated : Filename - {}'.format(file_name))
    except ValueError as ve:
        logging.error('Got value Error while trying to write XML File {}'.format(ve))
    except PermissionError as pe:
        logging.error('Got Permission Error while trying to write XML File {}'.format(pe))


def html_to_pdf(html_file_name, pdf_file_name):
    """
    creates pdf with the html file while using pdfkit library
    :param html_file_name: html file from which pdf has to be created
    :param pdf_file_name: pdf file to be created
    :return: NULL
    """
    try:
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        options = {'page-height': '2500', 'page-width': '1270', 'encoding': "UTF-8"}
        # CONVERT HTML FILE TO PDF WITH PDFKIT
        pdfkit.from_file(html_file_name, pdf_file_name, configuration=config,
                         options=options)
        logging.info('pdf file has been generated : Filename - {}'.format(pdf_file_name))
    except FileNotFoundError as f:
        logging.error('pdf file not found {}'.format(f))
        logging.exception(f)
    except ValueError as ve:
        logging.error('Got value Error while trying to write pdf File {}'.format(ve))
    except PermissionError as pe:
        logging.error('Got Permission Error while trying to write pdf File {}'.format(pe))


def convert_files():
    """
    fetching crypto API data.
    calling all the conversion functions with the received json response
    :return: null
    """

    try:
        # Fetching data from API
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&" \
              + "order=market_cap_desc&per_page=100&page=1" \
              + "&sparkline=false&price_change_percentage=1h,24h" \
            # PATH = 'C:/Users/HP/PycharmProjects/pandas_study/week1/'
        csv_file = 'crypto.csv'
        response = requests.get(url)
        logging.info(response)
        csv_dataframe = json_to_csv(response.json(), csv_file)
        logging.debug('csv DF used for generating different formats : {}'.format(csv_dataframe))


    except requests.exceptions.HTTPError as e:
        logging.error('HTTP ERROR found : {}'.format(e))
    except json.JSONDecodeError as e:
        logging.error('Error occurred while decoding json : {}'.format(e))
    else:
        logging.info('Crypto.csv is available')

    # Generating Excel file
    excel_file_name = 'Crypto.xlsx'
    to_excel(csv_dataframe, excel_file_name)

    # Generating HTML file
    html_file_name = 'Crypto.html'
    to_html(csv_dataframe, html_file_name)

    # Generating XML File
    xml_file_name = 'Crypto.xml'
    to_xml(csv_dataframe, xml_file_name)

    # Generating PDF File from HTML
    pdf_file_name = 'Crypto.pdf'
    html_to_pdf(html_file_name, pdf_file_name)


if __name__ == '__main__':
    convert_files()
