class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        flowers = sorted(
            list(zip(plantTime, growTime)),
            key=lambda x: x[1],
            reverse=True,
        )

        bloom_day = 0
        current_day = 0

        for plant_time, grow_time in flowers:
            current_day += plant_time
            bloom_day = max(current_day + grow_time, bloom_day)

        return bloom_day
