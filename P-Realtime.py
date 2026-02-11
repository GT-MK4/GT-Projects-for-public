import time
hours=input("Enter Hour Now: ")
minutes=input("Enter Minutes Now: ")
sec=0
time=[hours,minutes,sec]
def timenow in time :
	i=0
	while True :
		i+=1
		if minute ==59 :
			show=str(input("you want time now(please perss G): "))
			if show==G :
				print(f"{time(0), : ,{time(1)}")
		sec+=1
		if sec ==59 :
			minutes+=1
			sec=0
			if minutes==59 :
				hours+=1
				minutes=0
				if hours==12 :
					hours=0
		time.sleep(1)
timenow