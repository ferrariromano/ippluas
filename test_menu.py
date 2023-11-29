import json
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

from fixproject import clear_screen, edit_data, hapus_barang, menu_penjual, restock_barang

def baca_data_json():
    try:
        with open("data.json", "r") as output:
            # Check if the file is empty or not
            if os.path.getsize("data.json") > 0:
                baca = json.load(output)
                for i in baca:
                    data.append(i)
    except FileNotFoundError:
        # Handle the case when the file doesn't exist
        print("File not found. Creating a new one.")
    except json.decoder.JSONDecodeError:
        # Handle the case when the file is empty or not in JSON format
        print("Invalid JSON format or empty file.")

class TestMenu(unittest.TestCase):
    # def setUp(self):
    #     self.data_filename = "data.json"
    #     self.data = [
    #         {
    #             "Nama Barang": "Barang 1",
    #             "Jumlah Barang": 10,
    #             "Harga Barang": 100
    #         },
    #         {
    #             "Nama Barang": "Barang 2",
    #             "Jumlah Barang": 5,
    #             "Harga Barang": 200
    #         }
    #     ]
    #     with open(self.data_filename, "w") as file:
    #         json.dump(self.data, file)

    
    
    def tearDown(self):
        os.remove(self.data_filename)

    def test_restock_barang(self):
        with patch("builtins.input", side_effect=["Barang 3", "15", "150"]):
            clear_screen()
            restock_barang()
            with open(self.data_filename, "r") as file:
                updated_data = json.load(file)
                self.assertEqual(len(updated_data), len(self.data) + 1)  # Check if a new item is added

    def test_hapus_barang(self):
        with patch("builtins.input", side_effect=["1"]):
            clear_screen()
            hapus_barang()
            with open(self.data_filename, "r") as file:
                updated_data = json.load(file)
                self.assertEqual(len(updated_data), len(self.data) - 1)  # Check if an item is removed

    def test_edit_data(self):
        with patch("builtins.input", side_effect=["1", "2", "y"]):
            clear_screen()
            edit_data()
            with open(self.data_filename, "r") as file:
                updated_data = json.load(file)
                self.assertEqual(updated_data[0]["Jumlah Barang"], 2)  # Check if the item's quantity is updated

    def test_menu_penjual(self):
        with patch("builtins.input", side_effect=["1"]):
            captured_output = StringIO()
            sys.stdout = captured_output
            menu_penjual()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue().strip()
            self.assertIn("WARMINDO DEPELE", output)  # Check if the menu is displayed

if __name__ == "__main__":
    unittest.main()