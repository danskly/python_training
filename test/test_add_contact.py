# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Vvvv", middlename="xxx", lastname="rty", nickname="uiop", tittle="hjkl",
                            company="ghjkl", address="fghjkl; 56", home="6789900", mobile="5678900",
                            email="dfgh@ghjk.mn", bday="10", bmonth="October", byear="1980", address2="fghhjjjh"))
    app.logout()

