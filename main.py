import csv
import sys
import pyperclip

class MDTable ():
    def __init__(self, file):
        # csv_file data list
        self.datas = []
        self.new_table = [] 
        # Loading csv_file in to list
        with open(file, newline='') as csvfile:
            csvdata = csv.reader(csvfile)
            for row in csvdata:
                self.datas.append(row)
        # Check csv file format        
        self.check()

    # Check the csv file format is correct
    # List length of each row shall be the same
    def check(self):
        fail_count = 0
        for row in self.datas:
            if len(self.datas[0]) != len(row):
                print("failed in'"+str(row)+"'")
                fail_count += 1
        if fail_count != 0:
            print(str(fail_count)+" wrongs")
            sys.exit()
        return

    # Make the " | --- | --- | --- | --- | --- | " and insert under header
    def mk_sepline(self):
        sepline = ""
        for a in self.datas[0]:
            sepline += "| --- "
        sepline += "|"
        self.new_table.insert(1,sepline)
        return

    # Make the table sting like: " | hostname | CPU | RAM | DISK | OS | "
    def mk_sepword(self):
        for rows in self.datas:
            new_rows = ''
            for word in rows:
                new_rows += "| " + word + " "
            new_rows += "|"
            self.new_table.append(new_rows)
        return

    # Start make Markdown table from csvfile
    def mk(self):
        table_str = ''
        self.mk_sepword()
        self.mk_sepline()
        for row in self.new_table:
            table_str += row + '\n'
        print(table_str)
        pyperclip.copy(table_str)
        print("CSV is converted to Markdown Table, the text is copied on clipboard")
        return

    # for debug
    def debug(self):
        print('hello')
        self.mk_sepword()
        self.mk_sepline()
        for row in self.new_table:
            print(row)

if __name__ == "__main__":
    a = MDTable('domains.csv')
    #a.debug()
    a.mk()