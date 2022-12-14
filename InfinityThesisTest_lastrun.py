#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Sat Nov 20 12:01:55 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

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
    originPath='/Users/sophiecb/Desktop/InfinityThesisTest5/InfinityThesisTest_lastrun.py',
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

# Initialize components for Routine "BlockSelect"
BlockSelectClock = core.Clock()
nRepsblock1=0
nRepsblock2=0

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

# Initialize components for Routine "SlowInstr"
SlowInstrClock = core.Clock()
SlowInstrText = visual.TextStim(win=win, name='SlowInstrText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
SlowInstrKey = keyboard.Keyboard()

# Initialize components for Routine "SlowTrial"
SlowTrialClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[-1.0000, -1.0000, -1.0000],
    opacity=None, depth=0.0, interpolate=True)
SlowText = visual.TextStim(win=win, name='SlowText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
SlowKey = keyboard.Keyboard()

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
Blockselectloop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BlockSelectLoop.xlsx'),
    seed=None, name='Blockselectloop')
thisExp.addLoop(Blockselectloop)  # add the loop to the experiment
thisBlockselectloop = Blockselectloop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockselectloop.rgb)
if thisBlockselectloop != None:
    for paramName in thisBlockselectloop:
        exec('{} = thisBlockselectloop[paramName]'.format(paramName))

