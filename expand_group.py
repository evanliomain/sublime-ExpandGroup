"""
ExpandGroup v0.1
by Evan Liomain
https://github.com/iamjessu/sublime-SplitScreen-Resizer

A fork of:
    SplitScreen-Resizer v3.0.0
    by Jesus Leon
    https://github.com/iamjessu/sublime-SplitScreen-Resizer
"""
import sublime, sublime_plugin
import logging
import time

# time.time() for when we called "focus_group" command
LAST_FOCUS_GROUP_TIME = 0.
# amout of time (in seconds) that we expect "on_activated" event to arrive after calling "focus_group"
# so in that case we can assume "on_activated" was not triggered by mouse.
EVENT_TIME = 0.4

def getLogger():
  logging.basicConfig(format='%(message)s')
  logger = logging.getLogger('test')
  logger.setLevel(logging.DEBUG)
  return logger

def getLayoutStructure(window):
    layout  = window.get_layout()
    nbRows  = len(layout["rows"]) - 1
    nbCols  = len(layout["cols"]) - 1
    nbCells = len(layout["cells"])

    if 1 == nbCells: return 'single'
    if 2 == nbCells:
        if 2 == nbCols and 1 == nbRows: return '2cols'
        if 1 == nbCols and 2 == nbRows: return '2rows'
    if 3 == nbCells:
        if 3 == nbCols and 1 == nbRows: return '3cols'
        if 1 == nbCols and 3 == nbRows: return '3rows'
        # TODO: other cases:
        # 2 rows, 2 cols on top 1 on bottom
        # 2 rows, 1 cols on top 2 on bottom

        # 2 cols, 2 rows on left 1 on right
        # 2 cols, 1 cols on left 2 on right

    if 4 == nbCells:
        if 2 == nbCols and 2 == nbRows: return '4grid'
        if 4 == nbCols and 0 == nbRows: return '4cols'
        if 0 == nbCols and 4 == nbRows: return '4rows'
        # TODO: other cases:

    return 'unknown'



class PanelChangedCommand(sublime_plugin.EventListener):
    last_work_group = None
    settings = None
    def on_activated(self, view):
        # Load settings.
        win  = view.window()
        if self.settings == None:
            self.settings = sublime.load_settings("ExpandGroup.sublime-settings")

        # If mouse focus disabled. Exit.
        triggered_by_command = time.time() - LAST_FOCUS_GROUP_TIME < EVENT_TIME
        triggered_by_mouse = not triggered_by_command

        if triggered_by_mouse and self.settings.get('resize_on_focus') == False: return 0

        # If theres only one group in current window. Do nothing.
        if win.num_groups() == 1: return 0

        # Current active group.
        current_active_group = win.active_group()

        # Working group not changed. Do nothing.
        if self.last_work_group == current_active_group: return 0

        # Update last work group.
        self.last_work_group = current_active_group





        # By default we show left side.
        # Note the extra parameter ignore_focus_on_resize.
        # It prevents an infinite loop. A short circuit! :O
        args = {"ignore_focus_on_resize":True}
        win.run_command("expand_group", args)

class GoToGroupCommand(sublime_plugin.WindowCommand):
    settings = None
    def run(self, direction, withCurrentFile=False):
        win       = self.window
        num       = win.num_groups()
        act       = win.active_group()
        group     = 0
        action    = "focus_group"
        structure = getLayoutStructure(win)

        logger = getLogger()

        #logger.info('GoToGroupCommand===================================')
        #logger.info('structure:  %s', structure)
        #logger.info('num  : %d', num)
        #logger.info('act  : %d', act)

        if withCurrentFile: action = "move_to_group"

        if '2cols' != structure and '2rows' != structure and '4grid' != structure:
            return 0

        if direction == 'left'  : group = act - 1
        if direction == 'right' : group = act + 1

        if '2cols' == structure or '4grid' == structure:
          if direction == 'up'    : group = act - 2
          if direction == 'down'  : group = act + 2

        if '2rows' == structure:
          if direction == 'up'    : group = act - 1
          if direction == 'down'  : group = act + 1

        #logger.info('group : %d', group)
        #logger.info('action: %s', action)

        global LAST_FOCUS_GROUP_TIME
        LAST_FOCUS_GROUP_TIME = time.time()
        win.run_command(action, {"group": group})
        #logger.info('===================================================')

class ExpandGroupCommand(sublime_plugin.WindowCommand):
    settings = None
    def run(self, ignore_focus_on_resize=False):
        # Load settings
        if self.settings == None:
            self.settings = sublime.load_settings("ExpandGroup.sublime-settings")

        win       = self.window
        num       = win.num_groups()
        act       = win.active_group()
        ratioConf = self.settings.get('ratio')
        ratio     = 0.3
        middle    = 0.5
        structure = getLayoutStructure(win)

        logger = getLogger()
        #logger.info('ExpandGroupCommand=================================')
        #logger.info('structure:  %s', structure)
        #logger.info('act      : %d', act)
        #logger.info('ratio    : %f', ratio)


        if ratioConf != None: ratio = ratioConf

        if '2cols' != structure and '2rows' != structure and '4grid' != structure:
            return 0

        if '2cols' == structure:
            if act == 0: colSep = middle + ratio
            if act == 1: colSep = middle - ratio

            #logger.info('colSep: %f', colSep)

            self.window.run_command('set_layout', {
                "cols" : [0, colSep, 1],
                "rows" : [0, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
            })

        if '2rows' == structure:
            if act == 0: rowSep = middle + ratio
            if act == 1: rowSep = middle - ratio

            #logger.info('rowSep: %f', rowSep)

            self.window.run_command('set_layout', {
                "cols" : [0, 1],
                "rows" : [0, rowSep, 1],
                  "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
            })

        if '4grid' == structure:
            if act == 0:
                colSep = middle + ratio
                rowSep = middle + ratio

            if act == 1:
                colSep = middle - ratio
                rowSep = middle + ratio

            if act == 2:
                colSep = middle + ratio
                rowSep = middle - ratio

            if act == 3:
                colSep = middle - ratio
                rowSep = middle - ratio

            #logger.info('colSep: %f', colSep)
            #logger.info('rowSep: %f', rowSep)

            self.window.run_command('set_layout', {
                "cols" : [0, colSep, 1],
                "rows" : [0, rowSep, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1],
                          [0, 1, 1, 2], [1, 1, 2, 2]]
            })
        #logger.info('===================================================')
