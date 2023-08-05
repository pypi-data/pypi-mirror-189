import typing as t

from abc import ABC, abstractmethod
from decimal import Decimal
from .candles import Candles
from .timeframes import Timeframes
from .analyser.analyser import Analyser
from .analyser.indicators.base import IndicatorParam
from .broker.base import (
    OrderSide,
    MarketOrderOptions,
    MarketOrderInfo,
    LimitOrderOptions,
    LimitOrderInfo,
    TakeProfitOptions,
    StopLossOptions,
    AbstractBroker
)


class TradingStrategy(ABC):
    """
    Base class for trading strategies. 
    Strategy must provide algorithm implementation in `tick` method, 
    which runs each time a new candle closes.

    In runtime, strategy has access to `broker`, `analyser` and `candles`.
        - `broker` - Manages orders in a simulated
            market environment. The broker executes/activates orders
            whose conditions fits the market.
        - `analyser` - Performs indicators calculation.
        - `candles` - Provides the last candle representation 
            for various timeframes. It is useful for checking 
            properties of a candle on one timeframe (H1, for example),
            while having data on another (for instance, M1).

    `TradingStrategy` also has several class attributes:
        - `title` - title of a strategy
        - `indicators` - Set of indicators params used in a strategy. 
            This is useful to infer how many market data is needed to store 
            to be able to calculate indicators at any time.
        - `candle_timeframes` - Set of timeframes whose candles may be
            requested during strategy run.

    There is no need to access or modify these class attributes
    from inside the strategy, normally.
    """
    title = ''
    indicators: t.Set[t.Tuple[IndicatorParam]] = set()
    candle_timeframes: t.Set[Timeframes] = set()

    def __init__(self, 
                 broker: AbstractBroker,
                 analyser: Analyser,
                 candles: Candles):
        self.broker=broker
        self.analyser=analyser
        self.candles=candles

    @classmethod
    def get_title(cls) -> str:
        return cls.title or cls.__name__

    @property
    def position(self) -> Decimal:
        return self.broker.balance.available_crypto_balance

    def buy(self, amount: t.Optional[Decimal] = None) -> MarketOrderInfo:
        """Shortcut for submitting market buy order."""
        order_amount = amount or self.broker.max_fiat_for_taker
        options = MarketOrderOptions(OrderSide.BUY, amount=order_amount)
        return self.broker.submit_market_order(options)

    def sell(self, amount: t.Optional[Decimal] = None) -> MarketOrderInfo:
        """Shortcut for submitting market sell order."""
        order_amount = amount or self.position
        options = MarketOrderOptions(OrderSide.SELL, amount=order_amount)
        return self.broker.submit_market_order(options)

    def limit_buy(self,
                  order_price: Decimal,
                  take_profit: t.Optional[TakeProfitOptions] = None,
                  stop_loss: t.Optional[StopLossOptions] = None,
                  amount: t.Optional[Decimal] = None) -> LimitOrderInfo:
        """Shortcut for submitting limit buy order."""
        order_amount = amount or self.broker.max_fiat_for_maker
        options = LimitOrderOptions(OrderSide.BUY,
                                    amount=order_amount,
                                    order_price=order_price,
                                    take_profit=take_profit,
                                    stop_loss=stop_loss)
        return self.broker.submit_limit_order(options)

    def limit_sell(self, 
                   order_price: Decimal,
                   take_profit: t.Optional[TakeProfitOptions] = None,
                   stop_loss: t.Optional[StopLossOptions] = None,
                   amount: t.Optional[Decimal] = None) -> LimitOrderInfo:
        """Shortcut for submitting limit sell order."""
        order_amount = amount or self.position
        options = LimitOrderOptions(OrderSide.SELL,
                                    amount=order_amount,
                                    order_price=order_price,
                                    take_profit=take_profit,
                                    stop_loss=stop_loss)
        return self.broker.submit_limit_order(order)

    @abstractmethod
    def tick(self) -> None:
        """The lands of user code. Runs each time a new candle closes."""
        pass