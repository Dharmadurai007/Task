from marshmallow import Schema, fields, validate

length = validate.Length(min=1)

class CreateExpense(Schema):
    name = fields.Str(validate=length, required=True)
    amount = fields.Int(validate=validate.Range(min=1), required=True)
    category = fields.Str(validate=length, required=True)

    class Meta:
        fields = ["name", "amount", "category"]
