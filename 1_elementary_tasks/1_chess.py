class Chess:

    def __init__(self, height, width):
        print(*self.chess(height, width), sep='\n')

    @staticmethod
    def chess(height, width):
        return [''.join([' ' if (i+j) % 2 else '*' for i in range(height)])
                for j in range(width)]


Chess(10, 5)
