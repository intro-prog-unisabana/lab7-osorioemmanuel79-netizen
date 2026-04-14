import csv

def encrypt_passwords_in_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            print(row)