class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max=0
        for i in range(len(sentences)):
            count=1
            for j in range(len(sentences[i])):
                if sentences[i][j]==" ":
                    count+=1
            if count > max:
                max=count
        return max            




        