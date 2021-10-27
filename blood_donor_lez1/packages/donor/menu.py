#!/usr/bin/python3
# -*- coding: utf-8 -*-

def config(root,application=None):
    donor = root.branch('Donor')
    donor.thpage('!![en]Cards',table='donor.card')
