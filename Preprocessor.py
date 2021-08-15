class Preprocessor:
    chunks = []
    
    def __init__(self, password):
        self.password = password
        self.pwSize = len(self.password)
        

    def convertPwToBin(self, input):
        convertedList = []
        for c in input:
            binStr = format(ord(c), 'b')
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
        dataSize = "{0:b}".format(self.pwSize * 8)
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
            start = 0
            if len(lastChunk) <= 63:
                lastChunk.append("10000000")
                missingPad = 64 - (len(lastChunk) + 1)
                for i in range(missingPad):
                    lastChunk.append("00000000")
                self.chunks[len(self.chunks) - 1] = lastChunk
            else:
                start = 1
                newChunk = []
                newChunk.append("10000000")
                for i in range(start, 56):
                    newChunk.append("00000000")
                self.chunks.append(newChunk)


    def running(self):
        rawData = self.convertPwToBin(self.password)
        self.chunks = self.toChunksForwards(rawData, 64)
        self.addPadding()
        self.addSizeInfo()