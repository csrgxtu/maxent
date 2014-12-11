from Utility import loadMatrixFromFile

DIR = '/home/archer/Documents/maxent/data/basketball/leaguerank/'

mat = loadMatrixFromFile(DIR + '1610612741.csv.sorted')

l1WinCount = 0
l1LoseCount = 0
l2WinCount = 0
l2LoseCount = 0
l3WinCount = 0
l3LoseCount = 0
l4WinCount = 0
l4LoseCount = 0

for row in mat:
  lr = float(loadMatrixFromFile(DIR + row[2] + '.l')[0][5])
  cat = False
  if lr >= 0 and lr < 0.02:
    cat = 'l1'
  elif lr >= 0.02 and lr < 0.04:
    cat = 'l2'
  elif lr >= 0.04 and lr < 0.06:
    cat = 'l3'
  elif lr >= 0.06:
    cat = 'l4'
  
  if row[0] == 'W' and cat == 'l1':
    l1WinCount = l1WinCount + 1
  elif row[0] == 'L' and cat == 'l1':
    l1LoseCount = l1LoseCount + 1
  elif row[0] == 'W' and cat == 'l2':
    l2WinCount = l2WinCount + 1
  elif row[0] == 'L' and cat == 'l2':
    l2LoseCount = l2LoseCount + 1
  elif row[0] == 'W' and cat == 'l3':
    l3WinCount = l3WinCount + 1
  elif row[0] == 'L' and cat == 'l3':
    l3LoseCount = l3LoseCount + 1
  elif row[0] == 'W' and cat == 'l4':
    l4WinCount = l4WinCount + 1
  elif row[0] == 'L' and cat == 'l4':
    l4LoseCount = l4LoseCount + 1

winCount = 0
loseCount = 0

for row in mat:
  if row[0] == 'W':
    winCount = winCount + 1
  elif row[0] == 'L':
    loseCount = loseCount + 1

print (l1WinCount/float(len(mat)))/(winCount/float(len(mat)))
print (l1LoseCount/float(len(mat)))/(loseCount/float(len(mat)))
print (l2WinCount/float(len(mat)))/(winCount/float(len(mat)))
print (l2LoseCount/float(len(mat)))/(loseCount/float(len(mat)))
print (l3WinCount/float(len(mat)))/(winCount/float(len(mat)))
print (l3LoseCount/float(len(mat)))/(loseCount/float(len(mat)))
print (l4WinCount/float(len(mat)))/(winCount/float(len(mat)))
print (l4LoseCount/float(len(mat)))/(loseCount/float(len(mat)))
