# 100 Days Of Code - Log

## Day 1: February 2, 2022

### Today's Progress:

Today, I am beginning the challenge. I'm starting off with a problem from codewars.com. The Kata for today is to remove the first and last character from a string.

### Thoughts:

Had some initial challenges with this one, I had the logic of the .slice() method backwards at first, but then ended up switching it around and got the answer!

```js
function removeChar(str) {
  return str.slice(1, -1);
}
```

### Link(s) to work:

[CodeWars](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/solutions/javascript)

## Day 2: February 3, 2022

### Today's Progress:

I started off the morning before class doing another CodeWars challenge. This one was to take an array and return the average sum, and return 0 if array is empty. This one didn't take too long.

### Thoughts:

Really just thought it out logically, then implemented it!

```js
function find_average(array) {
  if (array.length === 0) return 0;
  let sum = 0;
  array.forEach((num) => {
    sum += num;
  });
  return sum / array.length;
}
```

### Link(s) to work:

[CodeWars](https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/solutions/javascript)

## Day 3: February 4, 2022

### Today's Progress:

I started off the morning before class doing another CodeWars challenge. Since we just started learning Python YESTERDAY, I decided to challenge myself with a Python coding challenge. This one was to take a function that accepts a boolean, and return "Yes" if true, "No" if false.

### Thoughts:

I first started out with the long form (I will show below), but then thought, "There has to be a shorter way to do this..." so I researched the Python version of a ternary operator and implemented that!

First passing attempt:

```python
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    if boolean == False:
        return "No"
```

Using a ternary:

```python
def bool_to_word(boolean):
    return "Yes" if boolean else "No"
```

### Link(s) to work:

[CodeWars](https://www.codewars.com/kata/53369039d7ab3ac506000467/solutions/python)
