from pydantic import BaseModel


class NumberInfoRead(BaseModel):
    number: int
    is_prime: bool
    is_perfect: bool
    properties: list[str]
    digit_sum: int
    fun_fact: str


class ErrorRead(BaseModel):
    number: str
    error: bool
