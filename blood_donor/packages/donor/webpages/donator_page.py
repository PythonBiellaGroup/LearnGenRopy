# -*- coding: utf-8 -*-
from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
            
class GnrCustomWebPage(object):
    py_requires='th/th:TableHandler'
    
    def main(self, root, **kwargs):
        bc = root.borderContainer(region='center')
      
        bc.contentPane(region='center').thFormHandler(table='donor.donator', datapath='main.donator', 
                           startKey=self.db.currentEnv.get('current_donator_id'),
                           showtoolbar=False)
                           #, formResource='FormPaginaDonator')
        bc.contentPane(region='bottom', height='30px').button('Esci').dataController('genro.logout();')

