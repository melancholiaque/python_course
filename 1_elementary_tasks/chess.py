class Chess:

    @staticmethod
    def chess(height, width):
        return [''.join([' ' if (i+j) % 2 else '*' for i in range(height)])
                for j in range(width)]
