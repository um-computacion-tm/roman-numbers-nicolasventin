import unittest

def roman_to_decimal(roman):
     total = 0
     for letter in roman:
        if letter == 'I':
            total += 1
        elif letter == 'V':
            if total > 0:
                total = -1
            total += 5
        elif letter == 'X':
            if total > 0:
                total = -1
            total += 10
     return total


class TestRomanToDecimal(unittest.TestCase):
    def test_1 (self):
        resultado = roman_to_decimal ("I")
        self.assertEqual(resultado,1)
    
    def test_x(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado,10)


if __name__ == '__main__':
    unittest.main()