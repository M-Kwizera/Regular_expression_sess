#!/usr/bin/python3

import re
"""regex  that matches my phone number with country code."""
# phone_number = "+123 071 234 567"

phone_number = '+123 071 234 567'
print(re.search(r"\+\d{3} \d{3} \d{3} \d{3}", phone_number))

