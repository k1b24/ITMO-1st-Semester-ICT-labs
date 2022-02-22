inputS = input()
checkInput = False
alphabet = {'0', '1'}
inputSet = set(inputS)
if (inputSet == alphabet or inputSet == {'0'} or inputSet == {'1'}) and len(inputS) == 7:
    checkInput = True
while not(checkInput):
    print('Введите набор из 7 цифр 0 и 1')
    inputS = input()
    inputSet = set(inputS)
    if (inputSet == alphabet or inputSet == {'0'} or inputSet == {'1'}) and len(inputS) == 7:
        checkInput = True
code = {
    'r1': int(inputS[0]), 'r2': int(inputS[1]), 'i1': int(inputS[2]), 'r3': int(inputS[3]), 'i2': int(inputS[4]), 'i3': int(inputS[5]), 'i4': int(inputS[6])
}
rezultR = [ (code['i1'] + code['i2'] + code['i4']) % 2, 
           (code['i1'] + code['i3'] + code['i4']) % 2, 
           (code['i2'] + code['i3'] + code['i4']) % 2 ]
syndromes = [ (rezultR[0] + code['r1']) % 2, 
             (rezultR[1] + code['r2']) % 2, 
             (rezultR[2] + code['r3']) % 2 ]
syndrome = str(syndromes[0]) + str(syndromes[1]) + str(syndromes[2])
errorBit = {
    '001': 'r3', '010': 'r2', '011': 'i3', '100': 'r1', '101': 'i2', '110': 'i1', '111': 'i4'
}
if syndrome != '000':
    code[errorBit[syndrome]] = (code[errorBit[syndrome]] + 1) % 2 
    print('Ошибочный бит - ', errorBit[syndrome])
else:
    print('Последовательность не содержит ошибок')
answerString = str(code['i1']) + str(code['i2']) + str(code['i3']) + str(code['i4'])
print('Правильная последовательность информационных разрядов - ', answerString)