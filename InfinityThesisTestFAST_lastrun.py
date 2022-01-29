#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sat Jan 29 17:37:46 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'InfinityThesisTest5'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='/Users/sophiecb/Desktop/Thesis/ThesisTestFast/InfinityThesisTestFAST_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.0,1.0,1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Mouse"
MouseClock = core.Clock()
win.mouseVisible = True

# Initialize components for Routine "FastInstr"
FastInstrClock = core.Clock()
Instr1 = visual.TextStim(win=win, name='Instr1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
InstrResponse = keyboard.Keyboard()

# Initialize components for Routine "FastPractice"
FastPracticeClock = core.Clock()
fixcross1 = visual.ShapeStim(
    win=win, name='fixcross1', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
PracticeText = visual.TextStim(win=win, name='PracticeText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()
scaretone = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='scaretone')
scaretone.setVolume(1.0)

# Initialize components for Routine "PracticeEnd"
PracticeEndClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You have finished the trial period. You will now complete the official task. Judge the following statements as quickly as you can without sacrificing accuracy.\n\nPress ‘E’ if the statement is true and ‘I’ if the statement is false. \n\nPress E to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "FastTrial"
FastTrialClock = core.Clock()
fixcross = visual.ShapeStim(
    win=win, name='fixcross', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
Fasttext = visual.TextStim(win=win, name='Fasttext',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()
Timer = sound.Sound('A', secs=0.2, stereo=True, hamming=True,
    name='Timer')
Timer.setVolume(1.0)

# Initialize components for Routine "Demographics"
DemographicsClock = core.Clock()
win.allowStencil = True
Demographics1 = visual.Form(win=win, name='Demographics1',
    items='demotry1.xlsx',
    textHeight=0.025,
    font='Open Sans',
    randomize=False,
    style='custom...',
    fillColor=(1.0000, 1.0000, 1.0000), borderColor=None, itemColor=(-1.0000, -1.0000, -1.0000), 
    responseColor=(-1.0000, -1.0000, -1.0000), markerColor='red', colorSpace='rgb', 
    size=(1,1),
    pos=(0, 0),
    itemPadding=0.05
)
button = visual.ButtonStim(win, 
    text='Next', font='Arvo',
    pos=(0.4, -0.4),units='height',
    letterHeight=0.05,
    size=(0.3,0.1), borderWidth=0.0,
    fillColor=(-1.0000, -1.0000, -1.0000), borderColor=None,
    color=(1.0000, 1.0000, 1.0000), colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='button'
)
button.buttonClock = core.Clock()
mouse = event.Mouse(win=win)
x, y = [None, None]
mouse.mouseClock = core.Clock()

# Initialize components for Routine "EndStudy"
EndStudyClock = core.Clock()
EndStudyText = visual.TextStim(win=win, name='EndStudyText',
    text='Thank you for completing this study',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
endstudykey = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
testing = data.TrialHandler(nReps=0.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='testing')
thisExp.addLoop(testing)  # add the loop to the experiment
thisTesting = testing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTesting.rgb)
if thisTesting != None:
    for paramName in thisTesting:
        exec('{} = thisTesting[paramName]'.format(paramName))

for thisTesting in testing:
    currentLoop = testing
    # abbreviate parameter names if possible (e.g. rgb = thisTesting.rgb)
    if thisTesting != None:
        for paramName in thisTesting:
            exec('{} = thisTesting[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Mouse"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    MouseComponents = []
    for thisComponent in MouseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MouseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Mouse"-------
    while continueRoutine:
        # get current time
        t = MouseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MouseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MouseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Mouse"-------
    for thisComponent in MouseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    win.mouseVisible = False
    # the Routine "Mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Instrloop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('SpeededInstructionsSheet.xlsx'),
        seed=None, name='Instrloop')
    thisExp.addLoop(Instrloop)  # add the loop to the experiment
    thisInstrloop = Instrloop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstrloop.rgb)
    if thisInstrloop != None:
        for paramName in thisInstrloop:
            exec('{} = thisInstrloop[paramName]'.format(paramName))
    
    for thisInstrloop in Instrloop:
        currentLoop = Instrloop
        # abbreviate parameter names if possible (e.g. rgb = thisInstrloop.rgb)
        if thisInstrloop != None:
            for paramName in thisInstrloop:
                exec('{} = thisInstrloop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FastInstr"-------
        continueRoutine = True
        routineTimer.add(30.000000)
        # update component parameters for each repeat
        Instr1.setText(FastInstructions)
        InstrResponse.keys = []
        InstrResponse.rt = []
        _InstrResponse_allKeys = []
        # keep track of which components have finished
        FastInstrComponents = [Instr1, InstrResponse]
        for thisComponent in FastInstrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FastInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FastInstr"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FastInstrClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FastInstrClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Instr1* updates
            if Instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Instr1.frameNStart = frameN  # exact frame index
                Instr1.tStart = t  # local t and not account for scr refresh
                Instr1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Instr1, 'tStartRefresh')  # time at next scr refresh
                Instr1.setAutoDraw(True)
            if Instr1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Instr1.tStartRefresh + 30-frameTolerance:
                    # keep track of stop time/frame for later
                    Instr1.tStop = t  # not accounting for scr refresh
                    Instr1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Instr1, 'tStopRefresh')  # time at next scr refresh
                    Instr1.setAutoDraw(False)
            
            # *InstrResponse* updates
            waitOnFlip = False
            if InstrResponse.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                InstrResponse.frameNStart = frameN  # exact frame index
                InstrResponse.tStart = t  # local t and not account for scr refresh
                InstrResponse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstrResponse, 'tStartRefresh')  # time at next scr refresh
                InstrResponse.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(InstrResponse.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(InstrResponse.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if InstrResponse.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > InstrResponse.tStartRefresh + 28-frameTolerance:
                    # keep track of stop time/frame for later
                    InstrResponse.tStop = t  # not accounting for scr refresh
                    InstrResponse.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(InstrResponse, 'tStopRefresh')  # time at next scr refresh
                    InstrResponse.status = FINISHED
            if InstrResponse.status == STARTED and not waitOnFlip:
                theseKeys = InstrResponse.getKeys(keyList=['e'], waitRelease=False)
                _InstrResponse_allKeys.extend(theseKeys)
                if len(_InstrResponse_allKeys):
                    InstrResponse.keys = _InstrResponse_allKeys[-1].name  # just the last key pressed
                    InstrResponse.rt = _InstrResponse_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FastInstrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FastInstr"-------
        for thisComponent in FastInstrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Instrloop.addData('Instr1.started', Instr1.tStartRefresh)
        Instrloop.addData('Instr1.stopped', Instr1.tStopRefresh)
        # check responses
        if InstrResponse.keys in ['', [], None]:  # No response was made
            InstrResponse.keys = None
        Instrloop.addData('InstrResponse.keys',InstrResponse.keys)
        if InstrResponse.keys != None:  # we had a response
            Instrloop.addData('InstrResponse.rt', InstrResponse.rt)
        Instrloop.addData('InstrResponse.started', InstrResponse.tStartRefresh)
        Instrloop.addData('InstrResponse.stopped', InstrResponse.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Instrloop'
    
    # get names of stimulus parameters
    if Instrloop.trialList in ([], [None], None):
        params = []
    else:
        params = Instrloop.trialList[0].keys()
    # save data for this loop
    Instrloop.saveAsText(filename + 'Instrloop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # set up handler to look after randomisation of conditions etc
    Practice = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('InfinityThesisPracticeFast.xlsx'),
        seed=None, name='Practice')
    thisExp.addLoop(Practice)  # add the loop to the experiment
    thisPractice = Practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    for thisPractice in Practice:
        currentLoop = Practice
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                exec('{} = thisPractice[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FastPractice"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        PracticeText.setText(practicetext)
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        scaretone.setSound('A', secs=0.2, hamming=True)
        scaretone.setVolume(1.0, log=False)
        # keep track of which components have finished
        FastPracticeComponents = [fixcross1, PracticeText, key_resp_2, scaretone]
        for thisComponent in FastPracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FastPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FastPractice"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FastPracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FastPracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross1* updates
            if fixcross1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixcross1.frameNStart = frameN  # exact frame index
                fixcross1.tStart = t  # local t and not account for scr refresh
                fixcross1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross1, 'tStartRefresh')  # time at next scr refresh
                fixcross1.setAutoDraw(True)
            if fixcross1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross1.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross1.tStop = t  # not accounting for scr refresh
                    fixcross1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixcross1, 'tStopRefresh')  # time at next scr refresh
                    fixcross1.setAutoDraw(False)
            
            # *PracticeText* updates
            if PracticeText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                PracticeText.frameNStart = frameN  # exact frame index
                PracticeText.tStart = t  # local t and not account for scr refresh
                PracticeText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeText, 'tStartRefresh')  # time at next scr refresh
                PracticeText.setAutoDraw(True)
            if PracticeText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > PracticeText.tStartRefresh + 5.5-frameTolerance:
                    # keep track of stop time/frame for later
                    PracticeText.tStop = t  # not accounting for scr refresh
                    PracticeText.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(PracticeText, 'tStopRefresh')  # time at next scr refresh
                    PracticeText.setAutoDraw(False)
            
            # *key_resp_2* updates
            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + 5.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_2, 'tStopRefresh')  # time at next scr refresh
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['e', 'i'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    # was this correct?
                    if (key_resp_2.keys == str(practicecorrect)) or (key_resp_2.keys == practicecorrect):
                        key_resp_2.corr = 1
                    else:
                        key_resp_2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # start/stop scaretone
            if scaretone.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                scaretone.frameNStart = frameN  # exact frame index
                scaretone.tStart = t  # local t and not account for scr refresh
                scaretone.tStartRefresh = tThisFlipGlobal  # on global time
                scaretone.play(when=win)  # sync with win flip
            if scaretone.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > scaretone.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    scaretone.tStop = t  # not accounting for scr refresh
                    scaretone.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(scaretone, 'tStopRefresh')  # time at next scr refresh
                    scaretone.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FastPracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FastPractice"-------
        for thisComponent in FastPracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Practice.addData('fixcross1.started', fixcross1.tStartRefresh)
        Practice.addData('fixcross1.stopped', fixcross1.tStopRefresh)
        Practice.addData('PracticeText.started', PracticeText.tStartRefresh)
        Practice.addData('PracticeText.stopped', PracticeText.tStopRefresh)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
            # was no response the correct answer?!
            if str(practicecorrect).lower() == 'none':
               key_resp_2.corr = 1;  # correct non-response
            else:
               key_resp_2.corr = 0;  # failed to respond (incorrectly)
        # store data for Practice (TrialHandler)
        Practice.addData('key_resp_2.keys',key_resp_2.keys)
        Practice.addData('key_resp_2.corr', key_resp_2.corr)
        if key_resp_2.keys != None:  # we had a response
            Practice.addData('key_resp_2.rt', key_resp_2.rt)
        Practice.addData('key_resp_2.started', key_resp_2.tStartRefresh)
        Practice.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
        scaretone.stop()  # ensure sound has stopped at end of routine
        Practice.addData('scaretone.started', scaretone.tStartRefresh)
        Practice.addData('scaretone.stopped', scaretone.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Practice'
    
    # get names of stimulus parameters
    if Practice.trialList in ([], [None], None):
        params = []
    else:
        params = Practice.trialList[0].keys()
    # save data for this loop
    Practice.saveAsText(filename + 'Practice.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # ------Prepare to start Routine "PracticeEnd"-------
    continueRoutine = True
    routineTimer.add(10.000000)
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    PracticeEndComponents = [text, key_resp_3]
    for thisComponent in PracticeEndComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeEndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeEnd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeEndClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeEndClock)
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
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 7.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['e'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeEndComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeEnd"-------
    for thisComponent in PracticeEndComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    testing.addData('text.started', text.tStartRefresh)
    testing.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    testing.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        testing.addData('key_resp_3.rt', key_resp_3.rt)
    testing.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    testing.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    FastLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('InfinityThesisTest5.xlsx'),
        seed=None, name='FastLoop')
    thisExp.addLoop(FastLoop)  # add the loop to the experiment
    thisFastLoop = FastLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFastLoop.rgb)
    if thisFastLoop != None:
        for paramName in thisFastLoop:
            exec('{} = thisFastLoop[paramName]'.format(paramName))
    
    for thisFastLoop in FastLoop:
        currentLoop = FastLoop
        # abbreviate parameter names if possible (e.g. rgb = thisFastLoop.rgb)
        if thisFastLoop != None:
            for paramName in thisFastLoop:
                exec('{} = thisFastLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "FastTrial"-------
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        Fasttext.setText(Statement)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        Timer.setSound('A', secs=0.2, hamming=True)
        Timer.setVolume(1.0, log=False)
        # keep track of which components have finished
        FastTrialComponents = [fixcross, Fasttext, key_resp, Timer]
        for thisComponent in FastTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FastTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FastTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FastTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FastTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixcross* updates
            if fixcross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixcross.frameNStart = frameN  # exact frame index
                fixcross.tStart = t  # local t and not account for scr refresh
                fixcross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixcross, 'tStartRefresh')  # time at next scr refresh
                fixcross.setAutoDraw(True)
            if fixcross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixcross.tStartRefresh + 0.45-frameTolerance:
                    # keep track of stop time/frame for later
                    fixcross.tStop = t  # not accounting for scr refresh
                    fixcross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fixcross, 'tStopRefresh')  # time at next scr refresh
                    fixcross.setAutoDraw(False)
            
            # *Fasttext* updates
            if Fasttext.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Fasttext.frameNStart = frameN  # exact frame index
                Fasttext.tStart = t  # local t and not account for scr refresh
                Fasttext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fasttext, 'tStartRefresh')  # time at next scr refresh
                Fasttext.setAutoDraw(True)
            if Fasttext.status == STARTED:
                # is it time to stop? (based on local clock)
                if tThisFlip > 5.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fasttext.tStop = t  # not accounting for scr refresh
                    Fasttext.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fasttext, 'tStopRefresh')  # time at next scr refresh
                    Fasttext.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 5.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['e', 'i'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(Correct)) or (key_resp.keys == Correct):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # start/stop Timer
            if Timer.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
                # keep track of start time/frame for later
                Timer.frameNStart = frameN  # exact frame index
                Timer.tStart = t  # local t and not account for scr refresh
                Timer.tStartRefresh = tThisFlipGlobal  # on global time
                Timer.play(when=win)  # sync with win flip
            if Timer.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Timer.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    Timer.tStop = t  # not accounting for scr refresh
                    Timer.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Timer, 'tStopRefresh')  # time at next scr refresh
                    Timer.stop()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FastTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FastTrial"-------
        for thisComponent in FastTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        FastLoop.addData('fixcross.started', fixcross.tStartRefresh)
        FastLoop.addData('fixcross.stopped', fixcross.tStopRefresh)
        FastLoop.addData('Fasttext.started', Fasttext.tStartRefresh)
        FastLoop.addData('Fasttext.stopped', Fasttext.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(Correct).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for FastLoop (TrialHandler)
        FastLoop.addData('key_resp.keys',key_resp.keys)
        FastLoop.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            FastLoop.addData('key_resp.rt', key_resp.rt)
        FastLoop.addData('key_resp.started', key_resp.tStartRefresh)
        FastLoop.addData('key_resp.stopped', key_resp.tStopRefresh)
        Timer.stop()  # ensure sound has stopped at end of routine
        FastLoop.addData('Timer.started', Timer.tStartRefresh)
        FastLoop.addData('Timer.stopped', Timer.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'FastLoop'
    
    # get names of stimulus parameters
    if FastLoop.trialList in ([], [None], None):
        params = []
    else:
        params = FastLoop.trialList[0].keys()
    # save data for this loop
    FastLoop.saveAsText(filename + 'FastLoop.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'testing'

# get names of stimulus parameters
if testing.trialList in ([], [None], None):
    params = []
else:
    params = testing.trialList[0].keys()
# save data for this loop
testing.saveAsText(filename + 'testing.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Demographics"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the mouse
mouse.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
DemographicsComponents = [Demographics1, button, mouse]
for thisComponent in DemographicsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
DemographicsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Demographics"-------
while continueRoutine:
    # get current time
    t = DemographicsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=DemographicsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Demographics1* updates
    if Demographics1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Demographics1.frameNStart = frameN  # exact frame index
        Demographics1.tStart = t  # local t and not account for scr refresh
        Demographics1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Demographics1, 'tStartRefresh')  # time at next scr refresh
        Demographics1.setAutoDraw(True)
    
    # *button* updates
    if button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button.frameNStart = frameN  # exact frame index
        button.tStart = t  # local t and not account for scr refresh
        button.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button, 'tStartRefresh')  # time at next scr refresh
        button.setAutoDraw(True)
    if button.status == STARTED:
        # check whether button has been pressed
        if button.isClicked:
            if not button.wasClicked:
                button.timesOn.append(button.buttonClock.getTime()) # store time of first click
                button.timesOff.append(button.buttonClock.getTime()) # store time clicked until
            else:
                button.timesOff[-1] = button.buttonClock.getTime() # update time clicked until
            if not button.wasClicked:
                continueRoutine = False  # end routine when button is clicked
                None
            button.wasClicked = True  # if button is still clicked next frame, it is not a new click
        else:
            button.wasClicked = False  # if button is clicked next frame, it is a new click
    else:
        button.wasClicked = False  # if button is clicked next frame, it is a new click
    # *mouse* updates
    if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mouse.frameNStart = frameN  # exact frame index
        mouse.tStart = t  # local t and not account for scr refresh
        mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
        mouse.status = STARTED
        mouse.mouseClock.reset()
        prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
    if mouse.status == STARTED:  # only update if started and not finished!
        buttons = mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                try:
                    iter((button))
                    clickableList = (button)
                except:
                    clickableList = [(button)]
                for obj in clickableList:
                    if obj.contains(mouse):
                        gotValidClick = True
                        mouse.clicked_name.append(obj.name)
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DemographicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Demographics"-------
for thisComponent in DemographicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
Demographics1.addDataToExp(thisExp, 'columns')
Demographics1.autodraw = False
thisExp.addData('button.started', button.tStartRefresh)
thisExp.addData('button.stopped', button.tStopRefresh)
thisExp.addData('button.numClicks', button.numClicks)
if button.numClicks:
   thisExp.addData('button.timesOn', button.timesOn[0])
   thisExp.addData('button.timesOff', button.timesOff[0])
else:
   thisExp.addData('button.timesOn', "")
   thisExp.addData('button.timesOff', "")
# store data for thisExp (ExperimentHandler)
x, y = mouse.getPos()
buttons = mouse.getPressed()
if sum(buttons):
    # check if the mouse was inside our 'clickable' objects
    gotValidClick = False
    try:
        iter((button))
        clickableList = (button)
    except:
        clickableList = [(button)]
    for obj in clickableList:
        if obj.contains(mouse):
            gotValidClick = True
            mouse.clicked_name.append(obj.name)
thisExp.addData('mouse.x', x)
thisExp.addData('mouse.y', y)
thisExp.addData('mouse.leftButton', buttons[0])
thisExp.addData('mouse.midButton', buttons[1])
thisExp.addData('mouse.rightButton', buttons[2])
if len(mouse.clicked_name):
    thisExp.addData('mouse.clicked_name', mouse.clicked_name[0])
thisExp.addData('mouse.started', mouse.tStart)
thisExp.addData('mouse.stopped', mouse.tStop)
thisExp.nextEntry()
# the Routine "Demographics" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "EndStudy"-------
continueRoutine = True
# update component parameters for each repeat
endstudykey.keys = []
endstudykey.rt = []
_endstudykey_allKeys = []
# keep track of which components have finished
EndStudyComponents = [EndStudyText, endstudykey]
for thisComponent in EndStudyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndStudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndStudy"-------
while continueRoutine:
    # get current time
    t = EndStudyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndStudyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndStudyText* updates
    if EndStudyText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndStudyText.frameNStart = frameN  # exact frame index
        EndStudyText.tStart = t  # local t and not account for scr refresh
        EndStudyText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndStudyText, 'tStartRefresh')  # time at next scr refresh
        EndStudyText.setAutoDraw(True)
    if EndStudyText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > EndStudyText.tStartRefresh + 30-frameTolerance:
            # keep track of stop time/frame for later
            EndStudyText.tStop = t  # not accounting for scr refresh
            EndStudyText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(EndStudyText, 'tStopRefresh')  # time at next scr refresh
            EndStudyText.setAutoDraw(False)
    
    # *endstudykey* updates
    waitOnFlip = False
    if endstudykey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endstudykey.frameNStart = frameN  # exact frame index
        endstudykey.tStart = t  # local t and not account for scr refresh
        endstudykey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endstudykey, 'tStartRefresh')  # time at next scr refresh
        endstudykey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endstudykey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endstudykey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endstudykey.status == STARTED and not waitOnFlip:
        theseKeys = endstudykey.getKeys(keyList=['e'], waitRelease=False)
        _endstudykey_allKeys.extend(theseKeys)
        if len(_endstudykey_allKeys):
            endstudykey.keys = _endstudykey_allKeys[-1].name  # just the last key pressed
            endstudykey.rt = _endstudykey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndStudyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndStudy"-------
for thisComponent in EndStudyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndStudyText.started', EndStudyText.tStartRefresh)
thisExp.addData('EndStudyText.stopped', EndStudyText.tStopRefresh)
# check responses
if endstudykey.keys in ['', [], None]:  # No response was made
    endstudykey.keys = None
thisExp.addData('endstudykey.keys',endstudykey.keys)
if endstudykey.keys != None:  # we had a response
    thisExp.addData('endstudykey.rt', endstudykey.rt)
thisExp.addData('endstudykey.started', endstudykey.tStartRefresh)
thisExp.addData('endstudykey.stopped', endstudykey.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndStudy" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
