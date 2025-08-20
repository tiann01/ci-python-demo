
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b


class StringProcessor:
    def reverse(self, s: str) -> str:
        return s[::-1]

    def is_palindrome(self, s: str) -> bool:
        s_clean = ''.join(filter(str.isalnum, s.lower()))
        return s_clean == s_clean[::-1]

    def count_vowels(self, s: str) -> int:
        return sum(1 for c in s.lower() if c in "aeiou")


def main():
    calc = Calculator()
    print("3 + 5 =", calc.add(3, 5))

    sp = StringProcessor()
    print("Reverse 'hello' =", sp.reverse("hello"))
    print("'racecar' is palindrome?", sp.is_palindrome("racecar"))


if __name__ == "__main__":
    main()
