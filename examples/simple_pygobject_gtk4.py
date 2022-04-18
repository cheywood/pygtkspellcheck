# -*- coding:utf-8 -*-
#
# Copyright (C) 2012, Maximilian Köhl <linuxmaxi@googlemail.com>
# Copyright (C) 2012, Carlos Jenkins <carlos@jenkins.co.cr>
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

# Load example if running from source, ignore this
import sys
import os
from os.path import join, dirname
sys.path.append(join(dirname(__file__), "../src/"))

import gi
import locale
import logging
gi.require_version("Gtk", "4.0")
from gi.repository import GObject, Gtk

from gtkspellcheck import SpellChecker

logging.basicConfig(
    format="%(asctime)s | %(module)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO
)

class TestApp(Gtk.Application):

    def __init__(self, *args):
        super().__init__(*args)
        self.connect("activate", self.activate)

    def activate(self, _app: Gtk.Application):
        window = Gtk.Window()
        window.set_title("PyGtkSpellCheck Example")
        view = Gtk.TextView()

        self.spellchecker = SpellChecker(view, collapse=False)
        for code, name in self.spellchecker.languages:
            print("code: %5s, language: %s" % (code, name))

        self.spellchecker.connect("notify::language", self.__language_changed)

        self.view = view
        window.set_child(view)
        app.add_window(window)
        window.present()

    def __language_changed(self, _obj: GObject.Object, _spec: GObject.ParamSpec) -> None:
        print(f"New language {self.spellchecker.language}")

if __name__ == "__main__":
    app = TestApp()
    app.run()
