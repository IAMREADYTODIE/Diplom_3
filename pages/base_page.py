import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Constants

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        return WebDriverWait(self.driver, Constants.WAIT_TIME).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, Constants.WAIT_TIME).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Клик по элементу (стандартный)")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, Constants.WAIT_TIME).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Клик по элементу через JavaScript (силовой)")
    def click_element_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввод текста")
    def set_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    @allure.step("Получение текста элемента")
    def get_text(self, locator):
        return self.wait_for_visibility(locator).text

    @allure.step("Ожидание видимости элемента")
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, Constants.WAIT_TIME).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидание исчезновения элемента")
    def wait_for_invisibility(self, locator):
        return WebDriverWait(self.driver, Constants.WAIT_TIME).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Перетаскивание элемента (Drag and Drop)")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        # JS-скрипт для обхода бага Firefox с HTML5 Drag and Drop
        script = """
        function createEvent(typeOfEvent) {
            var event = document.createEvent("CustomEvent");
            event.initCustomEvent(typeOfEvent, true, true, null);
            event.dataTransfer = {
                data: {},
                setData: function (key, value) { this.data[key] = value; },
                getData: function (key) { return this.data[key]; }
            };
            return event;
        }
        function dispatchEvent(element, event, transferData) {
            if (transferData !== undefined) { event.dataTransfer = transferData; }
            if (element.dispatchEvent) { element.dispatchEvent(event); }
            else if (element.fireEvent) { element.fireEvent("on" + event.type, event); }
        }
        function simulateHTML5DragAndDrop(element, destination) {
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(element, dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(destination, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(element, dragEndEvent, dropEvent.dataTransfer);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(script, source, target)