from datetime import datetime
class library:
    def __init__(self,name): #constructor 
         #self.list_books=lista  not used currently
         self.name=name
         self.filepath="books.txt"
         self.dictbook={} #dictionary with key (id)and two values(title, status)
         id=10 #first id in dictbook
         b= open(self.filepath,'r') 
         content = b.readlines() #reading file line by line
         for line in content:
            self.dictbook.update({id:{'books_title':line.replace("\n",""), 'status':'available'}})
            id += 1   
         b.close()
         

    def display_books(self):
        print("Id","\t\t","Title of book") #header
        for key, value in self.dictbook.items():
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")
        print("")
        # for key in self.dictbook:
        #     print(key,self.dictbook.get(key))
    def time(self): 
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return current_time

    def lending(self):
        book_id=input('enter book id: ')
        # now = datetime.now()
        # current_time = now.strftime("%H:%M")
        book_id=int(book_id)
        if book_id in self.dictbook.keys():
            if self.dictbook[book_id]['status']=="available":
                print('this book is available')
                self.dictbook[book_id]['status']="not_available"
                print("Lended ",self.time()," id: ", book_id,"\t",self.dictbook[book_id]['books_title'],"\n")
            else:
                print('already lended','\n')
        else:
            print("There is no book with that ID")
        
    def addbook(self):
        
        new_book=input("Enter title of new book: ")
        if len(new_book)<2 or len(new_book)>20:
            print("We can'\t add your book title")
        else:
            self.dictbook.update({max(self.dictbook)+1:{'books_title':new_book,'status':'available'}})
            b=open(self.filepath,'a')
            b.write(self.dictbook[max(self.dictbook)]['books_title'])
            b.write("\nq")
            b.close()
            print(new_book," was added to your library")
        
    def returnbook(self):
        book_id=input('enter book id: ')
        book_id=int(book_id)
        for key in self.dictbook:
            if key==book_id: 
                self.dictbook[book_id]['status']="available"
                print(book_id," was returned successfully \n")
            else: 
                print("you can't return this book ")

if __name__ == "__main__": #this is main body, running first
    
        #exception handling
    try:
        #lista={"Python Programming for beginners","C++ tutorial","English for IT","Machine Learning","SQL databases","HTML basics",}
        mylib=library("technical")
        choice=False
        print("welcome in ",mylib.name," library")
        print("---------------------------------")
        while not(choice=='q'):
            print("press L for Lend Book")
            print("press R for Return Book")
            print("press D for Display all Books")
            print("press A for Add Book")
            print("press Q for Quit")
            choice=input() #gest choice 
            choice=choice.lower() #converting string to lowercase 

            if choice=='l': #lending book
                mylib.lending()
            elif choice=='r': #returning book
                mylib.returnbook()
            elif choice=='d': # displaying all books
                mylib.display_books()
                #break
            elif choice=='a': #adding book
                mylib.addbook()
            elif choice=='q': # exiting
                break
            else:
                print("try once again \n ")
    except:
        print("something gone wrong")
              
