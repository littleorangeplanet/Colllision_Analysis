'''
This package inits a user interaction system, displaying relevant tables, maps, figures, 
or descriptions according to commands entered by user.
'''
#"WN_User_Interact"
#if __name__ == '__main__':

from .Interaction_Modules  import ProgramIntroduction
from .Interaction_Modules import Mainmenu,SetTimeInterval
import os
def User_Interaction(dirname):
    ProgramIntroduction()
    TimeBegin,TimeEnd, SavePath = SetTimeInterval(dirname)
    print('Finish Interaction!')
