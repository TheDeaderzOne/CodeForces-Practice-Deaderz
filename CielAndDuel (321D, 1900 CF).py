import sys
input = sys.stdin.readline
output = sys.stdout.write
AttackCards = []; DefenseCards = []; GeneralPurpose = [0]*8000; GeneralPurposeNum = []

JiroPunchingBag,CielAttacker = [int(x) for x in input().replace("\n","").split()]

for _ in range(JiroPunchingBag):
    listy = input().replace("\n","").split()
    if listy[0] == "ATK":
        AttackCards.append(int(listy[1]))
    else:
        DefenseCards.append(int(listy[1]))

for _ in range(CielAttacker):
    tex = int(input().replace("\n",""))
    GeneralPurpose[tex-1]+=1
    GeneralPurposeNum.append(tex)

AttackCards.sort(reverse=True); DefenseCards.sort(); GeneralPurposeNum.sort()

def AllAttack(CielCardsArr, JiroAttackArr):
    Damage = 0
    CielPointer = len(CielCardsArr)-1
    JiroPointer = len(JiroAttackArr)-1
    while JiroPointer > -1 and CielPointer>-1:
        if CielCardsArr[CielPointer]-JiroAttackArr[JiroPointer] > 0:
            Damage+=(CielCardsArr[CielPointer]-JiroAttackArr[JiroPointer])
        JiroPointer-=1
        CielPointer-=1
    Damage = max(Damage,0)
    return Damage

def SemiAttack(CielCardsArr, JiroAttackArr, LongArr,damage):
    JiroAttackArr.sort()
    for j in range(len(JiroAttackArr)):
        leftpointer = JiroAttackArr[j]-1
        initial = int(leftpointer)
        while leftpointer<=len(LongArr)-1:
            if LongArr[leftpointer]>0:
                LongArr[leftpointer]-=1
                CielCardsArr.remove(leftpointer+1)
                damage += (leftpointer)-initial
                break
            else:
                leftpointer+=1
                if leftpointer==len(LongArr):
                    return 0          
    for x in CielCardsArr:
        damage+=x
    return damage

def AllDefense(CielCardsArr, JiroAttackArr,JiroDefenseArr, LongArr):
    damagetaken = 0
    for p in range(len(JiroDefenseArr)):
        temppointer = JiroDefenseArr[p]-1
        inity = int(temppointer)
        while temppointer<=len(LongArr)-1:
            if LongArr[temppointer]>0 and temppointer!=inity:
                LongArr[temppointer]-=1
                CielCardsArr.remove(temppointer+1)
                break
            else:
                temppointer+=1
                if temppointer==len(LongArr):
                    return 0
    return SemiAttack(CielCardsArr,JiroAttackArr,LongArr,damagetaken)


if len(DefenseCards)==0:
    dam = 0
    if len(GeneralPurposeNum)> len(AttackCards)+len(DefenseCards):
        bruiser = AllAttack(GeneralPurposeNum,AttackCards)
        finalans = max(bruiser,SemiAttack(GeneralPurposeNum,AttackCards,GeneralPurpose,dam))
        
    else:
        finalans = AllAttack(GeneralPurposeNum,AttackCards)
else:
    if len(GeneralPurposeNum)> len(AttackCards)+len(DefenseCards):
        holder = AllAttack(GeneralPurposeNum,AttackCards)
        finalans = max(holder,AllDefense(GeneralPurposeNum,AttackCards,DefenseCards,GeneralPurpose))
    else:
        finalans = AllAttack(GeneralPurposeNum,AttackCards)

output(str(finalans)+"\n")