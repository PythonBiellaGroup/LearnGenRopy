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
        card_pane = top.contentPane(region='left', width='70%')
        # Evoluzioni Donor #1
        self.cardForm(card_pane, title="Staff Card", rel_name="staff")
        # center = top.roundedGroupFrame(region='center', title='Staff Data')
        center = top.borderContainer(region='center')
        center.contentPane(region='top', height='90px').linkerBox('user_id', openIfEmpty=True,
                           dialog_height='400px',
                           dialog_width='650px', formResource='Form', label='User info',
                           default_firstname="=#FORM.record.@card_id.name",
                           default_lastname="=#FORM.record.@card_id.surname",
                           default_email="=#FORM.record.@card_id.email"
                           )
        fb = center.contentPane(region='center').formbuilder(cols=1)
        fb.field('department_id')
        fb.field('is_active')

        bc.contentPane(region='center')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
