from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from django.contrib.contenttypes.models import ContentType


class PermissionAddWindow(BaseEditWindow):

    def _init_components(self):
        super(PermissionAddWindow, self)._init_components()
        data = [(0, '')]
        for i, j in enumerate(ContentType.objects.all(), start=1):
            data.append((i,str(j)))

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__codename = ext.ExtStringField(
            label=u'Кодовое имя',
            name='codename',
            allow_blank=False,
            anchor='100%')

        self.field__content = make_combo_box(
            label=u'Контент',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=data)

    def _do_layout(self):
        super(PermissionAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__codename,
            self.field__content,
        ))

    def set_params(self, params):
        super(PermissionAddWindow, self).set_params(params)
        self.height = 'auto'
        
class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field_password = ext.ExtStringField(
            label=u'пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field_last_login = ext.ExtDateField(
            label=u'последний вход',
            name='last_login',
            allow_blank=True,
            anchor='100%')
        
        self.field_super = ext.ExtCheckBox(
            label=u'супер пользователь',
            name='is_superuser',
            allow_blank=True,
            anchor='100%')
        
        self.field_username = ext.ExtStringField(
            label=u'логин',
            name='username',
            allow_blank=False,
            anchor='100%')
        
        self.field_name = ext.ExtStringField(
            label=u'имя',
            name='first_name',
            allow_blank=True,
            anchor='100%')
        
        self.field_lastname = ext.ExtStringField(
            label=u'фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%')
        
        self.field_email = ext.ExtStringField(
            label=u'почта',
            name='email',
            allow_blank=True,
            anchor='100%')
        
        self.field_personal_status = ext.ExtCheckBox(
            label=u'статус персонала',
            name='is_staff',
            allow_blank=True,
            anchor='100%')
        
        self.field_acative = ext.ExtCheckBox(
            label=u'активен',
            name='is_active',
            allow_blank=True,
            anchor='100%')
        
        self.field_join = ext.ExtDateField(
            label=u'дата создания',
            name='date_joined',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field_password,
            self.field_last_login,
            self.field_super,
            self.field_username,
            self.field_name,
            self.field_lastname,
            self.field_email,
            self.field_personal_status,
            self.field_acative,
            self.field_join,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'