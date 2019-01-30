import unittest
from unittest.mock import mock_open
from unittest.mock import call

import chess
import envelope
import triangules
import parses
import num_to_str
import lucky_ticket
import seq
import fib_diapason


class ChessTest(unittest.TestCase):

    def test_chess(self):
        self.assertEqual(chess.Chess.chess(2, 2), ['* ', ' *'])


class EnvelopeTest(unittest.TestCase):

    def test_envelope(self):
        input = ['1', '2', '3', '4', 'no']
        output = []
        envelope.input = lambda _: input.pop(0)
        envelope.print = output.append
        envelope.f()
        self.assertEqual(output, [True])


class TrianglesTest(unittest.TestCase):

    def test_triangles(self):
        t1 = ['a', '1', '2', '3', 'y']
        t2 = ['b', '3', '4', '5', 'y']
        t3 = ['c', '1', '1', '1', 'n']

        input = t1 + t2 + t3
        triangules.input = lambda _: input.pop(0)

        output = []
        desired = [
            '[Triangle b]: 6.0 cm',
            '[Triangle c]: 0.4330127018922193 cm',
            '[Triangle a]: 0.0 cm'
        ]
        triangules.print = output.append

        triangules.f()

        self.assertEqual(desired, output)


class ParsesTest(unittest.TestCase):

    def test_parses_1(self):

        parses.argv = ['', 'file.txt', 'a']

        m = mock_open(read_data='a\nb\nc\na')  # only 3.7.1
        parses.open = m

        output = []
        desired = [2]
        parses.print = output.append

        parses.f()

        self.assertEqual(desired, output)

    def test_parses_2(self):

        parses.argv = ['', 'file.txt', 'a', 'z']

        m = mock_open(read_data='a\nb\nc\na')  # only 3.7.1
        parses.open = m

        call_list = list(map(call, ['z\n', 'b\n', 'c\n', 'z\n']))
        parses.f()

        handle = m()
        self.assertEqual(call_list, handle.write.call_args_list)


class NumToStrTest(unittest.TestCase):

    def test_num_to_str(self):
        self.assertEqual(num_to_str.NumToStr(211000).value, 'двести одиннадцать тысяч')


class LuckyTicketTest(unittest.TestCase):

    def test_ticket_simple(self):

        m = mock_open(read_data='Simple\n111222\n123321\n123222')
        lucky_ticket.open = m

        output = []
        desired = [2]
        lucky_ticket.print = output.append
        lucky_ticket.input = lambda _: 'file.txt'

        lucky_ticket.f()
        self.assertEqual(output, desired)

    def test_ticket_difficult(self):

        m = mock_open(read_data='Difficult\n132411\n123456\n111122')
        lucky_ticket.open = m

        output = []
        desired = [2]
        lucky_ticket.print = output.append
        lucky_ticket.input = lambda _: 'file.txt'

        lucky_ticket.f()
        self.assertEqual(output, desired)

    def test_ticket_mixed(self):

        m = mock_open(read_data='Mixed\n111111\n121212\n122122')
        lucky_ticket.open = m

        output = []
        desired = [2]
        lucky_ticket.print = output.append
        lucky_ticket.input = lambda _: 'file.txt'

        lucky_ticket.f()
        self.assertEqual(output, desired)


class SeqTest(unittest.TestCase):

    def test_seq(self):

        output = []
        desired = ['0, 1, 2, 3, 5, 7']
        seq.print = output.append

        seq.Main(100)
        self.assertEqual(output, desired)


class FibDiapasonTest(unittest.TestCase):

    def test_fibs(self):

        desired = [0, 1, 1, 2, 3, 5, 8]
        self.assertEqual(fib_diapason.Fibs(0, 10).value, desired)


if __name__ == '__main__':
    unittest.main()
