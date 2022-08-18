#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 01:46:51 2022

@author: amir
"""
from selenium import webdriver

PATH = './chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

URL = 'https://virgool.io/@'
