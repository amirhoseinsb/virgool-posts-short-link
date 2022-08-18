#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 20:23:02 2022

@author: amir
"""
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
from banner import BANNER_VPSL,FILESAVE
from sys import exit
from pathlib import Path

class VirgoolPostsShortLink:
    def __init__(self):
        self.file_name = input(BANNER_VPSL)
        self.check_exit()
        # self.file_save_name = input(f'\n{FILESAVE}')
    
    
    def file_input(self):
        self.postslink = []
        with open(f'./{self.file_name}/{self.file_name}.txt','r') as file:
            for link in file:
                self.postslink.append(link.replace("\n",""))
    
    def request_to_site(self):
        print('\n status for request to site \n')
        self.result = []
        for link in tqdm(self.postslink):
            session = requests.session()
            session.headers.update({'User-Agent':'Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36'})
            response = session.get(link).content
            self.result.append(response)
            session.close()
            
    def extract_link(self):
        print('\n status for extract link \n')
        self.shorts_link_with_title = []
        self.links = []
        for result in tqdm(self.result):
            soup = BeautifulSoup(result,'html.parser')
            title = soup.select_one('h1')
            short_link = soup.select_one('.shorturl-input > span')
            self.shorts_link_with_title.append(f'{title.contents[0]}\n{short_link.contents[0]}')
            self.links.append(short_link.contents[0])
    
    def write_in_disk(self):
        print('\n status for write in disk \n')
        
        path = Path(f'./{self.file_name}_short')
        path.mkdir(parents=True, exist_ok=True)
        
        with open(f'./{self.file_name}_short/{self.file_name}_with_title.txt','w') as file:
            for link in tqdm(self.shorts_link_with_title):
                file.writelines(f'{link}\n')

        with open(f'./{self.file_name}_short/{self.file_name}_slv.txt','w') as file :
            for link in tqdm(self.links):
                file.writelines(f'{link}\n')
        print(f'''
              
1 : link save in the file {self.file_name}_slv.txt
---------------------------------------------------------
2 : link and title save in the file {self.file_name}_with_title.txt ! ''')
   
    def check_exit(self):
        if self.file_name.lower() == 'x':
            exit()
        else :
            pass

