class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hand_bill = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                hand_bill[5] += 1
            elif bill == 10:
                hand_bill[10] += 1

                if hand_bill[5] == 0:
                    return False
                else:
                    hand_bill[5] -= 1

            else:
                if hand_bill[10] > 0 and hand_bill[5] > 0:
                    hand_bill[10] -= 1
                    hand_bill[5] -= 1
                elif hand_bill[5] >= 3:
                    hand_bill[5] -= 3
                else:
                    return False


        return True