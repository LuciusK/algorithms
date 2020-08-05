# Python
def recursion(level, param1, param2, ...): 


    
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 


    # process logic in current level 
    process(level, data...) 


    # drill down 
    self.recursion(level + 1, p1, ...) 


    # reverse the current level status if needed

"""1. 不要进行人肉递归(最大误区)
    2.找到最近最简方法，将其拆解成可重复解决的问题(重复子问题)
    3.数学归纳法思想"""