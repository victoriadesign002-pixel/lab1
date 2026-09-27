total_seconds = int(input("Enter seconds: "))

days = total_seconds // 86400
total_seconds %= 86400

hours = total_seconds // 3600
total_seconds %= 3600

minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).")
