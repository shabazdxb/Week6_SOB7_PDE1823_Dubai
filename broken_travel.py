# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? "))#Changed from '==' to '='
#changed input syntax. instead of"int.input(...." to "int(input(...."
#changed quotations from ' to "
if year < 1900:#strictly following logic insted of using "<="
    #added missing colon
    print("Woah, that's the past!")
    #changed to double quotations as python gives error with single
elif year >= 1900 and year <= 2020:#changed wrong logic operator
    print("That's totally the present!")
else:#changed from elif and put else
    print("Far out, that's the future!!")
