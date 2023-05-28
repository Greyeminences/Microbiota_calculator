import math

price = input("Is the price of the products the same [yes/no]: ")
# print(value)

if price == "yes":
    # table = [
    #     # [product1, product2, product3],
    #     # [price1, price2, price3]
    #     [1, 2, 3],
    #     # [capacity1, capacity2, capacity3]
    #     [50, 100, 500],
    # ]
    # print(table)

    product_name = ["swabs", "extraction_kit", "16S_barcoding_kit",
                    "polymerase", "flonge", "qubit_kit", "qubit_tubes"]
    product_price = [17, 2500, 4200, 4200, 400, 1500, 370] 
    product_capacity = [1, 50, 138, 500, 23, 250, 250]
    samples_number = int(input("How many samples you want to extract: "))
    #print(samples_number)

    # if samples_number <= capacity1:
    #     # result <- (price1 + price2 + price3)*samples_number
    #     result = (table[0][0] + table[0][1] + table[0][2]) * samples_number
    #     result = sum(table[0]) * samples_number
    
    # amount_of_product1 = samples_number / capacity1
    # price_for_product1 = amount_of_product1 * price1

    # if samples_number <= 50:
    #     # do smth
    #     pass
    # elif samples_number <= 100:
    #     # do smth else
    #     pass
    # else:
    #     # do smth else
    #     pass

    total_price = 0
    price_for_products = []
    for index in list(range(len(product_name))):
        product_amount = math.ceil(samples_number / product_capacity[index])        
        #total_price = total_price + product_amount * product_price[index]
        price_for_product = product_amount * product_price[index]
        total_price += price_for_product
        price_for_products.append(price_for_product)

    print("Total price for", samples_number, "samples =", total_price)
    # print(price_for_products)

    for index in list(range(len(product_name))):
        print(product_name[index], "=", price_for_products[index])

# print(result)
