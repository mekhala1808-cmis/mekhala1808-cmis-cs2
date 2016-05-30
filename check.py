def grid(w, h):
    row = ""
    result "\n"
    while h > 0:
        while w > 0:
            row += "."
            w -= 1
        result +- row + "\n"
        h -= h
    return result
print grid(10, 10)
