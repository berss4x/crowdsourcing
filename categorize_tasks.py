# Author :  Erick Garcia
# Project: Crowdsourcing Research

import re  
import csv
from sys import argv


#Text to examine
lines = [line.rstrip('\n') for line in open('textoprox.txt')]

#Main skills
skillDetec = ['Data Handling', 'Analysing','Speaking', 'Writting'] 

#Tasks of each skill
tasks = [
    ['classify','classifying','categorize','categorizing','category','identify','class','extract','items'],#Data Holding
    ['summarising','summarize','summary'],                                                                  #Analysing
    ['talk','microphone','speech','record','accent','intonation','whisper','voice','recording'],            #Speaking
    ['writing','write','listen','describe','description','tell','your opinions','answer']                  #Wrting
]



with open('taskscategorized.csv', 'w') as csvfile:
    fieldnames = ['task', 'category']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for c, categoryTask in enumerate(tasks):
        for line in lines:
            for task in tasks[c]:
                if task in line:
                    print line + skillDetec[c] # Just to set in command line the result
                    writer.writerow({'task': line, 'category': skillDetec[c]}) #saves in a csv file
                    break #It gets whith the first match found
                    
                    





