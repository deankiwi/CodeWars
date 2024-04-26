#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
     void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
     {

          if (n == 0)
          {
               return;
          }

          int i = m - 1, j = n - 1, k = m + n - 1;
          // cout << "nums1: [";
          // for (int num : nums1)
          // {
          //      cout << num << ' ';
          // }
          // cout << "]\n";
          // cout << "nums2: [";
          // for (int num : nums2)
          // {
          //      cout << num << ' ';
          // }
          // cout << "]\n";

          while (i >= 0 && j >= 0)
          {
               if (nums1[i] >= nums2[j])
               {

                    nums1[k] = nums1[i];
                    --i;
               }
               else
               {
                    nums1[k] = nums2[j];
                    --j;
               }
               --k;
          }
          while (j >= 0)
          {
               nums1[k] = nums2[j];
               --j;
               --k;
          }
     }
};

void testVoid1();
void testVoid2();
void testVoid3();
void testVoid4();

int main()
{
     testVoid1();
     testVoid2();
     testVoid3();
     testVoid4();

     int x = 5;
     cout << x;
     cout << --x;
     cout << --x;
     cout << --x;
     cout << --x;
     cout << --x;

     return 0;
}

void testVoid1()
{
     Solution s;
     vector<int> nums1 = {1, 2, 3, 0, 0, 0};
     vector<int> nums2 = {2, 5, 6};
     s.merge(nums1, 3, nums2, 3);
     for (int i = 0; i < nums1.size(); i++)
     {
          cout << nums1[i] << " ";
     }
     cout << "\n = [1,2,2,3,5,6]";
     cout << "\n";
}
void testVoid2()
{
     Solution s;
     vector<int> nums1 = {1};
     vector<int> nums2 = {};
     s.merge(nums1, 1, nums2, 0);
     for (int i = 0; i < nums1.size(); i++)
     {
          cout << nums1[i] << " ";
     }
     cout << " = [1]";
     cout << "\n";
}

void testVoid3()
{
     Solution s;
     vector<int> nums1 = {0};
     vector<int> nums2 = {1};
     s.merge(nums1, 0, nums2, 1);
     for (int i = 0; i < nums1.size(); i++)
     {
          cout << nums1[i] << " ";
     }
     cout << " = [1]";
     cout << "\n";
}

void testVoid4()
{
     Solution s;
     vector<int> nums1 = {2, 0};
     vector<int> nums2 = {1};
     s.merge(nums1, 1, nums2, 1);
     for (int i = 0; i < nums1.size(); i++)
     {
          cout << nums1[i] << " ";
     }
     cout << " = [1,2]";
     cout << "\n";
}

/*
same time but cleaner solution


class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1;
        int j = n - 1;
        int k = m + n - 1;
        
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
    }
};
*/