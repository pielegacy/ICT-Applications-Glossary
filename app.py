from bottle import *
import sqlite3
#Index
@route('/')
@route('/terms')
def getgloss():
	conn = sqlite3.connect('glossary.db')
	terms = []
	defins = []
	cats = []
	#SQLite query using familiar SQL 
	c = conn.execute("SELECT * from table_definitions")
	rows = c.fetchall()
	for row in rows:
		terms.append(row[1])
		defins.append(row[2])
		cats.append(row[3])
	conn.commit()
	conn.close()
	#ayelmao it works josiah
	#Returns a page using the required template file (.tpl)
	return template("list", terms=terms, defins=defins, cats=cats)
#List Definitions By Concept
@route('/category/<name>')
def getterms(name):
	conn = sqlite3.connect('glossary.db')
	terms = []
	defins = []
	c = conn.execute("SELECT * from table_definitions WHERE str_category = '%s'" %(name, ))
	rows = c.fetchall()
	for row in rows:
		terms.append(row[1])
		defins.append(row[2])
	conn.commit()
	conn.close()
	return template("category", name=name, defins=defins, terms=terms)
#List Concepts
@route('/concept')
def concept():
	conn = sqlite3.connect('glossary.db')
	terms = []
	defins = []
	c = conn.execute("SELECT * from table_category")
	rows = c.fetchall()
	for row in rows:
		terms.append(row[1])
	conn.commit()
	conn.close()
	return template("concept",terms=terms)

#Basic Static File Receiver
@get('/static/<filename>')
def send_static(filename):
    return static_file(filename, root='static/')

#Create New Definition
@route('/create')
def create():
	return template("create")
#Post Method for Create
@route('/create', method="POST")
def success():
        #Requesting elements from form
	term = request.forms.get('term')
	define = request.forms.get('define')
	cat = request.forms.get('category')
	conn = sqlite3.connect('glossary.db')
	count = 1
	c = conn.execute("SELECT * from table_definitions")
	rows = c.fetchall()
	for row in rows:
		count += 1
	if term != "" and define != "":
		if cat !="":
			c = conn.execute("INSERT INTO table_definitions (ID, str_term, str_definition, str_category) VALUES ('%s', '%s', '%s', '%s')" %(count, term, define, cat, ))
		else :
			c = conn.execute("INSERT INTO table_definitions (ID, str_term, str_definition) VALUES ('%s', '%s', '%s')" %(count, term, define,))
		conn.commit()
		conn.close()
		print(term + " added")
		return template("success")
	else : 
		conn.commit()
		conn.close()
		return template("failure")
#CSS Returner
@get('/main.css')
def stylesheets():
	return static_file("main.css", root='static')
#404 Page
@error(404)
def error404(error):
	return "Oi nah not working aye?"


# Debug Run #
#run(host='localhost', port=8080, debug=True, reloader=True)

run(host="localhost", port=8080)
