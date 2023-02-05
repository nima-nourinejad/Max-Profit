def mpr(l):
  n=len (l)
  pr=[]
  for i in range(n):
    for j in range(n):
      if j>i:
        pr.append([(l[j]-l[i]), i, j])
    upr=pr[0]
    npr=len (pr)
    for k in range(npr):
      if pr[k][0]>upr[0]:
        upr=pr[k]
      if pr[k][0]==upr[0]:
        if (pr[k][2]-pr[k][1])<(upr[2]-upr[1]):
          upr=pr[k]
  return upr
