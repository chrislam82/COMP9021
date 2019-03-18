# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
# 
# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
import gzip


filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None # Im assuming this means that if there is no value for indicators,return None. Yep, see below, lec already wrote own thing
countries_for_max_value_per_year = {} # Basically wants a dictionary

with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile) # file is a csv.reader object so use csv module to access
    # Ok, so i can iterate through file without overflowing
    # What we want to do is skip the first row, actually the indicator will never be in there, so we should be fine
    # type(cells) --> str
    # can be both float and int form
    # Empty cells are saved as an empty string ('') # can see by printing rows
    temp_value_store = 0 # for storing converted values
    for data_row in file:
        if indicator_of_interest in data_row[2:3]: # by doing so, i can check only element 2 in list, and only the whole name of indicator
            for data_col in range(4, len(data_row)): # checking all years starting in element 4 in list
                try: # testing if value is an int
                    temp_value_store = int(data_row[data_col])
                except:
                    pass # if not int, then move to 2nd try
                try: # testing if value is a float
                    temp_value_store = float(data_row[data_col])
                except:
                    continue # If neither, then nothing happens, continue will move to next loop
                
                if max_value == None: # initialise max_value for comp if indicator is found
                    max_value = 0
#                print (data_col)

                current_year = data_col + first_year - 4
                if temp_value_store == max_value: # then append based on yr to dictionary
                    if current_year in countries_for_max_value_per_year:
                        countries_for_max_value_per_year[data_col + first_year - 4].append(data_row[0]) # could just have another if statement instead
                    else:
                        countries_for_max_value_per_year[current_year] = [data_row[0]] # key = 1960 + col no. - 4 to adjust for cols starting at 4 and assign value to countryname for row
                elif temp_value_store > max_value:
                    countries_for_max_value_per_year = {} # reassign to an new empty dict
                    max_value = temp_value_store # assign max_value to new value
                    countries_for_max_value_per_year[current_year] = [data_row[0]] # key = 1960 + col no. - 4 to adjust for cols starting at 4 and assign value to countryname for row
                    print ("new country added. year==", str(current_year))


















if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value) # We'd just be storing this and changing or evaluating at end
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                                  for year in sorted(countries_for_max_value_per_year)
                   )
         )

# So here, it is clear that countries for max value per year is a dictionary
    # Question is, what are the keys and what are the values?
    # year is the key, countries are the values which are stored as a list

# So how do we access the csv file object, read lines

# How do we process the data in the .csv file
    # Lets look at how indicator names are stored inside
    # The Question asks for maxium value, so could store in there
    # Could store, then compare
    # if larger value found, then clear dictionary and replace values
    # update



'''
# ---------------------------- Edge Cases ----------------------------
same number of decminal places as file: # no need to deal with, just allow default formatting
Eric --> That value is the string in the file is converted to an int if possible, or to a float otherwise; no need to fiddle around with the resulting value.
    # something to do with storing as int vs float (i think store in whatever format the int is stored in) (or maybe its stored as a str, not sure)
Eric --> Rows with empty data are ignored

Limiting factors:
    row length
    mixed data types in row
    run-time stress test
    ordering (specific to lexicographic order)
    Empty rows, country data with no col, row that is completely empty ([])
    empty lines
    empty cells

30 secs/test is the runtime limit
    # remember, my laptop is slower than erics, so i might run slower, but better to err on the safe side







'''













