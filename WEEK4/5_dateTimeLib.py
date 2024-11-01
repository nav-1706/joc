import datetime                                                                                         
print(datetime.date.today())                                               # 2024-10-28
print(datetime.date.today().strftime("%Y"))                                # 2024
print(datetime.date.today().strftime("%y"))                                # 24
print(datetime.date.today().strftime("%B"))                                # October
print(datetime.date.today().strftime("%b"))                                # Oct
print(datetime.date.today().strftime("%m"))                                # 10
print(datetime.date.today().strftime("%d"))                                # 28
print(datetime.date.today().strftime("%D"))                                # 10/28/24
print(datetime.date.today().strftime("%W")) # week number                  # 44
print(datetime.date.today().strftime("%w")) # week day of the week         # 1 --> monday
print(datetime.date.today().strftime("%j")) # day of year                  # 302
print(datetime.date.today().strftime("%A")) # day of week                  # Monday
print(datetime.datetime.now()) # time and date                             # 2024-10-28 19:17:12.517855