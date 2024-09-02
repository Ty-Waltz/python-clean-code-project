# Library Management System (Now connected to SQL!)
## How it works:
1. Running the code for the first time will bring you to a menu, here you will see 4 options (Book Operation, User Operations, Author Operations, and Quit)
   -Book Operations will bring you to another menu with all the "book" operations  
    Book Operations:  
        1. Add a new book - This will ask you for a title, genre, author, and publication date for the book you would like to add, then it will add your book to the list of books in the library.  
        2. Borrow a book - This will ask you for a library ID then the book title you would like to borrow. If a valid title was chosen, it will add the book to your "borrowed books".  
        3. Return a book - This will also ask for your ID and title of books but this time it will check if the book is in your "borrowed books" and move it back onto the library selection.  
        4. Search for a book - This will ask for a title of a book, if it is found in the library, it will give you the details. If not, it will simply say "Book not found".  
        5. Display all books - This function will show all the books in the library currently.  
   -User Operations will bring you to the "User Operations" menu  
    User Operations:  
        1. Add a new user - This operation will ask you for a name and a Library ID to create, then add them to the data-base.  
        2. View user details - This operation will ask for a valid library ID then give you the deatails of the user or, if not found, will tell you "User not found".  
        3. Display all users - This operations will display all users currently in the data-base.  
   -Author Operations will bring you to the "Author Operations" menu  
   Author Operations:  
        1. Add a new author - This will ask for the name of the author you would like to add and a description of the author. Once complete, it will tell you the author was added successfully.  
        2. View author details - This will ask for the name of the authorfetch the details about the author. If not found, it will display the message "Author not found".  
        3. Display all authors - This operation will display all authors currently in the data-base.
   
### Class Book  
This class is used for all the book functions used in the main code. This is what will return all the info of the books like title, author, genre, publication date, and wether the book is borrowed or avalible.  
### Class User  
This class will set the user ID and name, as well as transfer borrowed books to said user and back to the library
### Class Author  
This class is how the author's name and description is put into the data-base
### utils.py  
This has the function "validate input" which will make sure all inputs are correct and inputted properly  

### How to Export and Use the Library Management System on a Local Device:
To use the Library Management System on a local device, follow these steps:  

Download the Code:  
1 .If the code is in a GitHub repository, you can clone the repository to your local machine using Git or download the code as a ZIP file and extract it.  
2. Ensure you have Python installed on your local device. You can download Python from python.org.  
3. Open a terminal or command prompt and navigate to the directory where the code is located.  

Run the Code:  
1. In the terminal, run the Python script by typing python <script_name>.py (replace <script_name> with the actual name of your main script, e.g., library_management.py).
2. Follow the on-screen instructions to interact with the Library Management System. Use the menus to perform book, user, and author operations.


