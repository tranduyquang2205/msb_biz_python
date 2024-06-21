from msb import MSB
import json

msb = MSB('CHECKER-ANVIET', 'Abc1231@', '80000012888')

#OTP is required first login only, then youn can call action without it after login
login = msb.doLogin()
print(login)

balance = msb.getlistAccount()
print(balance)
        
# OTP is required first login only, then youn can call action without it after login
result = msb.getHistories("13/05/2024", "31/05/2024", '80000012888', 1,100)
print((result))
# account_number="1047889848"
# amount="50000"
# message="123"
# result = msb.createTranferInMSB(account_number, amount, message)
# print((result))