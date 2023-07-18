import allure
import json
from requests import Session, Response
from curlify import to_curl
from utils.posts_api import PostsApi
from utils.errors import check_status


def log_response(resp: Response, *args, **kwargs):
    @allure.step('making {method} request to {path_url}')
    def allure_step(resp: Response, method: str, path_url: str, url: str):
        allure.attach(json.dumps(json.loads(resp.content),
                                 sort_keys=True,
                                 indent=4,
                                 separators=(',', ': ')),
                      attachment_type=allure.attachment_type.JSON, name='body')

        allure.attach(to_curl(request=resp.request), name='curl')

    allure_step(resp=resp, method=resp.request.method, path_url=resp.request.path_url, url=resp.url)


class Client:
    def __init__(self, host):
        self.host = host
        self.session = Session()
        self.posts = PostsApi(host=self.host, session=self.session)
        # не добавляется лог при упавшем запросе (при 404)
        self.session.hooks['response'] = [check_status, log_response]


if __name__ == '__main__':
    client = Client("https://jsonplaceholder.typicode.com/asd/asd")
    print(client.posts.host)

# todo как написать плагин к пайтесту
# todo библиотеки для ассертов (assertpy)
# todo библиотека Faker
# todo примеры использования allure
# todo setupPy что такое и как использовать
