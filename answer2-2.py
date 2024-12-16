f = open("input2.txt","r")
reports = []
for line in f:
  reports.append(line.strip().split(" "))
safeCount = 0

for report in reports:
  debug = "\n---------------------\n"
  safe = True
  assumptionFails = 0
  # loop through twice, under the assumption it's either ascending or descending
  for j in range(0,2):
    if(j == 0):
      ascending = True
      debug += "\nascending"
    else:
      debug += "\n\ndescending"
      ascending = False
      
    levelFails = 0
    dampenerCharges = 1
    i = 0

    reportCopy = report.copy()

    while i < len(reportCopy)-1:
      level1 = int(reportCopy[i])
      level2 = int(reportCopy[i+1])
      difference = abs(level1-level2)

      if(difference < 1 or difference > 3):
        dampenerCharges += -1
        debug += "\n" + str(reportCopy)
        debug += "\nPopping: " + reportCopy[i] + " because " + str(difference) + " < 1 or " + str(difference) + " > 3"
        reportCopy.pop(i)
        if(i != 0):
          i += -1
      elif(ascending and level1 > level2):
        debug += "\n"+str(reportCopy)
        debug += "\nPopping: " + reportCopy[i] + " because " + str(level1) + " > " + str(level2)
        dampenerCharges += -1
        reportCopy.pop(i)
        if(i != 0):
          i += -1
      elif(not ascending and level1 < level2):
        debug += "\n" + str(reportCopy)
        debug += "\nPopping: "+ reportCopy[i] + " because " + str(level1) + " < " + str(level2)
        dampenerCharges += -1
        reportCopy.pop(i)
        if(i != 0):
          i += -1
      else:
        i += 1

      if(dampenerCharges < 0):
        debug += "\nDampener failed"
        assumptionFails += 1
        break
    if(dampenerCharges > -1):
      break
 

  debug += "\nDampener fail count: "+ str(assumptionFails)
  if(assumptionFails < 2):
    safeCount += 1
    # print(debug)
  else:
    print(debug)

print("\n---------------------\n")
print(safeCount)
      
