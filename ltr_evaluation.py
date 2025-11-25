import operator as op
import regular_expressions as regexp
import re

__ops: dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.itruediv,
    "**": op.pow
}
__exprPattern = re.compile(regexp.arithmeticExpression(__ops))
__operatorPattern = re.compile(regexp.arithmeticOperatorRe(__ops))
__operandPattern = re.compile(r"[\d.]+")


def __checkParenthesesPairing(expr: str) -> bool:
    counter = 0
    for char in expr:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


def _checkArithmeticExpr(expr: str) -> tuple[bool, str]:
    if re.search(r'\d\s+\d', expr):
        pairing_valid = __checkParenthesesPairing(expr)
        if not pairing_valid:
            return False, "syntax error and parentheses pairing error"
        return False, "syntax error"
    
    expr_no_spaces = re.sub(r"\s+", "", expr)
    
    syntax_valid = bool(re.fullmatch(__exprPattern, expr_no_spaces))
    pairing_valid = __checkParenthesesPairing(expr_no_spaces)
    
    if not syntax_valid and not pairing_valid:
        return False, "syntax error and parentheses pairing error"
    elif not syntax_valid:
        return False, "syntax error"
    elif not pairing_valid:
        return False, "parentheses pairing error"
    
    return True, "valid"


def __binCompute(op1: float, op2: int, operation: float) -> float:
    operator = __ops.get(operation)
    if not operator:
        raise ValueError(f"{operation} not found")
    return operator(op1, op2)


def __ltrEvaluationNoParentheses(expr: str) -> float:
    operands: list[str] = re.split(__operatorPattern, expr)
    operators: list[str] = re.split(__operandPattern, expr)
    res = float(operands[0])
    for i in range(1, len(operands)):
        res = __binCompute(res, float(operands[i]), operators[i])
    return res


def ltrEvaluation(expr: str) -> int:
    is_valid, error_msg = _checkArithmeticExpr(expr)
    if not is_valid:
        raise ValueError(f"{error_msg} in '{expr}'")
    
    expr = re.sub(r"\s+", "", expr)
    while mo := re.search(r"\([^()]+\)", expr):
        inner = mo.group()[1:-1]
        value = __ltrEvaluationNoParentheses(inner)
        expr = expr[:mo.start()] + str(value) + expr[mo.end():]
    return __ltrEvaluationNoParentheses(expr)
