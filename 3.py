import re  
def is_valid_id(id_number):   
    if len(id_number) != 18:  
        return False  
    if not (id_number[0] in '1234567'):  
        return False   
    if not (id_number[1] in '01234567'):  
        return False  
    year = int(id_number[6:10])  
    month = int(id_number[10:12])  
    day = int(id_number[12:14])  
 
    if not (1900 <= year <= 2099):  
        return False  
    if not (1 <= month <= 12):  
        return False   
    if not (1 <= day <= 31):  
        return False  

    if not (id_number[17].isdigit() or id_number[17].upper() == 'X'):  
        return False  
    
    return True  
def count_valid_ids(filename):  
    valid_count = 0  
    with open(filename, 'r', encoding='utf-8') as file:  
        content = file.read()  
        id_numbers = content.splitlines()  
        for id_number in id_numbers:  
            id_number = id_number.strip()  
            if is_valid_id(id_number):  
                valid_count += 1  
                print(id_number)  
    return valid_count  

if __name__ == "__main__":  
    filename = 'IDNumbers.txt'  
    total_valid_ids = count_valid_ids(filename)  
    print(f'Total valid ID numbers: {total_valid_ids}')