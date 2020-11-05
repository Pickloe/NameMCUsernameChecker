#Requests is a library that lets you make HTTP requests to websites.
import requests
#BeautifulSoup is a library that helps with parsing specific text from the source code of a website.
from bs4 import BeautifulSoup
#Ctypes is being used to change the title of the CMD.
import ctypes

#We are setting these containers to hold the value of 0 and when we use "available += 1" in a line, it will add 1 to that container and we add that to the title
available = 0
unavailable = 0
availableLater = 0
tooLong = 0

#This is how we set the title
ctypes.windll.kernel32.SetConsoleTitleW(f"Minecraft Username Checker | By Pickloe")

#Made these two functions to save the text that are "Available" or "Available Later". Whatever text I send to the function will be saved.
def availL(text):
    with open('Available Later.txt', 'a+') as outputfile:
        outputfile.write(text + '\n')
        outputfile.close()

def avail(text):
    with open('Available.txt', 'a+') as outputfile:
        outputfile.write(text + '\n')
        outputfile.close()

#This will open the file called "users.txt" and 'r' stands for read and we are defining it as f
with open('users.txt', 'r') as f:
    #We are creating a loop to loop through each line
    for users in f:
        #As you can tell here I'm replacing \n (Which means new line) with nothing because when I wuold print the username and additional text it would print the name then go to next line then print unavailable.
        user = users.replace('\n','')

        #We are making a request to the website and doing "+ user" is saying to addon "user" to that URL | EXAMPLE URL: https://namemc.com/search?q=Steve
        a = requests.get(url='https://namemc.com/search?q=' + user)

        #I'm making if statements to find if certain text is inside the source code of the variable a which is where we made our HTTP request.

        if '<div>Unavailable</div>' in a.text:
            print(user + " | Unavailable")
            #Adds 1 to the container we made earlier.
            unavailable += 1
        elif '<div>Available Later*</div>' in a.text:
            #We are making it so we can parse specific data from the source code of the HTTP request we made earlier.
            soup = BeautifulSoup(a.text, "html.parser")
            #Finds anything with the tag <time> and grabs specifically 'datetime' text.
            time = soup.find("time")['datetime']
            print(user + " | Available @ " + time)
            #This will go straight to the function we made earlier with specific text to save
            availL(user + " | " + time)
            #Adds 1 to the container we made earlier.
            availableLater += 1
        elif '<div>Too Long</div>' in a.text:
            print(user + " | Exceeded Character Limit")
            #Adds 1 to the container we made earlier.
            tooLong += 1
        elif '<div>Available*</div>' in a.text:
            print(user + " | Available")
            #Adds 1 to the container we made earlier.
            available += 1
            #This will go straight to the function we made earlier with specific text to save
            avail(user)
        ctypes.windll.kernel32.SetConsoleTitleW(f"Minecraft Username Checker | Available: {str(available)} | Available Later: {str(availableLater)} | Unavailable: {str(unavailable)} | Too long: {str(tooLong)}")
