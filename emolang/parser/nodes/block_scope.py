from enum import Enum


class BlockScope(Enum):
    FUNCTION = "FUNCTION"
    LOOP = "LOOP"
    CONDITIONAL = "CONDITIONAL"
    GLOBAL = "GLOBAL"
