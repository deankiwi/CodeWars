def is_leap(year):
    if year%4==0:
        if year%100 ==0 and not year%400 ==0:
            return False
        return True
    return False

years = [1800,2500,2000,2400,2004,2003]
for year in years:
    print(is_leap(year))
