#author : saisuresh mv 

budget = float(input("Enter Your budget : "))
cart = {}
while True:
    try:
        choice = int(input("\n1.Add an item\n2.Exit\nEnter your choice : "))
        if choice == 2:
            break
        if choice > 2:
            print("\nInvalid choice, pls choose valid choice")
            continue
        product = input("\nEnter product : ").strip()
    
        qty,kg = input("Enter quantity : ").split()
        qty = float(qty)
    
        price = float(input("Enter Price : "))
    
    
        if(budget-price < 0):
            print("\nCan't Buy the product, because budget left is %.2f"%budget)
        else:
            budget -= price
            print("\nAmount left : %.2f"%budget)
            cart.setdefault(product,[0,0])
            cart[product][0] += qty
            cart[product][1] += price
    except:
        print("\nPls enter valid details")

buy_further = []
for i in cart:
    if budget >= (cart[i][1]/cart[i][0]):
        buy_further.append(i)
if buy_further != []:
    print("\nAmount left can buy you atleast 1kg in any one of these",end = '')
    for i in  range(len(buy_further)):
        if i == len(buy_further)-1:
            print(" %s."%buy_further[i],end = '')
        else:
            print(" %s,"%buy_further[i],end = '')
#print(cart)
print("\n\nGROCERY LIST is: \n")
table_head = ["product name","quantity","price"]
print("{: >20} {: >20} {: >20}\n".format(*table_head))
for i in cart:
    data = [i,cart[i][0],cart[i][1]]
    print("{: >20} {: >20} {: >20}".format(*data))



        