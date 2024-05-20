class OutputData:
    """Класс для группировки всех вычислений, сериализации и выгрузки"""

    def __init__(self, linear_a0, linear_a1, quadratic_a0, quadratic_a1, quadratic_a2, r_square_linear, correlation_linear, r_square_quadratic, correlation_quadratic, chart, resume) -> None:
        self.linear_a0: float = linear_a0
        self.linear_a1: float = linear_a1
        self.quadratic_a0: float = quadratic_a0
        self.quadratic_a1: float = quadratic_a1
        self.quadratic_a2: float = quadratic_a2
        self.r_square_linear: float  = r_square_linear
        self.correlation_linear: float = correlation_linear
        self.r_square_quadratic: float  = r_square_quadratic
        self.correlation_quadratic: float = correlation_quadratic
        self.chart: str = chart
        self.resume: str = resume

    def to_json(self):
        return {
            "linear_a0": self.linear_a0,
            "linear_a1": self.linear_a1,
            "quadratic_a0": self.quadratic_a0,
            "quadratic_a1": self.quadratic_a1,
            "quadratic_a2": self.quadratic_a2,
            "r_square_linear": self.r_square_linear,
            "correlation_linear": self.correlation_linear,
            "r_square_quadratic": self.r_square_quadratic,
            "correlation_quadratic": self.correlation_quadratic,
            "chart": self.chart,
            "resume": self.resume
        }