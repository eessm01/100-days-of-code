class Classy(object):
    def __init__(self):
        self.items = []
        
    def addItem(self, item):
        self.items.append(item)
        
    def getClassiness(self):
        points = {"tophat":2,"bowtie":4,"monocle":5}
        
        classiness = 0
        for item in self.items:
            for key, value in points.items():
                if key == item:
                    classiness += value
                    break
                
        return classiness


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(len(me.items))
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
# Should be 15
print(me.getClassiness())