ss=['01010100','01010101','01010110'] #encoded message


from bitstring import BitArray,BitStream
print('write it to file')
with open('binary.bin','wb') as f:
    s=''.join(ss);
    b=BitArray(bin=s)                 
    f.write(b.tobytes())# thanks to Scott, tobytes() method is very useful

print('read it to file')
b=BitArray(filename='binary.bin')
print(b.bin)