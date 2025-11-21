import re


class IPv4Patterns:
    """Constants and patterns for IPv4 address validation."""
    OCTET_250_255 = r'25[0-5]'
    OCTET_200_249 = r'2[0-4][0-9]'
    OCTET_0_199 = r'[01]?[0-9][0-9]?'

    @classmethod
    def octet(cls) -> str:
        """Returns the pattern for a single octet (0-255)."""
        return f'(?:{cls.OCTET_250_255}|{cls.OCTET_200_249}|{cls.OCTET_0_199})'

    @classmethod
    def full_address(cls) -> str:
        """Returns the full IPv4 address pattern."""
        oct_pattern = cls.octet()
        return rf'^{oct_pattern}\.{oct_pattern}\.{oct_pattern}\.{oct_pattern}$'


class IsraeliMobilePatterns:
    """Constants and patterns for Israeli mobile number validation."""
    PREFIX = '05'
    REMAINING_DIGITS = 8

    @classmethod
    def full_number(cls) -> str:
        """Returns the full Israeli mobile number pattern."""
        return rf'^{cls.PREFIX}\d{{{cls.REMAINING_DIGITS}}}$'


def ipV4AddressRe():
    """Returns a compiled regex object for IPv4 address validation."""
    return re.compile(IPv4Patterns.full_address())


def mobileIsraelNumberRe():
    """Returns a compiled regex object for Israeli mobile number validation."""
    return re.compile(IsraeliMobilePatterns.full_number())
