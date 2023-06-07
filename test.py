data = [
    "Aneka Buana Supermarket - Pondok Labu ",
    "Alfamart Pinang Raya",
    "Indomaret Plus Fatmawati",
    "Alfamart Margasatwa",
    "Indomaret H.Ipin"
]

excluded_place = [
    "Alfamart",
    "Indomaret"
]

filtered_data = []
for place in data:
    if not any(excluded in place for excluded in excluded_place):
        filtered_data.append(place)


print(filtered_data)
