# Input items from the user
ingevoerde_items_sinterklaas = []
#ingevoerde_items_sinterklaas = input("Wat zou je graag van Sinterklaas willen hebben: ")#.split())
if ingevoerde_items_sinterklaas != 'KLAAR':
#    ingevoerde_items_sinterklaas.append(input("Wat zou je graag van Sinterklaas willen hebben: "))
    ingevoerde_items_sinterklaas.append(input("Wat zou je graag van Sinterklaas willen hebben: "))
    lijst = list(ingevoerde_items_sinterklaas)
    gesorteerde_reeks = sorted(lijst)
#    print("de items die je van Sinterklaas wilt hebben:", ingevoerde_items_sinterklaas)
else:    # if ingevoerde_items_sinterklaas == 'KLAAR':
    print("de items die je van Sinterklaas wilt hebben:", gesorteerde_reeks)
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
