# s = "今晚" # 2字。=》 utf-8 => 6byte
# # bs = s.encode('utf-8') # 编码
# # # bytes
# # # b''  英文没有变换
# # # b'\xe4\xbb\x8a\xe6\x99\x9a' # 6个\x
# # print(bs)
# print(s.encode("GBK"))

# 'utf-8' codec can't decode byte 0xbd in position 0: invalid start byte
bs = b'\xbd\xf1\xcd\xed'
s = bs.decode("gbk")
print(s)

