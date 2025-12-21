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