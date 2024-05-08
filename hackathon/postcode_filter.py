
# sometimes posts codes are not written the same way as some can be capitalized and some not, spaces
# group postcodes by there first few letters and return the postcodes in a list
# TODO think if this would break for postcodes of different lengths

# data = [

#     "br2 0pt",
#     "br14 0pz",
#     "br1 0tz",
#     "BR10tt",
# ]


data = [
    "bn26 5ra",
    "bn26 5ra",
    "bn26 5ra",
    "bn26 5ra",
    "bn8 5ap",
    "bn8 6au",
    "bn8 6dp",
    "bn8 6nr",
    "bn8 6ns",
    "Bn8 6ta",
    "bn8 6an",
    "bn9 9an",
    "bn9 9at",
]


def postcode_filter(data):
    data = [x.lower() for x in data]
    data = [x.replace(" ", "") for x in data]
    return data


def postcode_match(postcodes: list, remove: int) -> dict:
    postcodes = postcode_filter(postcodes)
    postcode_dict = {}
    for postcode in postcodes:
        if postcode[:remove] not in postcode_dict:
            postcode_dict[postcode[:remove]] = [postcode]
        else:
            postcode_dict[postcode[:remove]].append(postcode)

    return postcode_dict


print()
print(postcode_match(data, -2))


def count_postcode_match(postcodes: list) -> dict:
    matchedPostcode = postcode_match(postcodes, -2)
    count = {}
    for key in matchedPostcode:
        count[key] = len(matchedPostcode[key])
    return count


print()
print(count_postcode_match(data))


def formate_postcode(postcide: str) -> str:
    return postcide[:-1] + " " + postcide[-1] + "**"


