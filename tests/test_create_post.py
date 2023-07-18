from assertpy import assert_that

from utils import models


def test_create_post(example_service_client, faker):
    req = models.PostRequest(
        userId=faker.pyint(min_value=0, max_value=10),
        title=faker.text(max_nb_chars=5),
        body=faker.text(max_nb_chars=100)
    )

    res = example_service_client.posts.create_post(req=req)

    assert_that(res).extracting('title').contains(req.title)
    assert_that(res).extracting('userId').contains(req.userId)
    assert_that(res).extracting('userId').contains(req.userId)
    assert_that(res).extracting('body').contains(req.body)
