is_male = True
is_tall = False

#1. or operator (perlu 1 True)
if is_male or is_tall:
    print("You are a male")
else:
    print("You are not a male")

#2. and operator (both need to be true)
# Else If (elif)
is_female = False
is_tall2 = True

if is_female and is_tall2:
    print("You are tall female")
elif is_female and not(is_tall):
    print("You are short female")
elif not(is_female) and is_tall2:
    print("You are not female but youre tall")
else:
    print("You are not a female and not tall")