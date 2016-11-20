#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD06BUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'CTA', MIN: 0, MAX: 9},
    {ID: 'COM', MIN: 0, MAX: 9},
    {ID: 'DTM', MIN: 0, MAX: 9},
    {ID: 'TSR', MIN: 0, MAX: 9},
    {ID: 'CUX', MIN: 0, MAX: 9},
    {ID: 'MOA', MIN: 0, MAX: 9},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'CNT', MIN: 0, MAX: 9},
    {ID: 'LOC', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
    ]},
    {ID: 'CPI', MIN: 0, MAX: 9, LEVEL: [
        {ID: 'CUX', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'MOA', MIN: 0, MAX: 9},
    ]},
    {ID: 'TDT', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 9},
        {ID: 'TSR', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'CTA', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'COM', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 9},
        ]},
    ]},
    {ID: 'GID', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'HAN', MIN: 0, MAX: 9},
        {ID: 'TMP', MIN: 0, MAX: 9},
        {ID: 'RNG', MIN: 0, MAX: 9},
        {ID: 'LOC', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'GDS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'MEA', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 9},
        ]},
        {ID: 'DIM', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 9},
        ]},
        {ID: 'RFF', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'EQN', MIN: 0, MAX: 9},
        ]},
        {ID: 'TPL', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'SGP', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 9},
            ]},
        ]},
        {ID: 'TCC', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'PRI', MIN: 0, MAX: 9},
            {ID: 'EQN', MIN: 0, MAX: 9},
            {ID: 'PCD', MIN: 0, MAX: 9},
            {ID: 'MOA', MIN: 0, MAX: 9},
            {ID: 'QTY', MIN: 0, MAX: 9},
            {ID: 'LOC', MIN: 0, MAX: 9},
            {ID: 'RFF', MIN: 0, MAX: 9},
            {ID: 'MEA', MIN: 0, MAX: 9},
            {ID: 'CUX', MIN: 0, MAX: 9},
            {ID: 'DTM', MIN: 0, MAX: 9},
            {ID: 'FTX', MIN: 0, MAX: 9},
        ]},
        {ID: 'DGS', MIN: 0, MAX: 9, LEVEL: [
            {ID: 'FTX', MIN: 0, MAX: 99},
            {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                {ID: 'EQN', MIN: 0, MAX: 1},
            ]},
            {ID: 'SGP', MIN: 0, MAX: 999, LEVEL: [
                {ID: 'MEA', MIN: 0, MAX: 9, LEVEL: [
                    {ID: 'EQN', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
    ]},
    {ID: 'EQD', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'EQN', MIN: 0, MAX: 9},
        {ID: 'FTX', MIN: 0, MAX: 9},
        {ID: 'RFF', MIN: 0, MAX: 9},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]