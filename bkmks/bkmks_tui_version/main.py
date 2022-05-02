from __future__ import unicode_literals
import questionary
from add import add
from delete import delete
from search import search
from update import update
from see import see

resposta = questionary.select(
    'What do you want to do?',
    choices=[
        'Add a Bookmark',
        'Search for a Bookmark',
        'See Bookmarks',
        'Update a Bookmark',
        'Delete a Bookmark'
            ]).ask()

if resposta == 'Add a Bookmark':
    add()
if resposta == 'Search for a Bookmark':
    search()
if resposta == 'See Bookmarks':
    see()
if resposta == 'Update a Bookmark':
    update()
if resposta == 'Delete a Bookmark':
    delete()
