# ICT-Applications-Glossary
Simple glossary Web App I made as an extra credit thing for class

Allows for definitions to be viewed by categories (a lot like Rippah Quotes) and is basically a simple dictionary.
Backend is written in python, using the bottle.py micro-framework. 
Unlike ASP.Net or even other Python web framworks like Django, bottle.py has no real scaffolding or defined structure
which means that I essentially wrote this one from scratch. Definitions are stored in an SQLite Database File, this also
allows for definitions to be added if necessary (localhost:8080/Create).
