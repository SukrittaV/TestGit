# ราคา BTC ล่าสุด
def ShowBTCPrice():
    from forex_python.bitcoin import BtcConverter
    b = BtcConverter()
    bitCoinTHB = b.get_latest_price('THB')
    print('BTC price :',bitCoinTHB,'THB')

# ถ้า BTC > THB +2% = ขาย BTC
# ถ้า BTC < THB -2% = ซื้อ BTC
def rebalance():
    from forex_python.bitcoin import BtcConverter
    b = BtcConverter()
    bitCoinTHB = b.get_latest_price('THB')
    percentage = 2  # % ที่จะ re-balance
    thb_Value = float(input('THB balance :'))  # มูลค่าเงินบาทที่มี
    btc_balance = float(input('BTC balance[Coin] : '))  # จำนวนเหรียญ BTC ที่มี
    btc_Value = bitCoinTHB * btc_balance  # มูลค่า BTC ที่มี
    print('BTC balance [value]', btc_Value)
    fix_Value = (btc_Value + thb_Value)/2 # มูลค่าส่วนต่างของ 2 asset
    print('fix value :',fix_Value)
    #print('fix value percentage :',fix_Value * (1+(percentage/100)))
    # ขายออก
    if btc_Value > (fix_Value * (1+(percentage/100))):  # * (1+(percentage/100)))
        amount = btc_Value - fix_Value
        #print(f'{btc_Value} > {(fix_Value * (1+(percentage/100)))}') check ค่าส่วนต่างถูกต้อง = ต้องมากกว่า 2%
        print(f'Sell BTC {amount} THB')
    # ซื้อเข้า
    elif btc_Value < (fix_Value * (1-(percentage/100))):
        amount = fix_Value - btc_Value
        #print(f'{btc_Value} < {(fix_Value * (1 + (percentage / 100)))}') check ค่าส่วนต่างถูกต้อง = ต้องน้อยกว่า 2%
        print(f'Buy BTC {amount} THB')
    else:
        print(f'wait . . . ยังไม่ถึง{percentage} percentage')

ShowBTCPrice()
rebalance()



