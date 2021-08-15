class MessageSchedule:
    chunks = []
    schedules = []

    def __init__(self, chunks):
        self.chunks = chunks

    def to32BitWords(self):
        preschedules = []
        for full in range(len(self.chunks)):
            singlePreSchedule = []
            for in8 in range(0, len(self.chunks[full]), 4):
                word = ""
                for single4 in range(0, 4):
                    word = word + self.chunks[full][in8 + single4]
                singlePreSchedule.append(word)
            if (len(singlePreSchedule) < 64):
                initShedSize = len(singlePreSchedule)
                for in8 in range(initShedSize, 64):
                    word0 = ""
                    for only0 in range(32):
                        word0 = word0 + "0"
                    singlePreSchedule.append(word0)
            preschedules.append(singlePreSchedule)
        return preschedules

    def createMSchedules(self, preschedules):
        for full in range(len(preschedules)):
            singleSched = []
            for word in range(0, 15):
                singleWord = preschedules[full][word]
                singleSched.append(singleWord)

            for word in range(16, 64):
                word7Rot = self.rotateRight(7, preschedules[full][word - 15])
                word18Rot = self.rotateRight(18, preschedules[full][word - 15])
                word3Shift = self.shiftRight(3, preschedules[full][word - 15])
                s0 = self.xorStr(word7Rot, word18Rot, word3Shift)
                word17Rot = self.rotateRight(17, preschedules[full][word - 2])
                word19Rot = self.rotateRight(19, preschedules[full][word - 2])
                word10Shift = self.shiftRight(10, preschedules[full][word - 2])
                s1 = self.xorStr(word17Rot, word19Rot, word10Shift)
                minus16Word = preschedules[full][word - 16]
                minus7Word = preschedules[full][word - 7]

                sum1 = self.binarySum(minus16Word, s0)
                sum2 = self.binarySum(sum1, minus7Word)
                result = self.binarySum(sum2, s1)

                singleSched.append(result)
            self.schedules.append(singleSched)


    def binarySum(self, left, right):
        sum = ""
        carry = "0"
        newCarry = "0"
        result = ""
        for digit in reversed(range(len(left))):
            if left[digit] == right[digit]:
                result = "0"
                newCarry = "0"
                if left[digit] == "1":
                    newCarry = "1"
            else:
                result = "1"
                newCarry = "0"
            if result == "0" and carry == "0":
                sum = "0" + sum
            elif result == "1" and carry == "1":
                sum = "0" + sum
                newCarry = "1"
            elif result == "1" and carry == "0" or result == "0" and carry == "1":
                sum = "1" + sum
            carry = newCarry
        return sum

    def rotateRight(self, offset, word):
        rotated = ""
        middle = word[0:len(word) - offset]
        end = word[len(word) - offset:len(word)]
        rotated = end + middle
        return rotated

    def shiftRight(self, offset, word):
        shifted = ""
        add0 = ""
        for add in range(offset):
            add0 = add0 + "0"
        middle = word[0:len(word) - offset]
        shifted = add0 + middle
        return shifted

    def xorStr(self, left, middle, right):
        xorFirstResult = ""
        xorResult = ""
        for digit in range(len(left)):
            if left[digit] == middle[digit]:
                xorFirstResult = xorFirstResult + "0"
            else:
                xorFirstResult = xorFirstResult + "1"
        for digit in range(len(left)):
            if xorFirstResult[digit] == right[digit]:
                xorResult = xorResult + "0"
            else:
                xorResult = xorResult + "1"
        return xorResult


    def running(self):
        preschedules = self.to32BitWords()
        self.createMSchedules(preschedules)