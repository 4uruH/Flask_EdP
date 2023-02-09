from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models.author import Author
from blog.schemas.author import AuthorSchema


class AuthorList(ResourceList):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorSchema
    data_layer = {
        'session': db.session,
        'model': Author,
    }