class Compression:
    messageSched = []
    hashValues = []
    roundConst = []

    util = ()

    def __init__(self, hashValues, roundConst, util):
        self.hashValues.clear()
        self.roundConst.clear()
        self.hashValues.append("{0:032b}".format(int(hashValues[0], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[1], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[2], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[3], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[4], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[5], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[6], 16)))
        self.hashValues.append("{0:032b}".format(int(hashValues[7], 16)))
        self.roundConst = roundConst
        self.util = util


    def compressionLoop(self):
        for full in range(len(self.messageSched)):
            a = self.hashValues[0]
            b = self.hashValues[1]
            c = self.hashValues[2]
            d = self.hashValues[3]
            e = self.hashValues[4]
            f = self.hashValues[5]
            g = self.hashValues[6]
            h = self.hashValues[7]
            for mutate in range(0, 64):
                S1 = self.util.xorStr(self.util.rotateRight(6, e), self.util.rotateRight(11, e), self.util.rotateRight(25, e))
                ch = self.util.xorStr(self.util.andStr(e, f), self.util.andStr(self.util.notStr(e), g), "#")
                temp1a = self.util.binarySum(h, S1)
                temp1b = self.util.binarySum(temp1a, ch)
                temp1c = self.util.binarySum(temp1b, "{0:032b}".format(int(self.roundConst[mutate], 16)))
                temp1 = self.util.binarySum(temp1c, self.messageSched[full][mutate])
                S0 = self.util.xorStr(self.util.rotateRight(2, a), self.util.rotateRight(13, a), self.util.rotateRight(22, a))
                maj = self.util.xorStr(self.util.andStr(a, b), self.util.andStr(a, c), self.util.andStr(b, c))
                temp2 = self.util.binarySum(S0, maj)
                h = g
                g = f
                f = e
                e = self.util.binarySum(d, temp1)
                d = c
                c = b
                b = a
                a = self.util.binarySum(temp1, temp2)
            h0 = self.util.binarySum(self.hashValues[0], a)
            h1 = self.util.binarySum(self.hashValues[1], b)
            h2 = self.util.binarySum(self.hashValues[2], c)
            h3 = self.util.binarySum(self.hashValues[3], d)
            h4 = self.util.binarySum(self.hashValues[4], e)
            h5 = self.util.binarySum(self.hashValues[5], f)
            h6 = self.util.binarySum(self.hashValues[6], g)
            h7 = self.util.binarySum(self.hashValues[7], h)

            self.hashValues[0] = h0
            self.hashValues[1] = h1
            self.hashValues[2] = h2
            self.hashValues[3] = h3
            self.hashValues[4] = h4
            self.hashValues[5] = h5
            self.hashValues[6] = h6
            self.hashValues[7] = h7


    def running(self, messageSched):
        self.messageSched.clear()
        self.messageSched = messageSched
        self.compressionLoop()
        finalHash = ""
        for hash in range(0, len(self.hashValues)):
            inHex = hex(int(self.hashValues[hash], 2))
            finalHash = finalHash + inHex[2:10]

        return finalHash