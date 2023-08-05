import re
import typing as t
from datetime import datetime, timezone
from decimal import Decimal
from backintime.data.data_provider import DataProvider
from backintime.broker.base import TradeInfo, OrderInfo
from .stats import Stats, TradeProfit, get_stats
from .csv import export_stats, export_orders, export_trades


class BacktestingStats:
    def __init__(self, 
                 strategy_title: str,
                 data_provider: DataProvider,
                 date: datetime,
                 stats: Stats):
        self._strategy_title = strategy_title
        self._data_title = data_provider.title
        self._data_timeframe = data_provider.timeframe
        self._data_since = data_provider.since
        self._data_until = data_provider.until
        self._symbol = data_provider.symbol
        self._date = date
        self._stats = stats

    @property
    def strategy_title(self) -> str:
        return self._strategy_title

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def algorithm(self) -> str:
        return self._stats.algorithm

    @property
    def average_profit(self) -> Decimal:
        return self._stats.average_profit

    @property
    def profit_loss_ratio(self) -> Decimal:
        return self._stats.profit_loss_ratio

    @property
    def profit_factor(self) -> Decimal:
        return self._stats.profit_factor

    @property
    def win_rate(self) -> Decimal:
        return self._stats.win_rate

    @property
    def win_loss_ratio(self) -> Decimal:
        return self._stats.win_loss_ratio

    @property
    def wins_count(self) -> int:
        return self._stats.wins_count

    @property
    def losses_count(self) -> int:
        return self._stats.losses_count

    @property
    def average_profit_all(self) -> Decimal:
        """Average profit for all trades."""
        return self._stats.average_profit_all

    @property
    def average_profit_all_percents(self) -> Decimal:
        """Average profit for all trades in percents."""
        return self._stats.average_profit_all_percents

    @property
    def average_profit(self) -> Decimal:
        """Average profit for profit-making trades."""
        return self._stats.average_profit

    @property
    def average_profit_percents(self) -> Decimal:
        """Average profit for profit-making trades in percents."""
        return self._stats.average_profit_percents

    @property
    def average_loss(self) -> Decimal:
        """Average loss for loss-making trades."""
        return self._stats.average_loss

    @property
    def average_loss_percents(self) -> Decimal:
        """Average loss for loss-making trades in percents."""
        return self._stats.average_loss_percents

    @property
    def best_deal_relative(self) -> t.Optional[TradeProfit]:
        """Best deal by relative gain."""
        return self._stats.best_deal_relative

    @property
    def best_deal_absolute(self) -> t.Optional[TradeProfit]:
        """Best deal by absolute gain."""
        return self._stats.best_deal_absolute

    @property
    def worst_deal_relative(self) -> t.Optional[TradeProfit]:
        """Worst deal by relative loss."""
        return self._stats.worst_deal_relative

    @property
    def worst_deal_absolute(self) -> t.Optional[TradeProfit]:
        """Worst deal by absolute loss."""
        return self._stats.worst_deal_absolute

    def __repr__(self) -> str:
        date = datetime.strftime(self._date, "%Y-%m-%d %H:%M:%S")
        header_message = f"Backtesting stats {date}"
        header = f"\n{'-' * 16}* {header_message} *{'-' * 16}\n\n"
        footer = f"\n{'-' * 73}\n"
        data_block = (f"{self._data_title} on {str(self._data_timeframe)}\n"
                      f"since: {self._data_since}\n"
                      f"until: {self._data_until}\n"
                      f"trading pair: {self._symbol}\n\n")

        return (f"{header}{data_block}"
                f"Strategy title: {self._strategy_title}\n"
                f"{repr(self._stats)}{footer}")


