# -*- coding: UTF-8 -*-
            
class GnrCustomWebPage(object):
    py_requires = "gnrcomponents/testhandler:TestHandlerBase"

    def test_1_formDonatore(self,pane,**kwargs):
        fb = pane.formbuilder(datapath='.record', cols=1)
        fb.dbSelect(table='donor.card', value='^.id', lbl='Card')
        fb.dbSelect(table='donor.donator_blood_group', value='^.blood_group_code', lbl='Blood group')
        fb.checkbox(value='^.news_request', lbl='News request')
    
    def test_2_formSmart(self, pane):
        fb = pane.formbuilder(datapath='.record', cols=1, table='donor.donator')
        fb.field('card_id')
        fb.field('blood_group_code')
        fb.field('news_request')
