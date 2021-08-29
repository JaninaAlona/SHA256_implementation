class MessageSchedule:
    chunks = []
    schedules = []

    util = ()

    def __init__(self, util):
        self.util = util

    def to32BitWords(self):
        preschedules = []
        for full in range(len(self.chunks)):
            singlePreSchedule = []
            for in8 in range(0, len(self.chunks[full]), 4):
                word = ""
                for single4 in range(0, 4):
                    word = word + self.chunks[full][in8 + single4]
                singlePreSchedule.append(word)
            preschedules.append(singlePreSchedule)
        return preschedules

    def createMSchedules(self, preschedules):
        for full in range(len(preschedules)):
            singleSched = []
            for word in range(0, 16):
                singleWord = preschedules[full][word]
                singleSched.append(singleWord)

            for word in range(0, 48):
                word7Rot = self.util.rotateRight(7, singleSched[len(singleSched) - 15])
                word18Rot = self.util.rotateRight(18, singleSched[len(singleSched) - 15])
                word3Shift = self.util.shiftRight(3, singleSched[len(singleSched) - 15])
                s0 = self.util.xorStr(word7Rot, word18Rot, word3Shift)
                word17Rot = self.util.rotateRight(17, singleSched[len(singleSched) - 2])
                word19Rot = self.util.rotateRight(19, singleSched[len(singleSched) - 2])
                word10Shift = self.util.shiftRight(10, singleSched[len(singleSched) - 2])
                s1 = self.util.xorStr(word17Rot, word19Rot, word10Shift)
                minus16Word = singleSched[len(singleSched) - 16]
                minus7Word = singleSched[len(singleSched) - 7]

                sum1 = self.util.binarySum(minus16Word, s0)
                sum2 = self.util.binarySum(sum1, minus7Word)
                result = self.util.binarySum(sum2, s1)

                singleSched.append(result)
            self.schedules.append(singleSched)


    def running(self, chunks):
        self.chunks.clear()
        self.schedules.clear()
        self.chunks = chunks
        preschedules = self.to32BitWords()
        self.createMSchedules(preschedules)