import random

# Solution
def say_hi_to(first:str, last:str="", do_print:bool=False)->str:
    text = "Hi" + " " + first + " " + last + "!"
    if do_print:
        print(text)
    else:
        return text
    

# Solution
def shuffle_trials(trials:list, max_iter:int=1000) -> list:
    ok = False
    count = 0
    while not ok:
        count+=1
        if count > max_iter:
            raise StopIteration
        found_duplicate = False
        for i in range(1, len(trials)):
            if trials[i] == trials[i-1]:
                found_duplicate = True
        if not found_duplicate:
            ok = True
        else:
            random.shuffle(trials)
    return trials

# Solution
def find_primes(start:int, stop:int) -> list:
    primes=[]
    for i in range(start, stop):
        is_prime = True
        for j in range(2,int(i/2)):
            if i%j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes