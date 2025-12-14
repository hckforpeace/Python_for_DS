import datetime  as datetime
import time as time

date = datetime.datetime.now().strftime("%b %d %Y")
t = time.time()
f1 = f"{t:,.4f}"
f2 = f"{t:.2e}"
print("Seconds since January 1, 1970:", f1, "or", f2, "in scientific notation")
print(date)
