import sublime, sublime_plugin
from os import path
import datetime

PACKAGE_SETTINGS = "AndyEdits.sublime-settings"
if sublime.platform() == "linux":
    # Try and load Linux Python2.6 lib.  Default path is for Ubuntu.
    linux_lib = sublime.load_settings(PACKAGE_SETTINGS).get("linux_python2.6_lib",
        "/usr/lib/python2.6/lib-dynload")
    if not linux_lib in sys.path and path.exists(linux_lib):
        sys.path.append(linux_lib)

# ICON: a small icon to appear in the gutter - defaults to True (use pencil)
if sublime.load_settings(PACKAGE_SETTINGS).get("use_icon", True):
    if sublime.load_settings(PACKAGE_SETTINGS).get("ST_icon", False):
        ICON = sublime.load_settings(PACKAGE_SETTINGS).get("ST_icon")
    else:
        ICON = path.pardir + '/AndyEdits/icon'
else:
    ICON = ""

ICONSCOPE = sublime.load_settings(PACKAGE_SETTINGS).get("icon_scope", "comment")
# affects the colour of the gutter icon and outlining
ICONCURRENT = sublime.load_settings(PACKAGE_SETTINGS).get("icon_current", "comment")
# affects the colour of the gutter icon for the current edit-region
SAVEDSCOPE = sublime.load_settings(PACKAGE_SETTINGS).get("saved_scope", "keyword")

SAVED_EDITS = sublime.load_settings(PACKAGE_SETTINGS).get("saved_edits", False)
OUTPUT_EDITS = sublime.load_settings(PACKAGE_SETTINGS).get("output_edits", False)

JUSTDELETED = {}
# Uses view.id() as key and a single boolean True/False value.
# (Prevents a deleted region from being immediately re-created.)

def showRegion(view, reg):
    view.sel().clear()
    view.sel().add(reg)
    view.show(reg)

def isView(view_id):
    if not view_id: return False
    window = sublime.active_window()
    view = window.active_view() if window != None else None
    return (view is not None and view.id() == view_id)

def adjustEdits(view):
    # Add recently edited line to all previous edits, 
    # also joins consecutive edit lines together.
    # Returns: the edited regions or False if there are none.
    edited = view.get_regions("edited_rgns") or []
    edited_last = view.get_regions("edited_rgn") or []
    if not edited and not edited_last:
        return False
    new_edits = []
    if edited_last:
        edited.extend(edited_last)
    eov = view.size()
    view.erase_regions("edited_rgns")
    for i, r in enumerate(sorted(edited)):
        if i > 0 and r.begin() <= prev_end + 1:
            # collapse adjoining regions
            new_edits.pop()
            r = sublime.Region(prev_begin, max(r.end(), prev_end))
        elif r.begin() < eov:
            curr_line, _ = view.rowcol(r.begin())
            if i > 0 and curr_line == prev_line + 1:
                # Check if there are ony spaces and/or tabs between 2 regions 
                # (on adjacent lines); if so, treat as a single edit-region.
                inter_region = sublime.Region(prev_end + 1, r.begin() - 1) if \
                    (prev_end + 1 < r.begin() - 1) else None
                if inter_region:
                    inter_content = view.substr(inter_region)
                    inter_content = inter_content.strip()
                    if inter_content == '' or inter_content is None:
                        new_edits.pop()
                        r = sublime.Region(prev_begin, max(r.end(), prev_end))
        new_edits.append(r)
        prev_begin, prev_end = (r.begin(), r.end())
        prev_line, _ = view.rowcol(prev_end)
    view.add_regions("edited_rgns", new_edits, ICONSCOPE, ICON, \
        sublime.HIDDEN | sublime.PERSISTENT)
    return view.get_regions("edited_rgns") or []

