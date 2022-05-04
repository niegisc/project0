# denary to binary
def dec2bin(dnum):
  result = ''
  while dnum != 0: # loop while quotient is non-zero ie can still divide
    remainder = dnum % 2 # divide and get remainder
    dnum = dnum // 2 # reduce the number by 2
    result = str(remainder) + result # add to front of result
  return result

# denary to hexadecimal
def dec2hex(dnum):
  hex_map = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', \
             9:'1', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
  result = ''
  while dnum != 0:
    remainder = dnum % 16
    dnum = dnum // 16
    result = hex_map[remainder] + result
  return result

# main
print(dec2bin(23))
print(dec2bin(28))
print(dec2hex(23))
print(dec2hex(28))
