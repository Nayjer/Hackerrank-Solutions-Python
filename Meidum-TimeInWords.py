def timeInWords(h, m):
    words_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                  6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                  11: 'eleven', 12: 'twelve', 13: 'thirteen',
                  14: 'fourteen', 16: 'sixteen', 17: 'seventeen',
                  18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                  21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
                  24: 'twenty four', 25: 'twenty five', 26: 'twenty six',
                  27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine'}
    if m == 00:
        time_words = words_dict[h]+" o' clock"
    elif m == 1:
        time_words = "one minute past "+words_dict[h]
    elif 1 < m < 15 or 15 < m < 30:
        time_words = words_dict[m]+" minutes past "+words_dict[h]
    elif m == 15:
        time_words = "quarter past " + words_dict[h]
    elif m == 30:
        time_words = "half past "+words_dict[h]
    elif 30 < m < 45 or 45 < m < 59:
        time_words = words_dict[60-m] + " minutes to " + words_dict[h+1]
    elif m == 45:
        time_words = "quarter to " + words_dict[h+1]
    elif m == 59:
        time_words = "one minute to " + words_dict[h+1]
    return time_words
