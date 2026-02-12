import time
hours=int(input("Enter Hour Now: "))
minutes=int(input("Enter Minutes Now: "))
PAm=input("PM or AM: ")
sec=0
while True :
	if minutes>=59 :
		hours+=1
		minutes=0
	if sec==59 :
		minutes+=1
		sec=0
	if hours>12:
		hours-=12
		if PAm=="PM" :
			PAm="AM"
		if PAm=="AM" :
			PAm="PM"
	sec+=1
	time.sleep(1)
	print(f"\r {hours:02d} : {minutes:02d} :{sec} /{PAm}", end="")