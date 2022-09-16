import pytest
import sys
import os
# from src.Parsing.Parser import Parser

# TESTS keywords_parser

# To test std
### captured = capsys.readouterr()
### assert captured.out == "hello\n"
### assert captured.err == "world\n"


#################### test_get_input_tokens_list TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ("", None),
# ])
# def test_get_input_tokens_list_valid(entry, expected):
#     assert Parser.get_input_tokens_list(entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ("", None),
# ])
# def test_get_input_tokens_list_error(entry, expected):
#     assert Parser.get_input_tokens_list(entry) == expected


#################### SELECT TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([['A', ',', 'B', ',', 'C', 'FROM', 'TEST'], "SELECT", None, []], (['FROM', 'TEST'], "SELECT", None, ['A', 'B', 'C'])),
#     ([['*', 'FROM', 'TEST'], "SELECT", None, []], (['FROM', 'TEST'], "SELECT", None, ['*'])),
# ])
# def test_select_parser_valid(entry, expected):
#     assert Parser.select_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([['A', 'B', 'C', 'FROM', 'TEST'], "SELECT", None, []], None),
# ])
# def test_select_parser_error(entry, expected):
#     assert Parser.select_parser(*entry) == expected


#################### FROM TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_from_parser_valid(entry, expected):
#     assert Parser.from_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_from_parser_error(entry, expected):
#     assert Parser.from_parser(*entry) == expected


#################### WHERE TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_where_parser_valid(entry, expected):
#     assert Parser.where_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_where_parser_error(entry, expected):
#     assert Parser.where_parser(*entry) == expected


#################### CREATE TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_create_parser_valid(entry, expected):
#     assert Parser.create_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_create_parser_error(entry, expected):
#     assert Parser.create_parser(*entry) == expected


#################### DROP TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_drop_parser_valid(entry, expected):
#     assert Parser.drop_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_drop_parser_error(entry, expected):
#     assert Parser.drop_parser(*entry) == expected


#################### INSERT TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_insert_parser_valid(entry, expected):
#     assert Parser.insert_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_insert_parser_error(entry, expected):
#     assert Parser.insert_parser(*entry) == expected


#################### USE TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_use_parser_valid(entry, expected):
#     assert Parser.use_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_use_parser_error(entry, expected):
#     assert Parser.use_parser(*entry) == expected


#################### SHOW TESTS ####################
# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_show_parser_valid(entry, expected):
#     assert Parser.show_parser(*entry) == expected

# @pytest.mark.parametrize("entry,expected", [
#     ([[''], None, None, []], None),
# ])
# def test_show_parser_error(entry, expected):
#     assert Parser.show_parser(*entry) == expected
