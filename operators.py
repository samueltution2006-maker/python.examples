list_items = [ 1, 2.0, "Three", True ] 

#for item in "1, 2.0, Three, True"

for item in list_items:
    if item == "Three":
       print("Item found") 

# Membership operator

if "Three" in list_items:
   print("Item found")

if not 6 in list_items:
   print("Item not found")