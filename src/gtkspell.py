# -*- coding:utf-8 -*-
#
# Copyright (C) 2012, Maximilian Köhl <linuxmaxi@googlemail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gtk
import gtkspellcheck

"""
Legacy API for old Python GtkSpell:
http://www.pygtk.org/pygtkspell/class-gtkspell.html
"""


class Spell:
    def __init__(self, textview, language="en"):
        if hasattr(textview, "spell"):
            self.spellchecker = textview.spell.spellchecker
            self.spellchecker.enable()
        else:
            self.spellchecker = gtkspellcheck.SpellChecker(textview, language)
        self.textview = textview
        self.textview.spell = self

    def set_language(self, language):
        self.spellchecker.language = language

    def recheck_all(self):
        self.spellchecker.recheck()

    def detach(self):
        self.spellchecker.disable()


def get_from_text_view(textview):
    if hasattr(textview, "spell"):
        return textview.spell
