#include <iostream>
#include <vector>

void moveZeroes(std::vector<int>& nums) {
    int n = nums.size();
    int nonZeroIndex = 0;

    // Move all non-zero elements to the front of the vector
    for (int i = 0; i < n; i++) {
        if (nums[i] != 0) {
            nums[nonZeroIndex] = nums[i];
            nonZeroIndex++;
        }
    }

    // Fill the remaining positions with zeros in the last
    for (int i = nonZeroIndex; i < n; i++) {
        nums[i] = 0;
    }
}

int main() {
    std::vector<int> nums = {0, 1, 0, 3, 12};
    moveZeroes(nums);

    // Print the modified vector
    for (int num : nums) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
