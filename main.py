import requests
import diamondLib

def CalcGoldPrice(karat, pricePerGram, weight):
  purity = karat / 24.0
  return 1.2 * (pricePerGram * 1.03) * purity * weight

def CalcDesignPrice(complexity):
  match complexity:
    case 'Simple' | 'simple' | 1:
      return 80
    case 'Medium' | 'medium' | 2:
      return 160
    case 'Complex' | 'complex' | 3:
      return 220
    case _:
      raise ValueError('Unavailable option entered.')

def main(verbose = False):
  # Gold Stuff
  goldKarat = float(input('Enter the carat of gold: '))
  goldPricePerGram = float(input('Enter today\'s gold price: '))
  goldWeight = float(input('Enter the weight of gold: '))
  
  totalGoldPrice = CalcGoldPrice(goldKarat, goldPricePerGram, goldWeight)

  # Design Stuff
  designComplexity = input('Enter design complexity (simple, medium, complex): ')
  totalDesignPrice = CalcDesignPrice(designComplexity)
  
  # Diamond Stuff
  if input('Are there diamonds? (y/n)') == 'y':
    numDiamondTypes = input('How many kinds or diamonds are there?')


  
  diamondSizeStr = input('Enter the size (in mm or ct): ')
  diamondClarity = input('Enter the clarity: ').upper()
  diamondColor = input('Enter the color: ').upper()

  # Convert mm to ct if needed
  diamondSizeInfo = diamondSizeStr.split()
  if diamondSizeInfo[1] == 'mm':
    diamondSize = ConvertMmToCarat(diamondSizeInfo[0])
  elif diamondSizeInfo[1] == 'ct':
    diamondSize = diamondSizeInfo[0]

  diamondPrice = diamondLib(diamondSize, diamondClarity, diamondColor, verbose)
  
  # Offer 2 options
  diamondCostMode = input('Will you enter total carat weight (0) or number of stones (1)?')
  if diamondCostMode:
    diamondAmount = input('Enter the number of stones')
    totalCaratWeight = diamondAmount * diamondSize
  else:
    totalCaratWeight = input('Enter the total weight carat: ')
  
  if totalCaratWeight <= 0:
    settingPrice = 0
  elif totalCaratWeight < 30:
    settingPrice = 5.0 * diamondAmount
  else: # totalCaratWeight >= 30
    settingPrice = 3.5 * diamondAmount
    
  totalPrice = totalGoldPrice + totalDesignPrice + settingPrice
  
  return totalPrice

main(False)