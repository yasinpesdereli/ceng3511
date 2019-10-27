from __future__ import print_function
from ortools.sat.python import cp_model
kakuro = open("kakuro_input.txt")
satırtoplam =kakuro.readline()
a = satırtoplam.split(',')
st1 = int(a[0])             ##---- st1   st2    st3
st2 = int(a[1])             ## sut1 a1-x    a2-y    a3-z
st3 = int(a[2])             ## sut2 a4-a    a5-b    a6-c
                            ## sut3 a7-d    a8-e    a9-f
sutuntoplam = kakuro.readline()
b = sutuntoplam.split(',')

sut1 = int(b[0])
sut2 = int(b[1])
sut3 = int(b[2])

def main():
  model = cp_model.CpModel()
  
  a1 = model.NewIntVar(1, 9, 'a1')
  a2 = model.NewIntVar(1, 9, 'a2')
  a3 = model.NewIntVar(1, 9, 'a3')
  a4 = model.NewIntVar(1, 9, 'a4')
  a5 = model.NewIntVar(1, 9, 'a5')
  a6 = model.NewIntVar(1, 9, 'a6')
  a7 = model.NewIntVar(1, 9, 'a7')
  a8 = model.NewIntVar(1, 9, 'a8')
  a9 = model.NewIntVar(1, 9, 'a9')

  model.Add(a7 != a8)
  model.Add(a7 != a9)
  model.Add(a8 != a9)
  model.Add(a1 != a2)
  model.Add(a1 != a3)
  model.Add(a2 != a3)
  model.Add(a4 != a5)
  model.Add(a4 != a6)
  model.Add(a5 != a6)
  model.Add(a1 != a4)
  model.Add(a1 != a7)
  model.Add(a4 != a7)
  model.Add(a2 != a5)
  model.Add(a2 != a8)
  model.Add(a5 != a8)
  model.Add(a3 != a6)
  model.Add(a3 != a9)
  model.Add(a6 != a9)
  model.Add(a1 + a2 + a3 == sut1 )
  model.Add(a4 + a5 + a6 == sut2 )
  model.Add(a7 + a8 + a9 == sut3)
  model.Add(a1 + a4 + a7 == st1 )
  model.Add(a2 + a5 + a8 == st2 )
  model.Add(a3 + a6 + a9 == st3 )
    
  model.Maximize(a1 + a2 + a3)
  model.Maximize(a4 + a5 + a6)
  model.Maximize(a7 + a8 + a9)
  model.Maximize(a1 + a4 + a7)
  model.Maximize(a2 + a5 + a8)
  model.Maximize(a3 + a6 + a9)

  solver = cp_model.CpSolver()
  status = solver.Solve(model)
  kakuro.close()
  f = open("kakuro_output.txt" , "w")
  yazı = 'x', st1 , st2 , st3 
  f.write(str(yazı))
  f.write('\n')
  yazı2 = sut1 , solver.Value(a1) , solver.Value(a2) , solver.Value(a3)
  f.write(str(yazı2))
  f.write('\n')
  yazı3 = sut2 , solver.Value(a4) , solver.Value(a5) , solver.Value(a6)
  f.write(str(yazı3))
  f.write('\n')
  yazı4 = sut3 , solver.Value(a7) , solver.Value(a8) , solver.Value(a9)
  f.close()

  
    
if __name__ == '__main__':
  main()
