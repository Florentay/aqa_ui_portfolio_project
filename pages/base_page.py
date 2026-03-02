from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver, url):
        # Конструктор. Передаем драйвер (браузер) и URL страницы, с которой будем работать
        self.driver = driver
        self.url = url

    def open(self):
        # Метод для открытия страницы по URL
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=50):
        self.go_to_element(self.element_is_present(locator))
        # Явное ожидание: ждем, пока элемент станет видимым на странице
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        # Ждем, пока ВСЕ элементы по этому локатору станут видимыми
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5):
        # Ждем, пока элемент появится в DOM (даже если он невидим)
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        # Ждем, пока ВСЕ элементы появятся в DOM
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        # Ждем, пока элемент станет невидимым (полезно, если нужно убедиться, что он исчез)
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        # Ждем, пока элемент станет кликабельным (видимым и доступным для клика)
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        # Скроллим к элементу, чтобы он попал в зону видимости
        self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def move_to_element(self, element):
        # Навести курсор мыши на элемент / проскролить (может быть нужно, чтобы появился выпадающий список или тултип)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def action_double_click(self, element):
        # Двойной клик по элементу (через ActionChains)
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        # Правый клик по элементу (контекстное меню)
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def remove_footer(self):
        # Удаляем footer и рекламу (может мешать кликам)
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('close-fixedban').remove();")


    def select_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)


    def select_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break