from talon.voice import Context, Key
from user.utils import text


ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    'channel': Key('cmd-k'),
    'channel <dgndictation>': [Key('cmd-k'), text, Key('enter')],
    'channel up': Key('alt-up'),
    'channel down': Key('alt-down'),
    '(highlight command | insert command)': ['``', Key('left')],
    '(highlight code | insert code)': ['``````', Key('left left left')],

    'baxley': Key('cmd-['),
    'fourthly': Key('cmd-]'),
    'goneck': Key('shift-alt-down'),
    'gopreev': Key('shift-alt-up'),

    'toggle sidebar': Key('cmd-.'),
    '(unread threads | new threads)': Key('cmd-shift-t'),
}

ctx.keymap(keymap)
