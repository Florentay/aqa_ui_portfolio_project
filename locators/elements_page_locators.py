from selenium.webdriver.common.by import By


# Локаторы для страницы с текстовыми полями
class TextBoxPageLocators:
    # Формы для ввода данных
    FULL_NAME = (By.CSS_SELECTOR, 'input[id="userName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="permanentAddress"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Созданные данные, которые отображаются после отправки формы
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


# Локаторы для страницы с чекбоксами
class CheckBoxPageLocators:
    # Кнопка для раскрытия всех чекбоксов
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')

    # Список всех чекбоксов
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    # Отметившиеся чекбоксы
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    # Локатор для конкретного чекбокса, с возможностью работы с иерархией
    TITLE_ITEM = './/ancestor::span[@class="rct-text"]'
    # Результат после выбора чекбокса
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')


# Локаторы для страницы с радио-кнопками
class RadioButtonPageLocators:
    # Различные радиокнопки на странице
    YES_RADIOBUTTON = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO_RADIOBUTTON = (By.XPATH, '//label[@for="noRadio"]')

    # Результат выбора радиокнопки
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


# Локаторы для страницы с таблицей
class WebTablePageLocators:
    # Формы для добавления данных о человеке
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Локаторы для таблицы
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # Локатор для кнопки редактирования данных
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


# Локаторы для страницы с кнопками
class ButtonsPageLocators:
    # Различные кнопки на странице
    DOUBLE_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')

    # Результаты после нажатия на кнопки
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    SUCCESS_RIGHT = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")


# Локаторы для страницы с ссылками
class LinksPageLocators:
    # Ссылки на различные страницы
    SIMPLE_LINK = (By.CSS_SELECTOR, "a[id='simpleLink']")
    BAD_REQUEST = (By.CSS_SELECTOR, "a[id='bad-request']")


# Локаторы для страницы с загрузкой и скачиванием файлов
class UploadAndDownloadPageLocators:
    # Локаторы для загрузки файла
    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    # Локаторы для скачивания файла
    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')


# Локаторы для страницы с динамическими свойствами
class DynamicPropertiesPageLocators:
    # Кнопки с динамическими изменениями
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')