# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method,oncalled
from gnr.core.gnrbag import Bag

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('is_active', semaphore=True, width='5em')
        r.fieldcell('username')
        r.fieldcell('department_id')

    def th_order(self):
        return 'username'

    def th_query(self):
        return dict(column='username', op='contains', val='')

class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record.contentPane()
        fb = pane.formbuilder(cols=1)
        fb.field('user_id')
        fb.field('is_active')
        fb.field('department_id')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )