from typing import Iterable

import pandas as pd

from app.domain.scanner_result import ScannerResult
from app.services.market.service import MarketService
from app.services.scanner.rules.base import Rule


class Scanner:
    """
    Scans one or more symbols using a collection of rules.
    """

    def __init__(self, market: MarketService):

        self._market = market
        self._rules: list[Rule] = []

    def add_rule(self, rule: Rule):

        self._rules.append(rule)

    def scan(
        self,
        symbol: str,
        df: pd.DataFrame,
    ) -> ScannerResult:

        passed_rules = []
        failed_rules = []

        for rule in self._rules:

            if rule.evaluate(df):
                passed_rules.append(rule.name)
            else:
                failed_rules.append(rule.name)

        total = len(self._rules)

        score = 0.0

        if total > 0:
            score = len(passed_rules) / total * 100.0

        return ScannerResult(
            symbol=symbol,
            passed=len(failed_rules) == 0,
            score=score,
            passed_rules=passed_rules,
            failed_rules=failed_rules,
        )

    def scan_watchlist(
        self,
        symbols: Iterable[str],
        timeframe: str = "1 day",
        lookback: str = "1 Y",
    ) -> list[ScannerResult]:

        results = []

        for symbol in symbols:

            df = self._market.get_history(
                symbol=symbol,
                timeframe=timeframe,
                lookback=lookback,
            )

            if df.empty:
                continue

            result = self.scan(symbol, df)

            results.append(result)

        results.sort(
            key=lambda r: r.score,
            reverse=True,
        )

        return results