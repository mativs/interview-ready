# Django Rest Framework Challenge

## 1. Implement a custom version of Model Serializer 

You must implement a custom version of the class `ModelSerializer` that is provided by the `restframework` library with the following features:

1. The fields should be populated automatically based on the `Meta` `fields` parameters 
2. Implement `CharField`, `IntegerField`, `BooleanField`, `FloatField`, `EmailField` and `SlugField`
3. Implement `read_only` and `write_only` parameters 
4. Implement `read`, `create` and `write` operations for the serializer
5. Create validations for `IntegerField`, `BooleanField`, `EmailField`, `SlugField`

The app `custom_rest_framework` has already been created with a dummy model `TestSerializerModel` with the required columns. 

A test file is already created with all tests working fine. 

You should change the import from the original `restframework` and import your custom one while having the test still working fine. 

For running the tests you should first install the depending library and then run the test

```
$ pipenv install
$ pipenv shell
$ python manage.py test
```