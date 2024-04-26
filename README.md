# fastapi-response-streaming
utilising lambda web adapter to perform response streaming

first install the requirements in a package folder using this command
```
pip install \
--platform manylinux2014_x86_64 \
--target=package \
--implementation cp \
--python-version 3.9 \
--only-binary=:all: --upgrade \
-r requirements.txt
```
now inside the package folder all the dependencies get installed

```
cd package
zip -r ../my_deployment_package.zip .
```

now add the both scripts into the zip file

```
cd ..
zip my_deployment_package.zip lambda_function.py
```

now create lambda function and do the following configurations:

add Lambda Web Adapter layer to the function and configure wrapper script.

1. attach Lambda Adapter layer to your function. This layer containers Lambda Adapter binary and a wrapper script.
    1. x86_64: `arn:aws:lambda:${AWS::Region}:753240598075:layer:LambdaAdapterLayerX86:22`
    2. arm64: `arn:aws:lambda:${AWS::Region}:753240598075:layer:LambdaAdapterLayerArm64:22`
2. configure Lambda environment variable `AWS_LAMBDA_EXEC_WRAPPER` to `/opt/bootstrap`. This is a wrapper script included in the layer.
3. set function handler to a startup command: `run.sh`. The wrapper script will execute this command to boot up your application.
4. Set the Timeout of the lambda function to a suitable duration

it is done!

reference links             
- [aws LWA repo](https://github.com/awslabs/aws-lambda-web-adapter/tree/main/examples/fastapi-response-streaming-zip)         
- [installing python libraries](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-native-libraries)