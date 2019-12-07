def header_string(text, length):
    string = ("\n" + "*" * length + "\n")
    string += ("*" + " " * (length - 2) + "*" + "\n")
    string += ("*" + text.center((length-2), " ") + "*" + "\n")
    string += ("*" + " " * (length - 2) + "*" + "\n")
    string += ("*" * length + "\n")
    return string
