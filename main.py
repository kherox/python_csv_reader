#!/usr/bin/python
import getopt
import sys
import threading
import csv_reader

#test list
pars_line = {"-i","--ifile"}
#valide extension
extension = {"csv","xml"}
#Parsing Command line
inputfile = "default"

"""Permet de parser le fichier csv et de le rendre comprenhensible"""

def main():
    reload(sys)
    sys.setdefaultencoding('utf8')
    reader = csv_reader.CSVReader()
    #test if parsing opts
    find = False
    #recuperation de l'a line d'argument
    argv = sys.argv[1:]
    try:
        opts,args = getopt.getopt(argv,"hi:o:",['ifile='])
    except getopt.GetoptError as e:
        print("usage : python  main.py -i filename")
        sys.exit(2)

    reader.csv_file_reader("file.csv")

    # for opt,arg  in opts:
    #     if opt in pars_line:
    #         inputfile = arg
    #         find = True
    # if not  find:
    #     sys.exit(2)
    #get extension
    # split_list = inputfile.split(".")
    # length = len(split_list)
    # ext = split_list[length-1]
    # if ext in extension:
    #      fcn =  str(ext)
    #      if fcn == "csv":
    #          print("Avant append")
    #          csv_reader.csv_file_reader(inputfile)

if __name__ == '__main__':
    main()
