#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 19:30:54 2022

@author: amir
"""
from vpl import VirgoolPostsLink
from vpsl import VirgoolPostsShortLink
from banner import WELCOME
from sys import exit 

def run_vpl():
    post = VirgoolPostsLink()    
    post.request_to_site()    
    post.scroll_down()    
    post.find_links()    
    post.extract_link()    
    post.write_in_disk()    
    post.close_driver()

def run_vpsl():
    post = VirgoolPostsShortLink()
    post.file_input()
    post.request_to_site()
    post.extract_link()
    post.write_in_disk()
    
if __name__ == '__main__':
    _ = input(WELCOME)
    if _.lower() == 'x':
        exit()
    elif int(_) == 1:
        run_vpl()
    elif int(_) == 2:
        run_vpsl()

