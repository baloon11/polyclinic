# coding: utf-8
from fitness_test import settings
from django import forms
import os

class CalendarWidget(forms.TextInput):
    '''
    Данный виджет является, практически, копией
    django.contrib.admin.widgets.AdminDateWidget
    Но наследование от AdminDateWidget не удалось из-за неверного
    порядка JS-файлов в результирующем html, при наследовании.

    Для работы необходимо в urls.py добавить:
    (r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    '''

    class Media:
        js = ('/admin/jsi18n/',
              # settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              # settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              # settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js"
                os.path.join(settings.BASE_DIR, 'static/admin/js/core.js'),
                os.path.join(settings.BASE_DIR, 'static/admin/js/calendar.js'),
                os.path.join(settings.BASE_DIR, 'static/admin/js/admin/DateTimeShortcuts.js'),
              )

        css = {
            'all': (
                # settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                # settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                # settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',
                os.path.join(settings.BASE_DIR, 'static/admin/css/forms.css'),
                os.path.join(settings.BASE_DIR, 'static/admin/css/base.css'),
                os.path.join(settings.BASE_DIR, 'static/admin/css/widgets.css'),
                )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField', 'size': '10'})