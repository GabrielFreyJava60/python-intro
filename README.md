# HW#35 Definition

## Write two functions according to TODO docstring and tests (see test_regular_expressions.py)

### Function ipV4AddressRe

Returns a compiled regular expression pattern that validates IPv4 addresses.

* IPv4 address consists of four decimal numbers (octets) from 0 to 255, separated by dots
* Each octet can be:
  - 250-255 (25[0-5])
  - 200-249 (2[0-4][0-9])
  - 0-199 ([01]?[0-9][0-9]?)

### Examples

* Valid: `192.168.1.1`, `0.0.0.0`, `255.255.255.255`
* Invalid: `256.256.256.256`, `192.168.1`, `abc.def.ghi.jkl`

### Function mobileIsraelNumberRe

Returns a compiled regular expression pattern that validates Israeli mobile phone numbers.

* Israeli mobile numbers start with `05` followed by 8 digits
* Total length: 10 digits
* Format: `05XXXXXXXX`

### Examples

* Valid: `0521234567`, `0501234567`, `0541234567`
* Invalid: `0621234567`, `052123456`, `521234567`

## Make sure the specified test pass

Run tests with:
```bash
python3 -m pytest test_regular_expressions.py -v
```
