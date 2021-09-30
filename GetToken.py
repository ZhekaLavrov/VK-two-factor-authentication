from Auth import auth
from AuthWithToken import auth_with_token

import os
import json


def get_token(login):
	access_token = None
	config_file = "vk_config.v2.json"
	if os.path.exists(config_file):
		with open(config_file, "r") as f:
			data = json.load(f)
			data = data.get(login)
			if data is not None:
				data = data.get("token")
				if len(data.keys()):
					data = data.get(list(data.keys())[0])
					if len(data.keys()):
						data = data.get(list(data.keys())[0])
						access_token = data.get("access_token")
	return access_token

if __name__ == '__main__':
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    vk_session, vk = auth(login, password)
    token = get_token(login)
    session, vk = auth_with_token(token)
    print(vk.users.get()[0])
