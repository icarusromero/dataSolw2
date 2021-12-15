"""Generate sales report showing total melons each salesperson sold."""

#instead of doing two separate lists it would be better to create a dictionary with each salesperson as a key and the melons sold as the value
salespeople = []#declaring empty var
melons_sold = []#declaring empty var

f = open('sales-report.txt')#opening sales report file
for line in f:#loops through each line of file
    line = line.rstrip()#strips whitespace from right side of line and reassigns it
    entries = line.split('|')#splits line at | and saves list to new var

    salesperson = entries[0]#saves value at entries index 0 to salesperson
    melons = int(entries[2])#saves value at entries index 2 as integer to melons

    if salesperson in salespeople:#if statement to be run if value of salesperson is in salespeople
        position = salespeople.index(salesperson)#saves the position of salesperson in salespeople

        melons_sold[position] += melons#adds melons to melons sold at postition
    else:#statement to be run if salesperson is not in salespeople
        salespeople.append(salesperson)#appends salesperson to salespeople
        melons_sold.append(melons)#appends melons to melons_sold

#it would be a good idea to close the file once the code is done with it
for i in range(len(salespeople)):#loops for length of salespeople list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')#prints the name of salesperson at index of i and how many melons they sold in a string
