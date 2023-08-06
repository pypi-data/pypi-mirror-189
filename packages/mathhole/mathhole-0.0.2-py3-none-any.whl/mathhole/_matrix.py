from typing import Generic, Union, List, Iterable, TypeVar


MData = TypeVar('MData', bound=Union[int, float])
MathTypes = Union[int, float, 'Matrix']


class Matrix(Generic[MData]):
    __slots__ = (
        'dimension',
        'data'
    )

    def __init__(self, col_number: int, data: List[MData]):
        row_count = len(data) // col_number
        column_count = col_number
        self.dimension = (row_count, column_count)
        self.data = data

    @property
    def column_count(self) -> int:
        return self.dimension[1]

    @property
    def row_count(self) -> int:
        return self.dimension[0]
    
    def get_col(self, col = 0) -> Iterable[MData]:
        for idx in range(col, len(self.data), self.column_count):
            yield self.data[idx]
    
    def get_row(self, row=0) -> Iterable[MData]:
        start = (row * self.column_count)
        end = start + self.column_count
        for idx in range(start, end):
            yield self.data[idx]
    
    def __mul__(self, other: MathTypes):
        if isinstance(other, float) or isinstance(other, int):
            values = [d * other for d in self.data]
            return Matrix(self.column_count, values)

        if not isinstance(other, Matrix):
            return ValueError('Not Matrix type')
        
        values = []
        for row_idx in range(self.row_count):
            row = list(self.get_row(row_idx))
            for col_idx in range(other.column_count):
                col = zip(row, other.get_col(col_idx))
                values.append(self.__reduce(col))

        return Matrix(other.column_count, values)
    
    def __rmul__(self, other: MathTypes):
        return self.__mul__(other)
    
    def __reduce(self, items):
        val = 0
        for i in items:
            val += (i[0]*i[1])
        return val