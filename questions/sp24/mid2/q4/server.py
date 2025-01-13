def generate(data):
    data["correct_answers"]["aii"] = "s[0]"
    data["correct_answers"]["b"] = "len(s) > 1 and s[0] + 1 == s[1]"
    data["correct_answers"]["c_i"] = "longest(s[1:])"
    data["correct_answers"]["c_iv"] = "k == result[-1] + 1"
    data["correct_answers"]["d_ii"] = "b.label == t.label + 1 and has_strip(b)"
    data["correct_answers"]["e_v"] = "has_strip(b) and (only_strips(b) or t.label + 1 == b.label)"

    


