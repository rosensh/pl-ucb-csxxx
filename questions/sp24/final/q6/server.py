def generate(data):
    data["correct_answers"]["a"] = "(if (f (car s)) 1 0)"
    data["correct_answers"]["d"] = "(if (< k (truths (car s) number?)) 0 (eights (cdr s)))"
