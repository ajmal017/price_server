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
    close: float


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
        prices.append(DailyPrice(tradedate=cur_date,
                                 close=cur_prc))
        cur_date = cur_date + timedelta(days=1)

    return prices
