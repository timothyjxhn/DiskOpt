from algorithm import DiskParameter

class SCANAlgorithm:
    def __init__(self):
        self.dp = DiskParameter.DiskParameter("diskq1")
        self.generateAnalysis()

    def printSequence(self, name, location):
        prev = self.dp.getCurrent()
        total = 0
        working1 = ""
        working2 = ""
        for i in location:
            curr = i
            total += abs(prev-curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev-curr)) + "+"
            prev = i

        working1 = working1[0:-1]
        working2 = working2[0:-1]
        order = str(self.dp.getCurrent())+", "+str(location)[1:-1]
        print(name+"\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")


# SCAN function
    def arrangeSCAN(self, curr, seq, prev, maxcyn):

        temp = seq[:]
        SCAN = []
        n = len(temp)

        def left(): # move disk head Right
            for i in reversed(temp):
                if curr > i >= 0: # find values smaller than current and equal to or bigger than smallest cylinder
                    SCAN.append(i) # if found, append to created empty list

        def right(): # move disk head Left
            for i in temp:
                if curr < i < maxcyn: # find values bigger than current and smaller than maximum cylinder
                    SCAN.append(i) # if found, append to created empty list

        diff = curr - prev # check if its going left or right
        if diff > 0:
            if maxcyn != 0 and maxcyn > temp[n - 1]:
                temp.append(maxcyn - 1) # append max cylinder number to list
                temp.sort()
                right()
                left()

        else:
            temp.append(0) # append minimum cylinder number to list
            temp.sort()
            left()
            right()

        return SCAN

    def generateSCAN(self):
        seq = self.dp.getSequence() # get values from data
        curr = self.dp.getCurrent()
        prev = self.dp.getPrevious()
        maxcyn = self.dp.getCylinders()
        self.printSequence("SCAN ", self.arrangeSCAN(curr, seq, prev, maxcyn)) # Print sequence for SCAN algorithm

    def generateAnalysis(self):
        self.generateSCAN()
