import numpy as np

def decode (string):

    lenString = float(len(string))

    # Find coincidence vector while looping in j == j+1. If it is equal we add
    # one in the coincidence vector. The position with the biggest coincidence
    # value is the size of the key.
    coincidences = [0]
    for i in range(1, len(string)):
            coincidences.append(0)
            for j in range(0, len(string)):
                if(string[j] == string[(j+i)%len(string)]):
                    coincidences[i] += 1

    keylength = coincidences.index(max(coincidences))
    print('Key Length: %d' % keylength)

    # Letter frequency in english language
    letterFrequency = [
        8.167, 1.492, 2.782, 4.253, 12.702, 2.015, 6.094, 2.228, 6.966, 0.153,
        0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056,
        2.758, 0.978, 2.360, 0.150, 1.974, 0.074
    ]

    key = ''
    # We need to find a character for each poisition in the key
    for i in range(0, keylength):
        # Here we are reseting the values
        textFrequency = {}
        maxValue = -1
        maxPosition = 0
        rolledArray = letterFrequency

        # For each character in the alphabet we need to find the biggest sum value
        # while alling it to some letter.
        for j in range(0, 26):
            if(j > 0):
                rolledArray = np.roll(rolledArray, 1)

            for k in range(0, 26):
                textFrequency[chr(k + 97)] = 0

            # Find the frequency of the positions in the key. We loop through the
            # string using the keylength and start at the position we want to find
            # the character for
            k = i;
            while(k < lenString):
                letter = string[k]
                textFrequency[letter] += 1/lenString * 100
                k += keylength;

            # Sum the values of textFrequency * rolledArray
            sumValues = 0;
            for k in range(0, 26):
                sumValues += textFrequency[chr(k + 97)] * rolledArray[k];

            # The biggest value wins
            if(sumValues > maxValue):
                maxValue = sumValues
                maxPosition = j

        # Since we loop for all the alphabet we know who is the owner of the biggest sum,
        # so we found one character of our key
        key += chr(maxPosition + 97)

    keyAsInt = [ord(i) for i in key]
    cipherAsInt = [ord(i) for i in string]
    plainText = ''

    # We have the key now we just need to decipher it! :)
    for i in range(0, int(lenString)):
        value = (cipherAsInt[i] - keyAsInt[i % keylength]) % 26
        plainText += chr(value + 97)

    print('Key: %s\n' % key)
    print('Decipher key: %s' % plainText)

decode('ocwyikoooniwugpmxwktzdwgtssayjzwyemdlbnqaaavsuwdvbrflauplooubfgqhgcscmgzlatoedcsdeidpbhtmuovpiekifpimfnoamvlpqfxejsmxmpgkccaykwfzpyuavtelwhrhmwkbbvgtguvtefjlodfefkvpxsgrsorvgtajbsauhzrzalkwuowhgedefnswmrciwcpaaavogpdnfpktdbalsisurlnpsjyeatcuceesohhdarkhwotikbroqrdfmzghgucebvgwcdqxgpbgqwlpbdaylooqdmuhbdqgmyweuik')
