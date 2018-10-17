################################################################################
# PART #1
# https://stackoverflow.com/questions/21107505/word-count-from-a-txt-file-program
################################################################################
   
    # This function should count the words in an unstructured text document
    # Inputs: A file name (string)
    # Outputs: A dictionary with the counts for each word
    # +1 bonus point for removing punctuation from the wordcounts
    
import string

def countWordsUnstructured(filename):
    wordCounts = {}
    file = open(filename).read().split()
    for word in file:
        for mark in string.punctuation:
            word = word.replace(mark, "")
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return wordCounts

# Prof Danielle's solution    
#def countWordsUnstructured(filename):
    #initialize a word count dictionary
#    wordCounts = {}
    #open a file and read it
#    datafile = open(filename).read()
    #open the file and read it
#    data = datafile.split()
    #count the words
#    for word in data:
#        if word in wordCounts:
#            wordCounts[word] = wordCounts[word] + 1
#        else:
#            wordCounts[word] = 1    
    #return the word count dictionary
#    return wordCounts

# Test your part 1 code below.

#bush1989 = countWordsUnstructured("state-of-the-union-corpus-1989-2017/Bush_1989.txt")
#print (bush1989)

################################################################################
# PART 2
# https://stackoverflow.com/questions/3086973/how-do-i-convert-this-list-of-dictionaries-to-a-csv-file
# https://stackabuse.com/reading-and-writing-csv-files-in-python/
# collab with Marissa and Taylor
################################################################################
    # This function should transform a dictionary containing word counts to a
    # CSV file. The first row of the CSV should be a header noting: 
    # Word, Count
    # Inputs: A word count list and a name for the target file
    # Outputs: A new CSV file named targetfile containing the wordcount data

import csv 

def generateSimpleCSV(targetfile, wordCounts): 
    
    #open a file as a csv_file
    with open(targetfile, "w") as csv_file:
                
        #create the csv
        writer = csv.writer(csv_file)
        
        #make the header row
        writer.writerow(['Word', 'Count'])
        
        #transform the word count dictionary to the content of the csv
        for key,value in wordCounts.items():
            writer.writerow([key, value])
            
    #close file
    csv_file.close()
        
    #return the CSV file
    return csv_file
# 
    
# Test your part 2 code below

#generateSimpleCSV('didthiswork', countWordsUnstructured("state-of-the-union-corpus-1989-2017/Bush_1989.txt"))

################################################################################
# PART 3
# https://www.tutorialspoint.com/python/os_listdir.htm
# worked on in class and with Marissa and Taylor
################################################################################
    # This function should create a dictionary of word count dictionaries
    # The dictionary should have one dictionary per file in the directory
    # Each entry in the dictionary should be a word count dictionary
    # Inputs: A directory containing a set of text files
    # Outputs: A dictionary containing a word count dictionary for each
    #          text file in the directory
    
import os
from os import listdir

def countWordsMany(directory): 
    
    #open directory and pull the list of file names
    directory_list = listdir(directory)
    
    #create an empty dictionary for the big dictionary of word count dictionaries
    wordCountDict = {}
        
    #iterate through the entries and create the dictionary containing the other word count dictionaries for each text file entry
    #loop through the list of files
            #for each file, call wordCounts function above for each file
    
    for file in directory_list:
        eachWordCount = countWordsUnstructured(directory + "/" + file)
    
        #place the word count dictionary into the empty dictionary
        wordCountDict[file] = eachWordCount

    #return the big dictionary
    return wordCountDict
    
# Test your part 3 code below

#big_dictionary = countWordsMany('./state-of-the-union-corpus-1989-2017')
#print(big_dictionary)

################################################################################
# PART 4
################################################################################
    # This function should create a CSV containing the word counts generated in
    # part 3 with the header: 
    # Filename, Word, Count
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: A CSV file named targetfile containing the word count data
    
import csv 

