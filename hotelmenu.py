menu={
        'pizza':250,'burger':50,'momo':50,'noodles':40,'salad':70,'pasta':130,
        'pepsi':40,'coca-cola':40,'red bull':50,'sprite':40,'mountain dew':40,'fanta':40,'monster':60,'lipton':40,
        'apple moscow mule':250,'thanksgiving mule':50,'cranberry lime':50,'cranberry basil sangria':40,'sparking mocktail':70,'black current mojito':130,
        'chocolate':60,'mango':40,'black current':50,'ice popsicle':40,'kulfi':30,'frozen yogurt':140,'snow cream':160,'soft serve':60
    }
#greet......
print("Welcome to our titance restaurant")
print("menu")
print("fastfood...\ncold drinks..\nmocktails.....\nice creams....\n")

order_total = 0
item_1 =input("enter the first order")
#using membership operator
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"order item {item_1} is not available yet!")

another_order = input("do you want to add another item....(yes/no)")
if another_order =="yes":
    item_2 =input("enter the second order")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"item {item_2} is not available yet!")
print(f"the total amount of order to pay is { order_total}")            

