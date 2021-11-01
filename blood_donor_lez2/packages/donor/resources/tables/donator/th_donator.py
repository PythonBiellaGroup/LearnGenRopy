#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fullname')
        r.fieldcell('@card_id.@birthplace_id.denominazione', name='Birthplace')
        r.fieldcell('@card_id.gender')
        r.fieldcell('@card_id.birthdate')
        r.fieldcell('@card_id.telephone')
        r.fieldcell('@card_id.email')
        r.fieldcell('job')
        r.fieldcell('journal_request', semaphore=True)
        r.fieldcell('news_request', semaphore=True)
        r.fieldcell('@card_id.address')
        r.fieldcell('@card_id.@city_id.denominazione', name='City')
        r.fieldcell('@card_id.fiscal_code')
        r.fieldcell('blood_group_code', width='8em')
        r.fieldcell('department_id')
        r.fieldcell('first_donation_date')
        r.fieldcell('last_donation_date')
        r.fieldcell('is_active', semaphore=True)
        r.fieldcell('donations_number')
        r.fieldcell('notes')

    def th_order(self):
        return 'fullname'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.borderContainer(region='top', height='50%', datapath='.record')
        card_fb = top.roundedGroupFrame(region='left', width='50%', title='Donor Card', datapath='.@anagrafica_id').formbuilder(
                                        cols=2, border_spacing='4px')
        card_fb.textbox('^.name', lbl='!![en]Name')
        card_fb.textbox('^.surname', lbl='!![en]Surname')
        card_fb.dbselect('^.birthplace_id', lbl='!![en]Birthplace', table='glbl.comune')
        card_fb.filteringSelect('^.gender',lbl='!![en]Gender', values='M:Male,F:Female' )
        card_fb.datetextbox('^.birthdate', lbl='!![en]Birthdate')
        card_fb.textbox('^.telephone', lbl='!![en]Phone')
        card_fb.textbox('^.email', lbl='!![en]E-mail')
        card_fb.textbox('^.address', lbl='!![en]Address')
        card_fb.dbselect('^.city_id', lbl='!![en]City', table='glbl.comune')
        card_fb.textbox('^.fiscal_code', lbl='!![en]Fiscal code')
       
        data_fb = top.roundedGroupFrame(region='center', title='Donor Data').formbuilder(
                                        cols=2, border_spacing='4px')
        data_fb.field('user_id' )
        data_fb.field('blood_group_code')
        data_fb.field('department_id')
        data_fb.field('job')
        data_fb.field('journal_request')
        data_fb.field('news_request' )
        data_fb.field('notes')

        tc = bc.tabContainer(region='center')
        tc.contentPane(title='Donations').dialogTableHandler(relation='@donations')
        tc.contentPane(title='Analysis').dialogTableHandler(relation='@analysis')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
