# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os,gettext

PluginLanguageDomain = "EPGImport"
PluginLanguagePath = "Extensions/EPGImport/po"

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
# 	print "[XMLTV-Import] set language to ", lang
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))
	gettext.bindtextdomain('enigma2', resolveFilename(SCOPE_LANGUAGE, ""))

def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
# 		print "[EPGImport] fallback to default translation for", txt
		t = gettext.dgettext('enigma2', txt)
	return t


localeInit()
language.addCallback(localeInit)
