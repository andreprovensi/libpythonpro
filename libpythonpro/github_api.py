import requests


def buscar_avatar(usuario: str):
    """
    Busca o avatar de um usuário no github
    :param usuario:str
    :return: str com o link do avatar
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == "__main__":

    print(buscar_avatar('renzon'))
