'''Name: Karm Patel
    student id:041008617
    Assignment 1'''
#import the csv api library
import csv
"""first with open line is used to open the csv file
   second there is the try loop for exception handling
    in the third line i have created a read variable and csv.reader method is used
    then i have printed file is open if the file is open and except is fired when the file does not exist
    and the last print is for the name of the author"""
    #print doc string for csv api
print(csv.__doc__)
with open('data.csv', 'r') as object:
    print(open.__doc__)
    print(object.__doc__)
    #the method in here is used to create a new_csv file but with space
    '''with open('new_csv','w') as newobject
        csvwriter = csv.writer(new_csv, delimiter='\t')
        print(csv.delimiter.__doc__)
        for list in read
            csvwriter.writerow(list)
            print(csv.writerow.__doc__)'''
    try:
        
        read = csv.reader(object)
        print(read.__doc__)
        print("file is open")
        print("Karm Patel")
       
    except FileNotFoundError or Exception:
        print("file does not found")
    """first i have initialize a variable
    then i have created a for loop to print the line 
    then there is a print statment to print the line
    then i have created a loop for limited number of rows to display"""
    
    loopforfile = 0
    print(loopforfile.__doc__)
    for list in read:
            print(list)
        
            """and for the if loop when the loop is greater than or equal to the given value it will break """
            
            if(loopforfile >= 5):
                break
            loopforfile +=1
#file io operation close the file
'''file is closed'''
object.close()
print(object.close.__doc__)