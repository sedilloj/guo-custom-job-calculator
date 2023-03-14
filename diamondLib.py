import pandas as pd
import numpy as np

priceTable = pd.read_csv('resources/diamondprice.csv')
sizeConversionTable = pd.read_csv('resources/diamondsize.csv')

colorList = np.array(['F', 'H', 'J', 'L', 'M', 'N'])
sizeList = np.array([0.03, 0.07, 0.14, 0.17])

def CalcTotalDiamondPrice(typeArr, countArr):
  totalPrice = 0
  for i in range(len(typeArr)):
    typeArr[i]
    priceIncrement = typeArr[i].iloc[0]['price'] * countArr[i]
    print(priceIncrement)
    totalPrice += priceIncrement
  
  print(totalPrice)
  return totalPrice

def GetDiamondType(size, clarity, color):
  adaptedSize = sizeList[np.searchsorted(sizeList, size)]
  adaptedColor = colorList[np.searchsorted(colorList, color)]

  # for size < 0.30
  adaptedClarity = clarity
  if (adaptedSize <= 0.3):
    if (clarity == 'IF' or clarity == 'VVS'):
      adaptedClarity = 'VVS2'
    elif (clarity == 'VS'):
      adaptedClarity = 'VS2'

  entry = priceTable[(priceTable['size'] == adaptedSize) & 
                     (priceTable['clarity'] == adaptedClarity) & 
                     (priceTable['color'] == adaptedColor)]
  
  return entry.index.to_numpy()

def GetDiamondPriceArr(numTypes):
  # typeArr = []
  typeIdxArr = []
  typeCountArr = []

  for typeNo in range(numTypes):
    print('Enter details for diamond type ' + str(typeNo + 1))
    amount = input('\tEnter amount of stones of this type: ')
    sizeStr = input('\tEnter the size (in mm or ct): ')
    clarity = input('\tEnter the clarity: ').upper()
    color = input('\tEnter the color: ').upper()

    # Convert mm to ct if needed
    sizeInfo = sizeStr.split()
    if sizeInfo[1] == 'mm':
      caratSize = ConvertMmToCarat(sizeInfo[0])
    elif sizeInfo[1] == 'ct':
      caratSize = sizeInfo[0]

    typeIdx = GetDiamondType(caratSize, clarity, color)[0]
    
    # check if equivalent type was already entered
    if typeIdxArr.count(typeIdx):
      typeCountArr[typeIdxArr.index(typeIdx)] += int(amount)
    else:
      typeIdxArr.append(typeIdx)
      typeCountArr.append(int(amount))
  
  return typeIdxArr, typeCountArr


def ConvertMmToCarat(mm):
  return round(np.interp(mm, sizeConversionTable['mm'], sizeConversionTable['ct']), 3)

# print(ConvertMmToCarat(9.05))

# entryArr = []
# entryArr.append(GetDiamondType(0.03, 'VS2', 'F'))
# entryArr.append(GetDiamondType(0.03, 'VVS2', 'F'))

# existingEntry = GetDiamondType(0.01, 'I3', 'F')
# print(existingEntry.index.to_numpy())

# print(entryArr.count(existingEntry))
# amountArr = [1, 2]

# print(entryArr)

# final test
entryArr, amountArr = GetDiamondPriceArr(3)
print(entryArr)
print(amountArr)
# CalcTotalDiamondPrice(entryArr, amountArr)