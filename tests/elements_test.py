import random
import time
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadAndDownloadPage, DynamicPropertiesPage


# Тесты для страницы с текстовыми полями
class TestTextBox:

    def test_text_box(self, driver):
        # Инициализируем страницу TextBoxPage
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()

        # Заполняем форму
        full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()

        # Проверяем, что значения в форме правильные
        output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

        # Сравниваем ожидаемые и фактические значения
        assert full_name == output_name
        assert email == output_email
        assert current_address == output_cur_addr
        assert permanent_address == output_per_addr


# Тесты для страницы с чекбоксами
class TestCheckBox:
    def test_check_box(self, driver):
        # Инициализируем страницу CheckBoxPage
        check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
        check_box_page.open()

        # Открываем полный список чекбоксов
        check_box_page.open_full_list()

        # Кликаем по случайному чекбоксу
        check_box_page.click_random_checkbox()

        # Получаем выбранные чекбоксы и результат на странице
        input_checkbox = check_box_page.get_checked_checkboxes()
        output_result = check_box_page.get_output_result()

        # Сравниваем выбранные чекбоксы с результатом на странице
        assert input_checkbox == output_result, 'checkboxes have not been selected'


# Тесты для страницы с радиокнопками
class TestRadioButton:
    def test_radio_button(self, driver):
        # Инициализируем страницу RadioButtonPage
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button_page.open()

        # Тестируем выбор радиокнопки "Yes"
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()

        # Тестируем выбор радиокнопки "Impressive"
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()

        # Тестируем выбор радиокнопки "No"
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()

        # Проверяем, что выбор радиокнопок был правильным
        assert output_yes == 'Yes', "'Yes' have not been selected"
        assert output_impressive == 'Impressive', "'Impressive' have not been selected"
        assert output_no == 'No', "'No' have not been selected"


# Тесты для страницы с таблицей
class TestWebTable:

    def test_web_table_add_person(self, driver):
        # Инициализируем страницу WebTablePage
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()

        # Добавляем нового человека в таблицу
        new_person = web_table_page.add_new_person()

        # Проверяем, что человек был добавлен в таблицу
        table_result = web_table_page.check_new_added_person()
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        # Инициализируем страницу WebTablePage
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()

        # Ищем случайного человека в таблице
        key_word = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_some_person(key_word)

        # Проверяем, что человек был найден
        table_result = web_table_page.check_search_person()
        assert key_word in table_result, "the person was not found in the table"

    def test_web_table_update_person_info(self, driver):
        # Инициализируем страницу WebTablePage
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()

        # Получаем фамилию нового человека
        lastname = web_table_page.add_new_person()[1]

        # Ищем этого человека по фамилии
        web_table_page.search_some_person(lastname)

        # Обновляем информацию о человеке
        age = web_table_page.update_person_info()
        row = web_table_page.check_search_person()

        # Проверяем, что данные обновились
        assert age in row, "the person card has not been changed"

    def test_web_table_delete_person(self, driver):
        # Инициализируем страницу WebTablePage
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()

        # Получаем email нового человека
        email = web_table_page.add_new_person()[3]

        # Ищем человека по email
        web_table_page.search_some_person(email)

        # Удаляем человека из таблицы
        web_table_page.delete_person()

        # Проверяем, что человек был удален
        text = web_table_page.check_deleted()
        assert text == "No rows found"

    def test_web_table_change_count_row(self, driver):
        # Инициализируем страницу WebTablePage
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()

        # Меняем количество строк на странице
        count = web_table_page.select_up_to_some_rows()

        # Проверяем, что количество строк изменилось
        assert count == [5, 10, 20, 25, 50,
                         100], "The number of rows in the table has not been changed or has changed incorrectly"


# Тесты для страницы с кнопками
class TestButtonsPage:
    def test_different_click_on_the_buttons(self, driver):
        # Инициализируем страницу ButtonsPage
        button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
        button_page.open()

        # Кликаем на разные кнопки
        double = button_page.click_on_different_button("double")
        right = button_page.click_on_different_button("right")
        click = button_page.click_on_different_button("click")

        # Проверяем, что кнопки работают корректно
        assert double == "You have done a double click", "The double click button was not pressed"
        assert right == "You have done a right click", "The right click button was not pressed"
        assert click == "You have done a dynamic click", "The dynamic click button was not pressed"


# Тесты для страницы с ссылками
class TestLinksPage:

    def test_check_link(self, driver):
        # Инициализируем страницу LinksPage
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()

        # Проверяем, что ссылка работает корректно
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "the link is broken or url is incorrect"

    def test_broken_link(self, driver):
        # Инициализируем страницу LinksPage
        links_page = LinksPage(driver, "https://demoqa.com/links")
        links_page.open()

        # Проверяем, что ссылка ведет на несуществующую страницу
        response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
        assert response_code == 400, "the link works or the status code is not 400"


# Тесты для страницы загрузки и скачивания файлов
class TestUploadAndDownload:

    def test_upload_file(self, driver):
        # Инициализируем страницу UploadAndDownloadPage
        upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        upload_download_page.open()

        # Загружаем файл и проверяем, что он был загружен
        file_name, result = upload_download_page.upload_file()
        assert file_name == result, 'the file has not been uploaded'

    def test_download_file(self, driver):
        # Инициализируем страницу UploadAndDownloadPage
        upload_download_page = UploadAndDownloadPage(driver, "https://demoqa.com/upload-download")
        upload_download_page.open()

        # Проверяем, что файл был скачан
        check = upload_download_page.download_file()
        assert check is True, 'the file has not been downloaded'


# Тесты для страницы с динамическими свойствами
class TestDynamicPropertiesPage:

    def test_enable_button(self, driver):
        # Инициализируем страницу DynamicPropertiesPage
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()

        # Проверяем, что кнопка активируется через 5 секунд
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, 'button did not enable after 5 second'

    def test_dynamic_properties(self, driver):
        # Инициализируем страницу DynamicPropertiesPage
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()

        # Проверяем изменение цвета кнопки
        color_before, color_after = dynamic_properties_page.check_changed_of_color()
        assert color_before != color_after, 'colors have not been changed'

    def test_appear_button(self, driver):
        # Инициализируем страницу DynamicPropertiesPage
        dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
        dynamic_properties_page.open()

        # Проверяем, что кнопка появляется через 5 секунд
        appear = dynamic_properties_page.check_appear_of_button()
        assert appear is True, 'button did not appear after 5 second'