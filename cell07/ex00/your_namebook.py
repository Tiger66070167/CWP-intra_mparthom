def array_of_names(names_dict):
    result = []

    for first_name, last_name in names_dict.items():
        result.append(first_name.capitalize() + " " + last_name.capitalize())

    return result


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
