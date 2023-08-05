from typing import Callable

class IntegrationError(Exception): ...

def integrate_adaptive(f: Callable, intervals, eps_abs: Union[float, None] = ..., eps_rel: Union[float, None] = ..., criteria_connection: Callable = ..., kronrod_degree: int = ..., minimum_interval_length: float = ..., max_num_subintervals: float = ..., dot: Callable = ..., domain_shape: Union[tuple, None] = ..., range_shape: Union[tuple, None] = ...): ...
