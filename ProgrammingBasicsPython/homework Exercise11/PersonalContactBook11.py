# Exercise:
# 1. Write a program for personal contact book using Flask micro web framework.
# Menu based interface for creating, updating, searching and removing records.
# Following fields need to be used:
#    Name, Address, Birthday, Phone number, Email, Profession, Interests
# 3. Use templates:
# /templates  - in templates folder different templates used from the webapp to visualize and get data
# /static  - static content of a web app as CSS
# mycontacts.db - this is the DB file which holds all saved contacts records which have been added.
# All the APIs and functions are manipulating data residing in this file.
# and optionally cookies, sessions ids, create a login page, etc.
# 2. In order to increase the security of data and the web app itself by adding login functionality.
# - There should be a username and password form when the first application has been loaded
# - A session mechanism needs to be used via 'session' object.
# - The direct API call to other routes of an API of this web app should not be allowed unless
# the user first authenticated via username and password.
# USERNAME: admin
# PASSWORD: admin
from flask import Flask, url_for, request, render_template, session, redirect
import os


contact_book = Flask(__name__)


contact_book.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@contact_book.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('main_menu.html')


@contact_book.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = "Please try again."
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@contact_book.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))


@contact_book.route('/create', methods=['GET', 'POST'])
def create():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'GET':
            return render_template('menu_create.html')
        elif request.method == 'POST':
            name = request.form['name']
            address = request.form['address']
            phone_number = request.form['phone']
            email = request.form['email']
            profession = request.form['profession']
            interests = request.form['interests']
            with open('contacts.db', 'a+', encoding='utf-8') as contact_list:
                contact_list.write("{};{};{};{};{};{}\n".format(name, address, phone_number, email, profession, interests))
            return render_template('create_message.html') % name
        else:
            return render_template('error_message.html')


@contact_book.route('/delete', methods=['GET', 'POST'])
def delete():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'GET':
            return render_template('delete_name_input.html')
        elif request.method == 'POST':
            deletion_flag=False
            with open("contacts.db", "r") as f:
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
            with open("contacts.db", "w") as f:
                f.write(newContactList)
                f.write("\n")
            if deletion_flag:
                return render_template('delete_message.html').format(name)
            else:
                return render_template('name_not_found.html').format(name)
        else:
            return render_template('error_message.html')


@contact_book.route('/search', methods=['GET', 'POST'])
def search():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'GET':
            return render_template('search_name.html')
        elif request.method == 'POST':
            searching_flag = False
            name = request.form['search_name']
            address = ""
            phone_number = ""
            email = ""
            profession = ""
            interests = ""
            contactList = open("contacts.db", "r")
            for line in contactList:
                if line.startswith(name):
                    name, address, phone_number, email, profession, interests = line.split(';')
                    searching_flag = True
            if searching_flag:
                return render_template('search_result.html').format(name, address, phone_number, email, profession, interests)
            else:
                return render_template('name_not_found.html').format(name)
        else:
            return render_template('error_message.html')


@contact_book.route('/update', methods=['GET', 'POST'])
def update():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        if request.method == 'GET':
            return render_template('update_name.html')
        elif request.method == 'POST':
            name = str(request.form.get('update_name'))
            updating_flag = False
            address = ""
            phone_number = ""
            email = ""
            profession = ""
            interests = ""
            with open("contacts.db", "r") as f:
                contact_list = f.read()
            newline = ""
            oldline = ""
            for line in contact_list.splitlines():
                if line.startswith(name):
                    oldline = str(line)
                    name, address, phone_number, email, profession, interests = line.split(';')
                    updating_flag = True
            newContactList = contact_list.replace(oldline, newline)
            newContactList = os.linesep.join([s for s in newContactList.splitlines() if s.strip()])
            with open("contacts.db", "w") as f:
                f.write(newContactList)
                f.write("\n")
            if updating_flag:
                return render_template('update_menu_result.html').format(name, address, phone_number, email, profession, interests)
            else:
                name = request.form['name']
                address = request.form['address']
                phone_number = request.form['phone']
                email = request.form['email']
                profession = request.form['profession']
                interests = request.form['interests']
                with open('contacts.db', 'a+', encoding='utf-8') as contact_list:
                    contact_list.write(
                        "{};{};{};{};{};{}\n".format(name, address, phone_number, email, profession, interests))
                return render_template('update_message.html') % name
        else:
            return render_template('error_message.html')


if __name__ == '__main__':
    contact_book.run(port=5004, debug=True)
