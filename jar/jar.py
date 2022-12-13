class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        self.size += int(n)


    def withdraw(self, n):
        self.size -= int(n)

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity or size < 0:
            raise ValueError
        self._size = size


#check50 cs50/problems/2022/python/jar
def main():
    jar = Jar()
    print(jar.capacity)
    print(jar.deposit(2))
    #print(jar.__str__())
    print(jar.size)



if __name__ == '__main__':
    main()