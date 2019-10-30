# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(firstname='text'))
    app.contact.modify_first_contact(
        Contact(firstname="Leonardo", middlename="", lastname="Davinci", nickname="genius", tittle="innovator",
                company="ip", address="Florence", home="", mobile="",
                email="", bday="15", bmonth="April", byear="1452", address2="Italy"))
