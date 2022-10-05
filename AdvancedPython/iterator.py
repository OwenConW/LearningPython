import time 

class FiboIter():

    def __init__(self, num=None):
        self.max = num

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if not self.max or self.n1 + self.n2 <= self.max:
            if self.counter == 0:
                self.counter += 1
                return self.n1
            elif self.counter == 1:
                self.counter += 1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
        else:
            raise StopIteration


def fibo_recursion(num=40000, before=0, nextt=1):
    time.sleep(0.15)
    aux = before + nextt 
    if aux >= num:  
        return
    else:
        print(aux) 
        before, nextt = nextt, aux 
        fibo_recursion(num, before, nextt)


if __name__ == "__main__":
    fibonacci = FiboIter(4242)
    for num in fibonacci:
        print(num)
        time.sleep(0.15)
    fibo_recursion(4242)
