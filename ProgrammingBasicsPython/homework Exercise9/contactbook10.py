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


from flask import Flask, url_for, request, render_template

contactbook=Flask(__name__)


@contactbook.route('/')
def index():
    return render_template('mainmenu.html')


@contactbook.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('creating.html')
    elif request.method == 'POST':
        Names = request.form['names']
        Address = request.form['address']
        Birth_day = request.form['bday']
        Phone_Number = request.form['phone']
        Email_address = request.form['email']
        Profession = request.form['prof']
        Interests = request.form['interests']
        with open('contactdp.csv','a+', encoding = 'utf-8') as contactbookdb:
            contactbookdb.write("{},{},{},{},{},{},{}\n".format(Names,Address,Birth_day,Phone_Number,Email_address,Profession,Interests))
        return """<html><body>The Contact for %s has been added successfully!
          <p> To add new concact <a href=/create > click here </a>
          <p> To go to the main menu <a href=/> click here </a></body></html>""" % Names
    else:
        return "NOK"

@contactbook.route('/update')
def update():
    return "<html><body>Updaiting</body></html>"

@contactbook.route('/search')
def search():
    return """<html><body>Searching</body></html>"""

@contactbook.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        Name_to_delete = request.form['del_name']
        contactbookmem=[]
        deletion_flag=False
        with open('contactdp.csv','r', encoding = 'utf-8') as contactbookdb:
            contactbookmem_str=contactbookdb.read()
            contactbookmem=contactbookmem_str.split('\n')
            i=0
            for line in contactbookmem:
                try:
                    Name,Address,Birthday,Phonenumber,Email,Profession,Interests = line.split(',')
                except:
                    Name=line
                if not Name:
                    continue
                print(Name)
                if Name_to_delete.upper()==Name.upper():
                   del contactbookmem[i]
                   deletion_flag=True
                i+=1
        with open('contactdp.csv','w', encoding = 'utf-8') as contactbookdb:    
            for line in contactbookmem:
                line_string=''.join(line)
                contactbookdb.write("{}\n".format(line_string))
        if deletion_flag:
            return "<html><body>{} was deleted successfully !<p> <a href=/> Back to main menu </a></p></body></html>".format(Name_to_delete )
        else:
            return """<html><body><h3>{} was not found in the contact book !</h3> <p> <a href=/> Back to main menu </a> </body></html>""".format(Name_to_delete)          
    else:
        return render_template('deleting.html')
   


if __name__ == '__main__':
    contactbook.run(host='0.0.0.0', debug=True)