def generateDirectoryCSV(wordCounts, targetfile): 
    
    #open a file as a csv_file
    with open(targetfile, "w") as csv_file:
                
        #create the csv
        writer = csv.writer(csv_file)
         
        #make the header row
        writer.writerow(['Filename', 'Word', 'Count'])
        
        #iterate through the word count directory and add to the csv
        for key,value in wordCounts.items():
            writer.writerow([key, value])
            
    #close file
    csv_file.close()
        
    #return the CSV file
    return csv_file
# 
    
# Test your part 4 code below
    
#generateDirectoryCSV(countWordsMany("state-of-the-union-corpus-1989-2017"), 'part4CSV')

################################################################################
# PART 5
#https://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
#https://stackoverflow.com/questions/31728361/append-to-dictionary-file-in-json-python
#worked with Taylor and Marissa and Steven
################################################################################
    # This function should create a JSON containing the word counts generated in
    # part 3. Architect your JSON file such that the hierarchy will allow
    # the user to quickly navigate and compare word counts between files. 
    # Inputs: A word count dictionary and a name for the target file
    # Outputs: An JSON file named targetfile containing the word count data

import json

def generateJSONFile(wordCounts, targetfile): 

    #open a file as a json_file
    with open(targetfile, "w") as json_file:
                
        #transform the word count directory to the content of the json
        json_file.write(str(wordCounts).replace("\'", "\""))

        #close file
        json_file.close()
        
        #return the json file
        return json_file

# Test your part 5 code below

#generateJSONFile(big_dictionary, 'part5file')

################################################################################
# PART 6
#worked with Taylor and Marissa and Jacob
################################################################################
    # This function should search a CSV file from part 4 and find the filename
    # with the largest count of a specified word
    # Inputs: A CSV file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word

import csv 

def searchCSV(csvfile, word):
    
    #set the variables to use later
    largest_count_file = ""
    largest_count = 0
    
    #open the csv file
    with open(csvfile) as csv_file:
        file = csv.reader(csv_file)
    
    #make a loop for finding the file that has the highest count for that word
        for line in file:
            if line[1] == word and int(line[2]) > int(largest_count):
                largest_count = line[2]
                largest_count_file = line[0]
                
    #return the file with the largest wordcounts
    return largest_count_file

    
    #close file
    csv_file.close()

    # This function should search a JSON file from part 5 and find the filename
    # with the largest count of a specified word
    # Inputs: An JSON file to search and a word to search for
    # Outputs: The filename containing the highest count of the target word

import json

def searchJSON(JSONfile, word): 
    
    #set the variables to use later
    largest_count_file = ""
    largest_count = 0
    
    #open the json file
    with open(JSONfile) as json_file:
        data = json.load(json_file)
        
    #make a loop for finding the file that has the highest count for that word
        for file in data:
            if data[file][word] > largest_count:
                largest_count = data[file][word]
                largest_count_file = file
        
    #return the json file with the largest wordcounts
    return largest_count_file
    
    #close file
    json_file.close()
    
# Test your part 6 code to find which file has the highest count of a given word
#print(searchCSV("part4CSV", "on"))
#print(searchJSON("part5file", "on"))

# +1 bonus point for figuring out how many datapoints you had to process to 
# compute this value

################################################################################
# PART 7 - Friday Problem 3
#worked with Taylor and Marissa and Jacob
################################################################################

#import sqlite3

#set up a connection to the database
#conn = sqlite3.connect('presidents_speech.db')
#c = conn.cursor()

#ask the connection to execute a SQL statement
#c.execute('''CREATE TABLE wordCounts (filename, word, counts)''')
#c.execute('''CREATE TABLE presidentInformation (index, number, start, end, president_name, prior_occupation, party, VP)''')

#the tables could be joined on president name or year of their presidency 
# Table 1 - wordCounts
    #text filename
    #text word
    #integer counts
# Table 2 - presidentInformation
    #integer index
    #integer number
    #text start
    #text end
    #text president_name
    #text prior occupation
    #text party
    #text VP
    
#save the changes
#conn.commit()

#close the connection
#conn.close()