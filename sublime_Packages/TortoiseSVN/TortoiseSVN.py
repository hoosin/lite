import sublime
import sublime_plugin
import os
import subprocess


def _svn_command(command, path):
	settings = sublime.load_settings('TortoiseSVN.sublime-settings')
	tortoiseproc_path = settings.get('tortoiseproc_path')

	if not os.path.isfile(tortoiseproc_path):
		sublime.error_message(''.join(['can\'t find TortoiseProc.exe,',
			' please config setting file', '\n   --sublime-TortoiseSVN']))
		raise

	proce = subprocess.Popen('"' + tortoiseproc_path + '"' + ' /closeonend:3' + 
		' /command:' + command + ' /path:"%s"' % path , stdout=subprocess.PIPE)

class SvnUpdateCommand(sublime_plugin.TextCommand):

	def run(self, edit, paths=None):
		if paths:
			dir = '*'.join(paths)
		else:
			dir = self.view.file_name()

		_svn_command('update', dir)

		(row,col) = self.view.rowcol(self.view.sel()[0].begin())
		self.lastLine = str(row + 1);

		if not paths:
			sublime.set_timeout(self.revert, 100)

	def revert(self):
		self.view.run_command('revert')
		sublime.set_timeout(self.revertPoint, 600)

	def revertPoint(self):
		self.view.window().run_command('goto_line',{'line':self.lastLine})


class SvnCommitCommand(sublime_plugin.TextCommand):

	def run(self, edit, paths=None):
		if paths:
			dir = '*'.join(paths)
		else:
			dir = self.view.file_name()

		_svn_command('commit', dir)


class SvnRevertCommand(sublime_plugin.TextCommand):

	def run(self, edit, paths=None):
		if paths:
			dir = '*'.join(paths)
		else:
			dir = self.view.file_name()

		_svn_command('revert', dir)

		(row,col) = self.view.rowcol(self.view.sel()[0].begin())
		self.lastLine = str(row + 1);

		if not paths:
			sublime.set_timeout(self.revert, 100)

	def revert(self):
		self.view.run_command('revert')
		sublime.set_timeout(self.revertPoint, 600)

	def revertPoint(self):
		self.view.window().run_command('goto_line',{'line':self.lastLine})


class SvnLogCommand(sublime_plugin.TextCommand):

	def run(self, edit, paths=None):
		if paths:
			dir = '*'.join(paths)
		else:
			dir = self.view.file_name()

		_svn_command('log', dir)


class SvnDiffCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		_svn_command('diff', self.view.file_name())
