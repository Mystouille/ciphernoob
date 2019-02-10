import numpy as np
from ortools.linear_solver import pywraplp

#params
#numberList: the list of numbers
#target: the total sum we want to get as close as possible
def solve(numberList, target):
  solver = pywraplp.Solver('SolveIntegerProblem', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
  
  varList = []
  objective = solver.Objective()
  absVar = solver.NumVar(-50, 50, 'R')

  constPos1 = solver.Constraint(-solver.infinity(), float(target))
  constPos2 = solver.Constraint(-solver.infinity(), -float(target))
  constPos1.SetCoefficient(absVar, -1)
  constPos2.SetCoefficient(absVar, -1)
  #absVar >= sum(Xi*Ki)-target
  #absVar >= -(sum(Xi*Ki)-target)
  for idx, number in enumerate(numberList):
    numberFloat = float(number)
    newVar = solver.BoolVar('X'+str(idx))
    varList.append((newVar,idx,numberFloat))
    constPos1.SetCoefficient(newVar, numberFloat)
    constPos2.SetCoefficient(newVar, -numberFloat)

  objective = solver.Objective()
  objective.SetCoefficient(absVar, 1)
  objective.SetMinimization()
  solver.Solve()
  total = np.float(0)
  nbNumberUsed = 0
  idxList=[]
  for (var, idx, number) in varList:
    if var.solution_value():
      total += number
      nbNumberUsed+=1
      idxList.append(1)
    else:
      idxList.append(0)
  diff = np.abs(total-float(target))
  #print('target: '+str(target))
  #print('reached: '+str(total)+' with '+str(nbNumberUsed)+' numbers')
  #print('diff: '+str(diff))
  solver.Clear()  
  return (idxList, nbNumberUsed, diff)