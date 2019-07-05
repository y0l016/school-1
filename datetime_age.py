import datetime

ymd = [int(i) for i in input("enter ur birthday (dd-mm-yyyy): ").split("-")]
birth = datetime.date(ymd[2], ymd[1], ymd[0])
now = datetime.date.today()
diff = now - birth

print("your age is: ", diff.days / 365)
