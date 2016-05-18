# -*- coding: utf-8 -*-
from model.group import Group
import pytest



def test_add_group(app, db, json_groups, check_ui):
    group=json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When i add a group %s to the list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            ui_list=app.group.get_group_list()
            def clean(group):
                return Group(id=group.id, name=group.name.strip())
            db_list=map(clean, new_groups)
            assert sorted(db_list, key=Group.id_or_max) == sorted(ui_list, key=Group.id_or_max)

