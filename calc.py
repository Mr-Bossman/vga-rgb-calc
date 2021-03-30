
def r2rTotal(i):
        if not i:
            return 1
        return 1/(1 + 1/(r2rTotal(i - 1)+0.5))

R = 1000
Vin = 1
Vout = .7
for x in range(0,5):
    print("Rcalc " + str(-(r2rTotal(x)*1000*Vout)/(Vout - Vin)))


