# test_hangman.py

import unittest
from unittest.mock import patch, mock_open
from hangmangame import (
    get_random_word, draw_hangman, is_valid_input, is_already_guessed, handle_correct_guess, handle_wrong_guess,
    update_display, win_game, lose_game
)

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.mock_file_content = "hangman\npython\nprogramming\n"

    def test_get_random_word(self):
        # Mock open function to simulate file reading
        with patch('builtins.open', mock_open(read_data=self.mock_file_content)):
            word = get_random_word()
            self.assertIn(word, ['hangman', 'python', 'programming'])

    def test_draw_hangman(self):
        with patch('builtins.print') as mocked_print:
            draw_hangman(7)
            mocked_print.assert_any_call("_________     ")
            draw_hangman(6)
            mocked_print.assert_any_call("_________     ")
            draw_hangman(5)
            mocked_print.assert_any_call("________      ")
            draw_hangman(4)
            mocked_print.assert_any_call("________  ")
            draw_hangman(3)
            mocked_print.assert_any_call("________      ")
            draw_hangman(2)
            mocked_print.assert_any_call("________      ")
            draw_hangman(1)
            mocked_print.assert_any_call("________      ")
            draw_hangman(0)
            mocked_print.assert_any_call("________      ")

    def test_validate_input_valid(self):
        self.assertTrue(is_valid_input('a'))
        self.assertTrue(is_valid_input('A'))  # Test case insensitivity

    def test_validate_input_non_alphabet(self):
        self.assertFalse(is_valid_input('1'))
        self.assertFalse(is_valid_input('?'))
        self.assertFalse(is_valid_input(' '))

    def test_validate_input_multiple_characters(self):
        self.assertFalse(is_valid_input('ab'))

    def test_validate_input_null(self):
        self.assertFalse(is_valid_input(''))

    def test_already_guessed_true(self):
        guessed_chars = ['a', 'b', 'c']
        self.assertTrue(is_already_guessed('a', guessed_chars))

    def test_already_guessed_false(self):
        guessed_chars = ['a', 'b', 'c']
        self.assertFalse(is_already_guessed('d', guessed_chars))

    def test_handle_correct_guess(self):
        word = 'hangman'
        guessed_chars = []
        temp = '_ _ _ _ _ _ _ '
        character = 'a'

        new_temp = handle_correct_guess(word, guessed_chars, temp, character)
        self.assertEqual(new_temp, '_ a _ _ _ a _')

        new_temp = handle_correct_guess(word, guessed_chars, new_temp, 'n')
        self.assertEqual(new_temp, '_ a n _ _ a n')

    def test_handle_wrong_guess(self):
        chances = 7
        word = 'hangman'
        guessed_chars = []

        new_chances = handle_wrong_guess(chances, word, guessed_chars)
        self.assertEqual(new_chances, 6)

    def test_update_display(self):
        word = 'hangman'
        guessed_chars = ['a', 'n']
        self.assertEqual(update_display(word, guessed_chars), '_ a n _ _ a n')

    def test_win_game(self):
        with patch('builtins.print') as mocked_print:
            win_game('hangman')
            mocked_print.assert_any_call("\nThe word was: hangman")
            mocked_print.assert_any_call("\nYou did it! The hangman is spared...for now. You live to see another day!")

    def test_lose_game(self):
        with patch('builtins.print') as mocked_print:
            lose_game('hangman')
            mocked_print.assert_any_call("\nThe word was: hangman")
            mocked_print.assert_any_call("\nNo! The word remains unsolved and the hangman claims another victim.")

if __name__ == '__main__':
    unittest.main()
