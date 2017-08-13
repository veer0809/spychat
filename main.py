print "Let's get Started!"
spy_name = raw_input("provide your name please:")
if  len(spy_name)>0:
    spy_salutation = raw_input("what should we call you?:")
    spy_name = spy_salutation + " " + spy_name
    spy_age = 0
    spy_rating= 0.0
    spy_is_online = False
    spy_age = raw_input("what is your age? ")
    spy_age  = int(spy_age)

    if 12 < spy_age <50:

        print "Alright "  +  spy_name +  " i would like to know more about you"
        print "Welcome "  +  spy_name +  " Glad to have you back"

else:
    print"Invalid Name, Try again"