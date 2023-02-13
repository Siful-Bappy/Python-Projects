### pip install pycountry
### pip install phonenumbers
### pip install phone-iso3166

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
x = phonenumbers.parse("+442083661177", None)
print(geocoder.description_for_number(x, "en"))

y = phonenumbers.parse("+919872529361", None)
print(carrier.name_for_number(y, "en"))