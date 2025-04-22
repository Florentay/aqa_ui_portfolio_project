import base64
import os
import random
import time
import requests
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadAndDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()  # Локаторы для элементов на странице

    def fill_all_fields(self):
        """
        Заполняет все поля на странице TextBox с случайными данными,
        полученными из генератора.
        Возвращает введенные значения для проверки.
        """
        person_info = next(generated_person())  # Генерация случайных данных
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        # Заполнение полей на странице
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)

        # Нажатие кнопки отправки формы
        self.element_is_visible(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """
        Проверяет, что данные, введенные в форму, отображаются корректно
        после отправки.
        Возвращает данные, которые были отправлены, чтобы сверить их с отображаемыми.
        """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        """
        Открывает полный список чекбоксов на странице.
        """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """
        Кликает по случайному числу чекбоксов из доступных на странице.
        """
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        # for item in item_list:
        #     self.go_to_element(item)
        #     item.click()
        count = 4  # Количество чекбоксов, по которым нужно кликнуть
        while count != 0:
            item = item_list[random.randint(1, 15)]  # Выбираем случайный элемент
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """
        Возвращает список всех отмеченных чекбоксов на странице.
        """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(By.XPATH, self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        """
        Возвращает результат из области вывода на странице,
        где отображаются выбранные чекбоксы.
        """
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        """
        Кликает на радиокнопку в зависимости от выбранного варианта:
        'yes', 'impressive' или 'no'.
        """
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
                   'no': self.locators.NO_RADIOBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        """
        Возвращает текст из области вывода результата
        после выбора радиокнопки.
        """
        return self.element_is_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    # Закомментированный код для добавления большего количества персон
    # def add_new_person(self, count=1): или
    # def add_new_person(self):
    #     # count = random.randint(1, 3)
    #     list = [] # переименовать в более осмысленное имя
    #     count = 5
    #     while count != 0:
    #         person_info = next(generated_person())
    #         firstname = person_info.firstname
    #         lastname = person_info.lastname
    #         email = person_info.email
    #         age = person_info.age
    #         salary = person_info.salary
    #         department = person_info.department
    #         self.element_is_visible(self.locators.ADD_BUTTON).click()
    #         self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
    #         self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
    #         self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
    #         self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
    #         self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
    #         self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
    #         self.element_is_visible(self.locators.SUBMIT).click()
    #         count -= 1
    #         list.append([firstname, lastname, str(age), email, str(salary), department])
    #     return list

    # Функция добавления одного нового человека в таблицу
    def add_new_person(self):
        """
        Добавляет нового человека в таблицу, заполняя поля с использованием данных, сгенерированных генератором.
        Возвращает информацию о добавленном человеке.
        """
        count = 1
        while count != 0:
            person_info = next(generated_person())  # Генерация данных для нового человека
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department

            # Заполнение формы добавления нового человека
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1  # Снижаем счетчик, чтобы завершить добавление

            return [firstname, lastname, str(age), email, str(salary), department]  # Возвращаем данные нового человека

    def check_new_added_person(self):
        """
        Проверяет, что новый человек был добавлен в таблицу, и возвращает список данных о добавленных людях.
        """
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)  # Получаем все записи из таблицы
        data = []
        for item in people_list:
            data.append(item.text.splitlines())  # Извлекаем данные каждой строки
        return data

    def search_some_person(self, key_word):
        """
        Ищет человека в таблице по ключевому слову.
        """
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        """
        Проверяет, что найденный человек отображается корректно в таблице.
        """
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        """
        Обновляет информацию о человеке, например, его возраст.
        Возвращает новый возраст для проверки.
        """
        person_info = next(generated_person())  # Генерируем данные для обновления
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()  # Нажимаем кнопку "Редактировать"
        self.element_is_visible(self.locators.AGE_INPUT).clear()  # Очищаем поле возраста
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)  # Вводим новый возраст
        self.element_is_visible(self.locators.SUBMIT).click()  # Сохраняем изменения
        return str(age)  # Возвращаем новый возраст

    def delete_person(self):
        """
        Удаляет человека из таблицы.
        """
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        """
        Проверяет, что человек был удален, и возвращает сообщение "No rows found", если таблица пуста.
        """
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        """
        Меняет количество отображаемых строк на странице (5, 10, 20, 25, 50 или 100).
        Возвращает список изменений.
        """
        count = [5, 10, 20, 25, 50, 100]  # Возможные значения для количества строк
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()  # Кликаем по выпадающему списку
            self.element_is_visible((By.CSS_SELECTOR, f'option[value="{x}"]')).click()  # Выбираем значение
            data.append(self.check_count_rows())  # Проверяем, что количество строк изменилось
        return data

    def check_count_rows(self):
        """
        Проверяет количество строк на странице.
        Возвращает количество строк.
        """
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        """
        В зависимости от типа клика ('double', 'right', 'click') выполняет соответствующее действие:
        - double: выполняет двойной клик
        - right: выполняет правый клик
        - click: выполняет обычный клик
        """
        if type_click == "double":
            # Выполняем двойной клик по кнопке
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)

        if type_click == "right":
            # Выполняем правый клик по кнопке
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)

        if type_click == "click":
            # Выполняем обычный клик по кнопке
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        """
        Проверяет, что текст, связанный с кнопкой, появился после клика.
        Возвращает текст, который отображается на экране после клика.
        """
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        """
        Проверяет, что ссылка открывается в новой вкладке и возвращает URL ссылки.
        Проверяется статус ответа, чтобы убедиться, что ссылка работает.
        """
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()  # Кликаем по ссылке, если она работает
            self.driver.switch_to.window(self.driver.window_handles[1])  # Переключаемся на новую вкладку
            url = self.driver.current_url  # Получаем текущий URL
            return link_href, url
        else:
            return link_href, request.status_code  # Возвращаем код ошибки, если ссылка не работает

    def check_broken_link(self, url):
        """
        Проверяет, что ссылка ведет на несуществующую страницу (например, 404).
        Если ссылка "битая", возвращает статус ошибки.
        """
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code  # Возвращаем код ошибки


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadPageLocators()

    def upload_file(self):
        """
        Загружает файл с использованием элемента input. Файл передается через атрибут 'send_keys'.
        После загрузки файла, удаляет его из файловой системы для предотвращения накопления ненужных файлов.
        Возвращает имя файла и текстовый результат с подтверждением загрузки.
        """
        file_name, path = generated_file()  # Генерация файла для загрузки
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)  # Отправка файла в input
        os.remove(path)  # Удаляем файл после загрузки, чтобы не оставлять мусор
        text = self.element_is_visible(self.locators.UPLOADED_RESULT).text  # Получаем сообщение о загрузке
        return file_name.split('/')[-1], text.split('\\')[-1]  # Возвращаем имя файла и результат

    def download_file(self):
        """
        Загружает файл с использованием ссылки для скачивания. Файл сохраняется на локальную систему.
        После скачивания, файл удаляется.
        Возвращает результат скачивания — существует ли файл в системе.
        """
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')  # Получаем ссылку
        link_b = base64.b64decode(link)  # Декодируем ссылку
        path_name_file = rf'/Users/olle/PycharmProjects/aqa_ui_portfolio_project/filetest{random.randint(0, 999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')  # Ищем начало изображения
            f.write(link_b[offset:])  # Записываем данные в файл
            check_file = os.path.exists(path_name_file)  # Проверяем, был ли файл создан
            f.close()
        os.remove(path_name_file)  # Удаляем файл, чтобы не засорять систему
        return check_file  # Возвращаем факт существования файла


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        # enable_button = self.element_is_clickable(self.locators.ENABLE_BUTTON)
        """
        Проверяет, что кнопка "Enable" становится активной.
        Если она активируется, возвращает True, иначе — False.
        """
        try:
            self.element_is_clickable(self.locators.ENABLE_BUTTON)  # Проверяем, можно ли кликнуть по кнопке
        except TimeoutException:
            return False  # Если кнопка не активна (по истечении времени), возвращаем False
        return True  # Кнопка активна, возвращаем True

    def check_changed_of_color(self):
        """
        Проверяет изменение цвета кнопки.
        Сначала фиксируем цвет, затем ждем 5 секунд и снова проверяем цвет.
        Возвращаем начальный и конечный цвета кнопки.
        """
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')  # Цвет до изменений
        time.sleep(5)  # Ждем 5 секунд
        color_button_after = color_button.value_of_css_property('color')  # Цвет после изменений
        # print(color_button_before, color_button_after)
        return color_button_before, color_button_after  # Возвращаем оба цвета для сравнения

    def check_appear_of_button(self):
        """
        Проверяет, что кнопка появляется через 5 секунд после загрузки страницы.
        Если кнопка появилась, возвращаем True, иначе — False.
        """
        # self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON, 1)
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)  # Ждем появления кнопки
        except TimeoutException:
            return False  # Если кнопка не появилась за 5 секунд, возвращаем False
        return True  # Кнопка появилась, возвращаем True
