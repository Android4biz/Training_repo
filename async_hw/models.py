from tortoise import fields, Tortoise
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    email = fields.TextField()


class Post(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
    body = fields.TextField()



class Todos(Model):
    id = fields.IntField(pk=True)
    title = fields.TextField()
