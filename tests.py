# Import the library re (regular expression)
import re

# Give the program the regular expression for it to compile
pattern = re.compile(r'g(ha(fla|nima)|a(lbana|rrufo)|uidichar)')


# Define the function to match the input string with the pattern
def match(st):
    return bool(pattern.fullmatch(st))


# Define the function to test whether the input strings are accepted by the regular expression or not
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

# Run function test()
test()
