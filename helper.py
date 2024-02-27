import math
months_dict = {
    '01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

def get_progress_bar (current, total):
    bar = ''
    percent = (current / float(total))*100
    dots = math.floor(50 * (current / float(total)))
    for x in range(0, dots):
        bar += '\u2588'
    for x in range(0, 50 - dots):
        bar += '\u2591'
    return bar+' - '+str(round(percent))+'%'

def count_total_elements(lst):
    total_elements = 0
    for item in lst:
        if isinstance(item, list):
            total_elements += count_total_elements(item)
        else:
            total_elements += 1
    return total_elements
