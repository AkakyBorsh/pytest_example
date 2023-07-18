import pytest
from assertpy import assert_that
from requests import HTTPError


@pytest.mark.commenttest
def test_get_comment_for_nonexistent_post(example_service_client):
    assert_that(example_service_client.posts.get_post).raises(HTTPError).when_called_with(1123123)


@pytest.mark.commenttest
def test_post_id_in_comment(example_service_client):
    response = example_service_client.posts.get_comments(1)
    assert_that(response).extracting("postId").contains(1)


@pytest.mark.commenttest
def test_list_of_comments_does_not_contain_dupliceates(example_service_client):
    response = example_service_client.posts.get_comments(1)
    assert_that(response).extracting("id").does_not_contain_duplicates()


@pytest.mark.parametrize('comment_id', [1, 2])
def test_get_some_comment(example_service_client, comment_id):
    response = example_service_client.posts.get_comments(comment_id)
    assert_that(response).extracting("postId").contains(comment_id)


@pytest.mark.skip('unimplemented')
def test_example_of_skipped_test():
    pass