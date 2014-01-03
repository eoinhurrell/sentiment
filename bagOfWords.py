#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Module to provide basic sentiment analysis for given text.

Author: Eoin Hurrell <UltimateHurl@gmail.com>
Created: 13-12-27

"""
import sys
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

POSFILE = os.path.join(__location__, 'wordlists/positive-words.txt')
POSWORDS = []
NEGFILE = os.path.join(__location__, 'wordlists/negative-words.txt')
NEGWORDS = []


def loadSentiment():
    global POSWORDS
    global NEGWORDS
    for line in open(POSFILE, 'r'):
        word = line.strip().decode('utf-8')
        POSWORDS.append(word)
    for line in open(NEGFILE, 'r'):
        word = line.strip().decode('utf-8')
        NEGWORDS.append(word)

def calculateBOWSentiment(text):
    global HITS
    text = text
    pos = 0
    neg = 0
    for x in POSWORDS:
        hitCount = text.count(x + ' ')
        pos += hitCount
    for x in NEGWORDS:
        hitCount = text.count(x + ' ')
        neg += hitCount
    return pos - neg


def getPositiveBOWTerms(text):
    hits = []
    for x in POSWORDS:
        if (x  + ' ') in text and x not in hits:
            hits.append(x)
    return hits


def getNegativeBOWTerms(text):
    hits = []
    for x in NEGWORDS:
        if (x  + ' ') in text and x not in hits:
            hits.append(x)
    return hits


loadSentiment()
