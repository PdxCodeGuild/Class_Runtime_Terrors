## Explanation of the project

The project is structured as follows:

- The folder 'Accounts' containes all the logic to manage users account creation, log in and log out

- The folder book_app contains all the library logic:

1. First you add an author in the system.
2. Then you create a book linked to that author.
3. After, a registered user can borrow a book and return it.
4. Once a book is borrowed, the general availability of that book is decreased. 

- There are 3 models:

1. Author: This model allows you to add an author from the list of authors in the system
2. Book: This models has a `Many to One` relationship with the Author model. Also, if you delete a book the author instance does not get deleted.
3. LandBook : This is for user management. Associates a registered user to the book borrowed and includes a timestamp to it. 

