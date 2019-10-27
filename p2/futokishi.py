from __future__ import print_function
from ortools.sat.python import cp_model


def main():
    fuku = open("fuku.txt")
    satırsayısı = 0
    while (fuku.readline()) :
        satırsayısı = satırsayısı + 1
        
    fuku.close()


    model = cp_model.CpModel()
       
    A1 = model.NewIntVar(1, 4, 'A1')
    A2 = model.NewIntVar(1, 4, 'A2')
    A3 = model.NewIntVar(1, 4, 'A3')
    A4 = model.NewIntVar(1, 4, 'A4')
    B1 = model.NewIntVar(1, 4, 'B1')
    B2 = model.NewIntVar(1, 4, 'B2')
    B3 = model.NewIntVar(1, 4, 'B3')
    B4 = model.NewIntVar(1, 4, 'B4')
    C1 = model.NewIntVar(1, 4, 'C1')
    C2 = model.NewIntVar(1, 4, 'C2')
    C3 = model.NewIntVar(1, 4, 'C3')
    C4 = model.NewIntVar(1, 4, 'C4')
    D1 = model.NewIntVar(1, 4, 'D1')
    D2 = model.NewIntVar(1, 4, 'D2')
    D3 = model.NewIntVar(1, 4, 'D3')
    D4 = model.NewIntVar(1, 4, 'D4')
    

    
    model.Add(A1 != A2)
    model.Add(A1 != A3)
    model.Add(A1 != A4)
    model.Add(A2 != A3)
    model.Add(A2 != A4)
    model.Add(A3 != A4)
    model.Add(B1 != B2)
    model.Add(B1 != B3)
    model.Add(B1 != B4)
    model.Add(B2 != B3)
    model.Add(B2 != B4)
    model.Add(B3 != B4)
    model.Add(C1 != C2)
    model.Add(C1 != C3)
    model.Add(C1 != C4)
    model.Add(C2 != C3)
    model.Add(C2 != C4)
    model.Add(C3 != C4)
    model.Add(D1 != D2)
    model.Add(D1 != D3)
    model.Add(D1 != D4)
    model.Add(D2 != D3)
    model.Add(D2 != D4)
    model.Add(D3 != D4)
    model.Add(A1 != B1)
    model.Add(A1 != C1)
    model.Add(A1 != D1)
    model.Add(B1 != C1)
    model.Add(B1 != D1)
    model.Add(C1 != D1)
    model.Add(A2 != B2)
    model.Add(A2 != C2)
    model.Add(A2 != D2)
    model.Add(B2 != C2)
    model.Add(B2 != D2)
    model.Add(C2 != D2)
    model.Add(A3 != B3)
    model.Add(A3 != C3)
    model.Add(A3 != D3)
    model.Add(B3 != C3)
    model.Add(B3 != D3)
    model.Add(C3 != D3)
    model.Add(A4 != B4)
    model.Add(A4 != C4)
    model.Add(A4 != D4)
    model.Add(B4 != C4)
    model.Add(B4 != D4)
    model.Add(C4 != D4)
    fuku = open("fuku.txt")
    for i in range(0,satırsayısı):
        deger = fuku.readline()
        deger2 = deger.split(',')
    
        try:
            deger2[0] = model.NewIntVar(int(deger2[1]),int(deger2[1]),str(deger2[0]))
            
        except ValueError :
            
            model.Add((deger2[0]) > (deger2[1]))
    
    
    
    model.Maximize(A1 and B1 and C1 and D1 and A2 and A3 and A4 and B2 and B3 and B4 and C2 and C3 and C4 and D2 and D3 and D4)
    

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        print('x = ',solver.Value(A1),' y = ',solver.Value(A2),' z = ',solver.Value(A3),' t = ',solver.Value(A4))
        print('a = ',solver.Value(B1),' b = ',solver.Value(B2),' c = ',solver.Value(B3),' d = ',solver.Value(B4))
        print('e = ',solver.Value(C1),' f = ',solver.Value(C2),' g = ',solver.Value(C3),' h = ',solver.Value(C4))
        print('j = ',solver.Value(D1),' k = ',solver.Value(D2),' l = ',solver.Value(D3),' m = ',solver.Value(D4))
        
    
    

if __name__ == '__main__':
  main()   
   
