import re


pattern = re.compile(r'g(ha(fla|nima)|a(lbana|rrufo)|uidichar)')

def match(st):
    return bool(pattern.fullmatch(st))


def test():
    sample = [
        ("ghafla", True),
        ("ghanima", True),
        ("galbana", True),
        ("garrufo", True),
        ("guidichar", True),
        ("sdkjhf", False),
        ("gafla", False),
        ("gharrufo", False),
    ]
    
    for input_st, expected in sample:
        result = match(input_st)
        assert result == expected
    print("Passed: All tests have been passed correctly")

test()