def hey(what):
    what = what.rstrip()
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    elif what == "":
        return 'Fine. Be that way!'
    else:
        return "Whatever."