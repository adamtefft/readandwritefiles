import csv

infile = csv.reader(open("sales.csv"))
next(infile)
outfile = open("salesreport.csv", "w")

customer_ID = '250'
cust_total = 0

outfile.write("ID   |  Total\n")

for i in infile:
    if customer_ID != i[0]:
        outfile.write(customer_ID + "\t\t" + str("%.2f" % cust_total) + "\n")
        # outfile.write(str(cust_total))

        customer_ID = i[0]
        cust_total = 0

    total = float(i[3]) + float(i[4]) + float(i[5])
    cust_total += total

outfile.write(customer_ID + "\t\t" + str("%.2f" % cust_total) + "\n")

outfile.close()
