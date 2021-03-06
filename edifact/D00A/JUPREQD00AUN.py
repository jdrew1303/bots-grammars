#Generated by bots open source edi translator from UN-docs.
from bots.botsconfig import *
from edifact import syntax
from recordsD00AUN import recorddefs


structure = [
{ID: 'UNH', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BGM', MIN: 1, MAX: 1},
    {ID: 'DTM', MIN: 1, MAX: 99},
    {ID: 'MOA', MIN: 0, MAX: 99},
    {ID: 'GIS', MIN: 0, MAX: 99},
    {ID: 'FTX', MIN: 0, MAX: 99},
    {ID: 'RFF', MIN: 0, MAX: 99, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
        {ID: 'CTA', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
    ]},
    {ID: 'DOC', MIN: 0, MAX: 999, LEVEL: [
        {ID: 'GIS', MIN: 0, MAX: 99},
        {ID: 'RFF', MIN: 0, MAX: 99},
        {ID: 'DTM', MIN: 0, MAX: 99},
        {ID: 'MOA', MIN: 0, MAX: 99},
        {ID: 'FTX', MIN: 0, MAX: 99},
        {ID: 'NAD', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'FII', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
        ]},
        {ID: 'DMS', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'NAD', MIN: 0, MAX: 99},
        ]},
        {ID: 'TAX', MIN: 1, MAX: 99, LEVEL: [
            {ID: 'MOA', MIN: 0, MAX: 99},
        ]},
        {ID: 'FOR', MIN: 0, MAX: 99, LEVEL: [
            {ID: 'GIS', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'RTE', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99},
            {ID: 'TAX', MIN: 0, MAX: 99},
            {ID: 'IND', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'RTE', MIN: 0, MAX: 99},
            ]},
        ]},
        {ID: 'LIN', MIN: 0, MAX: 999, LEVEL: [
            {ID: 'PIA', MIN: 0, MAX: 99},
            {ID: 'QTY', MIN: 0, MAX: 99},
            {ID: 'DTM', MIN: 0, MAX: 99},
            {ID: 'TAX', MIN: 0, MAX: 99},
            {ID: 'RTE', MIN: 0, MAX: 99},
            {ID: 'DMS', MIN: 0, MAX: 99},
            {ID: 'RFF', MIN: 0, MAX: 99},
            {ID: 'GIS', MIN: 0, MAX: 99},
            {ID: 'MOA', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'CUX', MIN: 0, MAX: 99},
                {ID: 'PAI', MIN: 0, MAX: 99},
            ]},
            {ID: 'NAD', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'FII', MIN: 0, MAX: 99},
            ]},
            {ID: 'FOR', MIN: 0, MAX: 99, LEVEL: [
                {ID: 'GIS', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'MOA', MIN: 0, MAX: 99},
            ]},
            {ID: 'ARD', MIN: 1, MAX: 99, LEVEL: [
                {ID: 'MOA', MIN: 0, MAX: 99},
                {ID: 'DTM', MIN: 0, MAX: 99},
                {ID: 'TAX', MIN: 0, MAX: 99},
                {ID: 'SEQ', MIN: 0, MAX: 99, LEVEL: [
                    {ID: 'GIS', MIN: 0, MAX: 99},
                    {ID: 'DTM', MIN: 0, MAX: 99},
                    {ID: 'MOA', MIN: 0, MAX: 99},
                    {ID: 'RFF', MIN: 0, MAX: 99},
                ]},
            ]},
        ]},
    ]},
    {ID: 'UNT', MIN: 1, MAX: 1},
]},
]
