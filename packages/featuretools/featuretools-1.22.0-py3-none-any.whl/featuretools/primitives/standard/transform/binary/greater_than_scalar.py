from woodwork.column_schema import ColumnSchema
from woodwork.logical_types import BooleanNullable

from featuretools.primitives.base.transform_primitive_base import TransformPrimitive
from featuretools.utils.gen_utils import Library


class GreaterThanScalar(TransformPrimitive):
    """Determines if values are greater than a given scalar.

    Description:
        Given a list of values and a constant scalar, determine
        whether each of the values is greater than the scalar.
        If a value is equal to the scalar, return `False`.

    Examples:
        >>> greater_than_scalar = GreaterThanScalar(value=2)
        >>> greater_than_scalar([3, 1, 2]).tolist()
        [True, False, False]
    """

    name = "greater_than_scalar"
    input_types = [ColumnSchema(semantic_tags={"numeric"})]
    return_type = ColumnSchema(logical_type=BooleanNullable)
    compatibility = [Library.PANDAS, Library.DASK, Library.SPARK]

    def __init__(self, value=0):
        self.value = value
        self.description_template = "whether {{}} is greater than {}".format(self.value)

    def get_function(self):
        def greater_than_scalar(vals):
            return vals > self.value

        return greater_than_scalar

    def generate_name(self, base_feature_names):
        return "%s > %s" % (base_feature_names[0], str(self.value))
