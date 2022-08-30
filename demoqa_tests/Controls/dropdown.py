from selene.core.entity import Element
from selene.support.shared import browser
from selene import command


class Dropdown:
    def __init__(self, element: Element):
        self.element = element

    def set_by_enter(self, location='NRC'):
        self.element.type(location).press_enter()

    def set_by_click(self, selector='#react-select-3-option-1'):
         self.element.click()
         browser.element(selector).perform(command.js.click)