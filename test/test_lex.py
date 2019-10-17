from typing import Any, List, Tuple
from unittest import TestCase

from rply import Token

from src.lexer import lex


class TestLex(TestCase):
    def test_lex(self) -> None:
        self.test_lex_number()
        self.test_lex_string()

    def test_lex_number(self) -> None:
        numbers = '0 -1 1 1234567890 -1234567890'
        numbers_types = [('NUMBER', '0'), ('NUMBER', '-1'), ('NUMBER', '1'),
                         ('NUMBER', '1234567890'), ('NUMBER', '-1234567890')]
        self.assertEqual(numbers, numbers_types)

    def test_lex_string(self) -> None:
        strings = '"fuck" "shit" "f" "s" "1" "123" "_+" "-+123" "123lou" "lou_+"'
        strings_types = [('STRING', '"fuck"'), ('STRING', '"shit"'), ('STRING', '"f"'), ('STRING', '"s"'),
                         ('STRING', '"1"'), ('STRING', '"123"'), ('STRING', '"_+"'), ('STRING', '"-+123"'),
                         ('STRING', '"123lou"'), ('STRING', '"lou_+"')]
        self.assertEqual(strings, strings_types)

    def assertEqual(self, first: str, second: List[Tuple[str, str]], msg: Any = ...) -> None:
        super().assertEqual(list(lex(first)), [Token(name, value) for name, value in second], msg)
