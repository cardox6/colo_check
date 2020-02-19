#!/usr/local/bin/python3
import os
import cgi
path="/Users/mati/Documents/CODE Uni/Foundations/color_check/colors.txt"

form = cgi.FieldStorage()
v_color = form.getvalue('color')

bottle = open(path,"r")
colors = bottle.read()

print()
if v_color in colors:
  print(f"""<!DOCTYPE html>
  <html lang="en">
    <head>
      <title>Hello!</title>
      <link rel="stylesheet" href="/style.css">
    </head>
    <body> 
      <h1 style="background-color:{v_color};"> {v_color} is a color </h1>
    </body>
  </html>""")
else:
  print(f"""<!DOCTYPE html>
    <html lang="en">
     <head>
    <title>Hello!</title>
    <link rel="stylesheet" href="/style.css">
     </head>
    <body> 
    <h1> {v_color} is not in my library :( </h1>
    </body>
    </html>""")