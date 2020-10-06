class CombineArray:
    def __init__(self,l1,l2):
        self.ary1 = l1
        self.ary2 = l2

    # def combine(self):
    #     result = [] + self.ary1 + self.ary2
    #     result.sort() #O(nlogn)
    #     return result

    def combine(self):#O(n)
        result = []
        i,j = 0,0
        while(i < len(self.ary1) and j < len(self.ary2)):
            if(self.ary1[i] <= self.ary2[j]):
                result.append(self.ary1[i])
                i += 1
            else:
                result.append(self.ary2[j])
                j += 1
        while i < len(self.ary1):
            result.append(self.ary1[i])
            i += 1
        
        while j < len(self.ary2):
            result.append(self.ary2[j])
            j += 1
        #result += self.ary2[j:]

        return result



if __name__ == "__main__":
    Comb = CombineArray([1,2,4],[1,3,4])
    result = Comb.combine()
    print(result)
