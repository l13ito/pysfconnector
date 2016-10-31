# -*- coding: utf-8 -*-
#import analyzer.header as o
#from sfapi.simple_salesforce import Salesforce
import analyzer.report as r
from simple_salesforce import Salesforce
import optionQuery as oQ
import getpass
import sys
import os
import io
import time


def switch(opt, sf, file):
  
    if opt == 4:
      #
      pathFile = '/home/casa/workspace/pycsva/pycsva/test'
      #if not file:
        #print "There is not file, please load again the script. "  
      #r.load_file(pathFile) # Read CVS
      print "Not available"

    elif opt == 5:
        #Display CVS future file it ll be take it by argc. file
        pathFile = '/home/casa/workspace/pycsva/pycsva/test'#Test path
        r.load_file_pro(pathFile)

    elif opt == 1:
        usernameT=raw_input("Please insert username: ")
        #usernameT = "Insert your user name"
        passwordT=getpass.getpass("Please insert password: ")
        #passwordT = "Insert your password"
        sf = Salesforce (usernameT,passwordT,'')# No token required
        return sf
        #Need to check if login was worng
      
    elif opt == 6:
      
      with io.open(filename,'r',encoding='utf8') as f:
        text = f.read()
      # process Unicode text
      with io.open(filename,'w',encoding='utf8') as f:
        f.write(text)

      print "-->The file" + file + " has been converted successfully to UTF-8"


    elif opt == 2:
          if sf != None:
            soQuery = raw_input("Please type your SOQL query:")
            #soQuery = 'Select Id, Email FROM Contact'
            sfQuery = sf.query(soQuery)
            os.system('cls' if os.name == 'nt' else 'clear')
            print "Here you have the ----->" + sfQuery[0]['errorCode']

            if sfQuery[0]['errorCode'] == 'MALFORMED_QUERY':# It is a bad  condition to  force the result
                print "Error. Malforformed SOQL Query. Error message: "+ sfQuery[0]['message']
                print "Please type a proper query"
            else:
                print "Query has retrieved successfully the results. Choose how you would like to see the results:"
                print "------------------------"
                print "(1) Terminal"
                print "(2) Create a csv file on the path " + str(sys.path[0])
                print "(3) Web Browser"
                print "(4) Terminal + csv file"
                print "(5) Exit"

                print "------------------------"
                outputQuery = raw_input("Enter your option:")
                if outputQuery.isdigit(): 
                  outputQuery = int(outputQuery)
                  oQ.displayQuery(outputQuery, sfQuery, soQuery)#Call the function displayQuery on optionQuery file
                else:
                  raw_input("It is not a valid number. Press Enter to continue...")   
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print "-->Please first login into Salesforce option (1)"
            raw_input("Press Enter to continue...")

    else:
      print "Exit............"
      raise SystemExit
