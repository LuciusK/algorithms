"""
（一）允许借空瓶：
能借到空瓶我们可以尽可能做到物尽其用
每换一次需要a个空瓶，而换来的酒喝完后又有b个空瓶，实际每次兑换空瓶减少(a-b)个
于是n个空瓶总共可兑换：n/(a-b) 次（式中除法为整数除法，商为兑换次数，余数则是最后剩余的空瓶数）
由于每次兑换可得到b瓶啤酒，于是共可兑换n/(a-b)*b瓶啤酒
一共能喝到的啤酒数当然也就为(n + n/(a-b)*b)瓶了
（二）不允许借空瓶
如果没人愿意借给你空瓶，此时只能“自力更生”了
若n小于a，很明显一次也兑换不了，一共能喝的也就是买的那n瓶啤酒
若n不小于a，一旦剩余空瓶数小于a，则兑换结束
为方便计算，预留a个空瓶，先兑换其余(n-a)个空瓶，于是可从预留的a个空瓶里去“借”，喝完再“归还”
根据“允许借空瓶”情况公式，(n-a)个空瓶总共可兑换：(n-a)/(a-b) 次（同上，式中除法表示整数除法）
由于预留的a个空瓶最后还可再进行一次兑换，故总兑换总次数为：(n-a)/(a-b)+1，化简后为(n-b)/(a-b) 次
最后预留的a个空瓶换的b瓶啤酒喝完后还会得到b个空瓶，故最后剩余的空瓶数为上式余数加b
由于每次兑换可得到b瓶啤酒，于是共可兑换(n-b)/(a-b)*b瓶啤酒
一共能喝到的啤酒数当然也就为(n + (n-b)/(a-b)*b)瓶了
为将以上公式通用化，当n小于b时，b取值同n
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1)//(numExchange - 1)

    def numWaterBottles1(numBottles: int, numExchange: int) -> int:
        cnt = numBottles

        while numBottles // numExchange:
            divisor = numBottles // numExchange
            remainder = numBottles % numExchange
            cnt += divisor
            numBottles = divisor + remainder

        return cnt