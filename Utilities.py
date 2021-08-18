class Utilities:
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
        if "#" in right:
            xorResult = xorFirstResult
        else:
            for digit in range(len(left)):
                if xorFirstResult[digit] == right[digit]:
                    xorResult = xorResult + "0"
                else:
                    xorResult = xorResult + "1"
        return xorResult

    def andStr(self, left, right):
        andResult = ""
        for digit in range(len(left)):
            if left[digit] == "0" or right[digit] == "0":
                andResult = andResult + "0"
            if left[digit] == "1" and right[digit] == "1":
                andResult = andResult + "1"
        return andResult

    def notStr(self, operand):
        notResult = ""
        for digit in range(len(operand)):
            if operand[digit] == "0":
                notResult = notResult + "1"
            else:
                notResult = notResult + "0"
        return notResult
