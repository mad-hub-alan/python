
country_codes = {
    "IN" : "India",
    "RU": "Russia",
    "AU": "Australia",
    "NZ": "NewZealand",
    "UAE" : "United Arab Emirates",
    "US": "United States of America",
    "UK": "United Kingdom",
    "WI": "WestIndies",
}

# print(country_codes["AR"])
country_codes.update({"WI":"Westie"})
country_codes.update({"SW":"Switzerland"})
# print(country_codes.get("AM","Not Found!"))

country_codes.pop("UP","UK")

print(country_codes.popitem())

# country_codes.clear()

temp_cc = country_codes.copy()

# print(temp_cc)

rss = country_codes.setdefault("RSS","Mascow")
print(rss)

key_set = country_codes.keys()

new_dic = country_codes.fromkeys(key_set,"---")
print(new_dic)

country_codes.update({"TK":"Turkey"})
print(country_codes)
print(temp_cc)

squares = {x: x**x for x in range(5)} #populating dict with and loop
print(squares)