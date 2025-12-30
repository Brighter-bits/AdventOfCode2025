Yet another year has gone by, it is time to save Christmas.

# Day 1

Quite simple today, it reminds me slightly of one of this year's EverybodyCodes quests, I'm not too happy with my solution overall as I just brute forced the second part instead of using mods to do the puzzle
properly. However, I kept being an idiot while trying to use the mods so I changed my solution to a simple brute forcer.

# Day 2

I got slightly delayed, but today wasn't too bad (though I feel like my solution is quite slow... again)

Placement: 23818

# Day 3

I feel like my solution is once again quite bad. For the first part, I used regex (because I realised I was supposed to use it yesterday); for the second part I went for a more greedy algorithm.

However, a fun off by one error messed me up badly for part 2, so I guess it's karma.


Placement: 22113

# Day 4

I was distracted by some practice I was doing so I completely forgot about todays advent. Quite easy surprisingly, though I feel like my solution is slightly inefficient... again. However, the input is small
enough that it runs quite quickly.

I did unfortunately have a slight problem where I got my xs and yx mixed round, as well as the problem that negative indexes wrap around to the back of the list. But otherwise, there weren't too many errors.

Placement: 21843

# Day 5

The practice yesterday did not pay off... Todays was quite easy and I got the general idea quite quickly. Though bounds are a theme so far this year (maybe that's the project management stuff?)

I actually managed to predict that I would need a plus one luckily, however I quickly realised that my elifs only work if the bounds are ordered from the first element smallest to largest, which was my only
error today.

One thing I don't like is my wall of elifs, but I think it's fine overall, and hardly as bad as the one I did for the fishbones in EC.

Placement: 14447

# Day 6

Oops, I completely forgot that AOC ran over the weekend. This was a relatively simple puzzle that reminded me that I need to eventually learn how to use numpy properly.

I only had one error, where during the while loop in part two, it wouldn't add the final calculation, but that was quickly fixed.

Placement: 54048

# Day 7

My eternal enemy: Reading the question; has once again attacked me. I calculated how many of the bottom parts get hit by the laser... turns out I wanted how many times it split.

Placement: 44372

# Day 8

This looks really complicated, however, it shouldn't be too bad if I start working on it.

I kept thinking about how to find the distance between the two points, trying to do sqrt(sqrt(x^2 + y^2)^2 + z^2). However, the square root and index cancel out to make sqrt(x^2 + y^2 + z^2).

Other than that, I mostly had small errors like using the wrong variables and running the code twice without changing anything.
I still feel that the code could run faster by eliminating redundant connections, but the code works in its current state, and so I'll live with it.

I should probably get better at naming my variables.

Placement: 37238

# Day 9:

This feels deceptively easy, and incredibly similar to the previous day (which I am still catching up from)

Ahhh, this part 2 is a worse problem. It seems similar to the Everybody Codes whistling maze. However, the old code from that doesn't seem to work with this after some poking about.

I have however, had a brilliant idea. We take the x coordinate, and check how many walls are to the left of it, if it's even, then we've gone into a wall, then left it.
Meanwhile if it is odd, then we are inside. So we just check all four corners to see if they are all inside.

Slight amendment to that, if the walls look liked this:

```
#### #####
#  # #   #
#  ###   #
#        #
##########
```

Then going from one corner to the other would be allowed, when it shouldn't be. What I actually need is to check they both have the same number of wall crosses and that they are odd.
A second change, if two points share a horizontal coordinate, you don't need to check the vertical ray.

I give up with all the fancy maths, I'm going to brute force this as it's already the 12th and I'm still stuck on this day.
Nevermind, I can't even make a grid.

I finally have some free time over the weekend, so I've now managed to learn coordinate compression, which is actually really cool. It even allows me to properly visualise large graphs in the terminal!

This took way too long, and I don't want to do day 10 tonight.

Placement: 28287 (though this is days afterwards...)

# Day 10

Okay, I have no idea how to tackle this, and the fact that Joltage is unecessary makes me very afraid.

Although, it seems that pressing a single button twice is basically useless, meaning it's closer to those games where you have to flip switches to turn lights on and off. So in reality, the number of
possibilities is 2^{num buttons} which isn't that bad.

Actually, yes I'm going to brute force it and see what happens.

The only problem is that I will need to XOR the buttons, which is a problem when using lists. This may be a bad idea, but I'm going to try and use binary.

That actually worked really well. New problem, Joltage. It seems to be another simultaneous equation problem, which means I may have to break out numpy.


It's a couple (10 days) days later and I've come back to this. And oh, it's so much worse than I expected. Looking at the reddit, I've found a couple of solutions that I might combine.

These are [a numpy solution](https://www.reddit.com/r/adventofcode/comments/1plzhps/2025_day_10_part_2_pivot_your_way_to_victory/) and [an interesting recursive solution](https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/)

Actually, after rereading the interesting recursive solution, I've found it's way easier than I realised, so I'm going to once again put off learning numpy properly (and learning gaussian elimination which I think I understand but probably don't).

The recursive solution has definitely heavily decreased the time it takes to run the program. But my computer is still spending an incredibly long time on only the third line of my input.

Okay, so my problem was that I wasn't including other possibilities into my solution. Meaning that, if you break the solution down into two parts: The recursive, and the extra bit. Just because you have the smallest extra bit, does not mean you will get a tractable recursive.

I have really poorly explained that, but I'm behind so...

I have suddenly realised why the algorithm is recursive. This is a mess, so I'm going to leave it overnight and just hope for the best.

Leaving it overnight did not help. My current problem is that if I have something like {4, 4, 4} this gets halved to {2, 2, 2} which is all even. I feel like I'm just being an idiot, but I can't figure out what to do from here.

It turns out, I have to allow just pressing 0 buttons? And I kept adding on old bits of code which no longer worked which I just assumed would work perfectly for some reason.

Again, I'm very unhappy with my relatively slow, unreadable, spaghetti solution.

But it's over.

Placement (does this even matter anymore??): 22234

# Day 11

Part 1 seems to just be a graph + some recursion.

Part 2 aswell?

Oh my god, that was so easy!

Placement: 27968 # I guess that's why more people have completed it.

# Day 12

I hate shapes. So much.

Okay, I'm fairly sure this isn't possible because I'm pretty sure all packing problems are supposed to basically be impossible to solve programatically in a reasonable time.

Just searched it up, I'm pretty sure most of them are...

I tried 0, it did not work. I'm going to make a rough guess on how much space each block paired up would take then just start making some stupid assumptions. There are only 101 possibilities and I've already tried one. Nevermind, I miscounted there are 1000.

Well, it's also not 100 nor 1000 I guess.

I got the right answer on my first attempt at solving the puzzle with my terrible numbers. My only problem was initialising ```total = 1```. Which was, to put it simply, very stupid of me.

I might go do another year now, or just relax and get on with other work. But, more importantly;

Christmas is saved! And it's definitely not nearly New Year's.

Placement: 18110