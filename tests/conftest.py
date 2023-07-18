from pytest import fixture, hookimpl
from random import randint
from utils.client import Client


@hookimpl
def pytest_addoption(parser):
    parser.addoption("--example_host", action="store",
                     default="https://jsonplaceholder.typicode.com")


@fixture()
def post_id():
    return randint(1, 100)


@fixture()
def example_service_client(request):
    return Client(request.config.getoption("--example_host"))
