# Input items from the user
ingevoerde_item_sinterklaas = []
ingevoerde_items_sinterklaas = []
#start the while loop
#ingevoerde_items_sinterklaas = input("Wat zou je graag van Sinterklaas willen hebben: ")#.split())
#def append(ingevoerde_items_sinterklaas):
#    pass

while ingevoerde_item_sinterklaas != "KLAAR":
#    ingevoerde_items_sinterklaas.append(input("Wat zou je graag van Sinterklaas willen hebben: "))
#    ingevoerde_items_sinterklaas.append(input("Wat zou je graag van Sinterklaas willen hebben: "))
    ingevoerde_item_sinterklaas = (input("Wat zou je graag van Sinterklaas willen hebben en druk enter, type KLAAR om te stoppen: "))
    ingevoerde_items_sinterklaas.append(ingevoerde_item_sinterklaas)
    lijst = list(ingevoerde_items_sinterklaas)
#    if ingevoerde_items_sinterklaas == "KLAAR":
#        break
    print("de items die je van Sinterklaas wilt hebben:", ingevoerde_items_sinterklaas)

else:    # if ingevoerde_items_sinterklaas == 'KLAAR':
#    lijst = list(ingevoerde_items_sinterklaas)
    gesorteerde_reeks = sorted(lijst)
#exclude KLAAR
    excluded_string = "KLAAR"
    filtered_list = [item for item in gesorteerde_reeks if item != excluded_string]
    print("de items die je van Sinterklaas wilt hebben gesorteerd:", filtered_list)
#break
#else:    # if ingevoerde_items_sinterklaas == 'KLAAR':
#        exit(ingevoerde_items_sinterklaas)
#break   #break here
#print("de items die je van Sinterklaas wilt hebben:", gesorteerde_reeks)

#    gesorteerde_reeks = sorted(ingevoerde_items_sinterklaas)
#    print("de items die je van Sinterklaas wilt hebben:", ingevoerde_items_sinterklaas)
# Sort the array
#gesorteerde_reeks = sorted(gesorteerde_reeks)
# Print the sorted array
#print("de items sie je wilt hebben van Sinterklaas alfabetisch gesorteerd:", gesorteerde_reeks)


#items = []
#item = list(input("Wat zou je graag van Sinterklaas willen hebben: ").split())
#while item != ("KLAAR"):
