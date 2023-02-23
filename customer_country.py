import csv

# infile = csv.reader(open("customers.csv"))

infile = csv.reader(open("customers.csv", "r"))

outfile = open("customer_country.csv", "w")


for i in infile:
    outfile.write(str(i[1]))
    outfile.write(" ")
    outfile.write(str(i[2]))
    outfile.write(", ")
    outfile.write(str(i[4]))
    outfile.write("\n")

outfile.close()
