# Dictionaries 
# <...> = {
#   key: value
# }

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    12: "December",
}

print(monthConversions["Jan"])

print(monthConversions[12])

#get(key, default_value)
print(monthConversions.get("tes", "Not a Valid Key"))

