#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:24:35 2017

@author: jenkinsc11
"""

def read_FASTA_strings(filename):
    with open(filename) as file:
        return file.read().split('>')[1:]

def read_FASTA_entries(filename):
    return [seq.partition('\n') for seq in read_FASTA_strings(filename)]
    
def read_FASTA_sequences(filename):
    return [[seq[0], seq[2].replace('\n', '')]           
             for seq in read_FASTA_entries(filename)]
