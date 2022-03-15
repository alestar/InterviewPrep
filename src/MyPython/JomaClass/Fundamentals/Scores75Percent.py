def score(total, correct, wrong):
    return (correct * 2 + wrong * 1)/(total *2) * 100


def score75(total, correct, wrong):
    return min(100, score((0.75*total),correct,(min(0.75*total,wrong))))


def score75_2(total, correct, wrong):
    return min(100, score((0.75*total),min(correct,0.75*total),wrong))