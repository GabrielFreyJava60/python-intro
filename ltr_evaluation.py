import operator as op
import re


OPERATORS: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
    "**": op.pow
}


def _build_operator_pattern():
    op_symbols = sorted(OPERATORS.keys(), key=len, reverse=True)
    return "(?:" + "|".join(re.escape(o) for o in op_symbols) + ")"


_operator_pattern = re.compile(_build_operator_pattern())
_operand_pattern = re.compile(r"[\d.]+")


def _check_parentheses_pairing(expr: str) -> bool:
    depth = 0
    for char in expr:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        if depth < 0:
            return False
    return depth == 0


def _compute_binary(left: float, right: float, operation: str) -> float:
    operator_func = OPERATORS.get(operation)
    if not operator_func:
        raise ValueError(f"{operation} not found")
    return operator_func(left, right)


def _evaluate_flat_expression(expr: str) -> float:
    operands = re.split(_operator_pattern, expr)
    operators = re.split(_operand_pattern, expr)
    result = float(operands[0])
    for i in range(1, len(operands)):
        result = _compute_binary(result, float(operands[i]), operators[i])
    return result


def ltrEval(expr: str) -> str:
    try:
        expr_normalized = re.sub(r"\s+", "", expr)
        
        if not _check_parentheses_pairing(expr_normalized):
            return f"Error: parentheses pairing error in '{expr}'"
        
        while match := re.search(r"\([^()]+\)", expr_normalized):
            inner_expr = match.group()[1:-1]
            value = _evaluate_flat_expression(inner_expr)
            expr_normalized = expr_normalized[:match.start()] + str(value) + expr_normalized[match.end():]
        
        result = _evaluate_flat_expression(expr_normalized)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

