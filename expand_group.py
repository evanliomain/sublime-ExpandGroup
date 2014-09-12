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

class PanelChangedCommand(sublime_plugin.EventListener):
    last_work_group = None
    settings = None
    def on_activated(self, view):
        # Load settings.
        if self.settings == None:
            self.settings = sublime.load_settings("expand-group.sublime-settings")

        # If mouse focus disabled. Exit.
        if self.settings.get('resize_on_focus') == False: return 0

        # If theres only one group in current window. Do nothing.
        if view.window().num_groups() == 1: return 0

        # Current active group.
        current_active_group = view.window().active_group()

        # Working group not changed. Do nothing.
        if self.last_work_group == current_active_group: return 0

        # Update last work group.
        self.last_work_group = current_active_group

        # By default we show left side.
        # Note the extra parameter ignore_focus_on_resize. 
        # It prevents an infinite loop. A short circuit! :O
        args = {"ignore_focus_on_resize":True}
        win  = view.window()
        win.run_command("expand_group", args)

class GoToGroupCommand(sublime_plugin.WindowCommand):
    settings = None
    def run(self, direction, withCurrentFile=False):
        win    = self.window
        num    = win.num_groups()
        act    = win.active_group()
        group  = 0
        action = "focus_group"

        if withCurrentFile: action = "move_to_group"

        #If theres only one or 3 group in current window. Do nothing.
        if num == 1: return 0
        if num == 3: return 0

        if direction == 'left'  : group = act - 1
        if direction == 'right' : group = act + 1
        if direction == 'up'    : group = act - 2
        if direction == 'down'  : group = act + 2

        win.run_command(action, {"group": group})

class ExpandGroupCommand(sublime_plugin.WindowCommand):
    settings = None
    def run(self, ignore_focus_on_resize=False):
        # Load settings
        if self.settings == None:
            self.settings = sublime.load_settings("expand-group.sublime-settings")
        win    = self.window
        num    = win.num_groups()
        act    = win.active_group()
        ratio  = 0.3
        middle = 0.5

        #If theres only one or 3 group in current window. Do nothing.
        if num == 1: return 0
        if num == 3: return 0
        if num == 2:
            if act == 0: colSep = middle + ratio
            if act == 1: colSep = middle - ratio
            self.window.run_command('set_layout', {
                "cols" : [0, colSep, 1],
                "rows" : [0, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
            })
        if num == 4:
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

            self.window.run_command('set_layout', {
                "cols" : [0, colSep, 1],
                "rows" : [0, rowSep, 1],
                "cells": [[0, 0, 1, 1], [1, 0, 2, 1],
                          [0, 1, 1, 2], [1, 1, 2, 2]]
            })
