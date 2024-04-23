import datetime
import pytz

# ASCII art representation of numbers 0-9
digits = [
    ["  ###  ", " #   # ", "#     #", "#     #", "#     #", " #   # ", "  ###  "],  # 0
    ["   #   ", "  ##   ", "   #   ", "   #   ", "   #   ", "   #   ", " ##### "],  # 1
    [" ##### ", "#     #", "      #", " ##### ", "#      ", "#      ", "#######"],  # 2
    [" ##### ", "#     #", "      #", " ##### ", "      #", "#     #", " ##### "],  # 3
    ["#      ", "#    # ", "#    # ", "#######", "     # ", "     # ", "     # "],  # 4
    ["#######", "#      ", "#      ", "###### ", "      #", "#     #", " ##### "],  # 5
    [" ##### ", "#     #", "#      ", "###### ", "#     #", "#     #", " ##### "],  # 6
    ["#######", "#    # ", "    #  ", "   #   ", "  #    ", " #     ", "#      "],  # 7
    [" ##### ", "#     #", "#     #", " ##### ", "#     #", "#     #", " ##### "],  # 8
    [" ##### ", "#     #", "#     #", " ######", "      #", "#     #", " ##### "]   # 9
]

def display_time_ascii(current_time):
    time_str = current_time.strftime("%H:%M:%S")
    time_ascii = ""
    for i in range(7):  # 7 rows of ASCII art for each digit
        line = ""
        for digit in time_str:
            if digit.isdigit():
                line += digits[int(digit)][i] + "  "
            else:
                line += "       "  # 7 spaces for non-digit characters
        time_ascii += line + "\n"
    print(time_ascii)

if __name__ == "__main__":
    # Prompt the user to enter their time zone
    time_zone = input("Enter your time zone (e.g., America/New_York): ")
    
    # Get the current time in the specified time zone
    current_time = datetime.datetime.now(pytz.timezone(time_zone))
    
    # Display the current time in ASCII art format
    print("Current time in", time_zone)
    display_time_ascii(current_time)
