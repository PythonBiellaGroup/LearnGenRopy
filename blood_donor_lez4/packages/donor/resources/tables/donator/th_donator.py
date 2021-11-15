#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('fullname')
        r.fieldcell('@card_id.@birthplace_id.denominazione', name='Birthplace')
        r.fieldcell('@card_id.gender', width='6em')
        r.fieldcell('@card_id.birthdate')
        r.fieldcell('@card_id.email', width='18em')
        r.fieldcell('journal_request', semaphore=True, width='6em')
        r.fieldcell('news_request', semaphore=True, width='6em')
        r.fieldcell('@card_id.@city_id.denominazione', name='City')
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
        return dict(column='fullname', op='contains', val='')



class Form(BaseComponent):
    py_requires='card_form:CardForm'

    def th_form(self, form):
        bc = form.center.borderContainer()
        top = bc.borderContainer(region='top', height='40%', splitter=True, datapath='.record')
        card_pane = top.roundedGroupFrame(region='left', width='70%', title='Donor Card')
        self.cardForm(card_pane)

        data_fb = top.roundedGroupFrame(region='center', title='Donor Data').formbuilder(
                                        cols=1, border_spacing='4px')
        data_fb.field('user_id' )
        data_fb.field('blood_group_code')
        data_fb.field('department_id')
        data_fb.field('job')
        data_fb.field('journal_request')
        data_fb.field('news_request' )
        data_fb.field('notes')

        tc = bc.tabContainer(region='center')
        tc.contentPane(title='Donations').inlineTableHandler(relation='@donations', viewResource='ViewEdit')
        tc.contentPane(title='Analysis').dialogTableHandler(relation='@analysis', formResource='FormFromDonator')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )