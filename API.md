# API Documentation

## Public Functions

### `ltr_evaluation(expr: str) -> float`
Evaluates arithmetic expression with parentheses using left-to-right strategy.

**Parameters:**
- `expr` - arithmetic expression string (e.g., "3 + (2 * 10)")

**Returns:**
- Result of evaluation as float

**Raises:**
- `ValueError` - if expression has syntax or parentheses pairing errors
- `ZeroDivisionError` - if division by zero occurs

**Supported operators:**
- `+` (addition)
- `-` (subtraction)
- `*` (multiplication)
- `/` (division)
- `**` (power)

**Examples:**
```python
ltr_evaluation("(3 + 2) * 10")  # Returns: 50.0
ltr_evaluation("2 ** 3 + 5")    # Returns: 13.0
```

### `_check_arithmetic_expr(expr: str) -> tuple[bool, str]`
Validates arithmetic expression for syntax and parentheses pairing.

**Parameters:**
- `expr` - expression to validate

**Returns:**
- Tuple of (is_valid, error_message)
  - `(True, "valid")` - if expression is valid
  - `(False, "syntax error")` - if syntax is incorrect
  - `(False, "parentheses pairing error")` - if parentheses don't match
  - `(False, "syntax error and parentheses pairing error")` - both errors

**Examples:**
```python
_check_arithmetic_expr("(10 + 20) * 5")      # (True, "valid")
_check_arithmetic_expr("10 + + 20")          # (False, "syntax error")
_check_arithmetic_expr("(10 + 20))))")       # (False, "parentheses pairing error")
```

## Internal Functions

### `_normalize_expression(expr: str) -> str`
Removes all whitespace from expression.

### `_check_parentheses_pairing(expr: str) -> bool`
Checks if parentheses are properly paired and balanced.

### `_compute_binary(left: float, right: float, operation: str) -> float`
Performs binary arithmetic operation.

### `_evaluate_flat_expression(expr: str) -> float`
Evaluates expression without parentheses using left-to-right order.

## Constants

### `ErrorMessages`
- `SYNTAX_ERROR` - "syntax error"
- `PAIRING_ERROR` - "parentheses pairing error"
- `BOTH_ERRORS` - "syntax error and parentheses pairing error"
- `VALID` - "valid"

### `Patterns`
- `ADJACENT_DIGITS` - regex for detecting adjacent numbers without operator
- `WHITESPACE` - regex for whitespace
- `INNERMOST_PARENTHESES` - regex for finding innermost parentheses groups

### `OPERATORS`
Dictionary mapping operator symbols to Python functions:
```python
{
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": operator.pow
}
```

## Algorithm

1. **Validation**: Check syntax and parentheses pairing
2. **Normalization**: Remove all whitespace
3. **Evaluation**:
   - Find innermost parentheses group
   - Evaluate it left-to-right
   - Replace with result
   - Repeat until no parentheses remain
   - Evaluate final expression

## Complexity

- **Time**: O(n²) in worst case (nested parentheses)
- **Space**: O(n) for expression storage

## Legacy Aliases

For backward compatibility:
- `ltrEvaluation` → `ltr_evaluation`
- `_checkArithmeticExpr` → `_check_arithmetic_expr`

