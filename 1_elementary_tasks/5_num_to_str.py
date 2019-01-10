class NumToStr:
    a = {
        10: 'десять',
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать'
    }

    b = {
        0: '',
        2: 'двадцать',
        3: 'тридцать',
        4: 'сорок',
        5: 'пятьдесят',
        6: 'шестьдесят',
        7: 'семьдесят',
        8: 'восемьдесят',
        9: 'девяносто'
    }

    c = {
        0: '',
        1: 'один',
        2: 'два',
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять'
    }

    d = {
        0: '',
        1: 'сто',
        2: 'двести',
        3: 'триста',
        4: 'четыреста',
        5: 'пятьсот',
        6: 'шестьсот',
        7: 'семьсот',
        8: 'восемьсот',
        9: 'девятьсот',
    }

    def parse_before_thsausand(self, num):
        before_thousand = num % 100
        if before_thousand in self.a:
            return self.a[before_thousand]
        elif before_thousand != 0:
            tens = before_thousand // 10
            rem = before_thousand % 10
            return f'{self.b[tens]} {self.c[rem]}'.lstrip()
        else:
            return ''

    def parse(self, num):
        hundreds = (num // 100) % 10
        thousands = num // 1000
        t1 = thousands // 100
        thousands = self.parse_before_thsausand(thousands)
        if thousands.endswith('один'):
            thousands = f"{thousands.replace('один', 'одна')} тысяча"
        elif thousands.endswith('два'):
            thousands = f"{thousands.replace('два', 'две')} тысячи"
        elif thousands:
            thousands += ' тысячи'
        return (f'{self.d[t1]} {thousands} {self.d[hundreds]} '
                f'{self.parse_before_thsausand(num)}'.lstrip())

    def __init__(self, num):
        self.num = num

    @property
    def value(self):
        return self.parse(self.num)


print(NumToStr(765291).value)
