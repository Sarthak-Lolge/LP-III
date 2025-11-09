# pr3


class Item:
  def __init__(self,value,weight):
    self.value = value
    self.weight = weight

def fractionalKnapSack(capacity,arr):
  arr.sort(key = lambda x:(x.value/x.weight), reverse = True)
  finalValue = 0.0
  
  for item in arr:
    if item.weight < capacity:
      capacity = capacity - item.weight
      finalValue = finalValue + item.value
    
    else:
      finalValue = (finalValue+item.value) * (capacity / item.weight)
    
    return finalValue
    
  
if __name__ == '__main__':
    capacity = 50
    arr = [Item(60,10), Item(100,20), Item(120,30)]
    result = fractionalKnapSack(capacity,arr)
    print(result)
    
