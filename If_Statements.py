
is_adult = False
is_indian = False

# print(not is_adult)

if is_indian and is_adult:
    print('You are Eligible to vote...')
elif is_indian and not is_adult:
    print('You must 18 or more to vote!')
elif is_adult and not is_indian:
    print('You must be Indian to vote!')
else:
    print('You must be adult and Indian to vote!')