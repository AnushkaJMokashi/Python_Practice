try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("No error occurred.")
finally:
    print("This code always runs.")

##error handling

try:
    pass
except:
    pass