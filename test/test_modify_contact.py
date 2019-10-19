# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.modify(Contact(firstname="Leonardo", middlename="", lastname="Davinci", nickname="genius", tittle="innovator",
                               company="ip", address="Florence", home="", mobile="",
                               email="", bday="15", bmonth="April", byear="1452", address2="Italy"))
    app.session.logout()
