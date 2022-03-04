# Infinite Monkey Theorem Simulator
## Play the simulator [here](https://replit.com/@DeepanShah/Infinite-Monkey-Simulator#main.py)!

![Alt Text](https://media.giphy.com/media/f5BwvEFBcgzU4/giphy.gif)

### Intro
For my CS109 Challenge Project, I decided to write a simulator for the Infinite Monkey Theorem, which states that "a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare" (Wikipedia). I had a lot of fun coding it up, and I hope you have fun playing with it and reading my write up! 

Disclaimer: No monkeys were harmed in the making of this project

### Code Explanation
In writing my code, I made multiple assumptions. The original theorem assumes that the monkey sits in front of a 50 key typewriter, but I chose to make the job easier on the monkey by providing the monkey a 26 key keyboard that consists of only lowercase alphabetical letters. I also used the original theorem's assumption that each key is equally likely to be pressed by the monkey.

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
            
After receiving an input word from the user, the code loops interminably until the string it creates matches the input string. We assume that our computer monkey knows how long of a word it needs to make, and also is blessed with the ability to know when the created word matches the input word. For each attempt the monkey makes, numTrials is incremented by one. At last, it returns numTrials, and the monkey gets a banana break.

### Probability Explanation
As I stated earlier, I assumed that each of the 26 lowercase alphabetical letters were equally likely to be pressed by the monkey. Therefore, the number of attempts to get an n-length word correct should be 26^n, and that is proven by calculating the mean numTrials over a large sample size. Here are the mean numTrials for n = 1, 2, 3:

For n = 1:
```
Calculating the mean numTrials for 'd' over 10,000 runs...
Mean numTrials: 25.9809
```
For n = 2:
```
Calculating the mean numTrials for 'hi' over 10,000 runs...
Mean numTrials: 673.2949
```
For n = 3:
```
Calculating the mean numTrials for 'bye' over 10,000 runs...
Mean numTrials: 17253.6449
```
The results follow what we expected as 25.98 is about 26, 673.29 is about 676 (26^2), and 17253.64 is about 17,576 (26^3). 

This is all good and fun for our simulator, but what about generating a large text, like the complete works of Shakespeare like the theorem mentions?
Using 50 equally likely keys as the theorem mentions (we need more keys to produce more complex texts than just lowercase words), the probability of not typing "hello" in a block of 5 letters is 1 - (1/50)^5 which equals .999 (with 5 additional 9s) (Wikipedia). However, the probability of not typing "hello" in x blocks decreases as x increases.
```
For x = 1,000,000: (1- (1/50)^5)^1,000,000 = .996
For x = 10,000,000: (1- (1/50)^5)^10,000,000 = .968
For x = 100,000,000: (1- (1/50)^5)^100,000,000 = .726
For x = 1,000,000,000: (1- (1/50)^5)^1,000,000,000 = .041
```
With a "string" as long as the complete works of Shakespeare and with an infinite number of blocks (and an infinite amount of time), a monkey could very well write the completed works of Shakespeare. We could also rapidly cut down on time by having an infinite number of monkeys working at the same time (where each monkey represents one block), but these days it's really hard to acquire an infinite amount of monkeys. Thus, I can say with absolute certainty that in our lifetime we will not see a monkey randomly type out the complete works of Shakespeare.

![Alt Text](https://media.giphy.com/media/ySpxjJmsq9gsw/giphy.gif)

Thanks for reading!



Sources:

Wikimedia Foundation. (n.d.). Infinite monkey theorem. Wikipedia. Retrieved February 21, 2022, from https://en.wikipedia.org/wiki/Infinite_monkey_theorem 

GIPHY. (n.d.). Retrieved February 21, 2022, from https://giphy.com/ 
