#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Thu Sep  1 15:54:22 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'trackedMotion'  # from the Builder filename that created this script
expInfo = {
    'participant': 'Prolific ID or unique code (initials + birthday)',
    'session': '001',
    'age': '',
    'dominant hand': '',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/simonknogler/Downloads/motion_arrcues_09_12 (1)_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "beginning" ---
beginning_text = visual.TextStim(win=win, name='beginning_text',
    text='Thank you for taking part in this study.\n\nIn this task you will see an arrow. \nAnd patterns of moving dots. \n\nYou will judge which direction the dots move in,\nand rate your confidence in your choices. \n\nPress SPACE to continue.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
beginning_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Practice_instructions" ---
practice_text = visual.TextStim(win=win, name='practice_text',
    text='First we will do 10 practice trials. \n\n\nAfter the white cross disappeared you will see a pattern of moving dots. \n\nSome of the dots will move consistently LEFT or RIGHT.\nYou will have to judge which direction the dots moved in\nand will have to report how confident you are in your choice.\nUsing the 1,2,3 and 4 keys on the keyboard.\n\nYou will receive feedback on your performance.   \n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
practice_resp = keyboard.Keyboard()

# --- Initialize components for Routine "main_instructions" ---
main_text = visual.TextStim(win=win, name='main_text',
    text='Now we will begin the main task.\n\nAt the start of each trial you will see a red arrow pointing either to the LEFT or to the RIGHT. These arrows are predictive of the motion direction.\n\n\nSome of the dots will move consistently LEFT or RIGHT.\nYou will have to judge which direction the dots moved in\nand will have to report how confident you are in your choice.\nUsing the 1,2,3 and 4 keys on the keyboard.\n\nThere will be breaks throughout the task and you will be updated on how many trials you have completed. \n\nYou will no longer receive feedback on your performance. \n\nGood luck! \n\nPress SPACE to continue. ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
main_resp = keyboard.Keyboard()

# --- Initialize components for Routine "fixation" ---
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.03, 0.03),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

# --- Initialize components for Routine "trial" ---
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()
# Run 'Begin Experiment' code from code
import numpy 
win.mouseVisible = False #controls whether the cursor is visible or not 
step=.04 #spacing between two adjacent values (because there are 25 dots, the coherence values can only be set in steps of 4% (0.04)

high_signal= .8 #high motion coherence signal (80% of dots moving coherently) 
tricky_signal=.16 #tricky coherence signal (40% moving coherently) 



trial_count=0; 
d1 = visual.ShapeStim(
    win=win, name='d1',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-2.0, interpolate=True)
d2 = visual.ShapeStim(
    win=win, name='d2',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-3.0, interpolate=True)
d3 = visual.ShapeStim(
    win=win, name='d3',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
d4 = visual.ShapeStim(
    win=win, name='d4',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
d5 = visual.ShapeStim(
    win=win, name='d5',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
d6 = visual.ShapeStim(
    win=win, name='d6',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-7.0, interpolate=True)
d7 = visual.ShapeStim(
    win=win, name='d7',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-8.0, interpolate=True)
d8 = visual.ShapeStim(
    win=win, name='d8',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-9.0, interpolate=True)
d9 = visual.ShapeStim(
    win=win, name='d9',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-10.0, interpolate=True)
d10 = visual.ShapeStim(
    win=win, name='d10',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-11.0, interpolate=True)
d11 = visual.ShapeStim(
    win=win, name='d11',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-12.0, interpolate=True)
d12 = visual.ShapeStim(
    win=win, name='d12',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-13.0, interpolate=True)
d13 = visual.ShapeStim(
    win=win, name='d13',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-14.0, interpolate=True)
d14 = visual.ShapeStim(
    win=win, name='d14',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-15.0, interpolate=True)
d15 = visual.ShapeStim(
    win=win, name='d15',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-16.0, interpolate=True)
d16 = visual.ShapeStim(
    win=win, name='d16',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-17.0, interpolate=True)
d17 = visual.ShapeStim(
    win=win, name='d17',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-18.0, interpolate=True)
d18 = visual.ShapeStim(
    win=win, name='d18',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-19.0, interpolate=True)
d19 = visual.ShapeStim(
    win=win, name='d19',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-20.0, interpolate=True)
d20 = visual.ShapeStim(
    win=win, name='d20',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-21.0, interpolate=True)
d21 = visual.ShapeStim(
    win=win, name='d21',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-22.0, interpolate=True)
d22 = visual.ShapeStim(
    win=win, name='d22',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-23.0, interpolate=True)
d23 = visual.ShapeStim(
    win=win, name='d23',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-24.0, interpolate=True)
d24 = visual.ShapeStim(
    win=win, name='d24',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-25.0, interpolate=True)
d25 = visual.ShapeStim(
    win=win, name='d25',
    size=(0.01, 0.01), vertices='circle',
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-26.0, interpolate=True)

# --- Initialize components for Routine "question" ---
text = visual.TextStim(win=win, name='text',
    text='Did the dots move left or right?\n(1 = Confident L, 2 = Guess L, 3= Guess R, 4= Confident R)',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_3
con_corr_count=0
incon_corr_count=0



# --- Initialize components for Routine "feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='Placeholder',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "break_screen" ---
break_text = visual.TextStim(win=win, name='break_text',
    text='You have completed 0 out of 400 trials.\n\nPress SPACE to Continue',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_resp = keyboard.Keyboard()

# --- Initialize components for Routine "thanks" ---
text_3 = visual.TextStim(win=win, name='text_3',
    text='This is the end of the task.\n\nPlease wait - you will be automatically redirected to Prolific to record your submission.\n\nIf you need to get in touch, please email Helen Olawole-Scott (holaw001@gold.ac.uk).\n\nThank you for taking part.\n',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "beginning" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
beginning_resp.keys = []
beginning_resp.rt = []
_beginning_resp_allKeys = []
# keep track of which components have finished
beginningComponents = [beginning_text, beginning_resp]
for thisComponent in beginningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "beginning" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *beginning_text* updates
    if beginning_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginning_text.frameNStart = frameN  # exact frame index
        beginning_text.tStart = t  # local t and not account for scr refresh
        beginning_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginning_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'beginning_text.started')
        beginning_text.setAutoDraw(True)
    
    # *beginning_resp* updates
    waitOnFlip = False
    if beginning_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        beginning_resp.frameNStart = frameN  # exact frame index
        beginning_resp.tStart = t  # local t and not account for scr refresh
        beginning_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(beginning_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'beginning_resp.started')
        beginning_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(beginning_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(beginning_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if beginning_resp.status == STARTED and not waitOnFlip:
        theseKeys = beginning_resp.getKeys(keyList=['space'], waitRelease=False)
        _beginning_resp_allKeys.extend(theseKeys)
        if len(_beginning_resp_allKeys):
            beginning_resp.keys = _beginning_resp_allKeys[-1].name  # just the last key pressed
            beginning_resp.rt = _beginning_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "beginning" ---
for thisComponent in beginningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if beginning_resp.keys in ['', [], None]:  # No response was made
    beginning_resp.keys = None
thisExp.addData('beginning_resp.keys',beginning_resp.keys)
if beginning_resp.keys != None:  # we had a response
    thisExp.addData('beginning_resp.rt', beginning_resp.rt)
thisExp.nextEntry()
# the Routine "beginning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blocks09_12.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "Practice_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    practice_resp.keys = []
    practice_resp.rt = []
    _practice_resp_allKeys = []
    # Run 'Begin Routine' code from code_12
    if blockCode!=1:
       continueRoutine=False 
       
      
    # keep track of which components have finished
    Practice_instructionsComponents = [practice_text, practice_resp]
    for thisComponent in Practice_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Practice_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practice_text* updates
        if practice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.tStart = t  # local t and not account for scr refresh
            practice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_text.started')
            practice_text.setAutoDraw(True)
        
        # *practice_resp* updates
        waitOnFlip = False
        if practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            practice_resp.frameNStart = frameN  # exact frame index
            practice_resp.tStart = t  # local t and not account for scr refresh
            practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(practice_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'practice_resp.started')
            practice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(practice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if practice_resp.status == STARTED and not waitOnFlip:
            theseKeys = practice_resp.getKeys(keyList=['space'], waitRelease=False)
            _practice_resp_allKeys.extend(theseKeys)
            if len(_practice_resp_allKeys):
                practice_resp.keys = _practice_resp_allKeys[-1].name  # just the last key pressed
                practice_resp.rt = _practice_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Practice_instructions" ---
    for thisComponent in Practice_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if practice_resp.keys in ['', [], None]:  # No response was made
        practice_resp.keys = None
    blocks.addData('practice_resp.keys',practice_resp.keys)
    if practice_resp.keys != None:  # we had a response
        blocks.addData('practice_resp.rt', practice_resp.rt)
    # the Routine "Practice_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "main_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    main_resp.keys = []
    main_resp.rt = []
    _main_resp_allKeys = []
    # Run 'Begin Routine' code from code_6
    if blockCode!=2:
       continueRoutine=False 
     
    
    # keep track of which components have finished
    main_instructionsComponents = [main_text, main_resp]
    for thisComponent in main_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "main_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_text* updates
        if main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_text.frameNStart = frameN  # exact frame index
            main_text.tStart = t  # local t and not account for scr refresh
            main_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_text.started')
            main_text.setAutoDraw(True)
        
        # *main_resp* updates
        waitOnFlip = False
        if main_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            main_resp.frameNStart = frameN  # exact frame index
            main_resp.tStart = t  # local t and not account for scr refresh
            main_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(main_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'main_resp.started')
            main_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(main_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(main_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if main_resp.status == STARTED and not waitOnFlip:
            theseKeys = main_resp.getKeys(keyList=['space'], waitRelease=False)
            _main_resp_allKeys.extend(theseKeys)
            if len(_main_resp_allKeys):
                main_resp.keys = _main_resp_allKeys[-1].name  # just the last key pressed
                main_resp.rt = _main_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in main_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "main_instructions" ---
    for thisComponent in main_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if main_resp.keys in ['', [], None]:  # No response was made
        main_resp.keys = None
    blocks.addData('main_resp.keys',main_resp.keys)
    if main_resp.keys != None:  # we had a response
        blocks.addData('main_resp.rt', main_resp.rt)
    # the Routine "main_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=blockReps, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('trial.xlsx', selection=rowsUsed),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "fixation" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        if blockCode>1:
            continueRoutine=False #feedback is only given on practice trials
        # keep track of which components have finished
        fixationComponents = [polygon]
        for thisComponent in fixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation" ---
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + .5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation" ---
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # setup some python lists for storing info about the mouse
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code
        if blockCode>1: #decides whether the block is a practice or test block. Calls variable from 'motionBlocks' spreadsheet. 1=practice, 2=deterministic cue, 3=test phase
            trial_count=trial_count+1 #will only count trials if it's in the test phase
            #d1.fillColor = ([0.5608, -0.8353, 0.0431]); d1.lineColor = ([0.5608, -0.8353, 0.0431]);
            #d2.fillColor = ([0.5608, -0.8353, 0.0431]); d1.lineColor = ([0.5608, -0.8353, 0.0431]);
            #d3.fillColor = ([0.5608, -0.8353, 0.0431]); d1.lineColor = ([0.5608, -0.8353, 0.0431]);
            #d4.fillColor = ([0.5608, -0.8353, 0.0431]); d1.lineColor = ([0.5608, -0.8353, 0.0431]);
            #d5.fillColor = ([0.5608, -0.8353, 0.0431]); d1.lineColor = ([0.5608, -0.8353, 0.0431]);
            
        
            
        
                
            
            
        frame=0
        mouse_x=[0]*10000
        mouse_y = [0]*10000
        r=0.15 #radius
        d=r*2 #diameter
        
        #setting the intial position of the 25 dots. REMEMBER we are working in radians, rather than degrees 
        d1_angle = 2*3.14*numpy.random.rand() #direction the dot will move in. 2*pi*redius value will give an angle value and therefore a direction that the dot will move in
        rand_ang = 2*3.14*numpy.random.rand() #random angle
        d1_dist = (d*numpy.random.rand())-r
        d1_x = (numpy.cos(rand_ang)*d1_dist) #funky maths to get the x and y coordinates for the dot
        d1_y = (numpy.sin(rand_ang)*d1_dist)
        d1.setPos([d1_x,d1_y]) #original position of the dot
        
        d2_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d2_dist = (d*numpy.random.rand())-r
        d2_x = (numpy.cos(rand_ang)*d2_dist)
        d2_y = (numpy.sin(rand_ang)*d2_dist)
        d2.setPos([d2_x,d2_y])
        
        d3_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d3_dist = (d*numpy.random.rand())-r
        d3_x = (numpy.cos(rand_ang)*d3_dist)
        d3_y = (numpy.sin(rand_ang)*d3_dist)
        d3.setPos([d3_x,d3_y])
        
        
        d4_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d4_dist = (d*numpy.random.rand())-r
        d4_x = (numpy.cos(rand_ang)*d4_dist)
        d4_y = (numpy.sin(rand_ang)*d4_dist)
        d4.setPos([d4_x,d4_y])
        
        d5_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d5_dist = (d*numpy.random.rand())-r
        d5_x = (numpy.cos(rand_ang)*d5_dist)
        d5_y = (numpy.sin(rand_ang)*d5_dist)
        d5.setPos([d5_x,d5_y])
        
        d6_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d6_dist = (d*numpy.random.rand())-r
        d6_x = (numpy.cos(rand_ang)*d6_dist)
        d6_y = (numpy.sin(rand_ang)*d6_dist)
        d6.setPos([d6_x,d6_y])
        
        d7_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d7_dist = (d*numpy.random.rand())-r
        d7_x = (numpy.cos(rand_ang)*d7_dist)
        d7_y = (numpy.sin(rand_ang)*d7_dist)
        d7.setPos([d7_x,d7_y])
        
        d8_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d8_dist = (d*numpy.random.rand())-r
        d8_x = (numpy.cos(rand_ang)*d8_dist)
        d8_y = (numpy.sin(rand_ang)*d8_dist)
        d8.setPos([d8_x,d8_y])
        
        d9_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d9_dist = (d*numpy.random.rand())-r
        d9_x = (numpy.cos(rand_ang)*d9_dist)
        d9_y = (numpy.sin(rand_ang)*d9_dist)
        d9.setPos([d9_x,d9_y])
        
        d10_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d10_dist = (d*numpy.random.rand())-r
        d10_x = (numpy.cos(rand_ang)*d10_dist)
        d10_y = (numpy.sin(rand_ang)*d10_dist)
        d10.setPos([d10_x,d10_y])
        
        d11_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d11_dist = (d*numpy.random.rand())-r
        d11_x = (numpy.cos(rand_ang)*d11_dist)
        d11_y = (numpy.sin(rand_ang)*d11_dist)
        d11.setPos([d11_x,d11_y])
        
        d12_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d12_dist = (d*numpy.random.rand())-r
        d12_x = (numpy.cos(rand_ang)*d12_dist)
        d12_y = (numpy.sin(rand_ang)*d12_dist)
        d12.setPos([d12_x,d12_y])
        
        d13_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d13_dist = (d*numpy.random.rand())-r
        d13_x = (numpy.cos(rand_ang)*d13_dist)
        d13_y = (numpy.sin(rand_ang)*d13_dist)
        d13.setPos([d13_x,d13_y])
        
        d14_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d14_dist = (d*numpy.random.rand())-r
        d14_x = (numpy.cos(rand_ang)*d14_dist)
        d14_y = (numpy.sin(rand_ang)*d14_dist)
        d14.setPos([d14_x,d14_y])
        
        d15_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d15_dist = (d*numpy.random.rand())-r
        d15_x = (numpy.cos(rand_ang)*d15_dist)
        d15_y = (numpy.sin(rand_ang)*d15_dist)
        d15.setPos([d15_x,d15_y])
        
        d16_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d16_dist = (d*numpy.random.rand())-r
        d16_x = (numpy.cos(rand_ang)*d16_dist)
        d16_y = (numpy.sin(rand_ang)*d16_dist)
        d16.setPos([d16_x,d16_y])
        
        d17_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d17_dist = (d*numpy.random.rand())-r
        d17_x = (numpy.cos(rand_ang)*d17_dist)
        d17_y = (numpy.sin(rand_ang)*d17_dist)
        d17.setPos([d17_x,d17_y])
        
        d18_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d18_dist = (d*numpy.random.rand())-r
        d18_x = (numpy.cos(rand_ang)*d18_dist)
        d18_y = (numpy.sin(rand_ang)*d18_dist)
        d18.setPos([d18_x,d18_y])
        
        d19_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d19_dist = (d*numpy.random.rand())-r
        d19_x = (numpy.cos(rand_ang)*d19_dist)
        d19_y = (numpy.sin(rand_ang)*d19_dist)
        d19.setPos([d19_x,d19_y])
        
        d20_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d20_dist = (d*numpy.random.rand())-r
        d20_x = (numpy.cos(rand_ang)*d20_dist)
        d20_y = (numpy.sin(rand_ang)*d20_dist)
        d20.setPos([d20_x,d20_y])
        
        d21_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d21_dist = (d*numpy.random.rand())-r
        d21_x = (numpy.cos(rand_ang)*d21_dist)
        d21_y = (numpy.sin(rand_ang)*d21_dist)
        d21.setPos([d21_x,d21_y])
        
        d22_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d22_dist = (d*numpy.random.rand())-r
        d22_x = (numpy.cos(rand_ang)*d22_dist)
        d22_y = (numpy.sin(rand_ang)*d22_dist)
        d22.setPos([d22_x,d22_y])
        
        d23_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d23_dist = (d*numpy.random.rand())-r
        d23_x = (numpy.cos(rand_ang)*d23_dist)
        d23_y = (numpy.sin(rand_ang)*d23_dist)
        d23.setPos([d23_x,d23_y])
        
        d24_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d24_dist = (d*numpy.random.rand())-r
        d24_x = (numpy.cos(rand_ang)*d24_dist)
        d24_y = (numpy.sin(rand_ang)*d24_dist)
        d24.setPos([d24_x,d24_y])
        
        d25_angle = 2*3.14*numpy.random.rand()
        rand_ang = 2*3.14*numpy.random.rand()
        d25_dist = (d*numpy.random.rand())-r
        d25_x = (numpy.cos(rand_ang)*d25_dist)
        d25_y = (numpy.sin(rand_ang)*d25_dist)
        d25.setPos([d25_x,d25_y])
        
        
        # There are two conditions. 
        # 1. High motion coherence (h_signal) corresponding to a strength value of  1
        # 2. Low motion coherence  (l_signal) corresponding to a strength value of -1
        # h_signal and l_signal are defined in the -Begin Experiment- section.
        
        #if strength==1: 
        #    signal = h_signal
        #if strength==-1:
        #    signal = l_signal
        
        if blockCode == 1: 
            signal = high_signal 
        if blockCode > 1: 
            signal = tricky_signal 
        
        
        
        #This section decides how many and which dots will move coherently
        if signal>=1*step: #e.g. if the signal was 0.8, this is >1*step (1*0.04)= 0.04. 
            d1_angle=0 #...therefore, d1_angle (or direction the dot will move in) will be changed to 0 (originally randomly set above). 0 = moving directly along the x axis.
        if signal>=2*step:
            d2_angle=0 #as soon as a threshold is reached (decided by signal), the dots will move in the random direction the variable d1_angle was originally allocated
        if signal>=3*step:
            d3_angle=0
        if signal>=4*step:
            d4_angle=0
        if signal>=5*step:
            d5_angle=0
        if signal>=6*step:
            d6_angle=0
        if signal>=7*step:
            d7_angle=0
        if signal>=8*step:
            d8_angle=0
        if signal>=9*step:
            d9_angle=0
        if signal>=10*step:
            d10_angle=0
        if signal>=11*step:
            d11_angle=0
        if signal>=12*step:
            d12_angle=0
        if signal>=13*step:
            d13_angle=0
        if signal>=14*step:
            d14_angle=0
        if signal>=15*step:
            d15_angle=0
        if signal>=16*step:
            d16_angle=0
        if signal>=17*step:
            d17_angle=0
        if signal>=18*step:
            d18_angle=0
        if signal>=19*step:
            d19_angle=0
        if signal>=20*step:
            d20_angle=0
        if signal>=21*step:
            d21_angle=0
        if signal>=22*step:
            d22_angle=0
        if signal>=23*step:
            d23_angle=0
        if signal>=24*step:
            d24_angle=0
        if signal>=25*step:
            d25_angle=0
        thisExp.addData('signal', signal) #saving out the data
        
        
        # keep track of which components have finished
        trialComponents = [mouse, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "trial" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            if mouse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > mouse.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    mouse.tStop = t  # not accounting for scr refresh
                    mouse.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('mouse.stopped', t)
                    mouse.status = FINISHED
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        continueRoutine = False  # abort routine on response            # Run 'Each Frame' code from code
            frame=frame+1
            #Speed variable = how much the dot moves in each frame (pos no.= move right, neg no.=move left)
            speed = 0.01*direction #direction variable defined in motion trials spreadsheet
            
            #dot 1
            d1_p = d1.pos
            d1_x = d1_p[0]+(numpy.cos(d1_angle)*speed) #how much we are adding to x and y coordinates to decide the final location 
            d1_y = d1_p[1]+(numpy.sin(d1_angle)*speed)
            
            #below makes sure that the dot doesn't leave the ring, if it does go outside the ring the code will just draw the dot randomly somewhere else and then repeat the loop for each frame until the presentation time is over
            if ((d1_p[0]**2)+(d1_p[1]**2))**.5 >r:
                d1_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d1_x = (numpy.cos(rand_ang)*d1_dist)
                d1_y = (numpy.sin(rand_ang)*d1_dist)
                d1.setPos([d1_x,d1_y])
            else:
                d1.setPos([d1_x,d1_y])
            #dot2
            d2_p = d2.pos
            d2_x = d2_p[0]+(numpy.cos(d2_angle)*speed)
            d2_y = d2_p[1]+(numpy.sin(d2_angle)*speed)
            
            if ((d2_p[0]**2)+(d2_p[1]**2))**.5 >r:
                d2_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d2_x = (numpy.cos(rand_ang)*d2_dist)
                d2_y = (numpy.sin(rand_ang)*d2_dist)
                d2.setPos([d2_x,d2_y])
            else:
                d2.setPos([d2_x,d2_y])
            #dot3
            d3_p = d3.pos
            d3_x = d3_p[0]+(numpy.cos(d3_angle)*speed)
            d3_y = d3_p[1]+(numpy.sin(d3_angle)*speed)
            
            if ((d3_p[0]**2)+(d3_p[1]**2))**.5 >r:
                d3_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d3_x = (numpy.cos(rand_ang)*d3_dist)
                d3_y = (numpy.sin(rand_ang)*d3_dist)
                d3.setPos([d3_x,d3_y])
            else:
                d3.setPos([d3_x,d3_y])
                
            #dot4
            d4_p = d4.pos
            d4_x = d4_p[0]+(numpy.cos(d4_angle)*speed)
            d4_y = d4_p[1]+(numpy.sin(d4_angle)*speed)
            
            if ((d4_p[0]**2)+(d4_p[1]**2))**.5 >r:
                d4_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d4_x = (numpy.cos(rand_ang)*d4_dist)
                d4_y = (numpy.sin(rand_ang)*d4_dist)
                d4.setPos([d4_x,d4_y])
            else:
                d4.setPos([d4_x,d4_y])
            
            #dot5
            d5_p = d5.pos
            d5_x = d5_p[0]+(numpy.cos(d5_angle)*speed)
            d5_y = d5_p[1]+(numpy.sin(d5_angle)*speed)
            
            if ((d5_p[0]**2)+(d5_p[1]**2))**.5 >r:
                d5_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d5_x = (numpy.cos(rand_ang)*d5_dist)
                d5_y = (numpy.sin(rand_ang)*d5_dist)
                d5.setPos([d5_x,d5_y])
            else:
                d5.setPos([d5_x,d5_y])
            
            #dot6
            d6_p = d6.pos
            d6_x = d6_p[0]+(numpy.cos(d6_angle)*speed)
            d6_y = d6_p[1]+(numpy.sin(d6_angle)*speed)
            
            if ((d6_p[0]**2)+(d6_p[1]**2))**.5 >r:
                d6_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d6_x = (numpy.cos(rand_ang)*d6_dist)
                d6_y = (numpy.sin(rand_ang)*d6_dist)
                d6.setPos([d6_x,d6_y])
            else:
                d6.setPos([d6_x,d6_y])
            
            #dot7
            d7_p = d7.pos
            d7_x = d7_p[0]+(numpy.cos(d7_angle)*speed)
            d7_y = d7_p[1]+(numpy.sin(d7_angle)*speed)
            
            if ((d7_p[0]**2)+(d7_p[1]**2))**.5 >r:
                d7_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d7_x = (numpy.cos(rand_ang)*d7_dist)
                d7_y = (numpy.sin(rand_ang)*d7_dist)
                d7.setPos([d7_x,d7_y])
            else:
                d7.setPos([d7_x,d7_y])
            
            #dot8
            d8_p = d8.pos
            d8_x = d8_p[0]+(numpy.cos(d8_angle)*speed)
            d8_y = d8_p[1]+(numpy.sin(d8_angle)*speed)
            
            if ((d8_p[0]**2)+(d8_p[1]**2))**.5 >r:
                d8_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d8_x = (numpy.cos(rand_ang)*d8_dist)
                d8_y = (numpy.sin(rand_ang)*d8_dist)
                d8.setPos([d8_x,d8_y])
            else:
                d8.setPos([d8_x,d8_y])
            
            #dot9
            d9_p = d9.pos
            d9_x = d9_p[0]+(numpy.cos(d9_angle)*speed)
            d9_y = d9_p[1]+(numpy.sin(d9_angle)*speed)
            
            if ((d9_p[0]**2)+(d9_p[1]**2))**.5 >r:
                d9_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d9_x = (numpy.cos(rand_ang)*d9_dist)
                d9_y = (numpy.sin(rand_ang)*d9_dist)
                d9.setPos([d9_x,d9_y])
            else:
                d9.setPos([d9_x,d9_y])
            
            #dot10
            d10_p = d10.pos
            d10_x = d10_p[0]+(numpy.cos(d10_angle)*speed)
            d10_y = d10_p[1]+(numpy.sin(d10_angle)*speed)
            
            if ((d10_p[0]**2)+(d10_p[1]**2))**.5 >r:
                d10_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d10_x = (numpy.cos(rand_ang)*d10_dist)
                d10_y = (numpy.sin(rand_ang)*d10_dist)
                d10.setPos([d10_x,d10_y])
            else:
                d10.setPos([d10_x,d10_y])
            
            #dot11
            d11_p = d11.pos
            d11_x = d11_p[0]+(numpy.cos(d11_angle)*speed)
            d11_y = d11_p[1]+(numpy.sin(d11_angle)*speed)
            
            if ((d11_p[0]**2)+(d11_p[1]**2))**.5 >r:
                d11_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d11_x = (numpy.cos(rand_ang)*d11_dist)
                d11_y = (numpy.sin(rand_ang)*d11_dist)
                d11.setPos([d11_x,d11_y])
            else:
                d11.setPos([d11_x,d11_y])
            
            #dot12
            d12_p = d12.pos
            d12_x = d12_p[0]+(numpy.cos(d12_angle)*speed)
            d12_y = d12_p[1]+(numpy.sin(d12_angle)*speed)
            
            if ((d12_p[0]**2)+(d12_p[1]**2))**.5 >r:
                d12_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d12_x = (numpy.cos(rand_ang)*d12_dist)
                d12_y = (numpy.sin(rand_ang)*d12_dist)
                d12.setPos([d12_x,d12_y])
            else:
                d12.setPos([d12_x,d12_y])
            
            #dot13
            d13_p = d13.pos
            d13_x = d13_p[0]+(numpy.cos(d13_angle)*speed)
            d13_y = d13_p[1]+(numpy.sin(d13_angle)*speed)
            
            if ((d13_p[0]**2)+(d13_p[1]**2))**.5 >r:
                d13_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d13_x = (numpy.cos(rand_ang)*d13_dist)
                d13_y = (numpy.sin(rand_ang)*d13_dist)
                d13.setPos([d13_x,d13_y])
            else:
                d13.setPos([d13_x,d13_y])
            
            #dot14
            d14_p = d14.pos
            d14_x = d14_p[0]+(numpy.cos(d14_angle)*speed)
            d14_y = d14_p[1]+(numpy.sin(d14_angle)*speed)
            
            if ((d14_p[0]**2)+(d14_p[1]**2))**.5 >r:
                d14_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d14_x = (numpy.cos(rand_ang)*d14_dist)
                d14_y = (numpy.sin(rand_ang)*d14_dist)
                d14.setPos([d14_x,d14_y])
            else:
                d14.setPos([d14_x,d14_y])
            
            #dot15
            d15_p = d15.pos
            d15_x = d15_p[0]+(numpy.cos(d15_angle)*speed)
            d15_y = d15_p[1]+(numpy.sin(d15_angle)*speed)
            
            if ((d15_p[0]**2)+(d15_p[1]**2))**.5 >r:
                d15_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d15_x = (numpy.cos(rand_ang)*d15_dist)
                d15_y = (numpy.sin(rand_ang)*d15_dist)
                d15.setPos([d15_x,d15_y])
            else:
                d15.setPos([d15_x,d15_y])
            
            #dot16
            d16_p = d16.pos
            d16_x = d16_p[0]+(numpy.cos(d16_angle)*speed)
            d16_y = d16_p[1]+(numpy.sin(d16_angle)*speed)
            
            if ((d16_p[0]**2)+(d16_p[1]**2))**.5 >r:
                d16_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d16_x = (numpy.cos(rand_ang)*d16_dist)
                d16_y = (numpy.sin(rand_ang)*d16_dist)
                d16.setPos([d16_x,d16_y])
            else:
                d16.setPos([d16_x,d16_y])
            
            #dot17
            d17_p = d17.pos
            d17_x = d17_p[0]+(numpy.cos(d17_angle)*speed)
            d17_y = d17_p[1]+(numpy.sin(d17_angle)*speed)
            
            if ((d17_p[0]**2)+(d17_p[1]**2))**.5 >r:
                d17_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d17_x = (numpy.cos(rand_ang)*d17_dist)
                d17_y = (numpy.sin(rand_ang)*d17_dist)
                d17.setPos([d17_x,d17_y])
            else:
                d17.setPos([d17_x,d17_y])
            
            #dot18
            d18_p = d18.pos
            d18_x = d18_p[0]+(numpy.cos(d18_angle)*speed)
            d18_y = d18_p[1]+(numpy.sin(d18_angle)*speed)
            
            if ((d18_p[0]**2)+(d18_p[1]**2))**.5 >r:
                d18_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d18_x = (numpy.cos(rand_ang)*d18_dist)
                d18_y = (numpy.sin(rand_ang)*d18_dist)
                d18.setPos([d18_x,d18_y])
            else:
                d18.setPos([d18_x,d18_y])
            
            #dot19
            d19_p = d19.pos
            d19_x = d19_p[0]+(numpy.cos(d19_angle)*speed)
            d19_y = d19_p[1]+(numpy.sin(d19_angle)*speed)
            
            if ((d19_p[0]**2)+(d19_p[1]**2))**.5 >r:
                d19_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d19_x = (numpy.cos(rand_ang)*d19_dist)
                d19_y = (numpy.sin(rand_ang)*d19_dist)
                d19.setPos([d19_x,d19_y])
            else:
                d19.setPos([d19_x,d19_y])
            
            #dot20
            d20_p = d20.pos
            d20_x = d20_p[0]+(numpy.cos(d20_angle)*speed)
            d20_y = d20_p[1]+(numpy.sin(d20_angle)*speed)
            
            if ((d20_p[0]**2)+(d20_p[1]**2))**.5 >r:
                d20_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d20_x = (numpy.cos(rand_ang)*d20_dist)
                d20_y = (numpy.sin(rand_ang)*d20_dist)
                d20.setPos([d20_x,d20_y])
            else:
                d20.setPos([d20_x,d20_y])
            
            #dot21
            d21_p = d21.pos
            d21_x = d21_p[0]+(numpy.cos(d21_angle)*speed)
            d21_y = d21_p[1]+(numpy.sin(d21_angle)*speed)
            
            if ((d21_p[0]**2)+(d21_p[1]**2))**.5 >r:
                d21_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d21_x = (numpy.cos(rand_ang)*d21_dist)
                d21_y = (numpy.sin(rand_ang)*d21_dist)
                d21.setPos([d21_x,d21_y])
            else:
                d21.setPos([d21_x,d21_y])
            
            #dot22
            d22_p = d22.pos
            d22_x = d22_p[0]+(numpy.cos(d22_angle)*speed)
            d22_y = d22_p[1]+(numpy.sin(d22_angle)*speed)
            
            if ((d22_p[0]**2)+(d22_p[1]**2))**.5 >r:
                d22_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d22_x = (numpy.cos(rand_ang)*d22_dist)
                d22_y = (numpy.sin(rand_ang)*d22_dist)
                d22.setPos([d22_x,d22_y])
            else:
                d22.setPos([d22_x,d22_y])
            
            #dot23
            d23_p = d23.pos
            d23_x = d23_p[0]+(numpy.cos(d23_angle)*speed)
            d23_y = d23_p[1]+(numpy.sin(d23_angle)*speed)
            
            if ((d23_p[0]**2)+(d23_p[1]**2))**.5 >r:
                d23_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d23_x = (numpy.cos(rand_ang)*d23_dist)
                d23_y = (numpy.sin(rand_ang)*d23_dist)
                d23.setPos([d23_x,d23_y])
            else:
                d23.setPos([d23_x,d23_y])
            
            #dot24
            d24_p = d24.pos
            d24_x = d24_p[0]+(numpy.cos(d24_angle)*speed)
            d24_y = d24_p[1]+(numpy.sin(d24_angle)*speed)
            
            if ((d24_p[0]**2)+(d24_p[1]**2))**.5 >r:
                d24_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d24_x = (numpy.cos(rand_ang)*d24_dist)
                d24_y = (numpy.sin(rand_ang)*d24_dist)
                d24.setPos([d24_x,d24_y])
            else:
                d24.setPos([d24_x,d24_y])
            
            #dot25
            d25_p = d25.pos
            d25_x = d25_p[0]+(numpy.cos(d25_angle)*speed)
            d25_y = d25_p[1]+(numpy.sin(d25_angle)*speed)
            
            if ((d25_p[0]**2)+(d25_p[1]**2))**.5 >r:
                d25_dist = (d*numpy.random.rand())-r
                rand_ang = 2*3.14*numpy.random.rand()
                d25_x = (numpy.cos(rand_ang)*d25_dist)
                d25_y = (numpy.sin(rand_ang)*d25_dist)
                d25.setPos([d25_x,d25_y])
            else:
                d25.setPos([d25_x,d25_y])
            
            #dots.setSpeed(speed)
            
            # *d1* updates
            if d1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d1.frameNStart = frameN  # exact frame index
                d1.tStart = t  # local t and not account for scr refresh
                d1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd1.started')
                d1.setAutoDraw(True)
            if d1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d1.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d1.tStop = t  # not accounting for scr refresh
                    d1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd1.stopped')
                    d1.setAutoDraw(False)
            
            # *d2* updates
            if d2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d2.frameNStart = frameN  # exact frame index
                d2.tStart = t  # local t and not account for scr refresh
                d2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd2.started')
                d2.setAutoDraw(True)
            if d2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d2.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d2.tStop = t  # not accounting for scr refresh
                    d2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd2.stopped')
                    d2.setAutoDraw(False)
            
            # *d3* updates
            if d3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d3.frameNStart = frameN  # exact frame index
                d3.tStart = t  # local t and not account for scr refresh
                d3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd3.started')
                d3.setAutoDraw(True)
            if d3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d3.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d3.tStop = t  # not accounting for scr refresh
                    d3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd3.stopped')
                    d3.setAutoDraw(False)
            
            # *d4* updates
            if d4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d4.frameNStart = frameN  # exact frame index
                d4.tStart = t  # local t and not account for scr refresh
                d4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd4.started')
                d4.setAutoDraw(True)
            if d4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d4.tStop = t  # not accounting for scr refresh
                    d4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd4.stopped')
                    d4.setAutoDraw(False)
            
            # *d5* updates
            if d5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d5.frameNStart = frameN  # exact frame index
                d5.tStart = t  # local t and not account for scr refresh
                d5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd5.started')
                d5.setAutoDraw(True)
            if d5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d5.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d5.tStop = t  # not accounting for scr refresh
                    d5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd5.stopped')
                    d5.setAutoDraw(False)
            
            # *d6* updates
            if d6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d6.frameNStart = frameN  # exact frame index
                d6.tStart = t  # local t and not account for scr refresh
                d6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd6.started')
                d6.setAutoDraw(True)
            if d6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d6.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d6.tStop = t  # not accounting for scr refresh
                    d6.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd6.stopped')
                    d6.setAutoDraw(False)
            
            # *d7* updates
            if d7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d7.frameNStart = frameN  # exact frame index
                d7.tStart = t  # local t and not account for scr refresh
                d7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd7.started')
                d7.setAutoDraw(True)
            if d7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d7.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d7.tStop = t  # not accounting for scr refresh
                    d7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd7.stopped')
                    d7.setAutoDraw(False)
            
            # *d8* updates
            if d8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d8.frameNStart = frameN  # exact frame index
                d8.tStart = t  # local t and not account for scr refresh
                d8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd8.started')
                d8.setAutoDraw(True)
            if d8.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d8.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d8.tStop = t  # not accounting for scr refresh
                    d8.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd8.stopped')
                    d8.setAutoDraw(False)
            
            # *d9* updates
            if d9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d9.frameNStart = frameN  # exact frame index
                d9.tStart = t  # local t and not account for scr refresh
                d9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd9.started')
                d9.setAutoDraw(True)
            if d9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d9.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d9.tStop = t  # not accounting for scr refresh
                    d9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd9.stopped')
                    d9.setAutoDraw(False)
            
            # *d10* updates
            if d10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d10.frameNStart = frameN  # exact frame index
                d10.tStart = t  # local t and not account for scr refresh
                d10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd10.started')
                d10.setAutoDraw(True)
            if d10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d10.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d10.tStop = t  # not accounting for scr refresh
                    d10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd10.stopped')
                    d10.setAutoDraw(False)
            
            # *d11* updates
            if d11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d11.frameNStart = frameN  # exact frame index
                d11.tStart = t  # local t and not account for scr refresh
                d11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd11.started')
                d11.setAutoDraw(True)
            if d11.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d11.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d11.tStop = t  # not accounting for scr refresh
                    d11.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd11.stopped')
                    d11.setAutoDraw(False)
            
            # *d12* updates
            if d12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d12.frameNStart = frameN  # exact frame index
                d12.tStart = t  # local t and not account for scr refresh
                d12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd12.started')
                d12.setAutoDraw(True)
            if d12.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d12.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d12.tStop = t  # not accounting for scr refresh
                    d12.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd12.stopped')
                    d12.setAutoDraw(False)
            
            # *d13* updates
            if d13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d13.frameNStart = frameN  # exact frame index
                d13.tStart = t  # local t and not account for scr refresh
                d13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd13.started')
                d13.setAutoDraw(True)
            if d13.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d13.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d13.tStop = t  # not accounting for scr refresh
                    d13.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd13.stopped')
                    d13.setAutoDraw(False)
            
            # *d14* updates
            if d14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d14.frameNStart = frameN  # exact frame index
                d14.tStart = t  # local t and not account for scr refresh
                d14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd14.started')
                d14.setAutoDraw(True)
            if d14.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d14.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d14.tStop = t  # not accounting for scr refresh
                    d14.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd14.stopped')
                    d14.setAutoDraw(False)
            
            # *d15* updates
            if d15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d15.frameNStart = frameN  # exact frame index
                d15.tStart = t  # local t and not account for scr refresh
                d15.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d15, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd15.started')
                d15.setAutoDraw(True)
            if d15.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d15.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d15.tStop = t  # not accounting for scr refresh
                    d15.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd15.stopped')
                    d15.setAutoDraw(False)
            
            # *d16* updates
            if d16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d16.frameNStart = frameN  # exact frame index
                d16.tStart = t  # local t and not account for scr refresh
                d16.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d16, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd16.started')
                d16.setAutoDraw(True)
            if d16.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d16.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d16.tStop = t  # not accounting for scr refresh
                    d16.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd16.stopped')
                    d16.setAutoDraw(False)
            
            # *d17* updates
            if d17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d17.frameNStart = frameN  # exact frame index
                d17.tStart = t  # local t and not account for scr refresh
                d17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd17.started')
                d17.setAutoDraw(True)
            if d17.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d17.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d17.tStop = t  # not accounting for scr refresh
                    d17.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd17.stopped')
                    d17.setAutoDraw(False)
            
            # *d18* updates
            if d18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d18.frameNStart = frameN  # exact frame index
                d18.tStart = t  # local t and not account for scr refresh
                d18.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d18, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd18.started')
                d18.setAutoDraw(True)
            if d18.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d18.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d18.tStop = t  # not accounting for scr refresh
                    d18.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd18.stopped')
                    d18.setAutoDraw(False)
            
            # *d19* updates
            if d19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d19.frameNStart = frameN  # exact frame index
                d19.tStart = t  # local t and not account for scr refresh
                d19.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d19, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd19.started')
                d19.setAutoDraw(True)
            if d19.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d19.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d19.tStop = t  # not accounting for scr refresh
                    d19.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd19.stopped')
                    d19.setAutoDraw(False)
            
            # *d20* updates
            if d20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d20.frameNStart = frameN  # exact frame index
                d20.tStart = t  # local t and not account for scr refresh
                d20.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d20, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd20.started')
                d20.setAutoDraw(True)
            if d20.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d20.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d20.tStop = t  # not accounting for scr refresh
                    d20.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd20.stopped')
                    d20.setAutoDraw(False)
            
            # *d21* updates
            if d21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d21.frameNStart = frameN  # exact frame index
                d21.tStart = t  # local t and not account for scr refresh
                d21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d21, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd21.started')
                d21.setAutoDraw(True)
            if d21.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d21.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d21.tStop = t  # not accounting for scr refresh
                    d21.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd21.stopped')
                    d21.setAutoDraw(False)
            
            # *d22* updates
            if d22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d22.frameNStart = frameN  # exact frame index
                d22.tStart = t  # local t and not account for scr refresh
                d22.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d22, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd22.started')
                d22.setAutoDraw(True)
            if d22.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d22.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d22.tStop = t  # not accounting for scr refresh
                    d22.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd22.stopped')
                    d22.setAutoDraw(False)
            
            # *d23* updates
            if d23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d23.frameNStart = frameN  # exact frame index
                d23.tStart = t  # local t and not account for scr refresh
                d23.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d23, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd23.started')
                d23.setAutoDraw(True)
            if d23.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d23.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d23.tStop = t  # not accounting for scr refresh
                    d23.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd23.stopped')
                    d23.setAutoDraw(False)
            
            # *d24* updates
            if d24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d24.frameNStart = frameN  # exact frame index
                d24.tStart = t  # local t and not account for scr refresh
                d24.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d24, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd24.started')
                d24.setAutoDraw(True)
            if d24.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d24.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d24.tStop = t  # not accounting for scr refresh
                    d24.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd24.stopped')
                    d24.setAutoDraw(False)
            
            # *d25* updates
            if d25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                d25.frameNStart = frameN  # exact frame index
                d25.tStart = t  # local t and not account for scr refresh
                d25.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(d25, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'd25.started')
                d25.setAutoDraw(True)
            if d25.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > d25.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    d25.tStop = t  # not accounting for scr refresh
                    d25.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'd25.stopped')
                    d25.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store data for trials (TrialHandler)
        x, y = mouse.getPos()
        buttons = mouse.getPressed()
        trials.addData('mouse.x', x)
        trials.addData('mouse.y', y)
        trials.addData('mouse.leftButton', buttons[0])
        trials.addData('mouse.midButton', buttons[1])
        trials.addData('mouse.rightButton', buttons[2])
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "question" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code_3
        trial_correct=0;
        # keep track of which components have finished
        questionComponents = [text, key_resp]
        for thisComponent in questionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "question" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                text.setAutoDraw(True)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1','2','3','4'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in questionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "question" ---
        for thisComponent in questionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # Run 'End Routine' code from code_3
        if key_resp.keys == '1' or key_resp.keys=='2': #collapses across confident and guess responses for same direction just to establish a count of correct responses 
            type1_resp = -1; #leftward movement
        elif key_resp.keys == '3' or key_resp.keys=='4':
            type1_resp=1; #rightward movement 
        
        if type1_resp==direction: #If the resp is the same as the direction then the response was correct
            trial_correct=1
        else:
            trial_correct=0
        
        if key_resp.keys == '1' or key_resp.keys=='4':
            trial_conf =1
        else:
            trial_conf=2
        
        
        #if congruency==1:
        #    if trial_correct ==1:
        #        con_corr_count=con_corr_count+1
        #    if trial_correct==0:
        #        c_signal = c_signal+step
        #        con_corr_count=0
        #
        #    if con_corr_count==2:
        #        c_signal = c_signal-step
        #        con_corr_count=0
        #elif congruency==-1:
        #    if trial_correct ==1:
        #        incon_corr_count=incon_corr_count+1
        #    if trial_correct==0:
        #        i_signal = i_signal+step
        #        incon_corr_count=0
        
        #    if incon_corr_count==2:
        #        i_signal = i_signal-step
        #        incon_corr_count=0
        
        thisExp.addData('trial_correct', trial_correct)
        
        
        #if h_signal>.8:
        #    h_signal=.8
        #elif h_signal<.04:
        #    h_signal=.04
        
        #if l_signal>.8:
        #    l_signal=.8
        #elif l_signal<.04:
        #    l_signal=.04
        
        
        
        
        
        # the Routine "question" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_8
        if blockCode>1:
            continueRoutine=False #feedback is only given on practice trials
        else:
            if trial_correct ==1:
                feed_str = 'Correct!'
            elif trial_correct==0:
                feed_str = 'Incorrect'
            feedback_text.setText(feed_str)
            
            
            
        # keep track of which components have finished
        feedbackComponents = [feedback_text]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "feedback" ---
        while continueRoutine and routineTimer.getTime() < 0.75:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                feedback_text.setAutoDraw(True)
            if feedback_text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > feedback_text.tStartRefresh + .75-frameTolerance:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    feedback_text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.750000)
        
        # --- Prepare to start Routine "break_screen" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        break_resp.keys = []
        break_resp.rt = []
        _break_resp_allKeys = []
        # Run 'Begin Routine' code from code_5
        if blockCode<2 or trial_count%20!=0:
            continueRoutine= False
        else:
            break_str = 'You have completed ' +str(trial_count)+' out of 400 trials.\n\n Press SPACE to Continue'
            break_text.setText(break_str)
        # keep track of which components have finished
        break_screenComponents = [break_text, break_resp]
        for thisComponent in break_screenComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break_screen" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *break_text* updates
            if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_text.frameNStart = frameN  # exact frame index
                break_text.tStart = t  # local t and not account for scr refresh
                break_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_text.started')
                break_text.setAutoDraw(True)
            
            # *break_resp* updates
            waitOnFlip = False
            if break_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                break_resp.frameNStart = frameN  # exact frame index
                break_resp.tStart = t  # local t and not account for scr refresh
                break_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(break_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'break_resp.started')
                break_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(break_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(break_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if break_resp.status == STARTED and not waitOnFlip:
                theseKeys = break_resp.getKeys(keyList=['space'], waitRelease=False)
                _break_resp_allKeys.extend(theseKeys)
                if len(_break_resp_allKeys):
                    break_resp.keys = _break_resp_allKeys[-1].name  # just the last key pressed
                    break_resp.rt = _break_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_screenComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_screen" ---
        for thisComponent in break_screenComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if break_resp.keys in ['', [], None]:  # No response was made
            break_resp.keys = None
        trials.addData('break_resp.keys',break_resp.keys)
        if break_resp.keys != None:  # we had a response
            trials.addData('break_resp.rt', break_resp.rt)
        # the Routine "break_screen" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed blockReps repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1 repeats of 'blocks'


# --- Prepare to start Routine "thanks" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [text_3]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "thanks" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_3.started')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.stopped')
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "thanks" ---
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
