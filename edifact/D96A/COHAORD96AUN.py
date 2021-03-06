#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD96AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 9},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 9, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 9},
    ]},
    {ID: 'EQD', MIN: 1, MAX: 999, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 9},
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'GOR', MIN: 0, MAX: 9},
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'TDT', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
        {ID: 'NAD', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'CNT', MIN: 1, MAX: 1},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
