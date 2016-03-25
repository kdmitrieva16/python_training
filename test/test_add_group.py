# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="gggg", header="hhhh", footer="hhhhyyy"))

def test_add__empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

