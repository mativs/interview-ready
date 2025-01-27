# Custom Model Serializer

Your task is to implement a custom version of the `ModelSerializer` class, originally provided by the rest_framework library, with the following features:

1. The serializer should automatically define its fields based on the `fields` parameter in the `Meta` class. 
2. Implement support for the following field types: `CharField`, `IntegerField`, `BooleanField`, `FloatField`, `EmailField` and `SlugField`
3. Implement the `read_only` and `write_only` parameters for the fields.
4. Implement the following methods in the serializer: `read`, `create` and `write`.
5. Implement proper validations for: `IntegerField`, `BooleanField`, `EmailField`, `SlugField`

The app `custom_rest_framework` has already been created with a dummy model named `TestSerializerModel` with the necessary fields. Additionally, a test file has been pre-configured, containing all the necessary test cases.

You should change the import from the original `restframework` and import your custom one while having the test still working fine. 

For running the tests you should first install `Django` and `restframework`

```
$ pipenv install
$ pipenv shell
$ python manage.py test
```