#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('name')
        r.fieldcell('surname')
        r.fieldcell('birthplace_id')
        r.fieldcell('gender')
        r.fieldcell('birthdate')
        r.fieldcell('telephone')
        r.fieldcell('email')
        r.fieldcell('address')
        r.fieldcell('city_id')
        r.fieldcell('fiscal_code')

    def th_order(self):
        return 'name'

    def th_query(self):
        return dict(column='name', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        center = bc.contentPane(region='center')
        fb = center.formbuilder(cols=2, border_spacing='4px')
        fb.field('name')
        fb.field('surname')
        fb.field('birthplace_id')
        fb.field('gender')
        fb.field('birthdate')
        fb.field('telephone')
        fb.field('email')
        fb.field('address')
        fb.field('city_id')
        fb.field('fiscal_code')
        fb.div('^.@donator.registration_num')

        right = bc.contentPane(region='right', width='100px', margin='10px')
        right.img(src='^.profile_photo', edit=True, crop_width='100px', crop_height='100px', 
                        placeholder=True, upload_folder='site:avatar', upload_filename='=.id')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
