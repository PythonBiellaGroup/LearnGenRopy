#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('registration_num')
        r.fieldcell('user_id')
        r.fieldcell('card_id')
        r.fieldcell('blood_group_code')
        r.fieldcell('department_id')
        r.fieldcell('job')
        r.fieldcell('journal_request')
        r.fieldcell('news_request')
        r.fieldcell('notes')

    def th_order(self):
        return 'registration_num' 

    def th_query(self):
        return dict(column='registration_num', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=1, border_spacing='4px')
        fb.field('registration_num', readOnly=True)
        fb.field('user_id')
        fb.textbox(value='^.card_id', lbl='Card id')
        fb.field('blood_group_code')
        fb.field('department_id')
        fb.field('job')
        fb.field('journal_request')
        fb.field('news_request')
        fb.field('notes')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
