#!/usr/bin/python
import csv
import asynchrone

class CSVReader():
    """docstring for CSVRea."""
    def __init__(self):
        self.asyn = asynchrone.Asynchrone()

    def csv_file_reader(self, arg):
        pass
        reader = csv.DictReader(open(arg))
        result = {}
        for row in reader:
            self.asyn.create_thread(row)
        self.asyn.joiner()
