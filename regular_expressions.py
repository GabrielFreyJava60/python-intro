import re


class IPv4Patterns:
    OCTET_250_255 = r'25[0-5]'
    OCTET_200_249 = r'2[0-4][0-9]'
    OCTET_0_199 = r'[01]?[0-9][0-9]?'

    @classmethod
    def octet(cls) -> str:
        return f'(?:{cls.OCTET_250_255}|{cls.OCTET_200_249}|{cls.OCTET_0_199})'

    @classmethod
    def full_address(cls) -> str:
        oct_pattern = cls.octet()
        return rf'^{oct_pattern}\.{oct_pattern}\.{oct_pattern}\.{oct_pattern}$'


class IsraeliMobilePatterns:
    PREFIX = '05'
    REMAINING_DIGITS = 8

    @classmethod
    def full_number(cls) -> str:
        return rf'^{cls.PREFIX}\d{{{cls.REMAINING_DIGITS}}}$'


def ipV4AddressRe():
    return re.compile(IPv4Patterns.full_address())


def mobileIsraelNumberRe():
    return re.compile(IsraeliMobilePatterns.full_number())


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
