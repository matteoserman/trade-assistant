from abc import ABC, abstractmethod

import pandas as pd


class Rule(ABC):
    """
    Base class for all scanner rules.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable rule name.
        """
        pass

    @abstractmethod
    def evaluate(self, df: pd.DataFrame) -> bool:
        """
        Evaluates the rule.

        Returns
        -------
        bool
            True if the rule passes.
        """
        pass