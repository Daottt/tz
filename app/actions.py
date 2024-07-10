from objectpack.ui import ModelEditWindow
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .ui import PermissionAddWindow, UserAddWindow

class ContentTypePack(ObjectPack):

    model = ContentType

    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True
    

    
class ContentUser(ObjectPack):

    model = User

    add_window = UserAddWindow
    edit_window = UserAddWindow

    add_to_desktop = True
    add_to_menu = True

class ContentGroup(ObjectPack):

    model = Group

    add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_desktop = True
    add_to_menu = True

class ContentPermission(ObjectPack):

    model = Permission

    add_window = PermissionAddWindow
    edit_window = PermissionAddWindow

    add_to_desktop = True
    add_to_menu = True
