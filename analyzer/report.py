# -*- coding: utf-8 -*-
import headers as h
import reportfile as r
import csv

#line_count_field
#change_separator


def fields_checker(line,headerCount,lineNum):
    lineCount = h.line_count_field(line)
    errorCounter = 0
    string = []

    if headerCount > lineCount:
        errorCounter += 1
        string = "Linea " + lineNum + " less fields than headers"

    elif headerCount < lineCount:
        errorCounter += 1
        string = "Linea" + lineNum + " more fields than headers"
# Check again errorCounter cannot be populate to the file from this fucntion
# Line how it will be write to the file??



def load_file(path):
    f = open(path, 'r')
    lineNum = 1
    headerCount = 0
    headerCount = h.line_count_field(f.readline(),",")

    for line in f:
        fields_checker(line, headerCount, lineNum)
        lineNum += lineNum

    f.close()

def load_file_pro(path):
    reader = csv.reader(open(path, 'rb'))

    for index,row in enumerate(reader):
        if  index == 0:
            header = row
        else:
            print 'Row: ' + str(index + 1)
            print '------------'
            i = 0
            for  rowC in row:
                if i+1 ==  len (row):
                    print header[i] + ': ' + rowC
                else:
                     print header[i] + ': ' + rowC + ', : '
            print '\n'