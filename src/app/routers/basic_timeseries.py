# encoding: utf-8
"""
Basic routes for the Norgate Data Server. These provide a RES
"""

from datetime import date, timedelta
from fastapi import APIRouter, HTTPException, Path, Query
import numpy as np
from pydantic import BaseModel
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

    cur_date = date(year=2019, month=1, day=1)
    cur_prc = 100.0

    end_date = date(year=2019, month=12, day=31)
    prices = []

    while cur_date < end_date:
        cur_date = cur_date + timedelta(days=1)
        cur_prc = cur_prc + np.random.normal()
        prices.append(DailyPrice(tradedate=cur_date,
                                 close=cur_prc))

    return prices
