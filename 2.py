import re  
with open('70.txt', 'r', encoding='utf-8') as file:  
    content = file.read()  

date_pattern = r'(\d{4}年\d{1,2}月\d{1,2}日|\d{4}年|\d{1,2}月\d{1,2}日)'  
event_pattern = r'([^\n。]*?(?:战役|战斗)[^\n。]*?)'  
 
dates = re.findall(date_pattern, content)  
events = re.findall(event_pattern, content)  
print("提取的日期:")  
for date in dates:  
    print(date)  

print("\n提取的事件:")  
for event in events:  
    print(event)