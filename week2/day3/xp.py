keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


result_dict = dict(zip(keys, values))
print(result_dict)

#Exercise 2: Cinemax



family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total_cost = 0
for member, age in family.items():
    if age < 3:
        cost = 0
    elif 3 <= age <= 12:
        cost = 10
    else:
        cost = 15
    print(f"{member} has to pay ${cost}.")
    total_cost += cost

print(f"Total cost for the family: ${total_cost}")

#Exercise 3: Zara

brand_info = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {'France': 'blue', 'Spain': 'red', 'US': ['pink', 'green']}
}


brand_info['number_stores'] = 2


print(f"Zara's clients are people looking for {', '.join(brand_info['type_of_clothes'])} clothing.")

brand_info['country_creation'] = 'Spain'

if 'international_competitors' in brand_info:
    brand_info['international_competitors'].append('Desigual')

del brand_info['creation_date']

print("Last international competitor:", brand_info['international_competitors'][-1])

print("Major clothes colors in the US:", brand_info['major_color']['US'])

print("Number of key-value pairs:", len(brand_info))

print("Keys of the dictionary:", list(brand_info.keys()))

more_on_zara = {'creation_date': 1975, 'number_stores': 10000}

brand_info.update(more_on_zara)

print("Value of the key number_stores:", brand_info['number_stores'])

#Exercise 4: Disney Characters

users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]


disney_users_A = {user: index for index, user in enumerate(users)}
print(disney_users_A)

disney_users_B = {index: user for index, user in enumerate(users)}
print(disney_users_B)

disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(disney_users_C)

recreated_disney_users_A = {}
for index, user in enumerate(users):
    recreated_disney_users_A[user] = index
print(recreated_disney_users_A)

recreated_disney_users_B = {}
for index, user in enumerate(users):
    recreated_disney_users_B[index] = user
print(recreated_disney_users_B)

recreated_disney_users_C = {user: index for index, user in enumerate(sorted(users))}
print(recreated_disney_users_C)

disney_users_containing_i = {user: index for index, user in enumerate(users) if 'i' in user}
print(disney_users_containing_i)

disney_users_starting_with_m_or_p = {user: index for index, user in enumerate(users) if user[0].lower() in ['m', 'p']}
print(disney_users_starting_with_m_or_p)