from bots.botsconfig import *
from records004030 import recorddefs

syntax = { 
        'version'    :  '00403',    #version of ISA to send
        'functionalgroup'    :  'BA',
        }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'M10', MIN: 1, MAX: 1},
    {ID: 'P4', MIN: 1, MAX: 20, LEVEL: [
        {ID: 'M20', MIN: 1, MAX: 9999},
    ]},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
