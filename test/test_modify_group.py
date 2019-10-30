# _*_ coding: utf-8 _*_
from model.group import Group


def test_modify_first_group(app):
    if app.group.count == 0:
        app.group.create(Group(name='text'))
    app.group.modify_first_group(Group(name="Top", header="Start", footer="Stop"))
