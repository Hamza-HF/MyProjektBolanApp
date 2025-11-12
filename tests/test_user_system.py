import unittest
import sys
import os
import json
import tempfile
import shutil
from unittest.mock import patch
from io import StringIO
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.user_system import UserSystem

class TestUserSystem(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_users.json")
        self.user_system = UserSystem(self.test_file)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_registrera_ny_anvandare(self):
        with patch('builtins.input', side_effect=['hamza@test.com']), \
             patch('getpass.getpass', side_effect=['Hamza123', 'Hamza123']):
            
            self.user_system.register()
            
            self.assertIn('hamza@test.com', self.user_system.users)
            self.assertEqual(self.user_system.users['hamza@test.com'], 'Hamza123')

    def test_lyckad_inloggning(self):
        self.user_system.users['hamza@test.com'] = 'Hamza123'
        self.user_system.save_users()
        
        with patch('builtins.input', return_value='hamza@test.com'), \
             patch('getpass.getpass', return_value='Hamza123'):
            
            result = self.user_system.login()
            self.assertEqual(result, 'hamza@test.com')

    def test_misslyckad_inloggning(self):
        self.user_system.users['hamza@test.com'] = 'Hamza123'
        self.user_system.save_users()
        
        with patch('builtins.input', return_value='hamza@test.com'), \
             patch('getpass.getpass', return_value='fel_losenord'), \
             patch('builtins.print') as mock_print:
            
            result = self.user_system.login()
            self.assertIsNone(result)

    def test_andera_losenord(self):
        self.user_system.users['hamza@test.com'] = 'gammalt_losenord'
        
        with patch('builtins.input', return_value='hamza@test.com'), \
             patch('getpass.getpass', side_effect=['gammalt_losenord', 'nytt_losenord', 'nytt_losenord']):
            
            self.user_system.change_password()
            
            self.assertEqual(self.user_system.users['hamza@test.com'], 'nytt_losenord')

    def test_ogiltig_email(self):
        with patch('builtins.input', return_value='ogiltig_email'), \
             patch('builtins.print') as mock_print:
            
            self.user_system.users = {} 
            
            with self.assertRaises(StopIteration):
                with patch('builtins.input', side_effect=['ogiltig_email'] * 10):
                    self.user_system.register()

    def test_ladda_anvandare_fran_fil(self):
        test_users = {
            "alex1@test.com": "Alex11",
            "anka2@test.com": "Anka22"
        }
        
        with open(self.test_file, 'w', encoding='utf-8') as f:
            json.dump(test_users, f)
        
        user_system = UserSystem(self.test_file)
        self.assertEqual(len(user_system.users), 2)
        self.assertIn('alex1@example.com', user_system.users)

if __name__ == '__main__':
    unittest.main()