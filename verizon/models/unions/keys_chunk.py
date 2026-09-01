from __future__ import annotations

from typing import TypeAlias

from ..enable_promo_exp import EnablePromoExp, EnablePromoExpDict
from ..key_data_percentage50 import KeyDataPercentage50, KeyDataPercentage50Dict
from ..key_service_plan import KeyServicePlan, KeyServicePlanDict
from ..keysms_percentage50 import KeysmsPercentage50, KeysmsPercentage50Dict
from ..no_of_days_b4_promo_exp import NoOfDaysB4PromoExp, NoOfDaysB4PromoExpDict

KeysChunk: TypeAlias = (
    KeyServicePlan
    | KeyDataPercentage50
    | KeyDataPercentage50
    | KeyDataPercentage50
    | KeyDataPercentage50
    | KeysmsPercentage50
    | KeysmsPercentage50
    | KeysmsPercentage50
    | KeysmsPercentage50
    | NoOfDaysB4PromoExp
    | EnablePromoExp
)

KeysChunkDict: TypeAlias = (
    KeyServicePlanDict
    | KeyDataPercentage50Dict
    | KeyDataPercentage50Dict
    | KeyDataPercentage50Dict
    | KeyDataPercentage50Dict
    | KeysmsPercentage50Dict
    | KeysmsPercentage50Dict
    | KeysmsPercentage50Dict
    | KeysmsPercentage50Dict
    | NoOfDaysB4PromoExpDict
    | EnablePromoExpDict
)
