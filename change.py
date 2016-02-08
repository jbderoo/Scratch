def change_reducer(total):
    statement     = repr(total) + '$ is most efficently split into'
    print(statement)

#   This is because of the rounding error, integers are always kept exact, but floats get left off    
    total         = total * 100
    
#   hundreds block
    hundreds      = total // 10000
    total         = total - hundreds * 10000
    if hundreds   > 1:
        print('{0:.0f} hundreds'.format(hundreds))
    if hundreds   == 1:
        print('{0:.0f} hundred'.format(hundreds))

#   fifties block
    fifties       = total // 5000
    total         = total - fifties * 5000
    if fifties    > 1:
        print('{0:.0f} fifties'.format(fifties))
    if fifties    == 1:
        print('{0:.0f} fifty'.format(fifties))
    
#   twenties block
    twenties      = total // 2000
    total         = total - twenties * 2000
    if twenties   > 1:
        print('{0:.0f} twenties'.format(twenties))
    if twenties   == 1:
        print('{0:.0f} twenty'.format(twenties))

#   tens block
    tens          = total // 1000
    total         = total - tens * 1000
    if tens       > 1:
        print('{0:.0f} tens'.format(tens))
    if tens       == 1:
        print('{0:.0f} ten'.format(tens))

#   fives block
    fives         = total // 500
    total         = total - fives * 500
    if fives      > 1:
        print('{0:.0f} fives'.format(fives))
    if fives      == 1:
        print('{0:.0f} five'.format(fives))
    
#   ones block
    ones         = total // 100
    total        = total - ones * 100
    if ones      > 1:
        print('{0:.0f} ones'.format(ones))
    if ones      == 1:
        print('{0:.0f} one'.format(ones))

#   quarters block
    quarters     = total // 25
    total        = total - quarters * 25
    if quarters  > 1:
        print('{0:.0f} quarters'.format(quarters))
    if quarters  == 1:
        print('{0:.0f} quarter'.format(quarters))

#   dimes block
    dimes        = total // 10
    total        = total - dimes * 10
    if dimes     > 1:
        print('{0:.0f} dimes'.format(dimes))
    if dimes     == 1:
        print('{0:.0f} dime'.format(dimes))
    
#   nickels block
    nickels      = total // 5
    total        = total - nickels * 5
    if nickels   > 1:
        print('{0:.0f} nickels'.format(nickels))
    if nickels   == 1:
        print('{0:.0f} nickel'.format(nickels))
    
#   pennies block
    pennies      = total // 1
    total        = total - pennies * 1
    if pennies   > 1:
        print('{0:.0f} pennies'.format(pennies))
    if pennies   == 1:
        print('{0:.0f} penny'.format(pennies))

#   Can't go less than .01, but higher than 0  
    if total < 1 and total > 0:
        print("We don't go in between pennies!")
    return ''  

print(change_reducer(393.97))
print(change_reducer(186.41))
