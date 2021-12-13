class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    # practice 1.1
    def __ne__(self, other):
        if other is None:
            return False
        return self.num != other.num and self.prime != other.prime

    def __add__(self, other):
        # 위수가 같지 않다면 계산은 무의미하다
        if self.prime != other.prime:
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime
        # self.__class__ 대신 FieldElement 사용 가능하나 상속 시 하위 클래스에서 __add__ 가 실행될 때
        # 해당 하위 클래스가 아닌 FieldElement 인스턴스를 반환하게 됨. 상속문에 대비하여 이렇게 코딩함.
        return self.__class__(num, self.prime)

    # practice 1.3
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    # practice 1.6
    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, power, modulo=None):
        n = power % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)

    # practice 1.9
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in different Fields')
        num = (self.num * pow(other.num, self.prime - 2)) % self.prime
        return self.__class__(num, self.prime)
