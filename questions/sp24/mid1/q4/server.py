def generate(data):
    data["correct_answers"]["a_ii"] = "d != n % 10"
    data["correct_answers"]["b"] = "n % 10 != d"
    data["correct_answers"]["d"] = "k == count_if(lambda i: i == d)(n)"
    data["correct_answers"]["e"] = "count_if(lambda d: True)(n) == count_if(lambda d: d > 0 and d < 7 and d == n % 10)(n)"

