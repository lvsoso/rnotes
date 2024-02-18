
[https://openapi-generator.tech/docs/generators/go](https://openapi-generator.tech/docs/generators/go)
[https://openapi-generator.tech/docs/usage/](https://openapi-generator.tech/docs/usage/)


```shell
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate     -i /local/v1_json.tmpl     -g go     -o /local/out/go

## package name 
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate     -i /local/v1_json.tmpl     -g go     -o /local/out/go  --package-name gitea_go_sdk

## generateInterfaces
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate     -i /local/v1_json.tmpl     -g go     -o /local/out/go   --additional-properties=generateInterfaces=true

## get config
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli  config-help  -g go

## gen mock
mockgen   -source out/go/api_user.go  -destination mocktest/mock_client.go -package mock UserApi
```







