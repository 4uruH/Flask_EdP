from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models.tag import Tag
from blog.schemas.tag import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }