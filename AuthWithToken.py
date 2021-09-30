import vk_api


def auth_with_token(access_token):
	session = vk_api.VkApi(token=access_token, app_id=2685278, api_version="5.120")
	vk = session.get_api()
	return session, vk