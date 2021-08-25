def get_bill(to_pens):
    if purchase_item<=5:
        total_cost=purchase_item*10
        gst=(2/100)*total_cost
        final_cost=total_cost+gst
        print(f"Price of {purchase_item} pen : ",total_cost)
        print("GST included : ",gst)
        print(f"Total cost of {purchase_item} pen is : ",final_cost)
    elif purchase_item>5 and purchase_item<=10:
        total_cost=purchase_item*9
        gst=float((3/100)*total_cost)
        final_cost=total_cost+gst
        print(f"Price of {purchase_item} item is : ", total_cost)
        print(f"GST included of {purchase_item} item is : ", gst)
        print(f"Total cost of {purchase_item} item is : ", final_cost)
    elif purchase_item>10 and purchase_item<=50:
        total_cost = purchase_item*7
        gst = float((6 / 100) * total_cost)
        final_cost = total_cost + gst
        print(f"Price of {purchase_item} item: ", total_cost)
        print(f"GST included of {purchase_item} item : ", gst)
        print(f"Total cost of {purchase_item} item : ", final_cost)
    else:
        total_cost = purchase_item*6
        gst = (5 / 100) * total_cost
        final_cost = total_cost + gst
        print(f"Price of {purchase_item} item is : ", total_cost)
        print(f"GST included of {purchase_item} item is : ", gst)
        print(f"Total cost of {purchase_item} item is : ", final_cost)

purchase_item=int(input("Enter the pens : "))
get_bill(purchase_item)

