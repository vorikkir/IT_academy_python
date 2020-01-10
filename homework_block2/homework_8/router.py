#!/usr/bin/python3.7
# -*- coding: utf-8 -*-


class Router:
    """Роутер помнит каждый сохранённый путь и метод доступа к этому пут"""
    def __init__(self):
        self.repository = {}

    def add_path(self, path, method, func):
        """Добавляет соответствие переданному методу и пути нужной функции"""
        self.repository[method + path] = func

    def request(self, method, path):
        """Запрашивает функцию по переданному методу и пути и вызывает её"""
        clue = method + path
        if clue in self.repository.keys():
            return self.repository[clue](method, path)
        elif path in str(self.repository.keys()):
            return str(405) + "," + ' Error 405: Method Not Allowed'
        elif path not in self.repository.keys():
            return str(404) + "," + ' Error 404: Not Found'

    methods_list = ['get', 'post', 'post', 'patch', 'delete', 'options']

    def __getattr__(self, method):
        def wrap(*args, **kwargs):
            return self.request(method.upper(), *args, **kwargs)
        if method in self.methods_list:
            return wrap


if __name__ == "__main__":
    router = Router()

    result_fun = lambda path, method: str(200) + "," " OK"

    router.add_path('/me', 'GET', result_fun)
    router.add_path('/me', 'UPDATE', result_fun)
    router.add_path('/about', 'POST', result_fun)

    print(router.request('GET', '/me'))
    print(router.get("/me"))

    print(router.post("/me"))
    print(router.get("/us"))

    print(router.delete('/me'))
