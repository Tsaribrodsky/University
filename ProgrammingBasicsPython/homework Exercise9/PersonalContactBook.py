# Write a program for personal contact book using Flask micro web framework.
# Menu based interface for creating, updating, searching and removing records.
# The information needs to be stored in a semi-column(;) separated text file
# in the location where the server application is.
# Following fields need to be used:
# Name, Address, Birthday, Phone number, Email, Profession, Interests
# Find attached the main structure of the flask web app.
from flask import Flask, url_for, request
import os


contact_book = Flask(__name__)


@contact_book.route('/')
def index():
    return """<html>
              <body>
              <h2>Contact Book</h2>  
              <table>
              <tr><td><a href='http://127.0.0.1:5000/create'>Create a contact</a></td></tr>
              <tr><td><a href='http://127.0.0.1:5000/update'>Update a contact</a></td></tr>
              <tr><td><a href='http://127.0.0.1:5000/search'>Search a contact</a></td></tr>
              <tr><td><a href='http://127.0.0.1:5000/delete'>Remove a contact</a></td></tr>
              </table>
              </body></html>"""


@contact_book.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return """<html><body>
               <h2>Create a contact</h2> 
               <form action='/create', method = 'post'>
               <table>
               <tr><td>name</td><td><input type=text name="name"></td></tr>
               <tr><td>address</td><td><input type=text name="address"></td></tr>
               <tr><td>phone number</td><td><input type=text name="phone"></td></tr>
               <tr><td>email</td><td><input type=text name="email"></td></tr>
               <tr><td>profession</td><td><input type=text name="profession"></td></tr>
               <tr><td>interests</td><td><input type=text name="interests"></td></tr>
               </table>
               <input type=submit value=Submit>
               </form>
               </body></html>"""
    elif request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone']
        email = request.form['email']
        profession = request.form['profession']
        interests = request.form['interests']
        with open('contacts.txt', 'a+', encoding='utf-8') as contact_list:
            contact_list.write("{},{},{},{},{},{}\n".format(name, address, phone_number, email, profession, interests))
        return """<html><body>
          <h3 style="color:blue;">The contact %s has been added.</h3>  
          <p><a href=/create style="text-decoration:none">Add a contact</a>
          <p><a href=/ style="text-decoration:none">Go Home</a></body></html>""" % name
    else:
        return """<html><body>
          <h3>something went wrong</h3>
          <p><a href=/>Go Home</a></body></html>"""


@contact_book.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'GET':
        return """<html>
                  <body>
                  <h3>Deleting the contact. Enter a name: </h3>
                  <form action='/delete', method='post'>
                  <input type='text' name='del_name'>
                  <input type='submit' value='Delete'>
                  </form>
                  </body>
                  </html>"""
    elif request.method == 'POST':
        deletion_flag=False
        with open("contacts.txt", "r") as f:
            contactList = f.read()
        name = request.form['del_name']
        newline = ""
        oldline = ""
        for line in contactList.splitlines():
            if line.startswith(name):
                oldline = str(line)
                deletion_flag = True
        newContactList = contactList.replace(oldline, newline)
        newContactList = os.linesep.join([s for s in newContactList.splitlines() if s.strip()])
        with open("contacts.txt", "w") as f:
            f.write(newContactList)
            f.write("\n")
        if deletion_flag:
            return "<html><body>{} was deleted.<p><a href=/>Go Home</a></p></body></html>".format(name)
        else:
            return """<html><body><h3>{} was not found.</h3><p><a href=/>Go Home</a></body></html>""".format(name)
    else:
        return """<html><body>
                  <h3>something went wrong</h3>
                  <p><a href=/>Go Home</a></body></html>"""


