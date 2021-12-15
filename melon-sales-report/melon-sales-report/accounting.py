def dorky_line():# declares function
    print("*" * 80)#prints a line of 80 asteriks

dorky_line()#calls dorky line func
ord_by_type = open("orders-by-type.txt")#opens orders by type file
melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}#creates dictionary with keys being melon types and values being the number melons and initially set to 0

for line in ord_by_type:#loops through each line of opened file
    data = line.split("|")#splits line at | and saves list to data var
    melon_type = data[1]#saves item at index 1 of data to melon type
    melon_count = int(data[2])#saves item at index 2 of data to melon count
    melon_tallies[melon_type] += melon_count#adds melon count to value of melon tallies according to melon type

ord_by_type.close()#closes order by type file

melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }#creates dictionary with key values being melon types and values being their prices
total_revenue = 0#declares total revenue var and sets its initial value to 0

for melon_type in melon_tallies:#loops through melon tallies dictionary with each key value pair being melon type
    price = melon_prices[melon_type]#gets price of melon type and saves it to price
    revenue = price * melon_tallies[melon_type]#multiplies price by amount of melon type and saves it to revenue
    total_revenue += revenue#adds the revenue for melon type to total revenue
    # print("We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue))
    print(f"We sold {melon_tallies[melon_type]} {melon_type} melons at {price:.2f} each for a total of {revenue:.2f}")

dorky_line()#calls dorky line func
ord_w_sales = open("orders-with-sales.txt")#opens orders with sales file
internet_rev = 0#declares internet revenue with initial value of 0
sales_ppl_rev = 0#declares sales ppl revenue with initial value of 0

for line in ord_w_sales:#loops through open file by line
    data = line.split("|")#splits line into list and saves it to data
    if data[1] == "0":#if statement to read if item at index 1 of data equals 0
        internet_rev += float(data[3])#adds item at index 3 of data to internet revenue as a float
    else:#else statement to read
        sales_ppl_rev += float(data[3])#adds item at index 3 of data to sales ppl revenue as a float

ord_w_sales.close()#closes order with sales file

print(f"Internet sales generated ${internet_rev:.2f} in revenue.")#prints stirng with internet revenue
print(f"Salespeople generated ${sales_ppl_rev:.2f} in revenue.")#prints string with sales ppl revenue

if sales_ppl_rev > internet_rev:# if statement to be run if sales ppl rev is greater than internet rev
    print("Guess there's some value to those salespeople after all.")#prints string
else:#else statement to be run
    print("Time to fire the sales team! Online sales rule all!")#prints string

dorky_line()#calls dorky line func
