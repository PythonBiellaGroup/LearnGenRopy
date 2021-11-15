# encoding: utf-8

from gnr.web.gnrbaseclasses import BaseComponent

#Creando un component possiamo richiamare un blocco di codice al bisogno
class CardForm(BaseComponent):
    
    def cardForm(self, pane):
        bc = pane.borderContainer(datapath='.@card_id')
        center = bc.contentPane(region='center')
        #Passando la table al formbuilder, possiamo sfruttare la "magia" del field
        fb = center.formbuilder(cols=2, border_spacing='4px', table='donor.card')
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

        right = bc.contentPane(region='right', width='100px', margin='10px')
        right.img(src='^.profile_photo', edit=True, crop_width='100px', crop_height='100px', 
                        placeholder=True, upload_folder='site:avatar', upload_filename='=.id')