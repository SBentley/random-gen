from random import random

class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = [-1,0,1,2,3]
    # Probability of the occurence of random_nums
    _probabilities = [0.01,0.3,0.58,0.1,0.01]

    def next_num(self):
        ran = random()
        print(ran)
        lower = 0
        higher = 0
        for prob in self._probabilities:
            higher += prob
            print(f'{lower} - {higher}')
            if lower <= ran <= higher:
                print('hit')
                pass
            lower = higher
        pass

ran = RandomGen()
a = ran.next_num()
print(a)
