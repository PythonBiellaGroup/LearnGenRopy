#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('user_id')
        r.fieldcell('department_id')
        r.fieldcell('card_id')
        r.fieldcell('is_active')

    def th_order(self):
        return '@card_id.fullname'

    def th_query(self):
        return dict(column='@card_id.fullname', op='contains', val='')



class Form(BaseComponent):
    py_requires='card_form:CardForm'
    
    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.borderContainer(region='top', height='50%', datapath='.record')
        card_pane = top.roundedGroupFrame(region='left', width='70%', title='Staff Card')
        self.cardForm(card_pane)

        center = top.roundedGroupFrame(region='center', title='Staff Data')
        fb = center.formbuilder(cols=1)
        fb.field('user_id')
        fb.field('department_id')
        fb.field('is_active')

        bc.contentPane(region='center').div('Ci deve essere sempre!')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
