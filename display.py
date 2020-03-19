
def get_display_str(display_file, descending, numbers):
    lines = list(display_file.readlines())
    ranks = list(range(1, len(lines) + 1))
    if descending:
        ranks.reverse()

    pre = ''
    if numbers:
        pre = '{}. '

    display_list = []
    for i in ranks:
        display_list.append(pre.format(i) + lines[i - 1])

    return ''.join(display_list)
