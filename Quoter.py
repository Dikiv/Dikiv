# file: update_readme.py
from cgitb import html
from fileinput import filename
import pathlib
import os
import json
from django.utils.html import format_html

from random import randrange
import markdown


# Define the paths to the .md and JSON files
md_file_path = "./README.md"
json_file_path = "./assets/quotes.json"


with open(json_file_path, 'r') as f:
    data = json.load(f)
    val =  data['quotes_by_people'][randrange(0,len(data['quotes_by_people']))]
    val1 = json.dumps(val)
    val2 = json.loads(val1)
    tmpauthor = val2["author"].replace(" ", "+")
    tmpquote = val2["quote"].replace(" ", "+")
    newQuote = 'https://readme-daily-quotes.vercel.app/api?theme=dark&author={0}&quote={1}'.format(tmpauthor, tmpquote)

with open(md_file_path, mode='r',encoding="utf8") as fi:
    txt = fi.readlines()
    count = 0
    #html = markdown.markdown(txt)
    
    
with open(md_file_path, mode='w',encoding="utf8") as new_file:
    for i in range(len(txt)):
        if txt[i].startswith('<img src="https://readme-daily-quotes.vercel.app/'):
            txt[i]= format_html('<img src="{newQuote}" width="400" height ="167">\n',newQuote=newQuote).replace(r'amp;', '')
            #print(chart)
    new_file.writelines(txt)
    
