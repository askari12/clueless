from django.http import JsonResponse
import json

def getData(request):

    from .src.ParseInfo import Parser as pi
    from datetime import date
    file_name = date.today().strftime("%d-%m-%Y") + ".txt"

    parseInfo = pi(file_name)

    cells = parseInfo.getGrid()
    a_clues_num , a_clues , d_clues_num , d_clues = parseInfo.getClues()

    result = {
        "cells": cells,
        "a_clues_num": a_clues_num ,
        "a_clues": a_clues,
        "d_clues_num": d_clues_num,
        "d_clues": d_clues
    }
    return JsonResponse(result, safe=False)