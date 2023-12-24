user_word = input("Enter a word: ")

letter_indexes = {}
for index, letter in enumerate(user_word):
    if letter not in letter_indexes:
        letter_indexes[letter] = [index]
    else:
        letter_indexes[letter].append(index)

print(letter_indexes)

#Challenge 2:

def convert_price_to_number(price_str):
    return int(price_str.replace('$', '').replace(',', ''))

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

wallet_amount = convert_price_to_number(wallet)

affordable_items = [item for item, price in items_purchase.items() if wallet_amount >= convert_price_to_number(price)]

affordable_items.sort()

if affordable_items:
    print(affordable_items)
else:
    print("Nothing")