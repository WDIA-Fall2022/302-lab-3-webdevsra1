import pylightxl as xl

with open('city.xlsx', 'rb') as f:
    db = xl.readxl(f)

country_code = list(db.ws(ws='Sheet1').col(col=3))

countries = list(db.ws(ws='Sheet1').col(col=4))

# ask the user for the code of the country and save it into a variable

counter = 0
country_looking_for = input("Please Enter a Country Code: ")
indexOfCountry = 0;
country_code_found = ''
# Scan the list l line by line and add 1 to the counter if the country is the one looked for
for country in country_code:
    if country == country_looking_for:
        indexOfCountry = country_code.index(country_looking_for)
        counter = counter + 1
        country_code_found = countries[indexOfCountry]

if (country_code_found != ""):

    # Format and print the result
    print("The country of {} is {} and it is {} times in the list".format(country_looking_for, country_code_found,
                                                                          counter))

else:
    print("ERROR:Enter a valid country code")

# Ask the user for the population looked for. Use a loop and a try except to validate the input as a valid integer

while True:
    try:
        num = int(input("\nEnter a population: "))
    except ValueError:
        print("Please enter a valid integer")
        continue
    else:
        print(f'You entered: {num}')
        break

# Store the population values into a list called l1 (see line 6)
l1 = list(db.ws(ws='Sheet1').col(col=5))

# Initialize a list lstOfRecords to an empty list
list_of_records = []

# Scan the list l1, if the population is larger than the population looked for, add the list index to lstOfRecords
for index, population_in_list in enumerate(l1):
    if population_in_list > num:
        list_of_records.append(index)

print("\nlist of records", list_of_records)

# Print the list l1
print("\nList of population is: ", l1)

# Bonus: Print the name of the cities whose index is in l1
cityList = list(db.ws(ws='Sheet1').col(col=2))
print("\nCities Whose Index is in l1 are :\n")
for index, population_in_list in enumerate(l1):
    print(cityList[index])