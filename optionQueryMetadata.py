#option to display salesforce query results
import os
import csv
import datetime
import displayFunctions as d

#Return field names from the query
def returnFieldsNames(sfQuery):
	fieldnames = list()
	for index in sfQuery['records'][0]:
		if index != 'attributes':
			fieldnames.append(index)
	return fieldnames

def displayQuery(opt, sfQuery, soQuery):

    if opt == 1:
    	os.system('cls' if os.name == 'nt' else 'clear')
    	d.terminal(sfQuery,soQuery)
				

    elif opt == 2:
    	d.csvFile(sfQuery,soQuery)
    	os.system('cls' if os.name == 'nt' else 'clear')
		

    elif opt == 3:
    	print "Not defined 3"


    elif opt == 4:
    	d.csvFile(sfQuery,soQuery)
    	d.terminal(sfQuery,soQuery)

    else:
		print "--> Back to main Menu"

def displayMetadata(opt, sf):

	if opt == 1: 
		os.system('cls' if os.name == 'nt' else 'clear')
		d.metadataQuery(sf)


	elif opt == 2:
		os.system('cls' if os.name == 'nt' else 'clear')
		d.objectDescribe(sf)
	
	else:
		print "-->Back to main Menu"