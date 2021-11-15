#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('address')
        r.fieldcell('name')
        r.fieldcell('type_id')
        r.fieldcell('telephone')
        r.fieldcell('email')
        r.fieldcell('city_id')
        r.fieldcell('notes')

    def th_order(self):
        return 'address'

    def th_query(self):
        return dict(column='name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('address' )
        fb.field('name' )
        fb.field('type_id' )
        fb.field('telephone' )
        fb.field('email' )
        fb.field('city_id' )
        fb.field('notes' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
