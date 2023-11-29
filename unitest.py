import unittest
import os
import json
import time

# Import functions from the main script
from fixproject import tulis_data_json, baca_data_json, restock_barang, hapus_barang, edit_data

# ... (Your existing code)

class TestWarmindoDepele(unittest.TestCase):

    def setUp(self):
        # Set up any initial conditions needed for testing
        global data
        data = []

    def tearDown(self):
        # Clean up after testing
        if os.path.exists("data.json"):
            os.remove("data.json")

    def test_tulis_data_json(self):
        # Test writing data to JSON
        test_data = [{"Nama Barang": "TestBarang", "Jumlah Barang": 10, "Harga Barang": 100}]
        tulis_data_json(test_data)
        self.assertTrue(os.path.exists("data.json"))

    def test_baca_data_json(self):
        # Test reading data from JSON
        test_data = [{"Nama Barang": "TestBarang", "Jumlah Barang": 10, "Harga Barang": 100}]
        tulis_data_json(test_data)
        baca_data_json()
        self.assertEqual(data, test_data)

    def test_restock_barang(self):
        # Test restocking a new item
        restock_barang()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Nama Barang"], "TestBarang")

    def test_hapus_barang(self):
        # Test removing an item
        restock_barang()
        hapus_barang(1)
        self.assertEqual(len(data), 0)

    def test_edit_data(self):
        # Test editing an item
        restock_barang()
        edit_data()
        self.assertEqual(data[0]["Nama Barang"], "EditedBarang")

if __name__ == "__main__":
    unittest.main()
