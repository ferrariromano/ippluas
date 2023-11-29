import unittest
import os
from unittest.mock import patch
from io import StringIO

from fixproject import *

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.data = []
        self.barang = []
        self.total = 0
    
    def tearDown(self):
        os.remove("data.json")

    @patch('builtins.input', side_effect=["item1", 5, 1000])
    def test_restock_barang(self, mock_input):
        restock_barang()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["Nama Barang"], "item1")
        self.assertEqual(data[0]["Jumlah Barang"], 5)
        self.assertEqual(data[0]["Harga Barang"], 1000)

    @patch('builtins.input', side_effect=["item1", 5, 1000])
    def test_hapus_barang(self, mock_input):
        data.append({"Nama Barang": "item1", "Jumlah Barang": 5, "Harga Barang": 1000})
        hapus_barang()
        self.assertEqual(len(data), 0)

    def test_edit_data_nama_barang(self):
        data.append({"Nama Barang": "item1", "Jumlah Barang": 5, "Harga Barang": 1000})
        
        with patch('builtins.input', side_effect=[1, "new_item", "y"]):
            edit_data()
        
        self.assertEqual(data[0]["Nama Barang"], "new_item")

    def test_edit_data_tambah_jumlah_barang(self):
        data.append({"Nama Barang": "item1", "Jumlah Barang": 5, "Harga Barang": 1000})

        with patch('builtins.input', side_effect=[1, 5, "y"]):
            edit_data()

        self.assertEqual(data[0]["Jumlah Barang"], 10)

    def test_edit_data_ubah_harga_barang(self):
        data.append({"Nama Barang": "item1", "Jumlah Barang": 5, "Harga Barang": 1000})

        with patch('builtins.input', side_effect=[1, 2000, "y"]):
            edit_data()

        self.assertEqual(data[0]["Harga Barang"], 2000)

    def test_show_admin(self):
        expected_output = "KERANJANG BARANG\n"
        expected_output += "----------------------------------------------------------------\n"
        expected_output += "| No  | Nama             | Jumlah Barang    | Harga/pcs          |\n"
        expected_output += "----------------------------------------------------------------\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            show_admin()
            self.assertEqual(fake_out.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()