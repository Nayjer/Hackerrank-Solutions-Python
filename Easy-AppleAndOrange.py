def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_house = [1 for apple in apples if s <= apple+a <= t]
    oranges_house = [1 for orange in oranges if s <= orange+b <= t]
    return [sum(apples_house), sum(oranges_house)]
