#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('registration_num',width='6em')
        r.fieldcell('fullname')
        r.fieldcell('@card_id.@birthplace_id.denominazione', name='Birthplace')
        r.fieldcell('@card_id.gender', width='6em')
        r.fieldcell('@card_id.birthdate',width='8em')
        r.fieldcell('@card_id.email', width='18em')
        r.fieldcell('journal_request', semaphore=True, width='6em')
        r.fieldcell('news_request', semaphore=True, width='6em')
        r.fieldcell('@card_id.@city_id.denominazione', name='City')
        r.fieldcell('blood_group_code', width='8em')
        r.fieldcell('first_donation_date',width='8em')
        r.fieldcell('last_donation_date',width='8em')
        r.fieldcell('is_active', semaphore=True)
        r.fieldcell('donations_number',width='8em')
        r.fieldcell('notes')

    def th_order(self):
        return 'fullname'

    def th_queryBySample(self):
        return dict(fields=[dict(field='fullname', lbl='!![en]Name/Surname', width='15em'),
                            dict(field='id', lbl='!![en]Reg.num.', tag='dbSelect', 
                                    table='donor.donator', columns='$registration_num,$fullname', 
                                    auxColumns='$registration_num,$fullname'),
                            dict(field='department_id', lbl='!![en]Department', hasDownArrow=True)
                            ], cols=3, isDefault=True)

    def th_sections_active_donators(self):
        return [dict(code='all',caption='All'),
                dict(code='active',caption='Only active',condition='$is_active IS TRUE')]

    def th_top_toolbar(self,top):
        top.slotToolbar('5,sections@active_donators,*,sections@blood_group_code,5',
                            childname='superiore',_position='<bar')

    # Gestione muti-tenant
    def th_options(self):
        return dict(partitioned=True)    

class Form(BaseComponent):
    py_requires='card_form:CardForm,gnrcomponents/attachmanager/attachmanager:AttachManager'

    def th_form(self, form):
        bc = form.center.borderContainer()
        
        # Parte superiore della form
        top = bc.borderContainer(region='top', height='40%', splitter=True, datapath='.record')
        
        # Parte sinistra del top: dati Card
        card_pane = top.roundedGroupFrame(region='left', width='70%')
        self.cardForm(card_pane, title="Donator Card", rel_name="donator")

        # Parte destra (center) del top: dati Card
        center = top.borderContainer(region='center')
        # Per user_id -> linkerBox
        center.contentPane(region='top', height='90px').linkerBox('user_id', openIfEmpty=True,
                           dialog_height='400px',
                           dialog_width='650px', formResource='Form', label='User info',
                           default_firstname="=#FORM.record.@card_id.name",
                           default_lastname="=#FORM.record.@card_id.surname",
                           default_email="=#FORM.record.@card_id.email",
                           default_status="conf",
                           default_group_code="D"
                           )
        fb = center.contentPane(region='center').formbuilder(cols=1)
        # department_id non inserito per la gestione multi-tenant        
        fb.field('blood_group_code')
        fb.field('job')
        fb.field('journal_request')
        fb.field('news_request' )
        fb.field('notes')

        # Parte inferiore della form
        tc = bc.tabContainer(region='center')
        tc.contentPane(title='Donations').dialogTableHandler(relation='@donations', viewResource='ViewEdit')
        tc.contentPane(title='Analysis').dialogTableHandler(relation='@analysis', formResource='FormFromDonator')
        self.donatorAttachments(tc.contentPane(title='Attachments'))

    def donatorAttachments(self, pane):
        pane.attachmentMultiButtonFrame()

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )