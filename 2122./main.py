class Solution:
    def check_if_possible(k, l, dictionary):
        counter = 0
        for i in l:
            if dictionary[i] == 0:
                continue
            if i + 2*k in dictionary:
                if dictionary[i + 2*k] != 0:
                    dictionary[i] -= 1
                    dictionary[i + 2*k] -= 1
                    counter += 1
                else:
                    break

            else:
                return False
        if counter == len(l) // 2:
            return True
        return False
    
    def form_array(k, l, dictionary):
        result = []
        for i in l:
            if dictionary[i] == 0:
                continue
            dictionary[i] -= 1
            dictionary[i + 2*k] -= 1
            result.append(i + k)
        return result
    
    def recoverArray(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        all_numbers = dict()
        
        for i in sorted_list:
            if i not in all_numbers:
                all_numbers[i] = 0
            all_numbers[i] += 1
        
        for i in range(1, len(sorted_list)):
            k = (sorted_list[i] - sorted_list[0]) // 2
            if k != 0:
                if Solution.check_if_possible(k, sorted_list, all_numbers.copy()):
                    return Solution.form_array(k, sorted_list, all_numbers.copy())
        return None
