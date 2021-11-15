#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('parent_id')
        r.fieldcell('description')
        r.fieldcell('hierarchical_description')
        r.fieldcell('_parent_h_description')
        r.fieldcell('hierarchical_pkey')
        r.fieldcell('_parent_h_pkey')

    def th_order(self):
        return 'parent_id'

    def th_query(self):
        return dict(column='parent_id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('parent_id')
        fb.field('description')
        fb.field('hierarchical_description')
        fb.field('_parent_h_description')
        fb.field('hierarchical_pkey')
        fb.field('_parent_h_pkey')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px', hierarchical=True)
