import pytest
from requests import HTTPError


def test_smoke_get_one_post(example_service_client):
    assert example_service_client.posts.get_post(20)


def test_post_id(example_service_client, post_id):
    response = example_service_client.posts.get_post(post_id)
    assert response.id == post_id


def test_get_not_found_error(example_service_client):
    with pytest.raises(HTTPError, match="404"):
        example_service_client.posts.get_post(100000)
