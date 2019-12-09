class Solution:
    def trap(self, height: List[int]) -> int:

        if len(height) <= 2:
            return 0

        water_content = 0
        start_point = 0
        end_point = len(height) - 1
        while start_point < end_point:
            if height[start_point] <= height[end_point]:
                current_height = height[start_point]
                while start_point < end_point and current_height >= height[start_point]:
                    water_content += current_height - height[start_point]
                    start_point += 1
            else:
                current_height = height[end_point]
                while start_point < end_point and current_height >= height[end_point]:
                    water_content += current_height - height[end_point]
                    end_point -= 1

            # print("start point is", start_point)
            # print("end point is", end_point)
        # sub_water_content = 0

        #         while end_point < len(height):
        #             if end_point == len(height) - 1:
        #                 break
        #             while end_point < len(height) - 1 and height[end_point + 1] <= height[end_point]:
        #                 end_point += 1
        #             # print(end_point)
        #             while end_point < len(height) - 1 and height[end_point + 1] >= height[end_point]:
        #                 end_point += 1
        #             # print(end_point)
        #             # pdb.
        #             sub_water_content_start = start_point + 1
        #             if height[start_point] >= height[end_point]:
        #                 while sub_water_content_start < end_point:
        #                     diff = height[end_point] - height[sub_water_content_start]
        #                     if diff > 0:
        #                         water_content += diff
        #                     sub_water_content_start += 1
        #             else:
        #                 while sub_water_content_start < end_point:
        #                     diff = height[start_point] - height[sub_water_content_start]
        #                     if diff > 0:
        #                         water_content += diff
        #                     sub_water_content_start += 1
        #             # print("start point is", start_point)
        #             # print("end point is", end_point)
        #             # print("water content is", water_content)

        #             start_point = end_point

        return water_content


