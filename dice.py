import random

class Dice:
  def throw(self, sides):
    num = random.randint(1,sides)
    return num

def rungame(sides):
  dice = Dice()
  if sides == 6:
    result = dice.throw(6) + dice.throw(6)
  else:
    result = dice.throw(12)
  return result

num_of_rounds = 500
results1 = [0] * 13
results2 = [0] * 13

if __name__ == '__main__':

  for round in range(0,num_of_rounds):
     result = rungame(6)     
     results1[result] = results1[result] + 1
     result = rungame(12)     
     results2[result] = results2[result] + 1
  for i in range(2, 13):
     print i, results1[i]*'|'
  print "################################################"
  for i in range(2, 13):
     print i, results2[i]*'|'
