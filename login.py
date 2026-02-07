degree = True
percentage = 86
skills = ['java', 'powerbi', 'tensorflow', 'PHP']
notice = 9
ctc = 8
def screening():
    print("talking to the person")
def technical_round():
    print("evaluating technical skills")   
def hr_round():
    print("Discussing the pay")

if degree and percentage >70:
    screening()
    if 'java' in skills and 'PHP' in skills:
        technical_round()
        if notice <10 and ctc < 10:
            hr_round()
            print("congrats you're appointed")
