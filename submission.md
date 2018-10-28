Step 1: Find all the different ways you could permute a hand of cards by grabbing a contiguous block of them and moving them somewhere else in the hand. I did this by a short Python function. For N = 6, there are 36 ways; for N = 13, there are 365.

Step 2: Figure out how to recognize an acceptable hand. I defined a hand's "fingerprint" as the order of runs of suits -- for example, a hand with spade, club, diamond, diamond, club, and heart in that order would have the fingerprint "scdch". With a little thought, I figured out an acceptable hand would have one of these 32 fingerprints: s h d c sh sd sc hs hd hc ds dh dc cs ch cd shc sdc hsd hcd dsh dch chs cds shcd sdch hsdc hcds dshc dchs chsd cdsh. (It's neat how the initial letter of the suits of red cards have ascenders and the ones for black cards don't.)

Step 3: See if some arrangement of suits in a hand had a good fingerprint. For the hand above, "scddch", taking the 3rd through 5th cards and moving them after the 1st card gives one of the good fingerprints:
Cards: sc <ddc> h
    sch <ddc>
    s <ddc> ch
Fingerprint: sdch
This step is just looking at each possible arrangement and seeing if it's in the list of good fingerprints.

Step 4: Figure out how likely it is for a specific arrangement of cards to appear in a real deck. I did step 3 with the 4^6=4096 (not quite; see below) possible arrangements of suits in a 6-card hand. However, not all of those will happen equally often. Without loss of generality (and with a large time savings), I assumed the first card of each hand would be a spade. Therefore, for the "scddch" arrangement, there are 13 * 13 * 13 * 12 * 12 * 13 = 4112784 different hands that can have that arrangement out of  13 * 51 * 50 * 49 * 48 * 47 = 3664533600 possible hands. Repeat this with all 4096 possible suit patterns, add up the hands, and divide by 3.7 billion or so. The answer you get is 2231305440/3664533600. That simplifies to 51083/83895 and divides out to 60.889%.

For N = 1 or 2, p = 1 trivially and without movement of cards.
For N = 3, if your initial hand is bad: If you have two cards of the same suit, move the other card to one end. If all your cards have different suits, put the card with a unique color in the middle. p = 1.

For N = 4 to 13, I used Python. The code is here:
https://github.com/plus1615/riddler-20181026

The answers are:
```
N = 4, p = 1624350/1624350 = 
   1.0
N = 5, p = 66461928/77968800 = 
   0.8524169667867146
N = 6, p = 2231305440/3664533600 = 
   0.608892067465284
N = 7, p = 62911927728/168568545600 = 
   0.37321273375215025
N = 8, p = 1531119110976/7585584552000 = 
   0.20184589605191444
N = 9, p = 32912903365056/333765720288000 = 
   0.09861079602979027
N = 10, p = 636116547882816/14351925972384000 = 
   0.044322730559426836
N = 11, p = 11205400474958976/602780890840128000 = 
   0.01858950846856046
N = 12, p = 181794231835856640/24714016524445248000 = 
   0.007355916091422835
N = 13, p = 2738618232266442240/988560660977809920000 = 
   0.00277030873306005
```
