#Write a program for personal contact book using Flask micro web framework.
#Menu based interface for creating, updating, searching and removing records.  
#The information needs to be stored in a comma separated text file in the location where the server application is. 
#Following fields need to be used:
#Name, Address, Birthday, Phone number, Email, Profession, Interests


#Flask url Routes
#0. / 
#1. creating of a record
#2. updateing of a record
#3. searching
#4. removing of a record


from flask import Flask, url_for, request

contactbook=Flask(__name__)


@contactbook.route('/')
def index():
    return """<html><body>this is main menu
              <table>
              <tr><td>To add a contact </td><td><a href='http://127.0.0.1:5000/create'>click</a></td></tr>
              <tr><td>To update acontact </td><td><a href='http://127.0.0.1:5000/update'>click</a></td></tr>
              <tr><td>To search a contact </td><td><a href='http://127.0.0.1:5000/search'>click</a></td></tr>
              <tr><td>To delete a contact </td><td><a href='http://127.0.0.1:5000/delete'>click</a></td></tr>
              </table>
            </body></html>"""


@contactbook.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return """<html><body>To create a new contact fill the fields
               <form action='/create', method = 'post'>
               <table>
               <tr><td>Names </td><td><input type=text name="names"></td></tr>
               <tr><td>Address </td><td><input type=text name="address"></td></tr>
               <tr><td>Phone Number </td><td><input type=text name="phone"></td></tr>
               <tr><td>Email </td><td><input type=text name="email"></td></tr>
               <tr><td>Profession </td><td><input type=text name="prof"></td></tr>
               <tr><td>Interests </td><td><input type=text name="interests"></td></tr>
               </table>
               <input type=submit value=Submit>
               </form>
               </body></html>"""
    elif request.method == 'POST':
        Names = request.form['names']
        Address = request.form['address']
        Phone_Number = request.form['phone']
        Email_address = request.form['email']
        Profession = request.form['prof']
        Interests = request.form['interests']
        with open('contactdp.csv', 'a+', encoding='utf-8') as contactbookdb:
            contactbookdb.write("{},{},{},{},{},{}\n".format(Names, Address, Phone_Number, Email_address, Profession, Interests))
        return """<html><body>The Contact for %s has been added successfully!
          <p> To add new contact <a href=/create > click here </a>
          <p> To go to the main menu <a href=/> click here </a></body></html>""" % Names
    else:
        return "NOK"

@contactbook.route('/update')
def update():
    return "<html><body>Updaiting</body></html>"

@contactbook.route('/search')
def search():
    return """<html><body>Searching</body></html>"""

@contactbook.route('/delete')
def delete():
    return """<html><body>Deleting</body></html>"""


if __name__ == '__main__':
    contactbook.run(debug=True)