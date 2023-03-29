# главная страница
ENTER_ACCOUNT_BUTTON = './/button[text()="Войти в аккаунт"]'  # кнопка "Войти в аккаунт" на главной странице
REGISTER_LINK = './/a[text()="Зарегистрироваться"]'  # ссылка на форму регистрации
CREATE_ORDER_BUTTON = './/button[text()="Оформить заказ"]'  # кнопка для оформления заказа
PERSONAL_ACCOUNT = './/p[text()="Личный Кабинет"]'  # нопка для входа в личный кабинет с главной страницы
BAKER_TAB = './/span[text()="Булки"]'  # вкладка выбора булок на главной странице
BAKER_HEADER = './/h2[text()="Булки"]'  # заголовок булки на главной странице
SAUCE_TAB = './/span[text()="Соусы"]'  # вкладка выбора соусы на главной странице
SAUCE_HEADER = './/h2[text()="Соусы"]'  # заголовок соусы на главной странице
FILLINGS_TAB = './/span[text()="Начинки"]'  # вкладка выбора начинки на главной странице
FILLINGS_HEADER = './/h2[text()="Начинки"]' # заголовок начинки на главной странице
HEADER_ON_MAIN_PAGE = 'h1'  # заголовок на главной странице

# личный кабинет
PROFILE = './/a[text()="Профиль"]'  # заголовок "Профиль" в личном кабинете
EXIT_ACCOUNT_BUTTON = './/button[text()="Выход"]'  # кнопка выхода из аккаунта
CONSTRUCTOR_LINK = './/p[text()="Конструктор"]'  # ссылка ведущая в конструктор
STELLA_BURGER_LABEL = 'AppHeader_header__logo__2D0X2'  # Stella Burger лейбл

# форма регистрации
NAME_INPUT_ON_REGISTRATION_FORM = './/label[text()="Имя"]/following::input'  # поле для ввода имени в форме регистрации
EMAIL_INPUT_ON_REGISTRATION_FORM = './/label[text()="Email"]/following::input'  # поле для ввода почты в
# форме регистрации
PASSWORD_INPUT_ON_REGISTRATION_FORM = './/label[text()="Пароль"]/following::input'  # поле ввода пароля в форме
# регистрации
REGISTER_BUTTON = './/button[text()="Зарегистрироваться"]'  # кнопка регистрации
INCORRECT_PASSWORD_MESSAGE = './/p[text()="Некорректный пароль"]'  # ообщение о некорректном пароле

# форма для входа
EMAIL_INPUT_ON_ENTERING_FORM = './/label[text()="Email"]/following::input'  # поле ввода почты при входе в систему
PASSWORD_INPUT_ON_ENTERING_FORM = './/label[text()="Пароль"]/following::input'  # поле ввода пароля при входе в систему
ENTER_BUTTON = './/button[text()="Войти"]'  # нопка "Войти" при входе в систему
PASSWORD_RECOVERY_LINK = './/a[text()="Восстановить пароль"]'  # ссылка на  восстановление пароля
ENTERING_LINK_FROM_RECOVERY_PASSWORD_PAGE = './/a[text()="Войти"]'  # ссылка на вход с формы восстановления пароля
ENTERING_HEADER = './/h2[text()="Вход"]'  # заголовок Вход на странице входа