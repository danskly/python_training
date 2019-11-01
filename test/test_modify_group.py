# _*_ coding: utf-8 _*_
from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='text', header='test', footer='jest'))
    app.group.modify_first_group(Group(name='test', header='fest', footer='rest'))
