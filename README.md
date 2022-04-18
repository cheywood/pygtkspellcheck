python-gtk4-temp-kludged-spellcheck
===================================

This is [pygtkspellcheck](https://github.com/koehlma/pygtkspellcheck) with some untasteful
changes made quickly to bring together a spelling solution under GTK4 in 
[Iotas](https://gitlab.gnome.org/cheywood/iotas). These changes are purely a stopgap until
a mature option is available for GTK4.

Please don't use this repo in any projects. This work won't be maintained, is not
supported, will crash and then eat your homework, etc.

This repo contains
- `pygtkspellcheck` crudely modified to operate atop GTK4
- Removal of Python 2 compatibility
- Removal of compatibility earlier GTK versions
- Some primitive support for batching the operation to recheck entire buffers
- Some half-cooked support for extending words into dictionary extra characters (which in
  practice due to the fact that `PyEnchant` doesn't expose `Hunspell`'s support for extra
  characters, means extending words through apostrophes)
- Tweaked default language selection behaviour

The credit for all of the good work done here of course goes to the original project 
authors (and all of the blame for the bad hatchet work in this body of changes lies with
me).

[The original project README](https://github.com/koehlma/pygtkspellcheck#readme).
