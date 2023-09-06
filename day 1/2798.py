def numberOfEmployeesWhoMetTarget(hours, target: int) -> int:
    return len([h for h in hours if h >= target])



if __name__ == '__main__':
    print( numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2) )