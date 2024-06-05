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


The regular expression is represented in the automaton. We start with the state that represents the letter g, which can then lead to either states h and a, a or uidichar. This means that the automata leads to forming either words that start with gha, ga or the word guidichar (Since this is the only word in the set that starts with a u).

From gha, the words that can be formed are ghafla or ghanima. 

From ga, the words that can be formed are galbana or garrufo.

# Other Solutions and why this one is best

Initially I had wanted to implement a solution that looked like this. 

![IMG_4505](https://github.com/produce101levi/TC2037/assets/117374505/36115600-511e-4aae-8b69-438ee10d708e)

This automata was extremely complicated because the idea was to have only one state per letter in the words. The diagram is hard to read, and also hard to organize. The regular expression representing this automata would not have been as easy to understand and/or validate in the tests. 

There are many states connecting to the same state, which can also make room for mistakes when a word in a language is analyzed. 

This is why I opted for a solution that's easier to understand, easier to test and easier to represent in a regular expression.

As for the regular expression, I had thought of plenty other interpretations.
    ga*(lbana|rrufo|h?(alfa|anima))
    ga*(lbana|rrufo|h?(afla|anima)|uidichar))
    gh*(afla|anima|a?(lbana|rrufo)|uidichar))
    gh*(afla|anima|a+(lbana|rrufo)|uidichar))
The problem with these regular expressions is the fact that they do not interpret the language correctly. 

ga*(lbana|rrufo|h?(alfa|anima)), for example, does not validate guidichar. It also implies that every word must begin with ga, which means words like ghafla would not be validated as correct, but words like gahalfa would. Also, words like gaalbana can be accepted because of the * symbol.

gh*(afla|anima|a+(lbana|rrufo)|uidichar)) implies that all words must begin with gh and that all words that contain at least one occurence of a are accepted. This means that words like galbana wouldn't be accepted, but words like ghalbana and ghaalbana would.

The final regular expression is not as complicated and is also easier to interpret. It also is a correct regular expression that has been validated by testing, so this is the best solution.



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

The pattern in this case is g(ha(fla|nima)|a(lbana|rrufo)|uidichar). The test analyzes each part of the pattern in a linear manner (from left to right). It checks the regular expression to see if the words match it and if they don't, the test continues analyzing the pattern. If none of the elements in the regular expression match the words, the value is false.

Because the algorithm runs through the entire regular expression in a linear manner, without backtracking, this is an algorithm that runs n times, therefore the time complexity is O(n).

