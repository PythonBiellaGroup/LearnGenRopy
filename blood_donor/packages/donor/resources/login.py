# -*- coding: UTF-8 -*-

from gnr.web.gnrwebpage import BaseComponent
        
class LoginComponent(BaseComponent):
    '''
    Mixin del modulo login base per gestire hard multi-tenant
    hook onAuthenticating_nomepackage
    utente autenticato -> avatar
    '''
    
    def onAuthenticating_donor(self, avatar, rootenv=None):
        # Lettura department_id dell'utente e settaggio nelle variabili di sessione (rootenv)
        department_id = self.db.table('donor.staff').readColumns(where='$user_id=:u_id', 
                            u_id=avatar.user_id, columns='$department_id')
        donator_id = self.db.table('donor.donator').readColumns(where='$user_id=:u_id',
                            u_id=avatar.user_id, columns='$id')
        rootenv['current_department_id'] = department_id
        rootenv['current_donator_id'] = donator_id