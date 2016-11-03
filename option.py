# -*- coding: utf-8 -*-
#import analyzer.header as o
#from sfapi.simple_salesforce import Salesforce
import analyzer.report as r
from simple_salesforce import Salesforce
import optionQueryMetadata as oQM
import getpass
import sys
import os
import io
import time


def switch(opt, sf, file):

    if opt == 3:
      #print sf.Contact.metadata()
      if sf != None:
        print "Choose how you would like to see the results:"
        print "------------------------"
        print "      Menu-Metadata     "
        print "(1) To display Objects List by Terminal"
        print "(2) To show Fields of an Object by Terminal"
        #print "(3) Create file with object description"
        #print "(4) Terminal + csv file"
        print "(5) Return Main Menu"
        print "------------------------"
        optQM = raw_input("Enter your option:")
        if optQM.isdigit(): 
          optQM = int(optQM)
          oQM.displayMetadata(optQM,sf)#Call the function displayQuery on optionQuery file          
      else:
          os.system('cls' if os.name == 'nt' else 'clear')
          print "-->Please first login into Salesforce option (1)"
          raw_input("Press Enter to continue...")      

      """print sf.CampaignFeed.describe()
      sf.describe()

      for x in sf.describe()["sobjects"]:
        print x["label"]"""
  
    elif opt == 4:
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
       #usernameT=
        passwordT=getpass.getpass("Please insert password: ")
        #passwordT=
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
            sfQuery = sf.query_all(soQuery)
            os.system('cls' if os.name == 'nt' else 'clear')
            if sfQuery[0]['errorCode'] == 'MALFORMED_QUERY':# It is a bad  condition to  force the result
                print "Error. Malforformed SOQL Query. Error message: "+ sfQuery[0]['message']
                print "Please type a proper query"
            else:
                print "Query has retrieved successfully the results. Choose how you would like to see the results:"
                print "------------------------"
                print "       Menu-Query       "
                print "(1) Terminal"
                print "(2) Create a csv file on the path " + str(sys.path[0])
                print "(3) Web Browser"
                print "(4) Terminal + csv file"
                print "(5) Return Main Menu"

                print "------------------------"
                optQM = raw_input("Enter your option:")
                if optQM.isdigit(): 
                  optQM = int(optQM)
                  oQM.displayQuery(optQM, sfQuery, soQuery)#Call the function displayQuery on optionQuery file
                else:
                  raw_input("It is not a valid number. Press Enter to continue...")   
          else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print "-->Please first login into Salesforce option (1)"
            raw_input("Press Enter to continue...")

    else:
      print "Exit............"
      raise SystemExit
