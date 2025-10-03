class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        } 

        HashMap <Character,Integer> map1 = new LinkedHashMap<>(); 
        HashMap <Character,Integer> map2 = new LinkedHashMap<>();

        for(char c:s.toCharArray()){
            map1.put(c,map1.getOrDefault(c,0)+1);
        }

        for(char c:t.toCharArray()){
            map2.put(c,map2.getOrDefault(c,0)+1);
        }

        if(map1.equals(map2)){
            return true;
        }else{
            return false;
        }
    }
}