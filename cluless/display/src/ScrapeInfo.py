from selenium import webdriver as wd

home_path = "/home/askari/PycharmProjects/NewYorkTimesMini/cluless/display/src"
driver_path = home_path + "/geckodriver"
puzzle_website = "https://www.nytimes.com/crosswords/game/mini"
start_button_class_name = "buttons-modalButton--1REsR"
end_span_class_name = "ModalBody-closeX--2Fmp7"

# Make the browser
browser = wd.Firefox(executable_path=driver_path)

# Reach the Puzzle Website
browser.get(puzzle_website)

# Start The Puzzle
startButton = browser.find_element_by_class_name(start_button_class_name)
startButton.click()

# Press the Reveal Button
def pressAreYouSureRevealButton(div):
    for k in div:

        if k.get_attribute("innerHTML") == "Are you sure you want to reveal the puzzle?":
            revealButtons = k.find_element_by_xpath("..").find_elements_by_tag_name("button")
            revealButtons[1].click()

            browser.find_element_by_class_name(end_span_class_name).click()

            print("Done")

            break
def pressPuzzleButton(a):
    for j in a:
        if j.get_attribute("innerHTML") == "Puzzle":

            j.click()

            div = browser.find_elements_by_tag_name("div")

            pressAreYouSureRevealButton(div)
            break
def pressRevealButton():
    buttons = browser.find_elements_by_tag_name("button")
    for i in buttons:
        if i.get_attribute("innerHTML") == "reveal":
            i.click()

            a = i.find_element_by_xpath("..").find_elements_by_tag_name("a")

            pressPuzzleButton(a)
            break

pressRevealButton()

# Get The Inner HTML
from datetime import date
file_name = date.today().strftime("%d-%m-%Y") + ".txt"

file = open(home_path + "/" + file_name , "w+")
file.write(browser.find_element_by_tag_name("body").get_attribute("innerHTML"))
file.close()

# Close the Browser
browser.close()


