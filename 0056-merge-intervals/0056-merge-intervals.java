class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->a[0]-b[0]);
        ArrayList<int[]> result=new ArrayList<>();
        result.add(intervals[0]);
        for(int i=0;i<intervals.length;i++){
            int[] last=result.get(result.size()-1);
            int[] curr=intervals[i];
            
            if(last[1]>=curr[0]){
                last[1]=Math.max(curr[1],last[1]);
            }
            else{
                result.add(curr);
            }
        }
        return result.toArray(new int[result.size()][]);
    }
}