import logging

from typing import Dict

import re

NasDaqDict = Dict[str,str]

def check_if_email_valid(contactdict: NasDaqDict) -> bool:
	for name,emailid in contactdict.items():
		if (not isinstance(name,str)) or (not isinstance(emailid,str)):
			return False
		if not re.match(r"[a-zA-Z0-9\._\+-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]+$",emailid):
			return False

	return True

print(check_if_email_valid({'aaron':'whatsappaaron@hotmail.com'}))
print(check_if_email_valid({'aaron':'whatsappaaron@hotmail.com',455:'wrongemail@hotmail.com'}))
