# fuck this one
def encodeR(input_string):
    prev = ''
    count = 1
    tally = ''
    for char in input_string:
        if char != prev:
            if prev:
                if count == 1:
                    tally += prev
                else:
                    tally += str(count) + prev
            count = 1
            prev = char
        else:
            count += 1
    else:
        if count == 1:
            tally += prev
        else:
            tally += str(count) + prev
    return tally

def decodeR(input_string):
    import re
    lst = []
    matches = re.findall(r'\d*\D', input_string, flags=re.UNICODE)
    for match in matches:
        if match[0].isdigit():
            number = re.findall(r'\d*', match, flags=re.UNICODE)
            alpha  = re.findall(r'\D', match, flags=re.UNICODE)
            multiple = int(number[0]) * alpha[0]
            lst.append(multiple)
        else:
            lst.append(match)

    merge = ''.join(lst)
    return merge


            