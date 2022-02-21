# Infinite Monkey Theorem Simulator
## Play the simulator [here](https://replit.com/@DeepanShah/Infinite-Monkey-Simulator#main.py)!

For my CS109 Challenge Project, I decided to write a simulator for the Infinite Monkey Theorem, which states that "a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare" (Wikipedia). I had a lot of fun coding it up, and I hope you have fun playing with it and reading my write up! *No monkeys were harmed in the making of this project

In writing my code, I made multiple assumptions. The original theorem assumes that the monkey sits in front of a 50 key typewriter, but I chose to make the job easier on the monkey by providing the monkey a 26 key _mechanical keyboard_ that consists of only lowercase alphabetical letters. I also used the original theorem's assumption that each key is equally likely to be pressed by the monkey.

The code itself is pretty simple. Here is the main chunk of code that does the monkey's work for them (sadly automation is even taking the jobs of monkeys...):
```markdown
  def generateWord(input):
    numTrials = 0
    str = ""
    while str != input:
        str = ""
        numTrials += 1
        for k in range(len(input)):
            letter = generateLetter()
            str += letter
        if str == input:
            return numTrials
```
            
After taking in an input word from the user, the code loops interminably until the string it creates matches the input string. We assume that our computer monkey knows how long of a word it needs to make, and also is blessed with the ability to know when the created word matches the input word. For each attempt the monkey makes, numTrials is incremented by one. At last, once the monkey is freed from its misery, it returns numTrials and takes a banana break.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/DeepanShah/imt/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