class BacktestingResult:
    """
    Represents backtesting result.

    Stats such as Win Rate, Profit/Loss, Average Profit
    can be obtained by calling `get_stats` method, which
    supports estimation in FIFO (First-In-First-Out), 
    LIFO (Last-In-First-Out) or AVCO (Average Cost) algorithms.
    The algorithm name specifies the order in which BUYs
    must be considered to estimate profit or loss.
    All these algorithms produce the same result if SELL
    order always follows only one BUY with the same amount.

    Orders, trades and stats can be exported to CSV file
    using `export_orders`, `export_trades`, `exports_stats`
    repectively, or via `export` - for exporting all 
    with default file names.
    """
    def __init__(self, 
                 strategy_title: str, 
                 data_provider: DataProvider,
                 start_balance: Decimal,
                 result_balance: Decimal,
                 result_equity: Decimal,
                 trades: t.Sequence[TradeInfo],
                 orders: t.Sequence[OrderInfo]):
        self._data_provider = data_provider
        self._data_title = data_provider.title
        self._data_timeframe = data_provider.timeframe
        self._data_since = data_provider.since
        self._data_until = data_provider.until
        self._symbol = data_provider.symbol
        self._strategy_title = strategy_title
        self._start_balance = start_balance
        self._result_balance = result_balance
        self._result_equity = result_equity
        diff = result_equity - start_balance
        self._total_gain = diff
        self._total_gain_percents = diff/(start_balance/100)
        self._trades = trades
        self._orders = orders
        self._trades_count = len(trades)
        self._orders_count = len(orders)
        self._date = datetime.now()

    @property
    def strategy_title(self) -> str:
        return self._strategy_title

    @property
    def date(self) -> datetime:
        return self._date

    @property
    def start_balance(self) -> Decimal:
        return self._start_balance

    @property
    def result_balance(self) -> Decimal:
        return self._result_balance

    @property
    def result_equity(self) -> Decimal:
        return self._result_equity

    @property
    def total_gain(self) -> Decimal:
        return self._total_gain

    @property
    def total_gain_percents(self):
        return self._total_gain_percents

    @property
    def trades_count(self) -> int:
        return self._trades_count

    @property
    def orders_count(self) -> int:
        return self._orders_count

    def get_stats(self, algorithm: str) -> BacktestingStats:
        """
        Get stats such as Win Rate, Profit/Loss, Average Profit, etc.
        Supports estimation in FIFO (First-In-First-Out), 
        LIFO (Last-In-First-Out) or AVCO (Average Cost) algorithms.
        The algorithm name specifies the order in which BUYs
        must be considered to estimate profit or loss.

        All these algorithms produce the same result if SELL
        order always follows only one BUY with the same amount.
        """
        return BacktestingStats(self._strategy_title, 
                                self._data_provider, 
                                self._date, 
                                get_stats(algorithm, self._trades))

    def export(self) -> None:
        """Export stats, trades and orders to CSV files."""
        self.export_stats()
        self.export_trades()
        self.export_orders()

    def export_stats(self, 
                     filename: t.Optional[str] = None,
                     delimiter=';') -> None:
        """Export stats to CSV file."""
        algorithms = ('FIFO', 'LIFO', 'AVCO')
        filename = filename or self._get_default_csv_filename('stats')
        stats = [ get_stats(algo, self._trades) for algo in algorithms ]

        export_stats(filename, delimiter, self.strategy_title,
                     self.date, self._data_title, self._data_timeframe, 
                     self._symbol, self._data_since, self._data_until, 
                     self.start_balance, self.result_balance, 
                     self.total_gain, self.total_gain_percents, stats)

    def export_trades(self, 
                      filename: t.Optional[str] = None,
                      delimiter=';') -> None:
        """Export trades to CSV file."""
        filename = filename or self._get_default_csv_filename('trades')
        export_trades(filename, delimiter, self._trades)

    def export_orders(self, 
                      filename: t.Optional[str] = None,
                      delimiter=';') -> None:
        """Export orders to CSV file."""
        filename = filename or self._get_default_csv_filename('orders')
        export_orders(filename, delimiter, self._orders)

    def _get_default_csv_filename(self, entity: str) -> str:
        """
        Get filename for exporting something that is called `entity`
        including .csv extension in the end.
        """
        strategy_title = self._strategy_title.lower()
        strategy_title = '_'.join(strategy_title.split())
        strategy_title = re.sub(r'[\\, /]', '_', strategy_title)
        date_postfix = datetime.strftime(self._date, "%Y%m%d%H%M%S")
        return f"{strategy_title}_{entity}_{date_postfix}.csv"

    def __repr__(self) -> str:
        date = datetime.strftime(self._date, "%Y-%m-%d %H:%M:%S")
        header_message = f"Backtesting result {date}"
        header = f"\n{'-' * 16}* {header_message} *{'-' * 16}\n\n"
        footer = f"\n{'-' * 73}\n"
        data_block = (f"{self._data_title} on {str(self._data_timeframe)}\n"
                      f"since: {self._data_since}\n"
                      f"until: {self._data_until}\n"
                      f"trading pair: {self._symbol}\n\n")

        content = (f"Strategy title: {self.strategy_title}\n"
                   f"Start balance:\t\t{self.start_balance:.2f}\n"
                   f"Result balance:\t\t{self.result_balance:.2f}\n"
                   f"Result equity:\t\t{self.result_equity:.2f}\n"
                   f"Total gain:\t\t{self.total_gain:.2f}\n"
                   f"Total gain percents:\t{self.total_gain_percents:.2f}%\n"
                   f"Trades count:\t{self.trades_count}\n"
                   f"Orders count:\t{self.orders_count}\n")

        return f"{header}{data_block}{content}{footer}"
