# Import the datetime module to work with dates and times
import datetime

# Print the current date in the format YYYY-MM-DD
print(datetime.date.today())

# Print the current date and time down to the microsecond
print(datetime.datetime.now())

# Store the current date and time in a variable
date = datetime.datetime.now()

# Format the 'date' in a more personalized format: Day/Month/Year, Hours:Minutes:Seconds
# and store it in 'personalized_date'
personalized_date = date.strftime("%d/%m/%Y, %H:%M:%S")

# Print the personalized formatted date and time
print(personalized_date)
