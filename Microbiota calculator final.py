#!/usr/bin/env python3
import math

price = input("Is the price of the products the same [yes/no]: ")
# print(value)

if price == "yes":
   
    product_name = ["swabs", "extraction_kit", "16S_barcoding_kit",
                    "polymerase", "flonge", "qubit_kit", "qubit_tubes"]
    product_price = [17, 2500, 4200, 4200, 400, 1500, 370] 
    product_capacity = [1, 50, 138, 500, 23, 250, 250]
    
    print("Uploded prices as follow:")
    for index in list(range(len(product_name))):
        print(product_name[index], "=", product_price[index], "PLN, capacity (", product_capacity[index], "samples )")

    samples_number = int(input("How many samples you want to extract: "))
  

    total_price = 0
    price_for_products = []
    for index in list(range(len(product_name))):
        product_amount = math.ceil(samples_number / product_capacity[index])        
        price_for_product = product_amount * product_price[index]
        total_price += price_for_product
        price_for_products.append(price_for_product)

 
    for index in list(range(len(product_name))):
        print(product_name[index], "=", price_for_products[index], "PLN")

    print("Total price for", samples_number, "samples =", total_price, "PLN")

