### cmd

```shell
bazel run @go_sdk//:bin/go -- mod tidy
bazel run //:gazelle-update-repos
bazel  run //:gazelle
```


### bazel go tutorial
[https://bazel-contrib.github.io/SIG-rules-authors/go-tutorial.html](https://bazel-contrib.github.io/SIG-rules-authors/go-tutorial.html)

[https://github.com/bazelbuild/rules_go/blob/master/docs/go/core/rules.md](https://github.com/bazelbuild/rules_go/blob/master/docs/go/core/rules.md)

[https://blog.bazel.build/2015/06/17/visualize-your-build.html](https://blog.bazel.build/2015/06/17/visualize-your-build.html)

### examples

[https://github.com/cockroachdb/cockroach-operator/blob/0ef4d1e1b4c94a8edf1393b0fa72d9de8bc21477/WORKSPACE#L20](https://github.com/cockroachdb/cockroach-operator/blob/0ef4d1e1b4c94a8edf1393b0fa72d9de8bc21477/WORKSPACE#L20)

[https://github.com/bazelbuild/rules_go/tree/master/examples/basic-gazelle](https://github.com/bazelbuild/rules_go/tree/master/examples/basic-gazelle)
