import sys
import csv

#Creates a table given a csv file thats been opened for writing
def create_table(csv_file):

    csv_reader = csv.DictReader(csv_file)
    
    table = []

    for line in csv_reader:
        table.append(line)

    return table

#Creates a dictionary matching each vendor to a proper category
def get_categories(table):

    categories = {}

    for row in table:
        if len(row["Category"].strip()) != 0: #Striping because of LONDON DRUGS having trailing spaces
            categories[row["Vendor"].strip()] = row["Category"].strip()

    return categories

#Creates a dictionary matching each vendor to a proper subcategory
def get_subcategories(table):

    subcategories = {}

    for row in table:
        if len(row["Subcategory"].strip()) != 0:
            subcategories[row["Vendor"].strip()] = row["Subcategory"].strip()

    return subcategories

#Returns the vendor of a row, for sorting
def get_vendor(row):
    return row["Vendor"]

#Writes a table into a new_file opened for writing
def write_table(new_file, table):

    fieldnames = ['Vendor', 'Category', 'Subcategory', 'Spend']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    for row in table:
        csv_writer.writerow(row)

#"main" function down here

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit()

with open(sys.argv[1], 'r') as csv_file:

    table = create_table(csv_file=csv_file)

    categories = get_categories(table)
    subcategories = get_subcategories(table)
    
    #Update the table with proper subcategories and categories
    for row in table:

        key = row["Vendor"].strip()

        if(key in categories):
            row["Category"] = categories[row["Vendor"].strip()]

        if(key in subcategories):
            row["Subcategory"] = subcategories[row["Vendor"].strip()]

    table.sort(key=get_vendor)

    with open('sorted_' + sys.argv[1], 'w') as new_file:
        write_table(new_file=new_file, table=table)
