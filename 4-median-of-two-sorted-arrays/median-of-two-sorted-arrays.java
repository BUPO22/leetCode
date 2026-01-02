class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int track1 = 0;
        int track2 = 0;
        int trk3 =0;
        int size = nums1.length + nums2.length;
        int[] tempArr = new int[size];
        while(track1 <= nums1.length && track2 <= nums2.length){
            if(track1 == nums1.length){
                while(track2 <= nums2.length-1){
                    tempArr[trk3] = nums2[track2];
                    track2++;
                    trk3++;
                }
                break;
            }
            if(track2 == nums2.length){
                while(track1 <= nums1.length-1){
                    tempArr[trk3] = nums1[track1];
                    track1++;
                    trk3++;
                }
                break;
            }
            if(nums1[track1] <nums2[track2]){
                tempArr[trk3] = nums1[track1];
                track1++;
                trk3++;
            }
            else{
                tempArr[trk3] = nums2[track2];
                track2++;
                trk3++;
            }
        }
        if(size % 2 != 0)
            return tempArr[size/2];
        else{
            return (tempArr[(size - 1) / 2] + tempArr[size / 2]) / 2.0;
        }
    }
}
