1. Use!
2. import pandas as pd
3. import Syndenv
4. from Syndenv import Syndbox
5. df=pd.read_excel('/content/filename.xlsx')
6. df1=Syndbox.TESI(df, Equation='Euc_p1', start=0.01, augmentation_factor=10)
7.                             
8. df1.pd_frame(save=True)
9. df1.arr()
10. 
11. 
12. Parameters 
13. start: (float): default=0.01: The starting value of the angle sequence.
14. stop: (int): default=1: The end value of the angle's sines vector. Should be always 1 because the angle's max sine is 1. 
15. augmentation_factor: (int): default (0.01): The number of times the data is augmented. Should be from 0 to infinity.
16. Equation: default='Euc_p1': Either the Euclidean or the following transformed Euclidean formulas.

17. 'Euc_p1': The linear polynomial.
18. 'Euc_p2': The quadratic polynomial.
19. 'Euc_p3': The cubic polynomial.
20. 'Euc_Log': The log-transformed euclidian formula.


 
 
 
