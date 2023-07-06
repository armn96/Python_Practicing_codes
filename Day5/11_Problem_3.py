def retur_indef(*args):
    counter = 0
    for n in args:
        if counter + 1 == len(args):
            return False
        elif args[counter] == 0 and args[counter+1] == 0:
            return True
        else:
            counter += 1

    return False


print(retur_indef(0,1,0,5,0,9,3,0))