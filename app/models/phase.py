# -*- coding: utf-8 -*-
import datetime
from dataclasses import dataclass


@dataclass
class Phase:
    id_phase :int
    type: str
    date: datetime.date
    awa_id: int
