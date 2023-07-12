import sys
sys.path.insert(0, './') # for the future to setupt github actions

from helpers.Parser import Parser
import pytest

def test_true_expression():
    p = Parser()
    expr = p.parse_expression("x**2")
    assert expr.subs("x", 2) == 4

def test_constant_function():
    p = Parser()
    expr = p.parse_expression("2")
    assert expr.subs("x", 100000) == 2
    
def test_false_expression():
    p = Parser()
    with pytest.raises(Exception):
        expr = p.parse_expression("x**2-")
        
def test_parse_value():
    p = Parser()
    x = p.parse_value("2.655")
    assert x == 2.655
    
def test_parse_value_negative():
    p = Parser()
    x = p.parse_value("-3005.87")
    assert x == -3005.87
    
def test_parse_value_scientific_notation():
    p = Parser()
    x = p.parse_value("-2.655e3")
    assert x == -2655
    
def test_parse_value_invalid():
    p = Parser()
    with pytest.raises(Exception):
        x = p.parse_value("2.655.5")
        
def test_parse_value_invalid2():
    p = Parser()
    with pytest.raises(Exception):
        x = p.parse_value("-3.6+4")