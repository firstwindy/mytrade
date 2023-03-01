import time
import pyupbit
import datetime
import log
import threading
import queue

access = "my"
secret = "my"
interval = "minute240"
ticker = "KRW-BTC"

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval, count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval, count=1)
    start_time = df.index[0]
    return start_time

def get_ma(ticker, bars):
    """이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval, count=bars)
    ma = df['close'].rolling(bars).mean().iloc[-1]
    return ma

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker)["orderbook_units"][0]["ask_price"]



# ###################################################################################

logger = log.logger_console()
logger.info("###################################################################################")
logger.info("## START")
logger.info("###################################################################################")

# 로그인
upbit = pyupbit.Upbit(access, secret)
logger.info("Success login")
tradeON = True
start_time = None

# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        
        #print( datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        #### bar 기준 거래 시작
        if start_time !=None and start_time < now < end_time - datetime.timedelta(seconds=5):
            logger.info('=============================================================================================')
            logger.info("## " + now.strftime('%Y-%m-%d %H:%M:%S') )
            logger.info("=============================================================================================")
            logger.info(" - start_time: "+ start_time.strftime('%Y-%m-%d %H:%M:%S') )
            logger.info(" -   end_time: "+ end_time.strftime('%Y-%m-%d %H:%M:%S') )
            logger.info(" - Condition : " + str(tradeON) )
            
            if not tradeON :
                logger.info('=============================================================================================')
                logger.info("")
                logger.info("")
                time.sleep(1)
                continue


            target_price = get_target_price(ticker, 0.5)
            ma20 = get_ma(ticker,20)
            ma200 = get_ma(ticker,200)
            current_price = get_current_price(ticker)
        
            
            #### 조건 일치시 매수 거래시간동안 한번만 거래, 마감때 거래 가능으로 변경
            #if True:
            if current_price > target_price > ma20 > ma200:
                krw = upbit.get_balance("KRW")
                if krw > 5000:
                    logger.info(" --------------------------------------------------------------------------------------------")
                    logger.info(" -- Start Buy : "+now.strftime('%Y-%m-%d %H:%M:%S') )
                    logger.info(" --    매수금액: "+ str(krw) )
                    logger.info(" --------------------------------------------------------------------------------------------")
                    logger.info("    -- current_price: " + str(current_price))
                    logger.info("    --  target_price: " + str(target_price))
                    logger.info("    --          ma20: " + str(ma20))
                    logger.info("    --         ma200: " + str(ma200),flush=True)
                    #upbit.buy_market_order("KRW-BTC", krw*0.9995)
                    logger.info("  -- END Buy --------------------- ")
                else:
                    logger.info(" - 잔액부족",flush=True)
                ### 매수 or 매수 실패 후 trade false 로 해당 bar trade 종료    
                tradeON = False
                logger.info(" - Condition : " + str(tradeON) )
             
        #### bar 마감
        else:
            logger.info('=============================================================================================')
            logger.info("## " + now.strftime('%Y-%m-%d %H:%M:%S') )
            logger.info("=============================================================================================")
            logger.info(" - Condition : " + str(tradeON) )        
            logger.info( upbit.get_balance("BTC") )       
            btc = upbit.get_balance("BTC")
            if btc != None and btc > 0.00008:
                before_btc = btc
                #upbit.sell_market_order("KRW-BTC", btc)
                after_btc = upbit.get_balance("BTC")
                krw = upbit.get_balance("KRW")
                logger.info("  - BTC 매도: "+ str(before_btc) )
                logger.info("  - BTC 잔량: "+ str(after_btc) )
                logger.info("  - KRW 잔고: "+ str(krw) )
                logger.info("  -- END Sell >>>> ")
            logger.info("")
            tradeON = True
            logger.info("  ------------------------------------------------------------------------------------------")
            logger.info("  - trade END: "+now.strftime('%Y-%m-%d %H:%M:%S'))
            ## 시간 재설정
            start_time = get_start_time("KRW-BTC")
            end_time = start_time + datetime.timedelta(hours=4)

        logger.info('=============================================================================================')
        logger.info("")
        logger.info("")
        time.sleep(1)
    except Exception as e:
        logger.debug(e)
        time.sleep(1)



