from bs4 import BeautifulSoup as bs
from Cells import Cells

html = ""
black_class_Name = "Cell-block--1oNaD"
white_class_name = "Cell-cell--1p4gH"

clues_class_name = "Layout-clueLists--10_Xl"

with open("html.txt" , "r") as html_file:
    html = html_file.read()

parsed_html = bs(html)

def getGrid():
    cells_array = []

    def find_info_cells(parsed_html):
        for g in parsed_html.find_all("g"):

            try:
                if (g['data-group'] == "cells"):
                    return g.find_all("g")

            except Exception as e:
                pass

    info_cells = find_info_cells(parsed_html)

    for cell in info_cells:

        try:

            rect = cell.find("rect")
            character = ""
            number = ""

            if (rect["class"] == [black_class_Name]):
                character = "Black"
            else:

                texts = cell.find_all("text")
                for a_text in texts:

                    if (a_text["text-anchor"] == "start"):
                        number = a_text.string

                    if (a_text["text-anchor"] == "middle"):
                        character = a_text.string

            cells_array.append(Cells(number=number, character=character))

        except Exception as e:
            pass

    return cells_array

cells_array = getGrid()

def getClues():
    sections = parsed_html.find_all("section")
    a_clues = []
    d_clues = []

    for a_section in sections:

        def getClue(clue_list):

            new_clue_list = []
            for clue in clue_list:
                new_clue_list.append(clue.find_all("span")[1].string)
            return new_clue_list

        # Section for clues section
        if (a_section["class"] == [clues_class_name]):
            # Search for accross clues
            across_clues = a_section.find("div").find_all("li")
            a_clues = getClue(across_clues)

            # Search for down clues
            down_clues = a_section.find_all("div")[1].find_all("li")
            d_clues = getClue(down_clues)

    return a_clues , d_clues

a_clues , d_clues = getClues()
