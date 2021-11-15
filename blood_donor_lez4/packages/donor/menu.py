#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    donor = root.branch('Blood Donor')
    donor.thpage('Analysis',table='donor.analysis')
    donor.thpage('Cards',table='donor.card')
    donor.thpage('Donators',table='donor.donator')
    donor.thpage('Donations',table='donor.donation')
    donor.thpage('Departments',table='donor.department')
    donor.thpage('Staff',table='donor.staff')
    donor.lookups('Lookup tables',lookup_manager='donor')
