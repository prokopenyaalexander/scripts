import os
import csv
 
directory = ''

def find_mp3(directory, prefix=""):

    items = os.listdir(directory)
    items.sort()
    folders = []
    files = []
    for item in items:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            folders.append(item)
    
    for folder in folders:
        for filename in os.listdir(os.path.join(directory,folder)):
            f = os.path.join(directory,folder, filename)
            if os.path.isfile(f) and filename.endswith('.mp3'):
                files.append(f)
                
    with open('data.csv', 'w', encoding="utf-8", newline='') as csvfile:
        fieldnames = ['Title']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for element in files:
            writer.writerow({'Title': element})

find_mp3(directory)