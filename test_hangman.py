import unittest
from unittest.mock import patch, mock_open
from hangmangame import (
    get_random_word, draw_hangman, validate_input, already_guessed, handle_guess,
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
        self.assertTrue(validate_input('a'))
        self.assertTrue(validate_input('A'))  # Test case insensitivity

    def test_validate_input_non_alphabet(self):
        self.assertFalse(validate_input('1'))
        self.assertFalse(validate_input('?'))
        self.assertFalse(validate_input(' '))

    def test_validate_input_multiple_characters(self):
        self.assertFalse(validate_input('ab'))

    def test_validate_input_null(self):
        self.assertFalse(validate_input(''))

    def test_already_guessed_true(self):
        guessed_chars = ['a', 'b', 'c']
        self.assertTrue(already_guessed('a', guessed_chars))

    def test_already_guessed_false(self):
        guessed_chars = ['a', 'b', 'c']
        self.assertFalse(already_guessed('d', guessed_chars))

    def test_handle_guess_valid_guess(self):
        word = 'hangman'
        guessed_chars = []
        chances = 7

        guessed_chars, chances, valid_guess = handle_guess(word, guessed_chars, chances, 'a')
        self.assertTrue(valid_guess)
        self.assertEqual(guessed_chars, ['a'])
        self.assertEqual(chances, 7)

    def test_handle_guess_already_guessed(self):
        word = 'hangman'
        guessed_chars = ['a']
        chances = 7

        guessed_chars, chances, valid_guess = handle_guess(word, guessed_chars, chances, 'a')
        self.assertFalse(valid_guess)
        self.assertEqual(guessed_chars, ['a'])
        self.assertEqual(chances, 7)

    def test_handle_guess_incorrect(self):
        word = 'hangman'
        guessed_chars = []
        chances = 7

        guessed_chars, chances, valid_guess = handle_guess(word, guessed_chars, chances, 'z')
        self.assertFalse(valid_guess)
        self.assertEqual(guessed_chars, ['z'])
        self.assertEqual(chances, 6)

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

