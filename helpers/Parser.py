import sympy as sp


class Parser():
    def __init__(self) -> None:
        pass
    
    # parse the expression and return a sympy expression
    def parse_expression(self, expression : str)->sp.Expr:
        expression = expression.replace("^", "**")
        expr = sp.sympify(expression)
        
        # Get a set of all symbols in the expression
        symbols = expr.free_symbols
        
        # Check if any of the symbols are not 'x'
        for symbol in symbols:
            if symbol != sp.Symbol('x'):
                raise RuntimeError
        return expr
    
    # parse the value and return a float
    def parse_value(self, value : str) -> float:
        val = float(value)
        if val == float("inf") or val == float('-inf'):
            raise RuntimeError
        return val