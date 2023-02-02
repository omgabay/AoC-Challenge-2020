import re 
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''


debug = False 
eye_color = ("amb", "blu", "brn","gry", "grn", "hzl", "oth")
def validate_passport(passport):  
    if 'byr' not in passport or not 1920 <= int(passport['byr']) <= 2002: 
        print('invalid byr')
        return False 
    if 'iyr' not in passport or not 2010 <= int(passport['iyr']) <= 2020:
        print('invalid iyr') 
        return False
    if 'eyr' not in passport or not 2020 <= int(passport['eyr']) <= 2030:      
        print('invalid eyr')
        return False

    # height 
    if 'hgt' not in passport: 
        print('invalid hgt')
        return False
    height = passport['hgt']    
    if 'cm' in height:
        height,_,_ = height.partition('cm')
        if not height.isdigit():
            return False
        height = int(height)
        if not 150 <= height <= 193:
            print(f'invalid hgt {passport["hgt"]}') 
            return False
    elif 'in' in height:
        height,_,_ = height.partition('in')
        if not height.isdigit():
            print('invalid hgt', height)
            return False
        height = int(height)
        if not 59 <= height <= 76: 
            print(f'invalid hgt {passport["hgt"]}')
            return False      
    else:
        print('invalid hgt')
        return False

    # check hair color
    if 'hcl' not in passport:
        print('invalid hcl')
        return False 
    hair_color = passport['hcl']
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hair_color)
    if not match:
        print('invalid hcl')
        return False    

    # check eye color 
    if 'ecl' not in passport or passport['ecl'] not in eye_color:
        print('invalid ecl')
        return False   

   # check passport id 
    if 'pid' not in passport or len(passport['pid']) != 9:
        print('invalid pid')
        return False 
    pid = passport['pid']
    if not pid.isdigit():
        print(f'invalid {passport["pid"]}')
        return False
    key = 'cid'
    if len(passport) == 8: 
        return 'cid' in passport
    return len(passport) == 7     


def main():
    validated = 0 
    passport = {} 
    with open("passports.txt", 'r', encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip()         
            if line == "": 
                if validate_passport(passport):
                    validated += 1
                    #print(f'{validated}:{passport}')
                else:
                    print(f'not validated! {passport}')  
                passport.clear()

            else: 
                fields = line.split()
                for field in fields: 
                    key, value = field.split(":", maxsplit=1)
                    passport[key] = value
    if validate_passport(passport):
        validated += 1                 
    print("total validated:",validated)




if __name__ == "__main__":
    main() 



