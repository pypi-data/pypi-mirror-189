# shyna/ShynaJokes



## Getting Started

Download links:

SSH clone URL: ssh://git@git.jetbrains.space/shyna623/shyna/ShynaJokes.git

HTTPS clone URL: https://git.jetbrains.space/shyna623/shyna/ShynaJokes.git



These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

What things you need to install the software and how to install them.

```
Examples
```

## Deployment

Add additional notes about how to deploy this on a production system.

## Resources

Add links to external resources for this project, such as CI server, bug tracker, etc.

## Features


Use Rapid API- jokes API
URL: https://rapidapi.com/Sv443/api/jokeapi-v2/
There is no limitation but there are chances of repetition. stay alert.

There are below method to use:

* shyna_random_jokes : any random jokes with no filter whatsoever.
* shyna_joke_contains: takes one parameter 'contains_string'. It will return any random jokes with that string
contained in it.
* shyna_programming_joke : Random jokes based on programming.
* shyna_pun_joke : Random jokes pun intended.
* shyna_spooky_joke: Random jokes on ghosts.
* shyna_christmas_joke: Random Christmas jokes.
* shyna_dad_joke: provide dad joke as text only.  


##Example

```python
from ShynaJokes import ShynaJokes
test = ShynaJokes.ShynaJokes()
print(test.shyna_pun_joke())
```