import sys
import csv

#Creates a table given a csv file thats been opened for writing
def create_table(csv_file):

    csv_reader = csv.DictReader(csv_file)
    
    table = []

    for line in csv_reader:
        table.append(line)

    return table

#Add a subcategory to a category if it did not exist and add it's spend value to it
def update_subcategory(category, row):

    subcategory_key = row["Subcategory"].strip()

    if len(subcategory_key) != 0:

        if subcategory_key not in category:
            category[subcategory_key] = 0

        category[subcategory_key] = round(category[subcategory_key] + float(row["Spend"]), 2)

#Add a category to the report if it did not exist and update it's sub category's value
def update_category(report, row):

    category_key = row["Category"].strip()

    if len(category_key) != 0:

        if category_key not in report:
            report[category_key] = {}

        update_subcategory(category=report[category_key], row=row)

#"main" function down here

if len(sys.argv) != 2:
    print("Incorrect number of arguments")
    exit()

with open(sys.argv[1], 'r') as csv_file:

    table = create_table(csv_file=csv_file)

    report = {}

    for row in table:
        update_category(report=report, row=row)

    for category_key in report.keys():

        print(category_key)#print the category
        category = report[category_key]

        for subcategory_key in category.keys(): #Print the subcategories of the category with values
            print("\t{:<15}${:.2f}".format(subcategory_key, category[subcategory_key]))

