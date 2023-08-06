from sqlite3 import connect
from datetime import datetime, timedelta, date

from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame


class HistoricDataClient:

    def __init__(self, key, secret, ledger="./ledger.db", cryptocurrency=True):
        CryptoSelection_SQL = "SELECT name FROM tracked_symbols WHERE type='crypto'"
        StocksSelection_SQL = "SELECT name FROM tracked_symbols WHERE type='stocks'"
        testSymbolTable_SQL = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}';"
        createSymbolTable_SQL = ("CREATE TABLE IF NOT EXISTS {}("\
                                                    "high REAL UNIQUE, "\
                                                    "low REAL UNIQUE, "\
                                                    "open REAL UNIQUE, "\
                                                    "close REAL UNIQUE, "\
                                                    "time REAL UNIQUE)" )

        self.key = key
        self.secret = secret
        self.ledger = ledger
        connection = connect(self.ledger)
        cursor = connection.cursor()

        if cryptocurrency: cursor.execute(CryptoSelection_SQL)
        else: cursor.execute(StocksSelection_SQL)
        self.AssetSymbolWatchlist = cursor.fetchall()

        for symbol in self.AssetSymbolWatchlist:
            if len(execute(testSymbolTable_SQL.format(symbol)).fetchall()) <= 0:
                cusor.execute(createSymbolTable_SQL.format(symbol))
                connection.commit()


    def BuildLedger(self, cmdline=False):

        insertSymbolData_SQL = ("INSERT OR REPLACE INTO {} "\
                                "(high, low, open, close, time) "
                                "VALUES(?, ?, ?, ?, ?);")

        # Future command-line functionality.
        if cmdline: pass
        else: pass

        connection.connect(self.ledger); cursor = connection.cursor()
        for symbol in self.AssetSymbolWatchlist:

            # Define start & end boundaries for requests; to stay within limits.
            _start = "2015-12-01"; _end = datetime.now() - timedelta(minutes=30)


            # Begin working on start date as datetime object and step from then to now.
            START = datetime.strptime(_start, "%Y-%m-%d")
            while START < _end:

                # Ensure that stock market requests don't begin on a weekend!!
                if self.cryptocurrency is False:
                    while date.weekday(START) >= 5:
                        START = START + timedelta(days=1)

                # Batch requests so we don't hog all the memory. ;)
                END = START + timedelta(days=120)
                if END > _end: END = _end

                # Call the proper data client; stocks vs crypto.
                if self.cyptocurrency:
                    data_client = CryptoHistoricalDataClient(self.key, self.secret)
                    parameters = CryptoBarsRequest( symbol_or_symbols=symbol,
                                                    timeframe=TimeFrame.Minute,
                                                    start=START,
                                                    end=END                    )
                    HistoricData =\
                        data_client.get_crypto_bars(parameters)

                else:
                    data_client = StockHistoricalDataClient(self.key, self.secret)
                    parameters = StockBarsRequest( symbol_or_symbols=symbol,
                                                   timeframe=TimeFrame.Minute,
                                                   start=START,
                                                   end=END                    )
                    HistoricData =\
                        data_client.get_stock_bars(parameters)

                # Read through the requested data and write each line to the symbols table.
                for line in HistoricData[symbol]:
                    time = datetime.timestamp(line.timestamp)
                    data = (line.high, line.low, line.open, line.close, time)
                    cursor.execute(insertSymbolData_SQL.format(symbol), data)
                    connection.commit()
                
                START = END
                sleep(5)

            return True


#class LiveDataClient: