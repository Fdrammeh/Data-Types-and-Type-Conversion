item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "4.99"
item3_qty = "1"

tax_rate = "0.075" 



item1_price = float(item1_price)
item1_qty = float(item1_qty)

item2_price = float(item2_price)
item2_qty = float(item2_qty)

item3_price = float(item3_price)
item3_qty = float(item3_qty)

tax_rate =float(tax_rate)

item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty



subtotal = item1_total + item2_total + item3_total
tax_amount = subtotal * tax_rate
grand_total = subtotal + tax_amount

print(f"item: {item1_name}")
print(f"price: ${item1_price} *{item1_qty} = {item1_total}")

print(f"tax ({tax_rate * 100}%): ${tax_amount:.2f}")

print("=" * 40)

print(f"item: {item2_name}")
print(f"price: ${item2_price} *{item2_qty} = {item2_total}")

print(f"tax ({tax_rate * 100}%): ${tax_amount:.2f}")

print("=" * 40)

print(f"item: {item3_name}")
print(f"price: ${item3_price} *{item3_qty} = {item3_total}")
print(f"subtotal: ${subtotal:.2f}")
print(f"tax ({tax_rate * 100}%): ${tax_amount:.2f}")
