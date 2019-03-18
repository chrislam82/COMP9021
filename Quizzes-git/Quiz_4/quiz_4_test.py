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
    for data_row in file:
        if indicator_of_interest in data_row: # make it specifically row with indicator name, else lecturer may pass in name of a country and cause a false +
            for data_col in range (something, len(data_row)):
                if data_col == max_value:
                    countries_for_max_value_per_year[whatever year].append(data_row[whatever col country name is in])
                elif:
                    data_col > max_value:
                    countries_for_max_value_per_year = {} # reassign to a new dict
                    max_value = data_col # reassign max_value to the new max value
                    countries_for_max_value_per_year[some kind of year calc].append(data_row[whatever col country name is in])

            # Run for comparison on list # different conditions
                # range = (start of 1960, 1960 + number_of_years) # make sure it doesnt overflow

            # Run comparison, else it will just skip row
            # if greater, write year and store

#    print (next(file))
# So each row is stored in lists with each cell an element of the list

# for each row, if indicator_of_interest in data_row:
    # then that row has indicator
# Access 

#



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





