# hello world

## build

```shell
mkdir build
cd build
# 执行cmake 生成 makefile
cmake ..
make
# 执行测试用例
# 执行 ctest OR make test
# 或者进入tests目录 ./test_hello（可查看gtest详细日志）
# 返回源码目录
cd ${OLDPWD}
```