def getEditList(view, edited):
    the_edits = []
    curr_edit = view.get_regions("edited_rgn") or []
    curr_edit = curr_edit[0] if curr_edit else None
    for i, r in enumerate(edited):
        curr_line, _ = view.rowcol(r.begin())
        curr_text = view.substr(r).strip()[:50]
        if not len(curr_text):
            curr_text = view.substr(view.line(r)).strip()[:50] + " (line)"
        if curr_edit and r.intersects(curr_edit):
            display_line = "*%03d %s" % (curr_line + 1, curr_text)
        else:
            display_line = " %03d %s" % (curr_line + 1, curr_text)
        the_edits.append(display_line)
    return the_edits

def getFullEditList(view, edited):
    the_edits = []
    locations = []
    curr_edit = view.get_regions("edited_rgn") or []
    curr_edit = curr_edit[0] if curr_edit else None
    for i, r in enumerate(edited):
        curr_line, _ = view.rowcol(r.begin())
        curr_text = view.substr(r).strip()[:50]
        if not len(curr_text):
            curr_text = view.substr(view.line(r)).strip()[:50] + " (line)"
        if curr_edit and r.intersects(curr_edit):
            display_line = "  * %03d %s" % (curr_line + 1, curr_text)
        else:
            display_line = "    %03d %s" % (curr_line + 1, curr_text)
        the_edits.append(display_line)
        locations.append((view, r))
    return the_edits, locations

class ListAllEdits(sublime_plugin.WindowCommand):
    def run(self):
        full_list = []
        self.locations = []
        for vw in self.window.views():
            edited = adjustEdits(vw)
            if edited:
                the_edits, locs = getFullEditList(vw, edited)
                if the_edits:
                    the_edits.insert(0, "%s" % (vw.file_name() or "No filename"))
                    locs.insert(0, (vw, vw.sel()[0]))
                    full_list += the_edits
                    self.locations += locs
        if full_list:
            self.window.show_quick_panel(full_list, self.on_chosen)
        else:
            sublime.status_message('No edits to list.')

    def on_chosen(self, index):
        if index == -1: return
        vw, reg = self.locations[index]
        sublime.active_window().focus_view(vw)
        showRegion(vw, reg)
        del self.locations[:]

class ToggleEditsCommand(sublime_plugin.TextCommand):
    # Toggles outlining of edited lines.
    def run(self, edit):
        if not isView(self.view.id()):
            sublime.status_message('Click into the view/tab first.')
            return
        edited = adjustEdits(self.view)
        if not edited:
            sublime.status_message('No edits to show or hide.')
            return
        toggled = self.view.get_regions("toggled_edits") or []
        if toggled:
            self.view.erase_regions("toggled_edits")
        else:
            self.view.add_regions("toggled_edits", edited, ICONSCOPE, \
                ICON, sublime.DRAW_OUTLINED)
            sublime.status_message("There are %d edit region(s)." % (len(edited)))

class PrevEditLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not isView(self.view.id()):
            sublime.status_message('Click into the view/tab first.')
            return
        currA = self.view.sel()[0].begin()
        edited = adjustEdits(self.view)
        if not edited:
            sublime.status_message('No edits to go to.')
            return
        for reg in [r for r in reversed(edited) if r.begin() < currA]:
            showRegion(self.view, reg)
            break
        else:
            sublime.status_message('No edits further up.')

class NextEditLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if not isView(self.view.id()):
            sublime.status_message('Click into the view/tab first.')
            return
        currA = self.view.sel()[0].begin()
        edited = adjustEdits(self.view)
        if not edited:
            sublime.status_message('No edits to go to.')
            return
        for reg in [r for r in edited if r.begin() > currA]:
            showRegion(self.view, reg)
            break
        else:
            sublime.status_message('No edits further down.')

class CreateEditCommand(sublime_plugin.TextCommand):
    # Create an edit region for the current selection.
    def run(self, edit):
        if not isView(self.view.id()):
            sublime.status_message('Click into the view/tab first.')
            return
        edited = adjustEdits(self.view) or []
        curr_region = self.view.sel()[0]
        if curr_region.empty():
            sublime.status_message('You must select some text.')
            return
        edited.append(curr_region)
        self.view.erase_regions("edited_rgns")
        self.view.add_regions("edited_rgns", edited, ICONSCOPE, ICON, \
            sublime.HIDDEN | sublime.PERSISTENT)
        sublime.status_message('New edit region created.')

