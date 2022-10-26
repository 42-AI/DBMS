from src.Parsing import Parser
from src.Parsing.ParsingNode import Node
from src.Parsing.test_resources.CreateTestData import CreateTestData
from src.Parsing.test_resources.InsertTestData import InsertTestData
from src.ErrorMessages import ErrorMessages
import pytest


#################### test_get_input_tokens_list TESTS ####################
@pytest.mark.parametrize("entry,expected", [
    (
        CreateTestData.get_input_token_list_entry,
        CreateTestData.get_input_token_list_expected
    ),
    (
        InsertTestData.get_input_token_list_entry,
        InsertTestData.get_input_token_list_expected
    ),
])
def test_get_input_tokens_list_valid(entry, expected):
    assert Parser.get_input_tokens_list(entry) == expected

@pytest.mark.parametrize("entry,expected", [
    ("", []),
])
def test_get_input_tokens_list_error(entry, expected):
    assert Parser.get_input_tokens_list(entry) == expected


#################### split_instructions TESTS ############################
@pytest.mark.parametrize("entry,expected", [
    (
        CreateTestData.split_instruction_entry,
        CreateTestData.split_instruction_expected
        
    ),
    (
        InsertTestData.split_instruction_entry,
        InsertTestData.split_instruction_expected
    ),
])
def test_split_instruction_valid(entry, expected):
    assert Parser.split_instruction(entry) == expected

@pytest.mark.parametrize("entry,expected", [
    ("", []),
])
def test_split_instruction_error(entry, expected):
    assert Parser.split_instruction(entry) == expected


#################### simple_parser TESTS ############################
@pytest.mark.parametrize("entry,expected", [
    (
        [[['variable', 'demo']], 'use'],
        [[], Node(keyword="use", data="demo")]
    ),
])
def test_simple_parser_valid(entry, expected):
    i_t, node = Parser.simple_parser(*entry)
    assert i_t == expected[0]
    assert node.keyword == expected[1].keyword
    assert node.data == expected[1].data

@pytest.mark.parametrize("entry,expected", [
    (
        [[['not a variable', 'demo']], 'use'],
        [[], Node(keyword="use", data="demo")]
    ),
])
def test_simple_parser_error(entry, expected):
    ErrorMsg = Parser.simple_parser(*entry)
    e = ErrorMessages.PARSING_SYNTAX
    assert ErrorMsg[0:len(e)] == e
