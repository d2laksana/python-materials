'''
TODO: Program BMI Calculator
'''


def getBMI(tb, bb):
    tb_meter = tb / 100
    tb_square = tb_meter * tb_meter

    # Hitung bmi
    bmi = bb / tb_square

    return bmi


def getResiko(bmi):
    if bmi >= 18.5 and bmi <= 25.0:
        return "Normal"
    elif bmi > 25.0 and bmi <= 30.0:
        return "Average"
    elif bmi > 30 and bmi <= 40:
        return "Important"
    elif bmi > 40:
        return "Severe"


# Input
berat_badan = float(input("Input berat badan (kg) : "))
tinggi_badan = float(input("Input tinggi badan (cm) : "))

# Cetak BMI
print("BMI =", getBMI(tinggi_badan, berat_badan))

# cetak Resiko kesehatan
print("Resiko kesehatan =", getResiko(getBMI(tinggi_badan, berat_badan)))
