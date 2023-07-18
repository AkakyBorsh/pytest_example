from attr import attrs, attrib
from attr.validators import instance_of


@attrs()
class Post:
    userId = attrib(type=int, validator=instance_of(int))
    id = attrib(type=int)
    title = attrib(type=str)
    body = attrib(type=str)


@attrs()
class PostRequest:
    userId = attrib(type=int, validator=instance_of(int))
    title = attrib(type=str)
    body = attrib(type=str)

@attrs()
class Comment:
    postId = attrib(type=int, validator=instance_of(int))
    id = attrib(type=int)
    name = attrib(type=str)
    email = attrib(type=str)
    body = attrib(type=str)
