'''
            Copyright (c) 2022 HOStudio123(ChenJinlin) ,
                      All Rights Reserved.
'''
# -*- coding:utf-8 -*-
import setuptools
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name = 'HOPYBOX',
    version = '1.6.6',
    author = 'ChenJinlin',
    author_email = 'hostudio.hopybox@foxmail.com',
    description = 'This is an open source, practical command Python box',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/HOStudio123/HOPYBOX',
    packages = setuptools.find_packages(),
    license = 'GPL-3.0-or-later',
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    entry_points = {
            "console_scripts":[
                "hopybox = hopybox:pattern",
                "HOPYBOX = hopybox:pattern",
                ]
            },
    python_requires = '>=3.7',
    install_requires = ['wget>=3.2','bs4==0.0.1','requests','lxml>=4.6.3','filetype','yagmail','rich>=12.5.1','chardet>=4.0.0','ipython>=8.3.0']    
)