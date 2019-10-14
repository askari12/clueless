from bs4 import BeautifulSoup as bs
from .Cells import Cells

class Parser:

    def __init__(self , file_name):

        self.file_name = file_name
        self.html = ""
        self.black_class_Name = "Cell-block--1oNaD"
        self.white_class_name = "Cell-cell--1p4gH"
        self.clues_class_name = "Layout-clueLists--10_Xl"

        try:
            with open("/home/askari/PycharmProjects/NewYorkTimesMini/cluless/display/src/" + file_name , "r") as html_file:
                self.html = html_file.read()
        except FileNotFoundError:
            # Scrape the information needed and get the html
            from . import ScrapeInfo
            with open("/home/askari/PycharmProjects/NewYorkTimesMini/cluless/display/src/" + file_name , "r") as html_file:
                self.html = html_file.read()

        self.parsed_html = bs(self.html)

    def getGrid(self):
        cells_array = []

        def find_info_cells(parsed_html):
            for g in parsed_html.find_all("g"):

                try:
                    if (g['data-group'] == "cells"):
                        return g.find_all("g")

                except Exception as e:
                    pass

        info_cells = find_info_cells(self.parsed_html)

        for cell in info_cells:

            try:

                rect = cell.find("rect")
                character = ""
                number = ""

                if (rect["class"] == [self.black_class_Name]):
                    character = "Black"
                else:

                    texts = cell.find_all("text")
                    for a_text in texts:

                        if (a_text["text-anchor"] == "start"):
                            number = a_text.string

                        if (a_text["text-anchor"] == "middle"):
                            character = a_text.string

                cells_array.append(Cells(number=number, character=character).toJSON())

            except Exception as e:
                pass

        return cells_array

    def getClues(self):
        sections = self.parsed_html.find_all("section")
        a_clues_num = []
        a_clues = []
        d_clues_num = []
        d_clues = []

        for a_section in sections:

            def getClue(clue_list):

                new_clue_list = []
                new_clue_num_list = []
                for clue in clue_list:
                    new_clue_list.append(clue.find_all("span")[1].string)
                    new_clue_num_list.append(clue.find_all("span")[0].string)
                return new_clue_num_list , new_clue_list

            # Section for clues section
            if (a_section["class"] == [self.clues_class_name]):
                # Search for accross clues
                across_clues = a_section.find("div").find_all("li")
                a_clues_num , a_clues = getClue(across_clues)

                # Search for down clues
                down_clues = a_section.find_all("div")[1].find_all("li")
                d_clues_num , d_clues = getClue(down_clues)

        return a_clues_num , a_clues , d_clues_num , d_clues