class QuickEditsCommand(sublime_plugin.TextCommand):
    # Shows a quick panel to jump to edit lines.
    def run(self, edit):
        self.vid = self.view.id()
        if not isView(self.vid):
            sublime.status_message('Click into the view/tab first.')
            return
        edited = adjustEdits(self.view)
        if not edited:
            sublime.status_message('No edits to list.')
            return
        the_edits = getEditList(self.view, edited)
        if the_edits:
            sublime.active_window().show_quick_panel(the_edits, self.on_chosen)

    def on_chosen(self, index):
        if index == -1: return
        if not isView(self.vid):
            sublime.status_message('You are in a different view.')
            return
        edited = self.view.get_regions("edited_rgns") or []
        for reg in [r for i, r in enumerate(edited) if i == index]:
            showRegion(self.view, reg)
            break

class DeleteEditCommand(sublime_plugin.TextCommand):
    # Shows a quick panel to remove edit history for a region.
    def run(self, edit):
        self.vid = self.view.id()
        if not isView(self.vid):
            sublime.status_message('Click into the view/tab first.')
            return
        edited = adjustEdits(self.view)
        if not edited:
            sublime.status_message('No edit history to delete.')
            return
        the_edits = getEditList(self.view, edited)
        if the_edits:
            the_edits.insert(0, " -- DELETE EDIT REGION (except most recent) -- ")
            sublime.active_window().show_quick_panel(the_edits, self.on_chosen)

    def removeTempHighlight(self, old_line):
        self.view.erase_regions("temp_del")
        sublime.status_message("Edit history removed from line %d." % old_line)

    def on_chosen(self, index):
        if index <= 0: return
        if not isView(self.vid):
            sublime.status_message('You are in a different view.')
            return
        edited = self.view.get_regions("edited_rgns") or []
        reg = edited[index - 1]
        current_editr = self.view.get_regions("edited_rgn") or []
        if current_editr and reg.intersects(current_editr[0]):
            sublime.status_message('Cannot delete most recent edit.')
            return
        del edited[index - 1]
        self.view.erase_regions("edited_rgns")
        self.view.add_regions("edited_rgns", edited, ICONSCOPE, ICON, \
            sublime.HIDDEN | sublime.PERSISTENT)
        toggled = self.view.get_regions("toggled_edits") or []
        if toggled:
            self.view.erase_regions("toggled_edits")
            self.view.add_regions("toggled_edits", edited, ICONSCOPE, \
                ICON, sublime.DRAW_OUTLINED)
        old_line, _ = self.view.rowcol(reg.begin())
        self.view.add_regions("temp_del", [reg], "invalid", sublime.DRAW_OUTLINED)
        sublime.set_timeout(lambda: self.removeTempHighlight(old_line + 1), 500)
        JUSTDELETED[self.vid] = True

