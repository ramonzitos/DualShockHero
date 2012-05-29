from distutils.core import setup
import py2exe

'''
Created on 27/05/2012

@author: Administrador
'''

setup(console=['__init__.py'], options={
                                        "py2exe":{"optimize": 2,
                                                  "bundle_files": 1,
                                                  "compressed": True}}, zipfile=None)