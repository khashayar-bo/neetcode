class Solution:
    def calculate_area(self, heights, left_index, right_index):
        height = min(heights[left_index], heights[right_index])
        width  = right_index - left_index

        return height * width

    def maxArea(self, heights: List[int]) -> int:
        left_index = 0
        right_index = 1
        max_area  = 0

        while right_index < len(heights):
            if right_index == len(heights) - 1 or heights[right_index + 1] < heights[right_index]:
                max_area = max(max_area, self.calculate_area(heights, left_index, right_index))

                pointer = left_index

                while pointer < right_index:
                    pointer_area = self.calculate_area(heights, pointer, right_index)
                    if  pointer_area > max_area:
                        max_area = pointer_area
                        left_index = pointer
                    pointer += 1

            right_index += 1

        return max_area

                

        
        