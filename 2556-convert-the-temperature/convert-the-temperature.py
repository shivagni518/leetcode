class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        # return [celsius+273.15,celsius*1.80+32.00]  

        kel=celsius+273.15
        fah=celsius*1.80+32.00
        return [kel,fah]
