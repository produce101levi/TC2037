# TC2037

# Description

**Chosen language:** Chakobsa #5

**Words to recognize:**

galbana

garrufo

ghafla

ghanima

guidichar

**Context of the language:**
This language is called Chakobsa. This is a fictional language created for “Dune: Part Two” by language constructors David J. Peterson and Jessie Peterson. They’d initially started out with just words that the author of the original 1965 novel, Frank Herbert, had made up for the story. From then, they created an entire language with its own vocabulary and gramma rules.

In the movie, this language is spoken by Indigenous people known as Fremen. Chakobsa is actually a real language originating from North West Caucasia, likely in the Circassian subgroup. This was originally a secret language only used by princes and nobles, and is still used to this day by their descendants. Possibly influenced by this language, Frank Herbert named the fictional language after this one in his novel. However, in the fictional world, the language is really a mix of Arabic, Romani and Serbo-Croatian, among other languages.

# Model

**Automata**

<img width="594" alt="Screenshot 2024-04-01 at 7 15 57 a m" src="https://github.com/produce101levi/TC2037/assets/117374505/d7f4245e-7eef-411b-a1c1-4d1bfafa0c33">

**Regular Expression**

g(ha(fla|nima)|a(lbana|rrufo)|uidichar)


# Implementation
For the implementation of the lexical analysis, I used the regular expression stated previously. I began by importing "re" which stands for "regular expression" in python. Then, I defined a variable "pattern" where the value was the regular expression. This means that the regular expression's pattern would be recognized and inserted into the variable for future comparison. After doing that, I defined a function "match" where a string "st" would be received and through that function, the string is compared with the pattern through a boolean operator. This means the function would return either a "True" or "False" value. 

The program has an array of strings that, according to the match function's returned values, would return a value of True or False. They look like this.

```
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
```

If one of the string has an incorrect value, such as

```
("gharrufo", True)
```
the program will not run, as "gharrufo" is not a valid result of the regular expression.

# Tests
The tests are shown in the tests.py file.


# Analysis

This automaton has a linear time complexity o(n)
With n being the length of the input string.

The time it takes to process a string is directly proportional to the length of the string
