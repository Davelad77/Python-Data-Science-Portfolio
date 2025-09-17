# This is an example Python program demonstrating for loops.
# It outputs a star pattern increasing from 1 star to 5 then back 1 on separate lines
# start counter at 0
# for counter (0, 11)
#   if counter <= 5 print counter * stars
#   elif counter > 5 print 10 - counter * stars
    

for i in range(0 , 11):
    stars = "**********"
    if i <= 5:
        print(stars[0:i]) 
    elif i > 5:
        index = 10-i
        print(stars[0:index])
