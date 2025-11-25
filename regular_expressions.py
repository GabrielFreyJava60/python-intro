import re


def arithmeticOperandRe() -> str:
    number: str = r"(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?"
    return rf"\s*\(*\s*{number}\s*\)*\s*"


def arithmeticOperatorRe(ops) -> str:
    op_symbols = sorted(ops.keys(), key=len, reverse=True)
    return "(?:" + "|".join(re.escape(op) for op in op_symbols) + ")"


def arithmeticExpression(ops) -> str:
    operand = arithmeticOperandRe()
    operator = arithmeticOperatorRe(ops)
    return rf"{operand}({operator}{operand})*"
