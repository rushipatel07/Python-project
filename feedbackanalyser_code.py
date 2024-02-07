# data set:
# "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

dataa="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
class textana(object):
    #convert string into lower Task 1 complate.
    def __init__(self,text):
        newdataset=text.replace("."," ").replace(","," ").replace("?"," ").replace("!"," ")
        newdataset=newdataset.lower()
        self.dataset=newdataset
    # tast 2
    def freqword(self):
        listt=self.dataset.split()
        dict={}
        for i in listt:
            dict[i]=listt.count(i)
        return dict
    #task 3
    def specword(self,i):
        spefreqword=self.freqword()
        if i in spefreqword:
            return spefreqword[i]
        else:
            print("404 not found!!!")
            return 0
object=textana(dataa)
print(f"data set:-\n {object.dataset}")
dictnory=object.freqword()
print(f"frequency of word is:\n {dictnory}")
print("Enter word:")
word=str(input())
givenword=object.specword(word)
print(f"the count of {word} is {givenword}")