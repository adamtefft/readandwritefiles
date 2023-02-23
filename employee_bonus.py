import csv

infile = csv.reader(open("EmployeePay.csv", "r"))

outfile = open("EmployeeTotal.csv", "w")

for i in infile:
    salary = str(i[3])
    bonus = str(i[4])
    total = salary * bonus
    outfile.write(f"The employee salary is: {salary}")
    outfile.write("\n")
    outfile.write(f"The employee bonus is: {bonus}")
    outfile.write("\n")


outfile.close
