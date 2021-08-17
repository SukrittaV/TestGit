# ราคา BTC ล่าสุด
from forex_python.bitcoin import BtcConverter
b = BtcConverter()
bitCoinTHB = b.get_latest_price('THB')
print('BTC price :',bitCoinTHB,'THB')

# ถ้า BTC > THB +2% = ขาย BTC
# ถ้า BTC < THB -2% = ซื้อ BTC
percentage = 2

THB_Value = 100000000  # มูลค่าเงินบาทที่มี
btc_balance = 0.0001  # จำนวนเหรียญ BTC ที่มี
btc_Value = bitCoinTHB * btc_balance  # มูลค่า BTC ที่มี
fix_Value = 50  # % ที่จะ re-balance
if btc_Value > (fix_Value * (1+(percentage/100))):  # * (1+(percentage/100)))
    amount = btc_Value - fix_Value
    print(f'Sell BTC {amount} THB')
elif btc_Value < (fix_Value * (1+(percentage/100))):
    amount = fix_Value - btc_Value
    print(f'Buy BTC {amount} THB')
else:
    print('wait . . .')



