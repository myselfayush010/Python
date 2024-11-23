print("Hello, welcome to our creative store")
creative_store_product = ['ram', 'mouse', 'ssd', 'display', 'cpu', 'gpu', 'motherboard']
print(creative_store_product)  # This line helps verify the list
user_demand = input("What do you want? ").lower()
if user_demand in creative_store_product:
    print(f"Yes, we have {user_demand} in stock.")
else:
    print(f"Sorry, we don't have {user_demand} right now.")