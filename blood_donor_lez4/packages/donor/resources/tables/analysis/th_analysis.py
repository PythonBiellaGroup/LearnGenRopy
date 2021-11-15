#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('reference_num')
        r.fieldcell('donator_id')
        r.fieldcell('analysis_type_id')
        r.fieldcell('date')
        r.fieldcell('next_check')
        r.fieldcell('notes')

    def th_order(self):
        return 'reference_num'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('reference_num' )
        fb.field('donator_id' )
        fb.field('analysis_type_id' )
        fb.field('date' )
        fb.field('next_check' )
        fb.field('notes' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )

#Definizione di una classe Form alternativa utilizzata in th_donator
class FormFromDonator(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('reference_num' )
        fb.field('analysis_type_id' )
        fb.field('date' )
        fb.field('next_check' )
        fb.field('notes' )


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
