import unittest
from unittest.mock import Mock
from src.classes.MimeSweeperMain import MimeSweeperMain
from src.classes.DifficultyDialog import DifficultyDialog


class TestMimeSweeperMain(unittest.TestCase):

    # def setUp(self) -> None:
    # self.main_window = MimeSweeperMain()

    @Mock('DifficultyDialog')
    def test_if_difficulty_difficulty_dialog_appears(self, mock_difficulty_dialog):
        self.window = MimeSweeperMain()
        mock_difficulty_dialog.assert_called_once()
