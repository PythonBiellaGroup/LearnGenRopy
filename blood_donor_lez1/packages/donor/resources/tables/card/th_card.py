#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name')
        r.fieldcell('surname')
        r.fieldcell('birthdate')
        r.fieldcell('phone')
        r.fieldcell('email')
        r.fieldcell('birthplace')
        r.fieldcell('address')
        r.fieldcell('city_code')
        r.fieldcell('fiscal_code')
        r.fieldcell('genre')

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='surname', op='contains', val='')

class ViewSimpatica(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name')

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('name' )
        fb.field('surname' )
        fb.field('birthdate' )
        fb.field('phone' )
        fb.field('email' )
        fb.field('birthplace' )
        fb.field('address' )
        fb.field('city_code' )
        fb.field('fiscal_code' )
        fb.field('genre' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
