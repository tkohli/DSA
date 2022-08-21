class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        """
        Mistake done in contest 
        Not Clear implementation plus started bas then gave up was close :')
        """
        energyNeeded = sum(energy) - initialEnergy + 1
        experienceNeeded = 0
        total = initialExperience

        for exp in experience:
            if total > exp:  # add experience to total if required experience < total experience
                total += exp
            else:  # get the experience needed then add it to the total experience
                experienceNeeded += exp - total + 1
                total += exp + experienceNeeded
        # uses max to prevent negative case when initial > needed
        return max(0, energyNeeded) + max(0, experienceNeeded)
