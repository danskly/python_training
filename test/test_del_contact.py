# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Vvvv", middlename="xxx", lastname="rty", nickname="uiop", tittle="hall",
        company="ghoul", address="fghjkl; 56", home="6789900", mobile="5678900",
        email="dfgh@ghjk.mn", bday="10", bmonth="October", byear="1980", address2="fghhjjjh"))
    app.contact.delete_first_contact()
