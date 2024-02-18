def _impl(ctx):  
    # 实现逻辑  
    output = ctx.actions.declare_file(ctx.label.name + ".out")  
    ctx.actions.write(output=output, content="Hello, World!")  
    return [DefaultInfo(files=depset([output]))]  
  

gen_openapi = rule(  
    implementation=_impl,  
    outputs = {"out": "%{name}.out"},  
)