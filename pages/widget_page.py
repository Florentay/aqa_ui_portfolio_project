import random

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generator.generator import generated_color
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
            {
                'title': self.locators.SECTION_FIRST,
                'content': self.locators.SECTION_CONTENT_FIRST
            },
            'second':
                {
                    'title': self.locators.SECTION_SECOND,
                    'content': self.locators.SECTION_CONTENT_SECOND
                },
            'third':
                {
                    'title': self.locators.SECTION_THIRD,
                    'content': self.locators.SECTION_CONTENT_THIRD
                }

        }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        # print(section_title.text)
        # print(section_content)
        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.WebDriverWait = None

    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.click()
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break  # добавляем, иначе следующая срока сломается - вернется 0. А с брейк удаляем только 1 элемент
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors


    def remove_all_values(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        clear_button = self.element_is_visible(self.locators.CLEAR_ALL_BUTTON)
        clear_button.click()
        self.element_is_not_visible(self.locators.MULTI_VALUE)
        input_field = self.element_is_visible(self.locators.MULTI_INPUT)
        input_value = input_field.get_attribute("value")

        # также есть еще такой вариант:
        # is_empty = self.element_is_not_visible(self.locators.MULTI_VALUE)
        # print(is_empty)
        # return count_value_before, is_empty
        # а в тесте assert is_empty

        return count_value_before, input_value


    def fill_input_single(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.click()
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text