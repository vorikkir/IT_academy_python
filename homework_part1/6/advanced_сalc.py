import re

regex = re.complite(r"([0-9\-]+)([+\-*/]{1,2})(\d+)")

operator_map = {"+": operator.add,
                "-": operator.sub,
                "/": operator.div,
                "*": operator.mul,
                "**": operator.pow,
                }

def calc(expr: str) -> int:
    expr = expr.replace(" ", "")
    first_operand, operator, second_operator = regex.findall(expr)[0]
    return operator_map[operator](int(first_operand), int(second_operator))

def sum():
