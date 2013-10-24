AndyEdits
=========

Jump between edited regions - optional gutter icon
THERE IS CURRENTLY A RENDERING ISSUE WITH WINDOWS

Can jump to next or previous edited-region or use a 
quick-panel which shows the edited text and line number. 
(If the edited text is just whitespace then the panel 
will display the full line's text.)

A shortcut can toggle outlining of the edited regions. 
An optional icon can appear in the gutter. You 
could use your own icon if you prefer! icon_scope 
determines the colour of the icon and outlining: 
"class" works well for me. icon_current is the scope 
for the current edit-region.

You can remove the edit history for a region using 
another shortcut, via a quick panel (although you 
cannot remove the most recent edit). If you highlight 
some text you can create/add it as an edit-region.

You can list, and jump to, edits across all open files.

Details for edited regions will persist if you close ST, 
but not if you close the file/view. This is the 
default persistence behaviour for ST.

My suggestions for your Key Bindings (User) are:
{ "keys": ["ctrl+alt+d"], "command": "delete_edit" },
{ "keys": ["ctrl+alt+h"], "command": "toggle_edits" },
{ "keys": ["ctrl+alt+j"], "command": "quick_edits" },
{ "keys": ["ctrl+alt+k"], "command": "prev_edit_line" },
{ "keys": ["ctrl+alt+l"], "command": "next_edit_line" },
{ "keys": ["ctrl+alt+m"], "command": "list_all_edits" },
{ "keys": ["ctrl+alt+c"], "command": "create_edit" }

CURRENT LIMITATIONS:
Mulitple Undo, Redo can disturb the edit-history: use Create and/or 
Delete edit-region to correct this. This is a consequence of the 
ST-API behaviour.

Multi-select will only remember the first selection area.

It doesn't include automatically inserted (matched) brackets
or quotes within the current edit-region, unless editing starts on 
a new line or at the end of an existing line. Therefore, the 
edit-region may be split into several edits, and/or the region may 
end before it should. Selecting the area and using Ctrl-Alt-C to 
Create a new (single) edit-region will correct this. This can be 
done at any time and allows you to explicity determine the start 
and end points for the edit-region.

ST-API ISSUE:
An issue when using add_regions() with Windows, and relating to colour 
themes, may arise. The gutter icon may not display and the scrollbar 
and ruler may be poorly rendered. Switching to a default theme and back 
to your chosen theme should resolve this. You may also need to close 
and re-start ST.