@contact_book.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'GET':
        return """<html>
                  <body>
                  <h3>Searching the contact. Enter a name: </h3>
                  <form action='/search', method='post'>
                  <input type='text' name='search_name'>
                  <input type='submit' value='Search'>
                  </form>
                  </body>
                  </html>"""
    elif request.method == 'POST':
        searching_flag = False
        name = request.form['search_name']
        address = ""
        phone_number = ""
        email = ""
        profession = ""
        interests = ""
        contactList = open("contacts.txt", "r")
        for line in contactList:
            if line.startswith(name):
                name, address, phone_number, email, profession, interests = line.split(',')
                searching_flag = True
        if searching_flag:
            return """<html><body>
               <h2>Search a contact</h2> 
               <form action='/create', method = 'post'>
               <table>
               <tr><td>name:</td><td><p style="color:blue;">{}</p></td></tr>
               <tr><td>address:</td><td><p style="color:blue;">{}</p></td></tr>
               <tr><td>phone number:</td><td><p style="color:blue;">{}</p></td></tr>
               <tr><td>email:</td><td><p style="color:blue;">{}</p></td></tr>
               <tr><td>profession:</td><td><p style="color:blue;">{}</p></td></tr>
               <tr><td>interests:</td><td><p style="color:blue;">{}</p></td></tr>
               </table>
               </form>
               <p><a href=/>Go Home</a></body></html>
               </body></html>""".format(name, address, phone_number, email, profession, interests)
        else:
            return """<html><body><h3>{} was not found.</h3><p><a href=/>Go Home</a></body></html>""".format(name)
    else:
        return """<html><body>
                  <h3>something went wrong</h3>
                  <p><a href=/>Go Home</a></body></html>"""


@contact_book.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        return """<html>
                  <body>
                  <h3>Updating the contact. Enter a name: </h3>
                  <form action='/update', method='post'>
                  <input type='text' name="update_name">
                  <input type='submit' value='Update'>
                  </form>
                  </body>
                  </html>"""
    elif request.method == 'POST':
        name = str(request.form.get('update_name'))
        updating_flag = False
        address = ""
        phone_number = ""
        email = ""
        profession = ""
        interests = ""
        with open("contacts.txt", "r") as f:
            contact_list = f.read()
        newline = ""
        oldline = ""
        for line in contact_list.splitlines():
            if line.startswith(name):
                oldline = str(line)
                name, address, phone_number, email, profession, interests = line.split(',')
                updating_flag = True
        newContactList = contact_list.replace(oldline, newline)
        newContactList = os.linesep.join([s for s in newContactList.splitlines() if s.strip()])
        with open("contacts.txt", "w") as f:
            f.write(newContactList)
            f.write("\n")
        if updating_flag:
            return """<html><body>
               <h2>Update a contact</h2> 
               <form action='/update', method = 'post'>
               <table>
               <tr><td>name</td><td><input type=text name="name" value="{}"></td></tr>
               <tr><td>address</td><td><input type=text name="address" value="{}"></td></tr>
               <tr><td>phone number</td><td><input type=text name="phone" value="{}"></td></tr>
               <tr><td>email</td><td><input type=text name="email" value="{}"></td></tr>
               <tr><td>profession</td><td><input type=text name="profession" value="{}"></td></tr>
               <tr><td>interests</td><td><input type=text name="interests" value="{}"></td></tr>
               </table>
               <input type=submit value=Submit>
               </form>
               <p><a href=/>Go Home</a></body></html>
               </body></html>""".format(name, address, phone_number, email, profession, interests)
        else:
            name = request.form['name']
            address = request.form['address']
            phone_number = request.form['phone']
            email = request.form['email']
            profession = request.form['profession']
            interests = request.form['interests']
            with open('contacts.txt', 'a+', encoding='utf-8') as contact_list:
                contact_list.write(
                    "{},{},{},{},{},{}\n".format(name, address, phone_number, email, profession, interests))
            return """<html><body>
                      <h3>The contact %s has been updated.</h3>
                      <p><a href=/>Go Home</a></body></html>""" % name
    else:
        return """<html><body>
                  <h3>something went wrong</h3>
                  <p><a href=/>Go Home</a></body></html>"""


if __name__ == '__main__':
    contact_book.run(debug=True)
