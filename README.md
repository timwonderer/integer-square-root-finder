# Integer Square Root Finder

_Because `math.sqrt()` felt too easy._

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

This isn’t just a square root finder.  
It’s a **thought experiment**:
- How do you find the **integer square root** of a number **efficiently**?  
- How do you **narrow the search space** without eating up memory or time?

Instead of **brute force**, this project uses **binary search**, **digit-based narrowing**, and a sprinkle of **math curiosity**.

---

## 🚀 Features

| Feature                          | How It Works                                                   |
|----------------------------------|----------------------------------------------------------------|
| 🔍 **Ending Digit Check**       | Filters out numbers that can't possibly have integer roots     |
| 🧲 **Digit-Based Range Estimate** | Narrows search based on number of digits (cuts the haystack)  |
| ⚙️ **Binary Search**              | Efficiently zeroes in on possible square roots                 |
| 💪 **Linear Search Finish**       | Final pass checks the last few candidates                      |

> **Efficiency** here isn’t about shortcuts—it’s about **knowing where not to look**.

---

## 💡 Example Output

```bash
Enter a number: 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127560071009217256545885393053328527589376

Integer square root: 1809251394333065553493296640760748560207343510400633813116524750123642650624
```

Even for **massive numbers**, this finder doesn’t break a sweat.

---

### 🛠️ How to Run

```bash
python integer_square_root_finder.py
```

Enter any positive integer—big or small.

---

## 🧰 Behind the Code

This project started with a **simple prime checker**—I needed a way to quickly determine if a number had an **integer square root**.  
But I noticed something odd:  
The **square root check** was the **slowest part** of the whole program. Sometimes it **crashed my machine**.

I could’ve used **`math.sqrt()`** like a sane person, but instead, I started asking:

- **Why is this so slow?**  
- **How could I find square roots faster?**

---

### The Brute Force Phase

At first, I did what anyone might do:  
**Square every number** from 3 up to half of the input.  
If one matched, I had my square root.  
If none did, I knew there wasn’t one.

But here’s the problem:  
Imagine finding the square root of **2⁵⁰⁰**.

That’s a **151-digit number**.  
And squaring every number up to half of it?  
You’re squaring **another 151-digit number**—**every time**.

Not practical. Not efficient.

---

### The “There Has to Be a Pattern” Phase

I started **looking for patterns**:

- **What do the ending digits** of perfect squares look like?  
- **Could I use that to filter out candidates?**

I discovered:

- Numbers ending in **2, 3, 7, or 8** can **never be perfect squares**.

This simple **ending digit check** let me **eliminate 40%** of numbers **immediately**.  
No need to square anything.

---

### The Digit Counting Epiphany

But I didn’t stop there. I noticed something else:

> **The number of digits in a square root is roughly half the number of digits in the original number.**

This became my **guiding hypothesis**:

- If the number has **y** digits, the square root probably has about **y/2** digits.
- That meant I could **narrow the search range** significantly—by looking at the **powers of 10** around that digit length.

It sounds simple, but it cut the search space **from trillions of numbers to just a few dozen**.

---

### The Binary Search Finale

Once I had the range, I applied **binary search** to **pin down the exact window** where the square root might be.

And when the range got **small enough** (within 10 numbers),  
I switched to **linear search** to finish.

For something as massive as **2⁵⁰⁰**, I could find the integer square root in **a few microseconds**—and my machine didn’t melt.

---

This wasn’t about **reinventing the wheel**.  
It was about **understanding the wheel better**.

If you’re the kind of person who enjoys **breaking problems apart** just to see what makes them tick—you’re in good company.

---

> **Disclaimer:**  
> This project is for **learning and exploration**.  
> It’s not a drop-in replacement for `math.isqrt()`—but it’ll show you **how things work** behind the scenes.

---

## License

MIT License – because **sharing the weird stuff we build** makes it better.