for thisBlockselectloop in Blockselectloop:
    currentLoop = Blockselectloop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockselectloop.rgb)
    if thisBlockselectloop != None:
        for paramName in thisBlockselectloop:
            exec('{} = thisBlockselectloop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BlockSelect"-------
    continueRoutine = True
    # update component parameters for each repeat
    if selectBlock==1:
     nRepsblock1=1
     nRepsblock2=0
    elif selectBlock==2:
     nRepsblock1=0
     nRepsblock2=1
    # keep track of which components have finished
    BlockSelectComponents = []
    for thisComponent in BlockSelectComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BlockSelectClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BlockSelect"-------
    while continueRoutine:
        # get current time
        t = BlockSelectClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BlockSelectClock)
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
        for thisComponent in BlockSelectComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BlockSelect"-------
    for thisComponent in BlockSelectComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BlockSelect" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    SpeededBlock = data.TrialHandler(nReps=nRepsblock1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SpeededBlock')
    thisExp.addLoop(SpeededBlock)  # add the loop to the experiment
    thisSpeededBlock = SpeededBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSpeededBlock.rgb)
    if thisSpeededBlock != None:
        for paramName in thisSpeededBlock:
            exec('{} = thisSpeededBlock[paramName]'.format(paramName))
    
    for thisSpeededBlock in SpeededBlock:
        currentLoop = SpeededBlock
        # abbreviate parameter names if possible (e.g. rgb = thisSpeededBlock.rgb)
        if thisSpeededBlock != None:
            for paramName in thisSpeededBlock:
                exec('{} = thisSpeededBlock[paramName]'.format(paramName))
        
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
                    if tThisFlipGlobal > fixcross.tStartRefresh + 0.5-frameTolerance:
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
    # completed nRepsblock1 repeats of 'SpeededBlock'
    
    
    # set up handler to look after randomisation of conditions etc
    SlowBlock = data.TrialHandler(nReps=nRepsblock2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='SlowBlock')
    thisExp.addLoop(SlowBlock)  # add the loop to the experiment
    thisSlowBlock = SlowBlock.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSlowBlock.rgb)
    if thisSlowBlock != None:
        for paramName in thisSlowBlock:
            exec('{} = thisSlowBlock[paramName]'.format(paramName))
    
    for thisSlowBlock in SlowBlock:
        currentLoop = SlowBlock
        # abbreviate parameter names if possible (e.g. rgb = thisSlowBlock.rgb)
        if thisSlowBlock != None:
            for paramName in thisSlowBlock:
                exec('{} = thisSlowBlock[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        SlowInstrLoop = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('SlowInstructionsSheet2.xlsx'),
            seed=None, name='SlowInstrLoop')
        thisExp.addLoop(SlowInstrLoop)  # add the loop to the experiment
        thisSlowInstrLoop = SlowInstrLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSlowInstrLoop.rgb)
        if thisSlowInstrLoop != None:
            for paramName in thisSlowInstrLoop:
                exec('{} = thisSlowInstrLoop[paramName]'.format(paramName))
        
        for thisSlowInstrLoop in SlowInstrLoop:
            currentLoop = SlowInstrLoop
            # abbreviate parameter names if possible (e.g. rgb = thisSlowInstrLoop.rgb)
            if thisSlowInstrLoop != None:
                for paramName in thisSlowInstrLoop:
                    exec('{} = thisSlowInstrLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "SlowInstr"-------
            continueRoutine = True
            routineTimer.add(30.000000)
            # update component parameters for each repeat
            SlowInstrText.setText(SlowInstructions)
            SlowInstrKey.keys = []
            SlowInstrKey.rt = []
            _SlowInstrKey_allKeys = []
            # keep track of which components have finished
            SlowInstrComponents = [SlowInstrText, SlowInstrKey]
            for thisComponent in SlowInstrComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            SlowInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "SlowInstr"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = SlowInstrClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=SlowInstrClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *SlowInstrText* updates
                if SlowInstrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SlowInstrText.frameNStart = frameN  # exact frame index
                    SlowInstrText.tStart = t  # local t and not account for scr refresh
                    SlowInstrText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SlowInstrText, 'tStartRefresh')  # time at next scr refresh
                    SlowInstrText.setAutoDraw(True)
                if SlowInstrText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > SlowInstrText.tStartRefresh + 30-frameTolerance:
                        # keep track of stop time/frame for later
                        SlowInstrText.tStop = t  # not accounting for scr refresh
                        SlowInstrText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(SlowInstrText, 'tStopRefresh')  # time at next scr refresh
                        SlowInstrText.setAutoDraw(False)
                
                # *SlowInstrKey* updates
                waitOnFlip = False
                if SlowInstrKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SlowInstrKey.frameNStart = frameN  # exact frame index
                    SlowInstrKey.tStart = t  # local t and not account for scr refresh
                    SlowInstrKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SlowInstrKey, 'tStartRefresh')  # time at next scr refresh
                    SlowInstrKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(SlowInstrKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(SlowInstrKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if SlowInstrKey.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > SlowInstrKey.tStartRefresh + 30-frameTolerance:
                        # keep track of stop time/frame for later
                        SlowInstrKey.tStop = t  # not accounting for scr refresh
                        SlowInstrKey.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(SlowInstrKey, 'tStopRefresh')  # time at next scr refresh
                        SlowInstrKey.status = FINISHED
                if SlowInstrKey.status == STARTED and not waitOnFlip:
                    theseKeys = SlowInstrKey.getKeys(keyList=['e'], waitRelease=False)
                    _SlowInstrKey_allKeys.extend(theseKeys)
                    if len(_SlowInstrKey_allKeys):
                        SlowInstrKey.keys = _SlowInstrKey_allKeys[-1].name  # just the last key pressed
                        SlowInstrKey.rt = _SlowInstrKey_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SlowInstrComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "SlowInstr"-------
            for thisComponent in SlowInstrComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            SlowInstrLoop.addData('SlowInstrText.started', SlowInstrText.tStartRefresh)
            SlowInstrLoop.addData('SlowInstrText.stopped', SlowInstrText.tStopRefresh)
            # check responses
            if SlowInstrKey.keys in ['', [], None]:  # No response was made
                SlowInstrKey.keys = None
            SlowInstrLoop.addData('SlowInstrKey.keys',SlowInstrKey.keys)
            if SlowInstrKey.keys != None:  # we had a response
                SlowInstrLoop.addData('SlowInstrKey.rt', SlowInstrKey.rt)
            SlowInstrLoop.addData('SlowInstrKey.started', SlowInstrKey.tStartRefresh)
            SlowInstrLoop.addData('SlowInstrKey.stopped', SlowInstrKey.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'SlowInstrLoop'
        
        # get names of stimulus parameters
        if SlowInstrLoop.trialList in ([], [None], None):
            params = []
        else:
            params = SlowInstrLoop.trialList[0].keys()
        # save data for this loop
        SlowInstrLoop.saveAsText(filename + 'SlowInstrLoop.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # set up handler to look after randomisation of conditions etc
        SlowLoop = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('InfinityThesisTest5.xlsx'),
            seed=None, name='SlowLoop')
        thisExp.addLoop(SlowLoop)  # add the loop to the experiment
        thisSlowLoop = SlowLoop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisSlowLoop.rgb)
        if thisSlowLoop != None:
            for paramName in thisSlowLoop:
                exec('{} = thisSlowLoop[paramName]'.format(paramName))
        
        for thisSlowLoop in SlowLoop:
            currentLoop = SlowLoop
            # abbreviate parameter names if possible (e.g. rgb = thisSlowLoop.rgb)
            if thisSlowLoop != None:
                for paramName in thisSlowLoop:
                    exec('{} = thisSlowLoop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "SlowTrial"-------
            continueRoutine = True
            # update component parameters for each repeat
            SlowText.setText(Statement)
            SlowKey.keys = []
            SlowKey.rt = []
            _SlowKey_allKeys = []
            # keep track of which components have finished
            SlowTrialComponents = [polygon, SlowText, SlowKey]
            for thisComponent in SlowTrialComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            SlowTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "SlowTrial"-------
            while continueRoutine:
                # get current time
                t = SlowTrialClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=SlowTrialClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *polygon* updates
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(True)
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                        polygon.setAutoDraw(False)
                
                # *SlowText* updates
                if SlowText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    SlowText.frameNStart = frameN  # exact frame index
                    SlowText.tStart = t  # local t and not account for scr refresh
                    SlowText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SlowText, 'tStartRefresh')  # time at next scr refresh
                    SlowText.setAutoDraw(True)
                
                # *SlowKey* updates
                waitOnFlip = False
                if SlowKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    SlowKey.frameNStart = frameN  # exact frame index
                    SlowKey.tStart = t  # local t and not account for scr refresh
                    SlowKey.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(SlowKey, 'tStartRefresh')  # time at next scr refresh
                    SlowKey.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(SlowKey.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(SlowKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if SlowKey.status == STARTED and not waitOnFlip:
                    theseKeys = SlowKey.getKeys(keyList=['e', 'i'], waitRelease=False)
                    _SlowKey_allKeys.extend(theseKeys)
                    if len(_SlowKey_allKeys):
                        SlowKey.keys = _SlowKey_allKeys[-1].name  # just the last key pressed
                        SlowKey.rt = _SlowKey_allKeys[-1].rt
                        # was this correct?
                        if (SlowKey.keys == str(Correct)) or (SlowKey.keys == Correct):
                            SlowKey.corr = 1
                        else:
                            SlowKey.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SlowTrialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "SlowTrial"-------
            for thisComponent in SlowTrialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            SlowLoop.addData('polygon.started', polygon.tStartRefresh)
            SlowLoop.addData('polygon.stopped', polygon.tStopRefresh)
            SlowLoop.addData('SlowText.started', SlowText.tStartRefresh)
            SlowLoop.addData('SlowText.stopped', SlowText.tStopRefresh)
            # check responses
            if SlowKey.keys in ['', [], None]:  # No response was made
                SlowKey.keys = None
                # was no response the correct answer?!
                if str(Correct).lower() == 'none':
                   SlowKey.corr = 1;  # correct non-response
                else:
                   SlowKey.corr = 0;  # failed to respond (incorrectly)
            # store data for SlowLoop (TrialHandler)
            SlowLoop.addData('SlowKey.keys',SlowKey.keys)
            SlowLoop.addData('SlowKey.corr', SlowKey.corr)
            if SlowKey.keys != None:  # we had a response
                SlowLoop.addData('SlowKey.rt', SlowKey.rt)
            SlowLoop.addData('SlowKey.started', SlowKey.tStartRefresh)
            SlowLoop.addData('SlowKey.stopped', SlowKey.tStopRefresh)
            # the Routine "SlowTrial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'SlowLoop'
        
        # get names of stimulus parameters
        if SlowLoop.trialList in ([], [None], None):
            params = []
        else:
            params = SlowLoop.trialList[0].keys()
        # save data for this loop
        SlowLoop.saveAsText(filename + 'SlowLoop.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'SlowBlock'
    
    # get names of stimulus parameters
    if SlowBlock.trialList in ([], [None], None):
        params = []
    else:
        params = SlowBlock.trialList[0].keys()
    # save data for this loop
    SlowBlock.saveAsText(filename + 'SlowBlock.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1.0 repeats of 'Blockselectloop'


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
