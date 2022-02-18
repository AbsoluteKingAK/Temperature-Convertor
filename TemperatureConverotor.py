temp = float(input("Please Enter the temperature in Celcius : "))
conv = (temp * 1.8) + 32
print("%0.1f degree Celcius is equal to %0.1f degree Fahrenheit"%(temp,conv))
if conv>104:
    print("It is hot")
elif conv<50:
    print("It is cold")
else:
    print("It is a nice weather")