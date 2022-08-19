#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 22:04:46 2022

@author: amir
"""
from selenium import webdriver

from time import sleep
from config import PATH,options,URL
from sys import exit
from banner import BANNER_VPL,BANNER_VPSL
from tqdm import tqdm
from pathlib import Path

class VirgoolPostsLink:
    def __init__(self):
        self.user_name = input(BANNER_VPL)
        self.check_exit()
        
    def request_to_site(self):
        print('\n status for request to site \n')
        for i in tqdm(range(1)):
            self.driver = webdriver.Chrome(PATH, chrome_options=options)
            self.driver.get(f'{URL}{self.user_name}')
            sleep(3)
        
    def scroll_down(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        while True:

            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            # Wait to load page
            sleep(1)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            
    def find_links(self):
        print('\n status for find link in the site\n')

        for i in tqdm(range(1)):
            self.title = self.driver.find_elements_by_css_selector('h3')
            self.item_link = self.driver.find_elements_by_css_selector('.streamItem--cover')


    def extract_link(self): 
        self.links = []
        self.slv = []
        counter = 1

        for (i,j) in zip(self.item_link,self.title):
            t = j.text
            link = i.get_attribute('href')
            # print(f'{t} \n {counter}: {link}')
            if 'https://virgool.io' in link :
                self.links.append(f'{t}\n {counter}: {link}')
                self.slv.append(link)
                counter+=1
            else :
                pass
    def write_in_disk(self):
        print('\n status for write in disk \n')
        path = Path(f'./VirgoolLinks/{self.user_name}_link')
        path.mkdir(parents=True, exist_ok=True)
        
        with open(f'./VirgoolLinks/{self.user_name}_link/{self.user_name}_title.txt','w') as f:
            for i in tqdm(self.links):
                f.write(f'{i}\n')
                
        with open(f'./VirgoolLinks/{self.user_name}_link/{self.user_name}_link.txt','w') as f:
            for i in tqdm(self.slv):
                f.write(f'{i}\n')
        print(f'''
{self.user_name}_link directory created

1 : link save in the file {self.user_name}_link.txt
------------------------------------------------------
2 : link and title save in the file {self.user_name}_title.txt ! ''')
              
    def close_driver(self):
        self.driver.close()
        
    def check_exit(self):
        if self.user_name.lower() == 'x':
            exit()
        else :
            pass
        
