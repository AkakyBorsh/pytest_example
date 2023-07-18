from utils.base_api import BaseApi
from utils.models import Post, PostRequest, Comment
from attr import asdict


class PostsApi(BaseApi):

    def get_post(self, post_id):
        self.url.path.segments = ['posts', post_id]
        return Post(**self.session.get(self.url).json())

    def get_all(self):
        return [Post(**kv) for kv in self.session.get(f'{self.host}/posts').json()]

    def get_comments(self, post_id):
        return [Comment(**kv) for kv in self.session.get(f'{self.host}/posts/{post_id}/comments').json()]

    def create_post(self, req: PostRequest):
        # return [Post(**kv) for kv in self.session.post(f'{self.host}/posts', json=asdict(req))]
        # ]{'userId': 1, 'title': 'test_title', 'body': 'test_body', 'id': 101}
        return Post(**self.session.post(f'{self.host}/posts', json=asdict(req)).json())

    # def get_comments(self, post_id):
    #     return [Comment(id=1, postId=1, name="test", email="test@test.com", body="body"),
    #             Comment(id=1, postId=1, name="test", email="test@test.com", body="body")]
