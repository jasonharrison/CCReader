## CCReader

CCReader parses magstripe data from ISO/IEC 7813 financial cards.

It is intended to be used with a USB card reader that emulates a keyboard.

## Usage

```
>>> import ccparser
card=ccparser.parsecard('%B4242424242424242^SMITH JOHN Q^15052011000000000000?;4242424242424242=15052011000000000000')
print(card)
{'exp_month': '05', 'name': 'JOHN Q SMITH', 'raw_name': 'SMITH/JOHN Q', 'number': '4242424242424242', 'exp_year': '2015', 'type': 'Visa'}
```
