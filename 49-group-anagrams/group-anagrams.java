class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
    HashMap <String,List<String>> map = new HashMap<>();

    for(String word : strs){
        char[] c = word.toCharArray();
        Arrays.sort(c);
        String key = new String(c);

        // if(!map.containsKey(key)){
        //     map.put(key,new ArrayList<>());
        // }
        // map.get(key).add(word);
        map.computeIfAbsent(key,k -> new ArrayList<>()).add(word);
    } 
    return new ArrayList<>(map.values());   
    }
}