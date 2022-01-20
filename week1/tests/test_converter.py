import unittest
from unittest.mock import patch
import logging
import json
import os
import pandas as pd

from week1.oops.converter_crypto_oops import Converter

logging.basicConfig(filename='test_logging.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


class TestConvertCSV(unittest.TestCase):
    """Test class that have different test_methods to check for the different formats"""

    def setUp(self):
        self.api_url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&" \
                       + "order=market_cap_desc&per_page=100&page=1&sparkline=false&price_" \
                       + "change_percentage=1h%2C24h"
        try:
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                   '../truth_folder/crynew.json'), encoding='utf-8') as file_name:
                self.json_data = json.load(file_name)
        except FileNotFoundError as file_err:
            logging.exception("Check the file path %s", file_err)

        self.sample = Converter(self.api_url, "crypto data")
        self.d_frame = self.generate_dataframe()

    def generate_dataframe(self):
        """generates the dataframe from the mocked json response"""
        with patch('week1.oops.converter_crypto_oops.requests.get') as mock_get:
            mock_get.return_value.json.return_value = self.json_data
            data_frame = self.sample.create_df()
        return data_frame

    def test_csv_generate_from_df(self):
        """generates csv file from mocked dataframe and checks to the path for its presence"""
        self.sample.to_csv('test_csv.csv')
        self.assertTrue('test_csv.csv')

    def test_compare_generated_csv_with_truth(self):
        """compares csv file generated after test to the actual csv file"""
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               '../truth_folder/cry.csv'), encoding='utf-8') as csv_file:
            original_csv = csv_file.read()
        with open('test_csv.csv') as generated_file:
            generated_csv_file = generated_file.read()
        self.assertEqual(original_csv, generated_csv_file)

    def test_excel_generate_from_df(self):
        """generates excel file from mocked dataframe and checks to the path for its presence"""
        self.sample.to_excel('test_excel.xlsx')
        self.assertTrue(os.path.isfile(os.path.join('test_excel.xlsx')))

    def test_compare_generated_excel_with_truth(self):
        """compares excel file generated after test to the actual excel file"""
        original_excel_df = pd.read_excel(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                       '../truth_folder/cry.xlsx'))
        generated_excel_df = pd.read_excel(os.path.join('test_excel.xlsx'))

        generated_excel_df.compare(original_excel_df)

    def test_xml_generate_from_df(self):
        """generates xml file from mocked dataframe and checks to the path for its presence"""
        self.sample.to_xml('test_xml.xml')
        self.assertTrue(os.path.isfile(os.path.join('test_xml.xml')))

    def test_compare_generated_xml_with_truth(self):
        """compares xml file generated after test to the actual xml file"""
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               '../truth_folder/Cry.xml'), encoding='utf-8') as xml_file:
            original_xml = xml_file.read()
        with open('test_xml.xml') as generated_file:
            generated_xml_file = generated_file.read()
        self.assertEqual(original_xml, generated_xml_file)

    def test_html_generate_from_df(self):
        """generates html file from mocked dataframe and checks to the path for its presence"""
        self.sample.to_html('test_html.html')
        self.assertTrue(os.path.isfile(os.path.join('test_html.html')))

    def test_compare_generated_html_with_truth(self):
        """compares html file generated after test to the actual html file"""
        with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               '../truth_folder/cry.html'), encoding='utf-8') as html_file:
            original_html = html_file.read()
        with open('test_html.html') as generated_file:
            generated_html_file = generated_file.read()
        self.assertEqual(original_html, generated_html_file)

    def test_pdf_generate_from_df(self):
        """generates pdf file from passed html file generated from test and
            checks to the path for its presence"""
        self.sample.html_to_pdf('test_html.html', 'test_pdf.pdf')
        self.assertTrue('test_pdf.pdf')
