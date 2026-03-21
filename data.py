class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru"
    
    # Страницы UI
    LOGIN_PAGE = f"{BASE_URL}/login"
    FEED_PAGE = f"{BASE_URL}/feed"
    PROFILE_PAGE = f"{BASE_URL}/account/profile"
    
    # API эндпоинты (нужны для создания юзера в фоне)
    API_REGISTER = f"{BASE_URL}/api/auth/register"
    API_USER = f"{BASE_URL}/api/auth/user"

class Constants:
    # Стандартное время ожидания для явных ожиданий (Explicit Waits)
    WAIT_TIME = 10
    