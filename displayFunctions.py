import os
import csv
import datetime
import time

#Return field names from the query
def returnFieldsNames(sfQuery):
	fieldnames = list()
	for index in sfQuery['records'][0]:
		if index != 'attributes':
			fieldnames.append(index)
	return fieldnames

#Dipslay results by terminal screen
def terminal(sfQuery, soQuery):
    os.system('cls' if os.name == 'nt' else 'clear')
    print " Query '" + soQuery + "' results: "
    time.sleep(2)
    for i in range(0,sfQuery['totalSize']-1):
        for index in sfQuery['records'][i]:
        	if index != 'attributes':
    			print '|'+ index+ '|:',
    			print sfQuery['records'][i][index]
    			
    	print ""
    raw_input("Press Enter to continue...")

#Create a csv file
def csvFile(sfQuery, soQuery):
	dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#file name created concatenating datetime + query
	filename = (dateTime.strip() + soQuery.strip()).replace(" ","") + ".csv"
	print "------------------------"
	print "-->Csv created: "+ filename
	print "------------------------"
	time.sleep(3)
	#Modify according our values
	with open(filename, 'w') as csvfile:
	 	fieldnames = returnFieldsNames(sfQuery)
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader() #Write csv headers
		rowQuery = {}
		for i in range(0,sfQuery['totalSize']-1):
			for index in sfQuery['records'][i]:
				if index != 'attributes': #avoiding attributes index from the obtanied json
					rowQuery.update({index:sfQuery['records'][i][index]})
			writer.writerow(rowQuery)
	raw_input("Press Enter to continue...")		