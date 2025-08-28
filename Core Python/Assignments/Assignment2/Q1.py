H = int(input("Enter the hours:"))
M = int(input("Enter the minutes:"))
S = int(input("Enter the seconds:"))

h_seconds = H * 3600
m_seconds = M * 60

total_seconds = h_seconds + m_seconds + S

print(f'Total seconds from the given hours, minutes, seconds are {total_seconds}.')