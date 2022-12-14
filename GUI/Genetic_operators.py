from operator import indexOf
import random

class OP:
  def __init__(self, chro, maxFit):
      self.chromosome = chro
      self.maxFitness = maxFit
  
  def __eq__(self, other):
      return self.chromosome == other.chromosome and self.maxFitness == other.maxFitness
    
  def fitness(self, chromosome, maxFitness):
      horizontal_collisions = (
          sum([self.chromosome.count(queen) - 1 for queen in self.chromosome]) / 2
      )
      diagonal_collisions = 0
      n = len(self.chromosome)
      left_diagonal = [0] * (2 * n - 1)
      right_diagonal = [0] * (2 * n - 1)
      for i in range(n):
          left_diagonal[i + self.chromosome[i] - 1] += 1
          right_diagonal[len(self.chromosome) - i + self.chromosome[i] - 2] += 1
      diagonal_collisions = 0
      for i in range(2 * n - 1):
          counter = 0
          if left_diagonal[i] > 1:
              counter += left_diagonal[i] - 1
          if right_diagonal[i] > 1:
              counter += right_diagonal[i] - 1
          diagonal_collisions += counter
      # 28-(2+3)=23
      return int(self.maxFitness - (horizontal_collisions + diagonal_collisions))
