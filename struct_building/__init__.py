'''
This package builds the fundamental data structure for the whole project.
Loading data from documents about monthly NYPD Motor Vehicle Collisions in whole NYC.
Building Classes for each precinct.
Building Classes for Information of Collisions happened in different intersections, highways, tunnels and bridges
'''

import sys
import os
from inspect import getsourcefile
from os.path import abspath
from struct_building.LoadingANDBuilding import load_data
from CheckandError.DefinedError import ExitALLProgram,WrongFilePathError
def StructureBuilding(TimeBegin,TimeEnd,path):
    '''
    Args:
        TimeBegin: Loading data from. format:[YYYY,M] example:[2015,1]
        TimeEnd: Loading data end in. format:[YYYY,M] example:[2016,2]
        path: data path
    return:
        city object
    Raise:
        FileNotFoundError
    '''
    try:
        print('Loading data and initiating the system...... ')
        DataPath=''.join([path,'/NYPD_DATA/'])
        while True:
            try:
                NYC = load_data(DataPath,TimeBegin,TimeEnd)
                return NYC
            except FileNotFoundError:
                print("FILE NOT FOUND! or FILE INCOMPLETED!")
                DataPath=input("Please Reset the data path to (Example: .../NYPD_DATA/):")
                if DataPath=='Exit':
                    raise ExitALLProgram               
    except EOFError:
        pass

    
