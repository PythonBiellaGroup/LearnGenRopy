# -*- coding: utf-8 -*-
            
class GnrCustomWebPage(object):
    #py_requires = 'plainindex'
    py_requires = 'frameindex'
    index_url = 'html_pages/splashscreen.html'
    def loginSubititlePane(self,pane):#here you can define the sub title as you required a 
        pane.div('Blood Donor App',
                    text_align='center',
                    font_size='.9em',
                    font_style='italic',color='#AAAAAA')   
    