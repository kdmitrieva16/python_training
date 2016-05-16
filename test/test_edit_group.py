from model.group import Group
import random

def test_edit_group_name(app,db):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group=random.choice(old_groups)
    group_data = Group(name="New group")
    #group.id = old_groups[group].id
    app.group.edit_group_by_id(group.id, group_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[group]=group_data
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_edit_first_group_header(app):
#    if app.group.count() == 0:
#     app.group.create(Group(name="test"))
 #   old_groups = app.group.get_group_list()
  #  app.group.edit_first_group(Group(header="New header"))
   # new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

