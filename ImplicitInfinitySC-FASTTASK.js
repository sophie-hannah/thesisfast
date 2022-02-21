/************************************ 
 * Implicitinfinitysc-Fasttask Test *
 ************************************/

import { core, data, sound, util, visual } from './lib/psychojs-2021.2.3.js';
const { PsychoJS } = core;
const { TrialHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'ImplicitInfinitySC-FASTTASK';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(MouseRoutineBegin());
flowScheduler.add(MouseRoutineEachFrame());
flowScheduler.add(MouseRoutineEnd());
flowScheduler.add(text_2RoutineBegin());
flowScheduler.add(text_2RoutineEachFrame());
flowScheduler.add(text_2RoutineEnd());
const InstrloopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(InstrloopLoopBegin(InstrloopLoopScheduler));
flowScheduler.add(InstrloopLoopScheduler);
flowScheduler.add(InstrloopLoopEnd);
const PracticeLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopBegin(PracticeLoopScheduler));
flowScheduler.add(PracticeLoopScheduler);
flowScheduler.add(PracticeLoopEnd);
flowScheduler.add(PracticeEndRoutineBegin());
flowScheduler.add(PracticeEndRoutineEachFrame());
flowScheduler.add(PracticeEndRoutineEnd());
const FastLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(FastLoopLoopBegin(FastLoopLoopScheduler));
flowScheduler.add(FastLoopLoopScheduler);
flowScheduler.add(FastLoopLoopEnd);
flowScheduler.add(EndStudyRoutineBegin());
flowScheduler.add(EndStudyRoutineEachFrame());
flowScheduler.add(EndStudyRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'InfinityThesisStimuliFAST.xlsx', 'path': 'InfinityThesisStimuliFAST.xlsx'},
    {'name': 'InfinityThesisPracticeFast.xlsx', 'path': 'InfinityThesisPracticeFast.xlsx'},
    {'name': 'SpeededInstructionsSheet.xlsx', 'path': 'SpeededInstructionsSheet.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.2.3';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var MouseClock;
var text_2Clock;
var text_3;
var key_resp_4;
var FastInstrClock;
var Instr1;
var INSTRESP;
var FastPracticeClock;
var fixcross1;
var PracticeText;
var key_resp_2;
var scaretone;
var FTrue;
var JFALSE;
var AdvanceClock;
var Continue;
var Advance_Resp;
var PracticeEndClock;
var text;
var key_resp_3;
var FastTrialClock;
var fixcross;
var Fasttext;
var key_resp;
var Timer;
var myCount;
var TRUE;
var FALSE;
var EncouragementClock;
var EncourageText;
var encouragekey;
var EndStudyClock;
var EndStudyText;
var endstudykey;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Mouse"
  MouseClock = new util.Clock();
  psychoJS.window.mouseVisible = true;
  
  // Initialize components for Routine "text_2"
  text_2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'Testing if experiment is uploading?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FastInstr"
  FastInstrClock = new util.Clock();
  Instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Instr1',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  INSTRESP = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FastPractice"
  FastPracticeClock = new util.Clock();
  fixcross1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixcross1', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  PracticeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  scaretone = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  scaretone.setVolume(1.0);
  FTrue = new visual.TextStim({
    win: psychoJS.window,
    name: 'FTrue',
    text: 'F=TRUE',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), 0.3], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -4.0 
  });
  
  JFALSE = new visual.TextStim({
    win: psychoJS.window,
    name: 'JFALSE',
    text: 'J=FALSE',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Advance"
  AdvanceClock = new util.Clock();
  Continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'Continue',
    text: 'Press Space to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  Advance_Resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeEnd"
  PracticeEndClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'You have finished the trial period. You will now complete the official task. Judge the following statements as quickly as you can without sacrificing accuracy.\n\nPress ‘F’ if the statement is true and ‘J’ if the statement is false. \n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "FastTrial"
  FastTrialClock = new util.Clock();
  fixcross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixcross', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 1.0, lineColor: new util.Color('white'),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  Fasttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fasttext',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Timer = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 0.2,
    });
  Timer.setVolume(1.0);
  myCount = 0;
  
  TRUE = new visual.TextStim({
    win: psychoJS.window,
    name: 'TRUE',
    text: 'F=TRUE',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.5), 0.3], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -5.0 
  });
  
  FALSE = new visual.TextStim({
    win: psychoJS.window,
    name: 'FALSE',
    text: 'J=FALSE',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.5, 0.3], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -6.0 
  });
  
  // Initialize components for Routine "Encouragement"
  EncouragementClock = new util.Clock();
  EncourageText = new visual.TextStim({
    win: psychoJS.window,
    name: 'EncourageText',
    text: 'Woah-oh! You’re Halfway There! \nKeep it Up! \n\nPress Space to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  encouragekey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndStudy"
  EndStudyClock = new util.Clock();
  EndStudyText = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndStudyText',
    text: 'Thank you for completing this study. Please enter the following unique code into Qualtrics to prove you have completed the study: \n\nCAT123\n\nPress Space to End the Study and Save your Results',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  endstudykey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var MouseComponents;
function MouseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Mouse'-------
    t = 0;
    MouseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    MouseComponents = [];
    
    for (const thisComponent of MouseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function MouseRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Mouse'-------
    // get current time
    t = MouseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MouseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MouseRoutineEnd() {
  return async function () {
    //------Ending Routine 'Mouse'-------
    for (const thisComponent of MouseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.window.mouseVisible = false;
    
    // the Routine "Mouse" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var text_2Components;
function text_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'text_2'-------
    t = 0;
    text_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    text_2Components = [];
    text_2Components.push(text_3);
    text_2Components.push(key_resp_4);
    
    for (const thisComponent of text_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function text_2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'text_2'-------
    // get current time
    t = text_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of text_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function text_2RoutineEnd() {
  return async function () {
    //------Ending Routine 'text_2'-------
    for (const thisComponent of text_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "text_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Instrloop;
var currentLoop;
function InstrloopLoopBegin(InstrloopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Instrloop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'SpeededInstructionsSheet.xlsx',
      seed: undefined, name: 'Instrloop'
    });
    psychoJS.experiment.addLoop(Instrloop); // add the loop to the experiment
    currentLoop = Instrloop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstrloop of Instrloop) {
      const snapshot = Instrloop.getSnapshot();
      InstrloopLoopScheduler.add(importConditions(snapshot));
      InstrloopLoopScheduler.add(FastInstrRoutineBegin(snapshot));
      InstrloopLoopScheduler.add(FastInstrRoutineEachFrame());
      InstrloopLoopScheduler.add(FastInstrRoutineEnd());
      InstrloopLoopScheduler.add(endLoopIteration(InstrloopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function InstrloopLoopEnd() {
  psychoJS.experiment.removeLoop(Instrloop);

  return Scheduler.Event.NEXT;
}


var Practice;
function PracticeLoopBegin(PracticeLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Practice = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'InfinityThesisPracticeFast.xlsx',
      seed: undefined, name: 'Practice'
    });
    psychoJS.experiment.addLoop(Practice); // add the loop to the experiment
    currentLoop = Practice;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice of Practice) {
      const snapshot = Practice.getSnapshot();
      PracticeLoopScheduler.add(importConditions(snapshot));
      PracticeLoopScheduler.add(FastPracticeRoutineBegin(snapshot));
      PracticeLoopScheduler.add(FastPracticeRoutineEachFrame());
      PracticeLoopScheduler.add(FastPracticeRoutineEnd());
      PracticeLoopScheduler.add(AdvanceRoutineBegin(snapshot));
      PracticeLoopScheduler.add(AdvanceRoutineEachFrame());
      PracticeLoopScheduler.add(AdvanceRoutineEnd());
      PracticeLoopScheduler.add(endLoopIteration(PracticeLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function PracticeLoopEnd() {
  psychoJS.experiment.removeLoop(Practice);

  return Scheduler.Event.NEXT;
}


var FastLoop;
function FastLoopLoopBegin(FastLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    FastLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'InfinityThesisStimuliFAST.xlsx',
      seed: undefined, name: 'FastLoop'
    });
    psychoJS.experiment.addLoop(FastLoop); // add the loop to the experiment
    currentLoop = FastLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisFastLoop of FastLoop) {
      const snapshot = FastLoop.getSnapshot();
      FastLoopLoopScheduler.add(importConditions(snapshot));
      FastLoopLoopScheduler.add(FastTrialRoutineBegin(snapshot));
      FastLoopLoopScheduler.add(FastTrialRoutineEachFrame());
      FastLoopLoopScheduler.add(FastTrialRoutineEnd());
      FastLoopLoopScheduler.add(EncouragementRoutineBegin(snapshot));
      FastLoopLoopScheduler.add(EncouragementRoutineEachFrame());
      FastLoopLoopScheduler.add(EncouragementRoutineEnd());
      FastLoopLoopScheduler.add(AdvanceRoutineBegin(snapshot));
      FastLoopLoopScheduler.add(AdvanceRoutineEachFrame());
      FastLoopLoopScheduler.add(AdvanceRoutineEnd());
      FastLoopLoopScheduler.add(endLoopIteration(FastLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function FastLoopLoopEnd() {
  psychoJS.experiment.removeLoop(FastLoop);

  return Scheduler.Event.NEXT;
}


var _INSTRESP_allKeys;
var FastInstrComponents;
function FastInstrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FastInstr'-------
    t = 0;
    FastInstrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    // update component parameters for each repeat
    Instr1.setText(FastInstructions);
    INSTRESP.keys = undefined;
    INSTRESP.rt = undefined;
    _INSTRESP_allKeys = [];
    // keep track of which components have finished
    FastInstrComponents = [];
    FastInstrComponents.push(Instr1);
    FastInstrComponents.push(INSTRESP);
    
    for (const thisComponent of FastInstrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FastInstrRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FastInstr'-------
    // get current time
    t = FastInstrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Instr1* updates
    if (t >= 0.0 && Instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Instr1.tStart = t;  // (not accounting for frame time here)
      Instr1.frameNStart = frameN;  // exact frame index
      
      Instr1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Instr1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Instr1.setAutoDraw(false);
    }
    
    // *INSTRESP* updates
    if (t >= 0.0 && INSTRESP.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      INSTRESP.tStart = t;  // (not accounting for frame time here)
      INSTRESP.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { INSTRESP.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { INSTRESP.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { INSTRESP.clearEvents(); });
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (INSTRESP.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      INSTRESP.status = PsychoJS.Status.FINISHED;
  }

    if (INSTRESP.status === PsychoJS.Status.STARTED) {
      let theseKeys = INSTRESP.getKeys({keyList: ['space'], waitRelease: false});
      _INSTRESP_allKeys = _INSTRESP_allKeys.concat(theseKeys);
      if (_INSTRESP_allKeys.length > 0) {
        INSTRESP.keys = _INSTRESP_allKeys[_INSTRESP_allKeys.length - 1].name;  // just the last key pressed
        INSTRESP.rt = _INSTRESP_allKeys[_INSTRESP_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FastInstrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FastInstrRoutineEnd() {
  return async function () {
    //------Ending Routine 'FastInstr'-------
    for (const thisComponent of FastInstrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('INSTRESP.keys', INSTRESP.keys);
    if (typeof INSTRESP.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('INSTRESP.rt', INSTRESP.rt);
        routineTimer.reset();
        }
    
    INSTRESP.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var FastPracticeComponents;
function FastPracticeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FastPractice'-------
    t = 0;
    FastPracticeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.050000);
    // update component parameters for each repeat
    PracticeText.setText(practicetext);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    scaretone.secs=0.2;
    scaretone.setVolume(1.0);
    // keep track of which components have finished
    FastPracticeComponents = [];
    FastPracticeComponents.push(fixcross1);
    FastPracticeComponents.push(PracticeText);
    FastPracticeComponents.push(key_resp_2);
    FastPracticeComponents.push(scaretone);
    FastPracticeComponents.push(FTrue);
    FastPracticeComponents.push(JFALSE);
    
    for (const thisComponent of FastPracticeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FastPracticeRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FastPractice'-------
    // get current time
    t = FastPracticeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross1* updates
    if (t >= 0.0 && fixcross1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross1.tStart = t;  // (not accounting for frame time here)
      fixcross1.frameNStart = frameN;  // exact frame index
      
      fixcross1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixcross1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixcross1.setAutoDraw(false);
    }
    
    // *PracticeText* updates
    if (t >= 1 && PracticeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeText.tStart = t;  // (not accounting for frame time here)
      PracticeText.frameNStart = frameN;  // exact frame index
      
      PracticeText.setAutoDraw(true);
    }

    frameRemains = 1 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (PracticeText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      PracticeText.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (t >= 1 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    frameRemains = 1 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_2.keys == practicecorrect) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop scaretone
    if (t >= 3.5 && scaretone.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      scaretone.tStart = t;  // (not accounting for frame time here)
      scaretone.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ scaretone.play(); });  // screen flip
      scaretone.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 3.5 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (scaretone.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {
        scaretone.stop();  // stop the sound (if longer than duration)
      }
      scaretone.status = PsychoJS.Status.FINISHED;
    }
    
    // *FTrue* updates
    if (t >= 0.05 && FTrue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FTrue.tStart = t;  // (not accounting for frame time here)
      FTrue.frameNStart = frameN;  // exact frame index
      
      FTrue.setAutoDraw(true);
    }

    frameRemains = 0.05 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (FTrue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      FTrue.setAutoDraw(false);
    }
    
    // *JFALSE* updates
    if (t >= 0.05 && JFALSE.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      JFALSE.tStart = t;  // (not accounting for frame time here)
      JFALSE.frameNStart = frameN;  // exact frame index
      
      JFALSE.setAutoDraw(true);
    }

    frameRemains = 0.05 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (JFALSE.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      JFALSE.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FastPracticeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FastPracticeRoutineEnd() {
  return async function () {
    //------Ending Routine 'FastPractice'-------
    for (const thisComponent of FastPracticeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(practicecorrect)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    scaretone.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _Advance_Resp_allKeys;
var AdvanceComponents;
function AdvanceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Advance'-------
    t = 0;
    AdvanceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    Advance_Resp.keys = undefined;
    Advance_Resp.rt = undefined;
    _Advance_Resp_allKeys = [];
    // keep track of which components have finished
    AdvanceComponents = [];
    AdvanceComponents.push(Continue);
    AdvanceComponents.push(Advance_Resp);
    
    for (const thisComponent of AdvanceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function AdvanceRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Advance'-------
    // get current time
    t = AdvanceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Continue* updates
    if (t >= 0.0 && Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Continue.tStart = t;  // (not accounting for frame time here)
      Continue.frameNStart = frameN;  // exact frame index
      
      Continue.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Continue.setAutoDraw(false);
    }
    
    // *Advance_Resp* updates
    if (t >= 0.0 && Advance_Resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Advance_Resp.tStart = t;  // (not accounting for frame time here)
      Advance_Resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Advance_Resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Advance_Resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Advance_Resp.clearEvents(); });
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Advance_Resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Advance_Resp.status = PsychoJS.Status.FINISHED;
  }

    if (Advance_Resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Advance_Resp.getKeys({keyList: ['space'], waitRelease: false});
      _Advance_Resp_allKeys = _Advance_Resp_allKeys.concat(theseKeys);
      if (_Advance_Resp_allKeys.length > 0) {
        Advance_Resp.keys = _Advance_Resp_allKeys[_Advance_Resp_allKeys.length - 1].name;  // just the last key pressed
        Advance_Resp.rt = _Advance_Resp_allKeys[_Advance_Resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of AdvanceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function AdvanceRoutineEnd() {
  return async function () {
    //------Ending Routine 'Advance'-------
    for (const thisComponent of AdvanceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('Advance_Resp.keys', Advance_Resp.keys);
    if (typeof Advance_Resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Advance_Resp.rt', Advance_Resp.rt);
        routineTimer.reset();
        }
    
    Advance_Resp.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var PracticeEndComponents;
function PracticeEndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'PracticeEnd'-------
    t = 0;
    PracticeEndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    PracticeEndComponents = [];
    PracticeEndComponents.push(text);
    PracticeEndComponents.push(key_resp_3);
    
    for (const thisComponent of PracticeEndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracticeEndRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'PracticeEnd'-------
    // get current time
    t = PracticeEndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // *key_resp_3* updates
    if (t >= 3.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    frameRemains = 3.0 + 7.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeEndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeEndRoutineEnd() {
  return async function () {
    //------Ending Routine 'PracticeEnd'-------
    for (const thisComponent of PracticeEndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var FastTrialComponents;
function FastTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'FastTrial'-------
    t = 0;
    FastTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.050000);
    // update component parameters for each repeat
    Fasttext.setText(Statement);
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    Timer.secs=0.2;
    Timer.setVolume(1.0);
    myCount = (myCount + 1);
    if ((myCount > 80)) {
        FastLoop.finished = true;
    }
    
    // keep track of which components have finished
    FastTrialComponents = [];
    FastTrialComponents.push(fixcross);
    FastTrialComponents.push(Fasttext);
    FastTrialComponents.push(key_resp);
    FastTrialComponents.push(Timer);
    FastTrialComponents.push(TRUE);
    FastTrialComponents.push(FALSE);
    
    for (const thisComponent of FastTrialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FastTrialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'FastTrial'-------
    // get current time
    t = FastTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixcross* updates
    if (t >= 0.0 && fixcross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixcross.tStart = t;  // (not accounting for frame time here)
      fixcross.frameNStart = frameN;  // exact frame index
      
      fixcross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixcross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixcross.setAutoDraw(false);
    }
    
    // *Fasttext* updates
    if (t >= 1 && Fasttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fasttext.tStart = t;  // (not accounting for frame time here)
      Fasttext.frameNStart = frameN;  // exact frame index
      
      Fasttext.setAutoDraw(true);
    }

    frameRemains = 1 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fasttext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fasttext.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 1 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp.keys == Correct) {
            key_resp.corr = 1;
        } else {
            key_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop Timer
    if (t >= 3.5 && Timer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Timer.tStart = t;  // (not accounting for frame time here)
      Timer.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Timer.play(); });  // screen flip
      Timer.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 3.5 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Timer.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.2 > 0.5) {
        Timer.stop();  // stop the sound (if longer than duration)
      }
      Timer.status = PsychoJS.Status.FINISHED;
    }
    
    // *TRUE* updates
    if (t >= 0.05 && TRUE.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TRUE.tStart = t;  // (not accounting for frame time here)
      TRUE.frameNStart = frameN;  // exact frame index
      
      TRUE.setAutoDraw(true);
    }

    frameRemains = 0.05 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (TRUE.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      TRUE.setAutoDraw(false);
    }
    
    // *FALSE* updates
    if (t >= 0.05 && FALSE.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FALSE.tStart = t;  // (not accounting for frame time here)
      FALSE.frameNStart = frameN;  // exact frame index
      
      FALSE.setAutoDraw(true);
    }

    frameRemains = 0.05 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (FALSE.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      FALSE.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FastTrialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FastTrialRoutineEnd() {
  return async function () {
    //------Ending Routine 'FastTrial'-------
    for (const thisComponent of FastTrialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (key_resp.keys === undefined) {
      if (['None','none',undefined].includes(Correct)) {
         key_resp.corr = 1;  // correct non-response
      } else {
         key_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for psychoJS.experiment (ExperimentHandler)
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    psychoJS.experiment.addData('key_resp.corr', key_resp.corr);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    Timer.stop();  // ensure sound has stopped at end of routine
    return Scheduler.Event.NEXT;
  };
}


var _encouragekey_allKeys;
var EncouragementComponents;
function EncouragementRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Encouragement'-------
    t = 0;
    EncouragementClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(13.000000);
    // update component parameters for each repeat
    encouragekey.keys = undefined;
    encouragekey.rt = undefined;
    _encouragekey_allKeys = [];
    // keep track of which components have finished
    EncouragementComponents = [];
    EncouragementComponents.push(EncourageText);
    EncouragementComponents.push(encouragekey);
    
    for (const thisComponent of EncouragementComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EncouragementRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Encouragement'-------
    // get current time
    t = EncouragementClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EncourageText* updates
    if (t >= 0.0 && EncourageText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EncourageText.tStart = t;  // (not accounting for frame time here)
      EncourageText.frameNStart = frameN;  // exact frame index
      
      EncourageText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 13 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (EncourageText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      EncourageText.setAutoDraw(false);
    }
    
    // *encouragekey* updates
    if (t >= 3.0 && encouragekey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      encouragekey.tStart = t;  // (not accounting for frame time here)
      encouragekey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { encouragekey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { encouragekey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { encouragekey.clearEvents(); });
    }

    frameRemains = 3.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (encouragekey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      encouragekey.status = PsychoJS.Status.FINISHED;
  }

    if (encouragekey.status === PsychoJS.Status.STARTED) {
      let theseKeys = encouragekey.getKeys({keyList: ['space'], waitRelease: false});
      _encouragekey_allKeys = _encouragekey_allKeys.concat(theseKeys);
      if (_encouragekey_allKeys.length > 0) {
        encouragekey.keys = _encouragekey_allKeys[_encouragekey_allKeys.length - 1].name;  // just the last key pressed
        encouragekey.rt = _encouragekey_allKeys[_encouragekey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    if ((FastLoop.thisN !== 40)) {
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EncouragementComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EncouragementRoutineEnd() {
  return async function () {
    //------Ending Routine 'Encouragement'-------
    for (const thisComponent of EncouragementComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('encouragekey.keys', encouragekey.keys);
    if (typeof encouragekey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('encouragekey.rt', encouragekey.rt);
        routineTimer.reset();
        }
    
    encouragekey.stop();
    return Scheduler.Event.NEXT;
  };
}


var _endstudykey_allKeys;
var EndStudyComponents;
function EndStudyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EndStudy'-------
    t = 0;
    EndStudyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(30.000000);
    // update component parameters for each repeat
    endstudykey.keys = undefined;
    endstudykey.rt = undefined;
    _endstudykey_allKeys = [];
    // keep track of which components have finished
    EndStudyComponents = [];
    EndStudyComponents.push(EndStudyText);
    EndStudyComponents.push(endstudykey);
    
    for (const thisComponent of EndStudyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndStudyRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EndStudy'-------
    // get current time
    t = EndStudyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndStudyText* updates
    if (t >= 0.0 && EndStudyText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndStudyText.tStart = t;  // (not accounting for frame time here)
      EndStudyText.frameNStart = frameN;  // exact frame index
      
      EndStudyText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (EndStudyText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      EndStudyText.setAutoDraw(false);
    }
    
    // *endstudykey* updates
    if (t >= 0.0 && endstudykey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endstudykey.tStart = t;  // (not accounting for frame time here)
      endstudykey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { endstudykey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { endstudykey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { endstudykey.clearEvents(); });
    }

    frameRemains = 0.0 + 30 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (endstudykey.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      endstudykey.status = PsychoJS.Status.FINISHED;
  }

    if (endstudykey.status === PsychoJS.Status.STARTED) {
      let theseKeys = endstudykey.getKeys({keyList: ['space'], waitRelease: false});
      _endstudykey_allKeys = _endstudykey_allKeys.concat(theseKeys);
      if (_endstudykey_allKeys.length > 0) {
        endstudykey.keys = _endstudykey_allKeys[_endstudykey_allKeys.length - 1].name;  // just the last key pressed
        endstudykey.rt = _endstudykey_allKeys[_endstudykey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndStudyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndStudyRoutineEnd() {
  return async function () {
    //------Ending Routine 'EndStudy'-------
    for (const thisComponent of EndStudyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('endstudykey.keys', endstudykey.keys);
    if (typeof endstudykey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('endstudykey.rt', endstudykey.rt);
        routineTimer.reset();
        }
    
    endstudykey.stop();
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
