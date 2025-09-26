# -*- coding: utf-8 -*-
"""

Sammenligning av årlige totalkostnader for elbil vs bensinbil
Lise Brændshøi (lisebrandshoi@gmail.com)
Oppdatert 26.09.2025

"""

#%% Forutsetninger like for begge biler
K = 20000  # [enhet kjørte km pr år]
TF = 8.38*365  # [årlig trafikkforsikringsavgift]


#%% Elbil
FE = 5000  # [årlig forsikringspremie elbil]
DE = 0.2*2  # [kostnad forbruk 0.2 kwh/km * 2 kr/kwh)]
BE = 0.1  # [bomavgift kr/km]


#%% Bensinbil
FB = 7500  # [årlig forsikringspremie bensinbil]
DB = 1  # [drivstoff kr/km]
BB = 0.3  # [bomavgift kr/km]


#%% Sammenligning av årlige kostnader 
TotE = FE + TF + (DE*K) + (BE*K)
TotB = FB + TF + (DB*K) + (BB*K)

print ('Totale årlige kostnader for elbil er', TotE,'kr')
print ('Totale årlige kostnader for bensinbil er', TotB, 'kr')
print ('Det vil koste', TotB - TotE,'kr mer per år ved å velge bensinbil i stedet for elbil')


