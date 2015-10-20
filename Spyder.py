# -*-coding:utf-8-*-
__author__ = 'adair'
import socket
url = ''
graped_dir = ''
graped_list = []
url_list = []
socket.setdefaulttimeout(10)

# now lets begin graping

# I have to say something on internet is a problem

# lets try something in localhost

def get_url(url:str)->list(str):
    '''
    this function will generate a list contains a serial of url included by one url.
    :param url:str
    :return:list contains str
    '''
    pass

def open_with_header(url:str,header:dict)->str:
    '''
    this function will open a url with header
    :param url: str
    :param header: dict
    :return:str
    '''
    pass

def generate_headers()->dict:
    '''
    generate dict as header for open_with_header
    :return:dict
    '''
    pass

def restore_file(path:str)->None:
    '''
    Restore file which given
    :param path:str
    :return:
    '''

def create_path(path:str)->None:
    '''
    generate path given as arguments
    :param path: str
    :return:None
    '''
    pass

if __name__ == '__main__':
    url_list= get_url(open_with_header(url))
    while url_list:
        url=url_list.pop()
        if url in graped_list:
            continue
        
