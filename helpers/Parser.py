import sympy as sp


class Parser():
    def __init__(self) -> None:
        pass
    
    # parse the expression and return a sympy expression
    def parse_expression(self, expression : str)->sp.Expr:
        expression = expression.replace("^", "**")
        return sp.sympify(expression)
    
    # parse the value and return a float
    def parse_value(self, value : str) -> float:
        val = float(value)
        if val == float("inf") or val == float('-inf'):
            raise RuntimeError
        return val