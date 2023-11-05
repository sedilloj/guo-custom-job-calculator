# import requests
from diamondLib import CalcDiamondPrice, ConvertMmToCarat, CalcSettingCost

def CalcGoldPrice(karat, pricePerGram, weight):
  procurementCost = 1.03
  castingLaborCost = 1.2
  purity = karat / 24.0
  return castingLaborCost * pricePerGram * procurementCost * purity * weight

def CalcSilverPrice(pricePerGram, weight):
  castingLaborCost = 4
  return pricePerGram * weight * castingLaborCost

def CalcPlatinumPrice(pricePerGram, weight):
  castingLaborCost = 1.6
  return pricePerGram * weight * castingLaborCost

def CalcDesignPrice(complexity):
  match complexity.lower():
    case 'simple':
      return 80
    case 'medium':
      return 160
    case 'complex':
      return 220
    case _:
      raise ValueError('Unavailable option entered.')
    
def CalcPolishingPrice(size):
  match size.lower():
    case 's' | 'small':
      return 50
    case 'm' | 'medium':
      return 100
    case 'l' | 'large':
      return 200

def main(verbose = False):
  ## Gold Stuff
  goldKarat = float(input('Enter the carat of gold: '))
  goldPricePerGram = float(input('Enter today\'s gold price: '))
  goldWeight = float(input('Enter the weight of gold: '))
  
  totalGoldPrice = CalcGoldPrice(goldKarat, goldPricePerGram, goldWeight)
  print(totalGoldPrice)
  
  ## Silver Stuff
  silverPricePerGram = float(input('Enter today\'s silver price: '))
  silverWeight = float(input('Enter the weight of silver: '))
  
  totalSilverPrice = CalcSilverPrice(silverPricePerGram, silverWeight)
  print(totalSilverPrice)
  
  ## Platinum Stuff
  platinumPricePerGram = float(input('Enter today\'s platinum price: '))
  platinumWeight = float(input('Enter the weight of platinum: '))
  
  totalPlatinumPrice = CalcPlatinumPrice(platinumPricePerGram, platinumWeight)
  print(totalPlatinumPrice)

  ## Design Stuff
  designComplexity = input('Enter design complexity (simple, medium, complex): ')
  totalDesignPrice = CalcDesignPrice(designComplexity)
  print(totalDesignPrice)
  
  ## Diamond Stuff
  # detailed entry
  if input('State whether calculation is done using total weight carat: ') == 'n':
    numDiamondTypes = int(input('Enter the number of diamond types: '))
    totalDiamondPrice, numStones = CalcDiamondPrice(numDiamondTypes)
  
  # simplified version  
  else:
    totalCaratWeight = input('Enter the total weight carat: ')
    totalDiamondPrice, _ = CalcDiamondPrice(1)
    sizeStr = input('\tEnter the size (in mm or ct): ')

    # Convert mm to ct if needed
    sizeInfo = sizeStr.split()
    if sizeInfo[1] == 'mm':
      avgCaratSize = ConvertMmToCarat(sizeInfo[0])
    elif sizeInfo[1] == 'ct':
      avgCaratSize = sizeInfo[0]
      
      numStones = totalCaratWeight / avgCaratSize # number setting stones
      
  print(totalDiamondPrice)
  
  ## Setting Stuff
  if numStones == 1:
    settingType = input('Enter the setting type: ')
    totalSettingCost = CalcSettingCost(1, settingType)
  else:
    totalSettingCost = CalcSettingCost(numStones)
  
  print(totalSettingCost)
  
  ## Polishing Stuff
  pieceSize = input('Enter the size of the piece (small, medium, large): ')
  totalPolishingPrice = CalcPolishingPrice(pieceSize)
  
  print(totalPolishingPrice)
  
  totalCost = totalGoldPrice + totalSilverPrice + totalPlatinumPrice \
            + totalDesignPrice + totalDiamondPrice + totalSettingCost + totalPolishingPrice
  customerPrice = totalCost * 2
  
  print(customerPrice)

main(False)
# print(CalcGoldPrice(14, 83, 10))