# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo")

order = "leek 4"
index_quantity = order.find("4")
quantity = int(order[index_quantity:index_quantity + 1])
sum_total = leek_price * quantity
print(sum_total)

broccoli_price = 2.34
order = "broccoli 1.6"
quantity_index = order.find("1.6")
quantity_broccoli = float(order[quantity_index:quantity_index+3])
total_price = round(quantity_broccoli * broccoli_price, 2)
print(str(quantity_broccoli) + "kg broccoli costs " + str(total_price) + "e")