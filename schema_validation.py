from flask_marshmallow import Schema
from marshmallow.fields import Str, Int
from marshmallow import validates_schema, ValidationError, validate

length = validate.Length(min=1)

class CreateExpense(Schema):
    class Meta:
        fields = ["name", "amount", "category"]
    name = Str(validate=length, required=True)
    amount = Int(validate=length, required=True)
    category = Str(validate=length, required=True)