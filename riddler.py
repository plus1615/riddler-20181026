import collections # Counter
import itertools # product, groupby

def make_orders(size):
    """Returns a list of tuples of arrangements after one grab/replace."""
    
    c = collections.Counter()
    for start in range(0,size):
        for end in range(start+1, size+1):
            for insert in range(size - end + start + 1):
                a = list(range(size))
                snip = a[start:end]
                leftover = a[0:start] + a[end:size]
                final = leftover[0:insert] + snip + leftover[insert:size]
                c[tuple(final)] += 1
    return sorted(c.keys())

# The fingerprint of a hand is the ordering of clumps of suits.

def good_fingerprints():
    """Returns a set of tuples of acceptable hand fingerprints."""

    # There are 32 good fingerprints:
    # * 4 are single-suited
    # * 12 are double-suited
    # * 8 are triple-suited
    # * 8 are four-suited
    # Note the red suit letters have ascenders and the black ones don't.
    fingerstr = ('s h d c ' + 'sh sd sc hs hd hc ds dh dc cs ch cd ' +
        'shc sdc hsd hcd dsh dch chs cds ' +
        'shcd sdch hsdc hcds dshc dchs chsd cdsh')
    fingerprints = set()
    for f in fingerstr.split():
        fingerprints.add(tuple(f))
    return fingerprints

def get_print(hand):
    """Returns the fingerprint of a hand as a tuple of characters."""
    return tuple(c for c, _ in itertools.groupby(hand))

def arrange_hand(hand, arrangement, size=None):
    """Returns the hand resorted."""

    if size == None: size = len(hand)
    new_hand = []
    for i in arrangement:
        new_hand.append(hand[i])
    return new_hand

def three_groups_one_suit(hand):
    c = collections.Counter(get_print(hand))
    return c.most_common(1)[0][1] >= 3

def possibilities(hand):
    c = collections.Counter(hand)
    ways = 1
    for keyval in c.most_common():
        for n in range(13, 0, -1)[0:keyval[1]]: # 13 to 1
            ways *= n
    return ways

def possible_hands(size):
    prod = 1
    for i in range(52, 39, -1)[0:size]:
        prod *= i
    return prod // 4 # dividing by 4 since the 1st card is a spade

def exhaust(size=6):
    total_ways = 0
    orders = make_orders(size)
    good_prints = good_fingerprints()
    for hand in itertools.product('sdhc', repeat=size-1):
        hand = ('s',) + hand # assuming spades are first WOLOG
        # minor optimization
        if three_groups_one_suit(hand): continue
        for o in orders:
            new_hand = arrange_hand(hand, o, size)
            new_print= get_print(new_hand)
            if new_print in good_prints:
                total_ways += possibilities(hand)
                break
    print('N = ', size, ', p = ', sep='', end='')
    print(total_ways, "/", possible_hands(size), ' = ', sep='')
    print('  ', total_ways / possible_hands(size))

for s in range(4, 14):
    exhaust(s)
