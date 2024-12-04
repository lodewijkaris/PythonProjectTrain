# Input an array from the user
ingevoerde_reeks = list(map(int, input("Voeg vijf gehele getallen in gescheiden door een spatie en druk enter: ").split()))

# Sort the array
gesorteerde_reeks = sorted(ingevoerde_reeks)

# Print the sorted array
print("de getallen gesorteerd van klein naar groot:", gesorteerde_reeks)