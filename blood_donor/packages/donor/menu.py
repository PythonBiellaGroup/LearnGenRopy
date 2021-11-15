#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    donor = root.branch('Blood Donor')
    donor.thpage('!![en]Analysis',table='donor.analysis')
    donor.thpage('!![en]Analysis type',table='donor.analysis_type')
    donor.thpage('!![en]Cards',table='donor.card')
    donor.thpage('!![en]Donators',table='donor.donator')
    donor.thpage('!![en]Donations',table='donor.donation')
    donor.thpage('!![en]Departments',table='donor.department')
    donor.thpage('!![en]Staff',table='donor.staff')
    donor.lookups('!![en]Lookup tables',lookup_manager='donor')
