# Place any necessary imports here
import sqlite3

####################################################
# Part 0
####################################################

# Move your parsers.py file to your Problem Set 7
# directory. Once you've done so, you can use the 
# following code to have access to all of your parsing
# functions. You can access these functions using the 
# parsers.<function name> notation as in: 
# parsers.countWordsUnstructured('./state-of-the-union-corpus-1989-2017/Bush_1989.txt')
import parsers.py

####################################################
# Part 1
# https://teamtreehouse.com/library/adding-multiple-rows-to-a-table
####################################################

    # Write a function that will populate your database
    # with the contents of the word counts and us_presidents.csv
    # to your database. 
    # Inputs: A string containing the filepath to your database,
    #         A word count dictionary containing wordcounts for 
    #         each file in a directory,
    #         A metadata file containing a dictionary of data
    #         extracted from a supplemental file
    # Outputs: None

def populateDatabase(databaseName, wordCounts, metaData):
    INSERT INTO wordCounts(filename, word, counts)
    VALUES ("filename_01", "key_wordCounts_file01", "value_wordCounts_file01"),
            ("filename_02", "key_wordCounts_file02", "value_wordCounts_file02"),
            ("filename_03", "key_wordCounts_file03", "value_wordCounts_file03");
            #continue for all files...
    
    INSERT INTO presidentInformation(index, number, start, end, president_name, prior_occupation, party, VP)
    VALUES ("index_01", "number_01", "start_date_01", "end_date_01", "president_name_01", "prior_occupation_01", "party_01", "VP_01"),
            ("index_02", "number_02", "start_date_02", "end_date_02", "president_name_02", "prior_occupation_02", "party_02", "VP_02"),
            ("index_03", "number_03", "start_date_03", "end_date_03", "president_name_03", "prior_occupation_03", "party_03", "VP_03");
            #continue for all presidents in csv...
            
    return 0

# I don't know how to write the proper code for this problem but I do know how it should work. First, you would use the "INSERT" function to populate the three columns in the wordCounts table. You would then use the "VALUES" function to create the rows in the table, the first containing the filename, the second containing the word, the third being the coordinating word count. 
# The second table would be presidentInformation that would be populated with the various values in the same way the first table was populated. We then don't want to have an output so we say "return 0".
# To test the code you would input the filepath, call the countWordsMany function to add the word count dictionary, and then you would call some function (I don't know what) that would extract the metadata from the CSV file that would be used to populate the second table.

# Test your code here
populateDatabase("./state-of-the-union-corpus-1989-2017", countWordsMany('./state-of-the-union-corpus-1989-2017'), extract_metadata("us_presidents.csv"))


####################################################
# Part 2
# http://www.mysqltutorial.org/python-mysql-query/
####################################################

    # Write a function that will query the database to find the 
    # president whose speech had the largest count of a specified word.
    # Inputs: A database file to search and a word to search for
    # Outputs: The name of the president whose speech contained 
    #          the highest count of the target word
    
from python_mysql_dbconfig import read_db_config
 
def searchDatabase(databaseName, word): 
    
    #set the variables to use later
    largest_count_file = ""
    largest_count = 0
    
    #open the database file 
    dbconfig = read_db_config(databasename)
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    file = cursor.fetchall()
    
    #make a loop for finding the file that has the highest count for that word
    for line in file:
        if line[1] == word and int(line[2]) > int(largest_count):
            largest_count = line[2]
            largest_count_file = line[0]    
                
    #return the file with the largest wordcounts
    return largest_count_file

    #close file
    cursor.close()
    file.close()

# I don't know if this code is 100% correct because I am unable to run the code but I used a combination of code from Part 6 of Parsers and then to open and close the database I found information in the lecture slides and at the link listed below the name of this problem. 
    
    # Write a function that will query the database to find the 
    # average length (number of words) of a speech by presidents
    # of the two major political parties.
    # Inputs: A database file to search and a word to search for
    # Outputs: The average speech length for presidents of each 
    #          of the two major political parties.
    
def computeLengthByParty(databaseName):
        
    #open the database file
    dbconfig = read_db_config(databasename)
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    file = cursor.fetchall()
    
    #create a groupby object to group the presidents by their party and aggregate it to find the average speech length for the party 
    SELECT "party",
    AVG(counts),
    FROM "presidentInformation",
    GROUP BY "party";
    
    #close the file
    cursor.close()
    file.close()

# I don't know if this code is correct but I used the same open/close code as the function above and then created a groupby object and aggregated it to find the average speech length for each party using the sample code in the lecture slides. 