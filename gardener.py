# Skeleton Program for the AQA A1 Summer 2017 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 environment

# Stage :
# Version Number : 4.2
# Original Author : S Langfield
# Edited by : S Langfield
# Edited on : 10 Ddecember 2016
# Edits: GetHowLongToRun, ReadFile, SimulateSummer

from random import *

SOIL = '.'
SEED = 'S'
PLANT = 'P'
ROCKS = 'X'

FIELDLENGTH = 20 
FIELDWIDTH = 35 

def GetHowLongToRun():
  print('Welcome to the Plant Growing Simulation')
  print()
  print('You can step through the simulation a year at a time')
  print('or run the simulation for 0 to 5 years')
  print('How many years do you want the simulation to run?')
  valid = False
  while not valid:
    try:
      user_input_list = input('Enter a number between 0 and 5, or -1 for stepping mode: ').split('.')
      print (user_input_list)
      if len(user_input_list) == 1:
        Seasons = int(user_input_list[0])*4
      elif len(user_input_list) == 2:
        Seasons = int(user_input_list[0])*4 + float('0.' + user_input_list[1])*4
      else:
        print('Invalid input - please try again (examples: 2, 3.25, 4.75')
      
      if (int(Seasons) == Seasons) and (Seasons/4 >-2 and Seasons/4 <6):
        valid = True
      else:
        print('Invalid input - please try again')
    except:
      print('Invalid input - please try again')
  return int(Seasons)

def CreateNewField(): 
  Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
  Row = FIELDLENGTH // 2
  Column = FIELDWIDTH // 2
  Field[Row][Column] = SEED
  return Field

def ReadFile():   
  FileName = input('Enter file name: ')
  Field = [[SOIL for Column in range(FIELDWIDTH)] for Row in range(FIELDLENGTH)]
  try:
    FileHandle = open(FileName, 'r')
    for Row in range(FIELDLENGTH):
      FieldRow = FileHandle.readline()
      for Column in range(FIELDWIDTH):
        Field[Row][Column] = FieldRow[Column]
    FileHandle.close()
  except:
    Field = CreateNewField()
  return Field

def InitialiseField(): 
  Response = input('Do you want to load a file with seed positions? (Y/N): ')
  if Response == 'Y':
    Field = ReadFile()
  else:
    Field = CreateNewField()
  return Field

def Display(Field, Season, Year):
  print('Season: ', Season, '  Year number: ', Year)
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      print(Field[Row][Column], end='')
    print('|{0:>3}'.format(Row))
  print()

def CountPlants(Field):
  NumberOfPlants = 0
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        NumberOfPlants += 1
  if NumberOfPlants == 1:
    print('There is 1 plant growing')
  else:  
    print('There are', NumberOfPlants, 'plants growing')
    
def SimulateSpring(Field):
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == SEED:  
        Field[Row][Column] = PLANT
  CountPlants(Field)
  if randint(0, 1) == 1:
    Frost = True
  else:
    Frost = False
  if Frost:    
    PlantCount = 0
    for Row in range(FIELDLENGTH):
      for Column in range(FIELDWIDTH):
        if Field[Row][Column] == PLANT:
          PlantCount += 1
          if PlantCount % 3 == 0:
            Field[Row][Column] = SOIL
    print('There has been a frost')
    CountPlants(Field)
  return Field

def SimulateSummer(Field): 
  RainFall = randint(0, 2)
  if RainFall == 0:
    PlantCount = 0
    for Row in range(FIELDLENGTH):
      for Column in range(FIELDWIDTH):
        if Field[Row][Column] == PLANT:
          PlantCount += 1
          if PlantCount % 2 == 0:
            Field[Row][Column] = SOIL
    print('There has been a severe drought')
    CountPlants(Field)
  return Field

def SeedLands(Field, Row, Column): 
  if Row >= 0 and Row < FIELDLENGTH and Column >= 0 and Column < FIELDWIDTH: 
    if Field[Row][Column] == SOIL:
      Field[Row][Column] = SEED
  return Field

def SimulateAutumn(Field): 
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        Field = SeedLands(Field, Row - 1, Column - 1)
        Field = SeedLands(Field, Row - 1, Column)
        Field = SeedLands(Field, Row - 1, Column + 1)
        Field = SeedLands(Field, Row, Column - 1)
        Field = SeedLands(Field, Row, Column + 1)
        Field = SeedLands(Field, Row + 1, Column - 1)
        Field = SeedLands(Field, Row + 1, Column)
        Field = SeedLands(Field, Row + 1, Column + 1)
  return Field

def SimulateWinter(Field):
  for Row in range(FIELDLENGTH):
    for Column in range(FIELDWIDTH):
      if Field[Row][Column] == PLANT:
        Field[Row][Column] = SOIL
  return Field

def SimulateOneYear(Field, Years):
  Field = SimulateSpring(Field)
  Display(Field, 'spring', Years)
  Field = SimulateSummer(Field)
  Display(Field, 'summer', Years)
  Field = SimulateAutumn(Field)
  Display(Field, 'autumn', Years)
  Field = SimulateWinter(Field)
  Display(Field, 'winter', Years)

def Simulation():
 YearsToRun = int(GetHowLongToRun()/4)
 if YearsToRun != 0:
  Field = InitialiseField()
  if YearsToRun >= 1:
    for Year in range(1, YearsToRun + 1):
      SimulateOneYear(Field, Year)
    if  user_input_list[1] == 25:
      Field = SimulateSpring(Field)
      Display(Field, 'spring', Year + 1)
    if user_input_list[1] == 5:
      Field = SimulateSummer(Field)
      Display(Field, 'summer', Year + 1)
    if user_input_list[1] == 75:
      Field = SimulateAutumn(Field)
      Display(Field, 'autumn', Year + 1)
      
  else:
    Continuing = True                     
    Year = 0
    while Continuing:
      Year += 1
      SimulateOneYear(Field, Year)
      Response = input('Press Enter to run simulation for another Year, Input X to stop: ')
      if Response == 'x' or Response == 'X':
        Continuing = False
  print('End of Simulation')
input()
   
   
if __name__ == "__main__":
  Simulation()      
   
   