class CaptureEditing(sublime_plugin.EventListener):
    edit_info = {}
    def on_modified(self, view):
        # Create hidden regions that mirror the edited regions.
        # Maintains a single edit region for the current line.
        vid = view.id()
        if not isView(vid):
            return
        if not vid in CaptureEditing.edit_info:
            CaptureEditing.edit_info[vid] = {}
        cview = CaptureEditing.edit_info[vid]
        sel = view.sel()[0]
        currA, currB = (sel.begin(), sel.end())
        cview['curr_line'], _ = view.rowcol(currA)
        if not ('prev_line' in cview) or cview['prev_line'] is None:
            # on first run, or just deleted an edit region
            cview['prev_line'] = cview['curr_line']
            if currA > 0 and sel.empty():
                # include the first character?
                same_line, _ = view.rowcol(currA - 1)
                if cview['curr_line'] == same_line:
                    currA -= 1
                cview['to_eol'] = (currB == view.line(currB).end())
            cview['lastx'], cview['lasty'] = (currA, currB)
        elif cview['curr_line'] == cview['prev_line']:
            # still on the same line
            cview['lastx'] = min(currA, cview['lastx'])
            if cview['to_eol']:
                cview['lasty'] = view.line(currB).end()
            else:
                # don't go beyond end of current line..
                cview['lasty'] = max(currB, min(cview['lasty'] + 1, \
                    view.line(sel).end()))
        else:
            # moving to a different line
            # if cview['to_eol']:
            #     # adjust previous edit region to end-of-line
            #     prev_editl = view.get_regions("edited_rgn") or []
            #     if prev_editl:
            #         prev_editl = prev_editl[0]
            #         prev_editl = sublime.Region(prev_editl.begin(), \
            #             view.line(prev_editl.begin()).end())
            #         view.erase_regions("edited_rgn")
            #         view.add_regions("edited_rgn", [prev_editl], ICONCURRENT, \
            #             ICON, sublime.HIDDEN | sublime.PERSISTENT)
            cview['prev_line'] = cview['curr_line']
            if currA > 0 and sel.empty():
                # include the first character?
                same_line, _ = view.rowcol(currA - 1)
                if cview['curr_line'] == same_line:
                    currA -= 1
            cview['to_eol'] = (currB == view.line(currB).end())
            cview['lastx'], cview['lasty'] = (currA, currB)
            _ = adjustEdits(view)
        if cview['lastx'] < cview['lasty']:
            curr_edit = sublime.Region(cview['lastx'], cview['lasty'])
            view.erase_regions("edited_rgn")
            view.add_regions("edited_rgn", [curr_edit], ICONCURRENT, \
                ICON, sublime.HIDDEN | sublime.PERSISTENT)

    def on_selection_modified(self, view):
        vid = view.id()
        if not isView(vid):
            return
        if not vid in CaptureEditing.edit_info:
            CaptureEditing.edit_info[vid] = {}
        cview = CaptureEditing.edit_info[vid]
        if vid in JUSTDELETED and JUSTDELETED[vid] == True:
            JUSTDELETED[vid], cview['prev_line'] = (False, None)
            return
        if ('prev_line' in cview) and cview['prev_line'] is not None:
            curr_line, _ = view.rowcol(view.sel()[0].begin())
            if (cview['prev_line'] != curr_line) and (cview['lastx'] < cview['lasty']):
                edited = view.get_regions('edited_rgns') or []
                for i, r in enumerate(edited):
                    if r.begin() >= cview['lastx'] and r.end() <= cview['lasty']:
                        break
                else:
                    edited.append(sublime.Region(cview['lastx'], cview['lasty']))
                    view.erase_regions("edited_rgns")
                    view.add_regions("edited_rgns", edited, ICONSCOPE, \
                        ICON, sublime.HIDDEN | sublime.PERSISTENT)
                    cview['prev_line'] = None

    def on_close(self, view):
        vid = view.id()
        if vid in CaptureEditing.edit_info:
            del CaptureEditing.edit_info[vid]

    def on_post_save(self, view):
        if not SAVED_EDITS: return
        vid = view.id()
        re_activate = isView(vid)
        if not re_activate: return
        _ = adjustEdits(view)
        saved_edits = view.get_regions('edited_rgns')
        if not saved_edits: return
        view.add_regions("saved_rgns", saved_edits, SAVEDSCOPE, \
                        ICON, sublime.PERSISTENT | sublime.DRAW_OUTLINED)
        
        if not OUTPUT_EDITS: return
        newview = sublime.active_window().new_file()
        edit = newview.begin_edit()
        newview.insert(edit, 0, view.file_name() + "\n")
        newview.insert(edit, newview.size(), 
            datetime.datetime.now().strftime("%c") + '\n')

        for i, r in enumerate(sorted(saved_edits)):
            editline, _ = view.rowcol(r.begin())
            newview.insert(edit, newview.size(), "\n-----\nLine: " + \
                str(editline) + '\n')
            newview.insert(edit, newview.size(), view.substr(r))
        newview.end_edit(edit)
        if re_activate:
            sublime.active_window().focus_view(view)