# encoding: utf-8
"""
Basic routes for the Norgate Data Server. These provide a RES
"""

from datetime import date, datetime, timedelta
from fastapi import APIRouter, Path
from pydantic import BaseModel
from random import seed, gauss
from starlette.status import *
from typing import List

router = APIRouter()


class DailyPrice(BaseModel):
    """Data Structure for Daily Prices"""
    tradedate: date
    open: float
    high: float
    low: float
    close: float
    volume: float


@router.get("/price_timeseries/{symbol}",
            status_code=HTTP_200_OK, response_model=List[DailyPrice])
async def get_price_timeseries(
        symbol: str = Path(...)) -> List[DailyPrice]:
    """Get daily OHLCV data plus turnover, unadjusted close and divs"""

    now = datetime.now()
    seed(now.microsecond)

    end_date = date.today()
    cur_date = end_date - timedelta(days=365)

    cur_prc = 100.0
    prices = []

    while cur_date < end_date:
        cur_prc = cur_prc + gauss(0, 1)
        close = cur_prc
        open = cur_prc + gauss(0, 0.2)
        high = cur_prc + abs(gauss(0, 0.2))
        low = cur_prc - abs(gauss(0, 0.2))
        high = max(open, high, low, close)
        low = min(open, high, low, close)
        volume = gauss(100000, 10000)
        prices.append(DailyPrice(tradedate=cur_date,
                                 open=open,
                                 high=high,
                                 low=low,
                                 close=close,
                                 volume=volume))
        cur_date = cur_date + timedelta(days=1)

    return prices
