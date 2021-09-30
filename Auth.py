import vk_api


def auth(login, password):
    def captcha_handler(captcha):
        """ При возникновении капчи вызывается эта функция и ей передается объект
            капчи. Через метод get_url можно получить ссылку на изображение.
            Через метод try_again можно попытаться отправить запрос с кодом капчи
        """

        key = input("Введите код с изображения {0}: ".format(captcha.get_url())).strip()

        # Пробуем снова отправить запрос с капчей
        return captcha.try_again(key)

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
    try:
    	vk_session.auth()	
    except vk_api.exceptions.BadPassword as e:
    	return None, None
    vk = vk_session.get_api()
    return vk_session, vk


if __name__ == '__main__':
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    vk_session, vk = auth(login, password)
    if vk is None:
    	print("Не удалось авторизоваться")
    else:
    	about_user = vk.users.get()[0]
    	print(f"Авторизован как {about_user['first_name']} {about_user['last_name']}")
