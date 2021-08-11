import config

import vk_api
from vk_api import exceptions


login = config.login
password = config.password


def captcha_handler(captcha):
    """ При возникновении капчи вызывается эта функция и ей передается объект
        капчи. Через метод get_url можно получить ссылку на изображение.
        Через метод try_again можно попытаться отправить запрос с кодом капчи
    """

    key = input("Введите код с изображения {0}: ".format(captcha.get_url())).strip()

    # Пробуем снова отправить запрос с капчей
    return captcha.try_again(key)


# Авторизация с помощью логина и пароля
try:
    vk_session = vk_api.VkApi(login, captcha_handler=captcha_handler)
    vk_session.auth()
    print("Авторизован с помощью cookies")
except exceptions.PasswordRequired as e:
    def auth_handler():
        """
        При двух факторной аутентификации вызывается эта функция.
        """

        # Код двух факторной аутентификации
        key = input("Введите код авторизации: ")
        # Если: True - сохранить, False - не сохранять.
        remember_device = True

        return key, remember_device
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler, captcha_handler=captcha_handler)
    vk_session.auth()
    print("Авторизован с помощью пароля")


vk = vk_session.get_api()

for i in range(50):
    post = vk.wall.repost(
        object="wall-109151593_3232"
    )
    print(post)
