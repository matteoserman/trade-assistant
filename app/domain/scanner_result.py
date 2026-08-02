from dataclasses import dataclass, field


@dataclass(slots=True)
class ScannerResult:
    """
    Result returned by the scanner.
    """

    symbol: str

    passed: bool

    score: float

    passed_rules: list[str] = field(default_factory=list)

    failed_rules: list[str] = field(default_factory=list)