'''Given day number, convert to date it refers to.

Input : day_num = “339”, year = “2020” 
Output : 12-04-2020 
Explanation : 339th Day of 2020 is 4th December.

Input : day_num = “4”, year = “2020” 
Output : 01-04-2020 
Explanation : 4th Day of 2020 is 4th January '''

from datetime import datetime
  
day = "339"
  
print("The day number : " + str(day))
  
day.rjust(3 + len(day), '0')
  
year = "2020"
  
res = datetime.strptime(year + "-" + day, "%Y-%j").strftime("%m-%d-%Y")
  
print("Date : " + str(res))