print("hi . I can help you to convert your units ")
Case = 1
while case == 1 :
    print("""
    1-length
    2-currency
    3-speed
    4-temperature
    5-weight
    6-volume \n""")
    cat = float(input("which category? "))
    if cat == 1:
        print("""
        1-kilometer
        2-meter
        3-centimeter
        4-mile
        5-feet
        6-yard
        7-inch""")
        cat3 = float(input("what is your input unit? "))
        print("""
        1-kilometer
        2-meter
        3-centimeter
        4-mile
        5-feet
        6-yard
        7-inch""")
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))
        if cat3 == 1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num * 1000))
            if cat2 == 3:
                print("answer : " + str(num * 100000))
            if cat2 == 4:
                print("answer : " + str(num * 0.62137))
            if cat2 == 5:
                print("answer : " + str(num * 3280.839))
            if cat2 == 6:
                print("answer : " + str(num * 1093.61))
            if cat2 == 7:
                print("answer :" + str(num * 39370.07))
        if cat3 == 2:
            if cat2==1 :
                    print("answer : " + str(num/1000))
            if cat2 == 2:
                    print("answer :" + str(num))
            if cat2 == 3:
                    print("answer : " + str(num * 100))
            if cat2 == 4:
                    print("answer : " + str(num * 0.00062137))
            if cat2 == 5:
                    print("answer : " + str(num * 3.280839))
            if cat2 == 6:
                    print("answer : " + str(num * 1.09361))
            if cat2 == 7:
                    print("answer :" + str(num * 39.37007))
        if cat3 == 3:
            if cat2 == 1:
                    print("answer : " + str(num/100000))
            if cat2 == 2:
                    print("answer :" + str(num/100))
            if cat2 == 3:
                    print("answer : " + str(num))
            if cat2 == 4:
                    print("answer : " + str(num * 0.0000062137))
            if cat2 == 5:
                    print("answer : " + str(num * 0.03280839))
            if cat2 == 6:
                    print("answer : " + str(num * 0.0109361))
            if cat2 == 7:
                    print("answer :" + str(num * 0.3937007))
        if cat3==3 :
            if cat2==1:
                print("answer : " + str(num / 100000))
            if cat2 == 2:
                print("answer :" + str(num / 100))
            if cat2 == 3:
                print("answer : " + str(num))
            if cat2 == 4:
                print("answer : " + str(num * 0.0000062137))
            if cat2 == 5:
                print("answer : " + str(num * 0.03280839))
            if cat2 == 6:
                print("answer : " + str(num * 0.0109361))
            if cat2 == 7:
                print("answer :" + str(num * 0.3937007))
        if cat3==4 :
            if cat2==1:
                print("answer : " + str(num*1.609444))
            if cat2 == 2:
                print("answer :" + str(num*1609.344))
            if cat2 == 3:
                print("answer : " + str(num*160934.4))
            if cat2 == 4:
                print("answer : " + str(num))
            if cat2 == 5:
                print("answer : " + str(num *5280))
            if cat2 == 6:
                print("answer : " + str(num * 1760))
            if cat2 == 7:
                print("answer :" + str(num * 63360))
        if cat3==5 :
            if cat2==1:
                print("answer : " + str(num*0.0003048))
            if cat2 == 2:
                print("answer :" + str(num*0.3048))
            if cat2 == 3:
                print("answer : " + str(num*30.48))
            if cat2 == 4:
                print("answer : " + str(num * 0.00018939))
            if cat2 == 5:
                print("answer : " + str(num))
            if cat2 == 6:
                print("answer : " + str(num * 0.33333))
            if cat2 == 7:
                print("answer :" + str(num * 12))
        if cat3==6 :
            if cat2==1:
                print("answer : " + str(num*0.0009144))
            if cat2 == 2:
                print("answer :" + str(num*0.9144))
            if cat2 == 3:
                print("answer : " + str(num*91.44))
            if cat2 == 4:
                print("answer : " + str(num * 0.000568181))
            if cat2 == 5:
                print("answer : " + str(num * 3))
            if cat2 == 6:
                print("answer : " + str(num * 1))
            if cat2 == 7:
                print("answer :" + str(num * 36))
        if cat3==7 :
            if cat2==1:
                print("answer : " + str(num* 0.0000254))
            if cat2 == 2:
                print("answer :" + str(num*0.0254))
            if cat2 == 3:
                print("answer : " + str(num*2.54))
            if cat2 == 4:
                print("answer : " + str(num * 0.0000015782828))
            if cat2 == 5:
                print("answer : " + str(num * 0.083333))
            if cat2 == 6:
                print("answer : " + str(num * 0.027777))
            if cat2 == 7:
                print("answer :" + str(num))
    elif cat == 2:
        print("""
            1-dollar
            2-euro
            3-rial
            4-lira """)
        cat3 = float(input("what is your input unit? "))
        print("""
            1-dollar
            2-euro
            3-rial
            4-lira """)
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))
        if cat3==1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num*0.85))
            if cat2 == 3:
                print("answer : " + str(num * 230000))
            if cat2 == 4:
                print("answer : " + str(num * 7.83))
        if cat3==2:
            if cat2 == 1:
                print("answer : " + str(num*1.17))
            if cat2 == 2:
                print("answer :" + str(num))
            if cat2 == 3:
                print("answer : " + str(num * 280000))
            if cat2 == 4:
                print("answer : " + str(num * 9.2))
        if cat3==3:
            if cat2 == 1:
                print("answer : " + str(num/230000))
            if cat2 == 2:
                print("answer :" + str(num/280000))
            if cat2 == 3:
                print("answer : " + str(num))
            if cat2 == 4:
                print("answer : " + str(num/ 50000))
        if cat3==4:
            if cat2 == 1:
                print("answer : " + str(num*0.13))
            if cat2 == 2:
                print("answer :" + str(num*0.11))
            if cat2 == 3:
                print("answer : " + str(num * 53000))
            if cat2 == 4:
                print("answer : " + str(num))
    elif cat==3:
        print("""
            1-km/h
            2-m/s
            3-mile/h
            4-knot
                5-speed of light """)
        cat3 = float(input("what is your input unit? "))
        print("""
            1-km/h
            2-m/s
            3-mile/h
            4-knot
                5-speed of light """)
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))
        if cat3==1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num*0.27777))
            if cat2 == 3:
                print("answer : " + str(num * 0.62137))
            if cat2 == 4:
                print("answer : " + str(num*0.539956))
            if cat2==5:
                print("answer : "+str(num*0.000000000926566))
        if cat3==2:
            if cat2 == 1:
                print("answer : " + str(num*3.6))
            if cat2 == 2:
                print("answer :" + str(num))
            if cat2 == 3:
                print("answer : " + str(num * 2.23693))
            if cat2 == 4:
                print("answer : " + str(num*1.9438))
            if cat2==5:
                print("answer : "+str(num*0.00000000333564))
        if cat3==3:
            if cat2 == 1:
                print("answer : " + str(num*1.6093))
            if cat2 == 2:
                print("answer :" + str(num*0.4470))
            if cat2 == 3:
                print("answer : " + str(num))
            if cat2 == 4:
                print("answer : " + str(num*0.868976))
            if cat2==5:
                print("answer : "+str(num*0.0000000001491164))
        if cat3==4:
            if cat2 == 1:
                print("answer : " + str(num*1.852))
            if cat2 == 2:
                print("answer :" + str(num*0.514444))
            if cat2 == 3:
                print("answer : " + str(num * 1.150779))
            if cat2 == 4:
                print("answer : " + str(num))
            if cat2==5:
                print("answer : "+str(num*0.00000000017160019))
        if cat3==5:
            if cat2 == 1:
                print("answer : " + str(num*1079252849))
            if cat2 == 2:
                print("answer :" + str(num*299792458))
            if cat2 == 3:
                print("answer : " + str(num * 670616629.4))
            if cat2 == 4:
                print("answer : " + str(num*582749918.4))
            if cat2==5:
                print("answer : "+str(num))
    elif cat==4:
        print("""
            1-celsius
            2-fahrenheit
            3-kelvin """)
        cat3 = float(input("what is your input unit? "))
        print("""
            1-celsius
            2-fahrenheit
            3-kelvin """)
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))
        if cat3==1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num*1.8 +32))
            if cat2 == 3:
                print("answer : " + str(num +273))
        if cat3==2:
            if cat2 == 1:
                print("answer : " + str((num-32)/1.8))
            if cat2 == 2:
                print("answer :" + str(num))
            if cat2 == 3:
                print("answer : " + str((num-32)/1.8+273))
        if cat3==3:
            if cat2 == 1:
                print("answer : " + str(num-273))
            if cat2 == 2:
                print("answer :" + str((num-273)*1.8+32))
            if cat2 == 3:
                print("answer : " + str(num))
    elif cat==5:
        print("""
            1-kg
            2-gram
            3-pound
            4-ounce""")
        cat3 = float(input("what is your input unit? "))
        print("""
            1-kg
            2-gram
            3-pound
            4-ounce""")
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))
        if cat3==1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num*1000))
            if cat2 == 3:
                print("answer : " + str(num * 2.2046))
            if cat2 == 4:
                print("answer : " + str(num * 35.2739))
        if cat3==2:
            if cat2 == 1:
                print("answer : " + str(num/1000))
            if cat2 == 2:
                print("answer :" + str(num))
            if cat2 == 3:
                print("answer : " + str(num * 0.0022046))
            if cat2 == 4:
                print("answer : " + str(num * 0.03527))
        if cat3==3:
            if cat2 == 1:
                print("answer : " + str(num*0.4535))
            if cat2 == 2:
                print("answer :" + str(num*453.59))
            if cat2 == 3:
                print("answer : " + str(num))
            if cat2 == 4:
                print("answer : " + str(num * 16))
        if cat3==4:
            if cat2 == 1:
                print("answer : " + str(num*0.02834))
            if cat2 == 2:
                print("answer :" + str(num*28.3490))
            if cat2 == 3:
                print("answer : " + str(num *0.0625 ))
            if cat2 == 4:
                print("answer : " + str(num ))
    elif cat==6:
        print("""
            1-cubic meter
            2-liter
            3-cc
            4-gallon""")
        cat3 = float(input("what is your input unit? "))
        print("""
            1-cubic meter
            2-liter
            3-cc
            4-gallon""")
        cat2 = float(input("what is your output unit? "))
        num = float(input("ok . what is your number ? "))

        if cat3==1:
            if cat2 == 1:
                print("answer : " + str(num))
            if cat2 == 2:
                print("answer :" + str(num*1000))
            if cat2 == 3:
                print("answer : " + str(num * 1000000))
            if cat2 == 4:
                print("answer : " + str(num * 264.172052))
        if cat3==2:
            if cat2 == 1:
                print("answer : " + str(num/1000))
            if cat2 == 2:
                print("answer :" + str(num))
            if cat2 == 3:
                print("answer : " + str(num * 1000))
            if cat2 == 4:
                print("answer : " + str(num * 0.264172052))
        if cat3==3:
            if cat2 == 1:
                print("answer : " + str(num/1000000))
            if cat2 == 2:
                print("answer :" + str(num/1000))
            if cat2 == 3:
                print("answer : " + str(num))
            if cat2 == 4:
                print("answer : " + str(num * 0.000264172))
        if cat3==4:
            if cat2 == 1:
                print("answer : " + str(num*0.00378541))
            if cat2 == 2:
                print("answer :" + str(num*3.78541))
            if cat2 == 3:
                print("answer : " + str(num *3785.411))
            if cat2 == 4:
                print("answer : " + str(num ))
    print("thanks :) ")
    case = int(input("""want to continue ?
     1- yes 
     2- No : """))






























