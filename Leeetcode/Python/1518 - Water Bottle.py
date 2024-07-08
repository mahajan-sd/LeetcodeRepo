class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        counter = numBottles
        eb = numBottles
        while eb >= numExchange:
            counter = counter + int(eb/numExchange)
            eb = int((eb / numExchange) + (eb % numExchange))
        return counter
