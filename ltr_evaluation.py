import operator as op
import regular_expressions as regexp
import re


class ErrorMessages:
    SYNTAX_ERROR = "syntax error"
    PAIRING_ERROR = "parentheses pairing error"
    BOTH_ERRORS = "syntax error and parentheses pairing error"
    VALID = "valid"


class Patterns:
    ADJACENT_DIGITS = r'\d\s+\d'
    WHITESPACE = r"\s+"
    INNERMOST_PARENTHESES = r"\([^()]+\)"


OPERATORS: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.itruediv,
    "**": op.pow
}

_expr_pattern = re.compile(regexp.arithmeticExpression(OPERATORS))
_operator_pattern = re.compile(regexp.arithmeticOperatorRe(OPERATORS))
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


def _check_arithmetic_expr(expr: str) -> tuple[bool, str]:
    has_adjacent_digits = bool(re.search(Patterns.ADJACENT_DIGITS, expr))
    expr_normalized = re.sub(Patterns.WHITESPACE, "", expr)
    
    is_syntax_valid = bool(re.fullmatch(_expr_pattern, expr_normalized)) and not has_adjacent_digits
    is_pairing_valid = _check_parentheses_pairing(expr_normalized)
    
    if not is_syntax_valid and not is_pairing_valid:
        return False, ErrorMessages.BOTH_ERRORS
    if not is_syntax_valid:
        return False, ErrorMessages.SYNTAX_ERROR
    if not is_pairing_valid:
        return False, ErrorMessages.PAIRING_ERROR
    
    return True, ErrorMessages.VALID


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


def ltr_evaluation(expr: str) -> float:
    is_valid, error_msg = _check_arithmetic_expr(expr)
    if not is_valid:
        raise ValueError(f"{error_msg} in '{expr}'")
    
    expr = re.sub(Patterns.WHITESPACE, "", expr)
    
    while match := re.search(Patterns.INNERMOST_PARENTHESES, expr):
        inner_expr = match.group()[1:-1]
        value = _evaluate_flat_expression(inner_expr)
        expr = expr[:match.start()] + str(value) + expr[match.end():]
    
    return _evaluate_flat_expression(expr)


_checkArithmeticExpr = _check_arithmetic_expr
ltrEvaluation = ltr_evaluation
