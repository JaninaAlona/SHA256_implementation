import sys

class Preprocessor:
    chunks = []
    dataSize = 0


    def convertPwToBin(self, input):
        convertedList = []
        self.dataSize = len(input)
        for c in input:
            binStr = format(ord(c), 'b')
            filledStr = self.fillUp(binStr)
            convertedList.append(filledStr)
        return convertedList


    def convertFileToBin(self, input):
        convertedList = []
        self.dataSize = len(input)
        for byte in input:
            binStr = bin(int.from_bytes(byte, byteorder=sys.byteorder))[2:]
            filledStr = self.fillUp(binStr)
            convertedList.append(filledStr)

        return convertedList

    def fillUp(self, characts):
        if len(characts) <= 8:
            more0 = 8 - len(characts) 
            for i in range(0, more0):
                characts = "0" + characts
        return characts


    def toChunksForwards(self, rawData, offset):
        div = int(len(rawData) / offset) + 1
        slices = []
        start = 0
        if len(rawData) <= offset:
            end = len(rawData)          
        else:
            end = offset
        
        divCounter = 1
        while divCounter <= div:
            unit = []
            for i in range(start, end):
                unit.append(rawData[i])
            if divCounter == div - 1:
                start += offset
                end = len(rawData)
            elif divCounter < div - 1:
                start += offset
                end += offset
            slices.append(unit)
            divCounter += 1
        return slices


    def toChunksBackwards(self, rawStr, offset):
        div = int(len(rawStr) / offset) + 1
        slices = []
        end = len(rawStr) - 1
        if len(rawStr) >= offset:
            start = end - offset
        else:
            start = -1
        
        divCounter = div
        while divCounter >= 1:
            tempStr = ""
            for i in range(end, start, -1):
                tempStr = rawStr[i] + tempStr
            if divCounter == 1:
                tempStr = self.fillUp(tempStr)
            elif divCounter == 2:
                start = -1
                end -= offset
            else:
                start -= offset
                end -= offset
            slices.append(tempStr)
            divCounter -= 1
        return slices


    def addSizeInfo(self):
        dataSize = "{0:b}".format(self.dataSize * 8)
        addSizeData = self.toChunksBackwards(dataSize, 8)

        missingPad = 8 - len(addSizeData)
        for i in range(missingPad):
            addSizeData.append("00000000")
        addSizeData.reverse()

        lastChunk = self.chunks[len(self.chunks) - 1]
        for i in addSizeData:
            lastChunk.append(i)
        self.chunks[len(self.chunks) - 1] = lastChunk


    def addPadding(self):
        lastChunk = self.chunks[len(self.chunks) - 1]
        if len(lastChunk) <= 55:
            missingPad = 55 - len(lastChunk)
            lastChunk.append("10000000")
            for i in range(missingPad):
                lastChunk.append("00000000")
            self.chunks[len(self.chunks) - 1] = lastChunk
        else:
            if len(lastChunk) <= 63:
                lastChunk.append("10000000")
                missingPadLastChunk = 64 - len(lastChunk)
                for i in range(missingPadLastChunk):
                    lastChunk.append("00000000")
                self.chunks[len(self.chunks) - 1] = lastChunk
                newChunk = []
                for new in range(56):
                    newChunk.append("00000000")
                self.chunks.append(newChunk)
            else:
                newChunk = []
                newChunk.append("10000000")
                for i in range(1, 56):
                    newChunk.append("00000000")
                self.chunks.append(newChunk)


    def running(self, data, isFile):
        self.chunks.clear()

        if isFile == True:
            rawData = self.convertFileToBin(data)
        else:
            rawData = self.convertPwToBin(data)

        self.chunks = self.toChunksForwards(rawData, 64)
        self.addPadding()
        self.addSizeInfo()