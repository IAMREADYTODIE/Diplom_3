from selenium.webdriver.common.by import By

class ConstructorLocators:

    CONSTRUCTOR_BTN = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED_BTN = (By.XPATH, ".//p[text()='Лента Заказов']")
    

    BUN_ITEM = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a")
    BUN_COUNTER = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']/parent::a//p[contains(@class, 'counter_counter')]")
    BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    

    MODAL = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BTN = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    

    ORDER_BTN = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NUMBER_MODAL = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title')]")
    