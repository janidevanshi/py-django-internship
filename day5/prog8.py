# Write a program with use of inheritance: Define a class publisher that stores the name of the title. Derive two classes book and tape, which inherit publisher. Book class contains member data called page no and tape class contain time for playing. Define functions in the appropriate classes to get and print the details.
class publisher:
    def info(self, title):
        print("Title of the book is", title)


class book(publisher):
    def member_data(self, pg_no):
        print("Page no. are", pg_no)


class tape(publisher):
    def timing(self, time):
        print("Time for playing is ", time)


b = book()
t = tape()
b.member_data(500)
b.info("2 states")
t.timing("30hrs")
