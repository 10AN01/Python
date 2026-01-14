import json
#!!!!!!!!!!!!!!! PRACTICE NOT FINISHED !!!!!!!!!!!!!!!!!!
# Menu
# Add books to library (e.g. Aurthor, Title of Book, Genre)
# List of books in library
# Remove books from library
def menu():
    library = Library()
    print("- - - |Library Menu| - - -")
    print("1. Add book")
    print("2. Remove book")
    print("3. Show books already stored.")
    print("4. End Program")
    while True:
        menu_choice = int(input("Enter an option from 1-4: "))
        if menu_choice == 1:
            library.addbook()
        elif menu_choice == 2:
            library.removebook()
        elif menu_choice == 3:
            library.showlist()
        elif menu_choice == 4:
            print()
        




class Library:
    # Sets the list
    def __init__ (self):
        self.books = []
    # Adds books to list/file
    def addbook(self):
        title = input("Input title of book: ")
        author = input("Enter the author: ")
        while True:
            try:
                year = int(input("Enter the year: "))
                break
            except ValueError:
                print("Invalid Year.")
        # Organizes the way it stored.
        #Adds datainputted to the list.
        datainputted = Book(title,author,year)
        data_dict = {
            "Title:":datainputted.title,
            "Author:":datainputted.author,
            "Year Made:":datainputted.year
        }
        
        try:
            # Reads files, loads exisiting data
            with open ("LibraryFile.json" ,"r" ) as f:
                exisitingdata = json.load(f)
                exisitingdata.append(data_dict)
            with open ("LibraryFile.json" ,"w" ) as f:
                json.dump(exisitingdata,f, indent= 4)
                print("Added data to LibraryFile.json!")
                #File not found just 
        except FileNotFoundError,json.JSONDecodeError:
            self.books.append(data_dict)
            with open ("LibraryFile.json" ,"w" ) as f:
                json.dump([data_dict],f, indent= 4)
    def removebook(self):
        try:
            with open ("LibraryFile.json","r" ) as f:
                load = json.load(f)
                counter = 0
                for i in range(self.books):
                    counter =+ 0
                    print(counter)
                    print(f"Title:{self.title} | Author:{self.author} | Year:{self.year}")
                while True:
                    choosebook = input("Enter a book title")
                    if choosebook == self.title:
                        load.remove(choosebook)
                    else:
                        print("Invalid book title")
                        
        except FileNotFoundError, json.JSONDecodeError:
            print("No data / File doesn't exist")
            menu()

class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
        
menu()