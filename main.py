from field_element import FieldElement

if __name__ == '__main__':
    a = FieldElement(1, 7)
    b = FieldElement(6, 7)
    print(a == b)
    print(a == a)
    print(a != a)
