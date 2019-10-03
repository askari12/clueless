from bs4 import BeautifulSoup as bs

html = ""
black_class_Name = "Cell-block--1oNaD"
white_class_name = "Cell-cell--1p4gH"

white_cells = []
black_cells = []

with open("html.txt" , "r") as html_file:
    html = html_file.read()

parsed_html = bs(html)

def find_info_cells(parsed_html):
    for g in parsed_html.find_all("g"):

        try:
            if (g['data-group'] == "cells"):
                return  g.find_all("g")

        except Exception as e:
            pass

info_cells = find_info_cells(parsed_html)

for cell in info_cells:

    try:

        rect = cell.find("rect")

        if (rect["class"] == [black_class_Name]):

            black_cells.append(cell)

        else:

            white_cells.append((cell))

    except Exception as e:
        pas

print (len(white_cells))
print (len(black_cells))

class Cells:

    def __init__(self):

        pass