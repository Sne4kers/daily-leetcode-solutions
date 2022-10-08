class Solution {
public:
    bool equalFrequency(string word) {
        map<char, int> charMap;
        map<int, int> countMap;
        for(int i = 0; i < word.size(); i++)
            charMap[word[i]]++;
        for(const auto &[key, value] : charMap) {
            countMap[value]++;
        }
        
        if(countMap.size() >= 3)
            return false;
        if(countMap.size() == 1) {
            for(const auto &[key, value] : countMap){
                if(key == 1 || value == 1)
                    return true;
            }
            return false;
        }
        else {
            int counter = 0;
            int key_a, key_b, val_a, val_b;
            for(const auto &[key, value] : countMap){
                if(counter){
                    key_a = key;
                    val_a = value;
                } else{
                    key_b = key;
                    val_b = value;
                    counter++;
                }
            }
            if(val_a != 1 && val_b != 1)
                return false;
            if(val_a == 1 && key_a - 1 == key_b)
                return true;
            if(val_b == 1 && key_b - 1 == key_a)
                return true;
            if((val_b == 1 && key_b == 1) || (val_a == 1 && key_a == 1))
                return true;
            return false;
        }
    }
};
