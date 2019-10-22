# _*_ coding: utf-8 _*_
from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="Top", header="Start", footer="Stop"))
    app.session.logout()
