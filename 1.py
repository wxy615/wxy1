import re  

telNumber = '''Suppose my Phone No. is 0535-1234567,\
yours is 010-12345678,\
his is 025-87654321.'''  

# 正则表达式匹配电话号码  
pattern = r'\d{3,4}-\d{7,8}'  

# 查找所有匹配的电话号码  
phone_numbers = re.findall(pattern, telNumber)  

# 输出结果  
print("提取的电话号码有：")  
for number in phone_numbers:  
    print(number)