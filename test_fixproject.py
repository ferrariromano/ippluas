import unittest
from unittest.mock import patch
from fixproject import InventoryManagement

class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.inventory = InventoryManagement()
        self.inventory.data = [{'Nama Barang': 'BarangTest', 'Jumlah Barang': 10, 'Harga Barang': 5000}]


    @patch('builtins.input', side_effect=['BarangTest', '10', '5000'])
    def test_restock_barang(self, mock_input):
        self.inventory.restock_barang()
        self.assertIn({'Nama Barang': 'BarangTest', 'Jumlah Barang': 10, 'Harga Barang': 5000}, self.inventory.data)

    @patch('builtins.input', side_effect=['1'])
    def test_hapus_barang(self, mock_input):
        self.inventory.data = [{'Nama Barang': 'BarangTest', 'Jumlah Barang': 10, 'Harga Barang': 5000}]
        self.inventory.hapus_barang()
        self.assertEqual(len(self.inventory.data), 0)

    @patch('builtins.input', side_effect=['1', '1', 'BarangEdit', 'y', '5'])
    def test_edit_data(self, mock_input):
        self.inventory.data = [{'Nama Barang': 'BarangTest', 'Jumlah Barang': 10, 'Harga Barang': 5000}]
        self.inventory.edit_data()
        self.assertEqual(self.inventory.data[0]['Nama Barang'], 'BarangEdit')

    @patch('builtins.input', side_effect=['BarangTest', '1'])
    def test_pembeli_beli(self, mock_input):
        self.inventory.data = [{'Nama Barang': 'BarangTest', 'Jumlah Barang': 10, 'Harga Barang': 5000}]
        initial_stock = self.inventory.data[0]['Jumlah Barang']
        self.inventory.menu_pembeli()
        final_stock = self.inventory.data[0]['Jumlah Barang']
        self.assertEqual(initial_stock - 1, final_stock)  # Pastikan jumlah barang berkurang sebanyak yang dibeli

    @patch('builtins.input', side_effect=['5000'])
    def test_pembeli_transaksi(self, mock_input):
        self.inventory.total = 5000
        self.inventory.menu_pembeli()
        # Menambahkan assert untuk memeriksa output transaksi

# Menjalankan test
if __name__ == '__main__':
    unittest.main()