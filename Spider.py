# -*-coding:utf-8-*-
import re

__author__ = 'adair'
import socket
import sys
import os
import urllib.request
import urllib.parse
import http
url = ''
graped_dir = ''
site_name=''
graped_list = []
url_list = []
socket.setdefaulttimeout(10)


# now lets begin graping

# I have to say something on internet is a problem

# lets try something in localhost

def get_url(url: str) -> list:
    '''
    this function will generate a list contains a serial of url included by one url.
    :param url:str
    :return:list contains str
    '''
    pass


def open_with_header(url: str, header: dict) -> str:
    '''
    this function will open a url with header
    :param url: str
    :param header: dict
    :return:str
    '''

    pass


def retrieve_with_header(url: str, header: dict) -> bytes:
    '''
    return byte which can write into files, which always full file.
    :param url: string : file url
    :param header : dict
    :return:bytes
    '''


def generate_headers() -> dict:
    '''
    generate dict as header for open_with_header
    :return:dict
    '''
    header_list=[
        {

        },
        {

        },
        {

        },
        {

        }
    ]
    pass


def restore_file(url: str, path: str) -> None:
    '''
    Restore file which given as url
    :param url: str
    :param path:str
    :return:
    '''
    create_path(path)
    open(path,'wb').write(retrieve_with_header(url,generate_headers()))



def create_path(path: str) -> None:
    '''
    generate path given as arguments
    :param path: str
    :return:None
    '''
    if re.match('.+?/\..+?',path):
        path=os.path.dirname(path)
    if os.path.exists(path):
        return 1
    elif not os.path.exists(os.path.dirname(path)):
        create_path(os.path.dirname(path))
        create_path(path)
    else:
        os.mkdir(path)


if __name__ == '__main__':
    url_list.extend(get_url(open_with_header(url, generate_headers())))
    while url_list:
        url = url_list.pop()
        if url in graped_list:
            continue
        if url.endswith('.html'):
            url_list.extend(get_url(open_with_header(url, generate_headers())))
        elif url.endswith('js') or url.endswith('css') or url.endswith('jpg') or url.endswith('png') or url.endswith(
                'gif') or url.endswith('bmp'):
            restore_file(url)
        else:
            open('logs', 'a').write('{} is not one of the setting'.format(url))
