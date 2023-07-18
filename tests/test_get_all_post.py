def test_count_of_posts(example_service_client):
    response = example_service_client.posts.get_all()
    assert len(response) == 100
