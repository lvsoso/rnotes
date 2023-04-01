(window.webpackJsonp=window.webpackJsonp||[]).push([[8],{400:function(t,s,a){"use strict";a.r(s);var n=a(4),e=Object(n.a)({},(function(){var t=this,s=t._self._c;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("p",[t._v("配置文档")]),t._v(" "),s("p",[t._v("⚗️功能亮点：")]),t._v(" "),s("ul",[s("li",[t._v("三步配置生成一个属于自己的免费个人博客。")]),t._v(" "),s("li",[t._v("使用"),s("a",{attrs:{href:"https://github.com/xugaoyi/vuepress-theme-vdoing",target:"_blank",rel:"noopener noreferrer"}},[t._v("Vdoing"),s("OutboundLink")],1),t._v("主题，感谢作者写出如此简洁美观的博客主题。")]),t._v(" "),s("li",[t._v("模板已内置集成全文搜索能力。")]),t._v(" "),s("li",[t._v("模板已内置集成基于GitHub Issue的vssue评论系统。")]),t._v(" "),s("li",[t._v("本地Markdown编写文档，提交到远程之后"),s("code",[t._v("GitHub Actions")]),t._v("自动构建发布。")])]),t._v(" "),s("p",[t._v("🦩 以下仅需简短的几步配置，就可以配置拥有一个免费的个人博客。准备好了吗，来吧！")]),t._v(" "),s("h2",{attrs:{id:"效果展示"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#效果展示"}},[t._v("#")]),t._v(" 效果展示")]),t._v(" "),s("p",[t._v("首页效果图：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_113642.png",alt:"image_20220721_113642"}})]),t._v(" "),s("p",[t._v("内部文章效果：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_165503.png",alt:"image_20220721_165503"}})]),t._v(" "),s("p",[t._v("如果你也想要一个这种效果的博客，请往下看，只需简单几个配置步骤，即可免费拥有。")]),t._v(" "),s("h2",{attrs:{id:"初始配置"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#初始配置"}},[t._v("#")]),t._v(" 初始配置")]),t._v(" "),s("p",[t._v("首先访问模板仓库："),s("a",{attrs:{href:"https://github.com//rnotes",target:"_blank",rel:"noopener noreferrer"}},[t._v("rnotes"),s("OutboundLink")],1),t._v("。点击此仓库右侧的 "),s("code",[t._v("Use this template")])]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_153908.png",alt:"image_20220721_153908"}})]),t._v(" "),s("p",[t._v("然后根据自己的实际情况，给仓库起名字：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_154115.png",alt:"image_20220721_154115"}})]),t._v(" "),s("blockquote",[s("p",[t._v("这里有一个注意点：仓库的名字将会是 "),s("code",[t._v("GitHub Pages")]),t._v(" 的访问一级路由。比如上边我仓库名字定义为："),s("code",[t._v("lql-notes")]),t._v("，那么配置成功之后的首页访问路径是： https://lql95.github.io/lql-notes  ，如果你想让首页的访问路径是根，那么只需把仓库名字命名为："),s("code",[t._v("lql95.github.io")]),t._v("。")])]),t._v(" "),s("p",[t._v("创建完成之后，自己仓库中的项目内容如下：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_154502.png",alt:"image_20220721_154502"}})]),t._v(" "),s("p",[t._v("然后将代码克隆到本地，使用编辑器打开：")]),t._v(" "),s("div",{staticClass:"language-sh line-numbers-mode"},[s("pre",{pre:!0,attrs:{class:"language-sh"}},[s("code",[t._v("$ "),s("span",{pre:!0,attrs:{class:"token function"}},[t._v("git")]),t._v(" clone git@github.com:lql95/lql-notes.git\n")])]),t._v(" "),s("div",{staticClass:"line-numbers-wrapper"},[s("span",{staticClass:"line-number"},[t._v("1")]),s("br")])]),s("h2",{attrs:{id:"调整内容"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#调整内容"}},[t._v("#")]),t._v(" 调整内容")]),t._v(" "),s("p",[t._v("接下来的操作就是将模板中的内容，替换成自己想要的内容，好在模板我已经精简了很多，不需要繁琐的配置，这里简单说明一下：")]),t._v(" "),s("h3",{attrs:{id:"全局替换关键字"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#全局替换关键字"}},[t._v("#")]),t._v(" 全局替换关键字")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_154907.png",alt:"image_20220721_154907"}})]),t._v(" "),s("p",[t._v("这样基本上就搞定了配置内容的一大步，剩下的就是一些修改美化方面的内容了。")]),t._v(" "),s("h3",{attrs:{id:"配置首页"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#配置首页"}},[t._v("#")]),t._v(" 配置首页")]),t._v(" "),s("p",[t._v("首页的配置信息在 "),s("code",[t._v("docs/index.md")]),t._v(" 这个文件当中，我们可以参照官方文档进行按需配置："),s("a",{attrs:{href:"https://doc.xugaoyi.com/pages/f14bdb/",target:"_blank",rel:"noopener noreferrer"}},[t._v("点我去看文档"),s("OutboundLink")],1)]),t._v(" "),s("h3",{attrs:{id:"配置评论"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#配置评论"}},[t._v("#")]),t._v(" 配置评论")]),t._v(" "),s("p",[t._v("模板默认内置了vssue的评论组件，也是基于github的issue作为评论的存储数据。")]),t._v(" "),s("p",[t._v("只需两步即可完成配置：")]),t._v(" "),s("ul",[s("li",[s("p",[t._v("第一步："),s("a",{attrs:{href:"https://vssue.js.org/zh/guide/github.html",target:"_blank",rel:"noopener noreferrer"}},[t._v("参考官方文档"),s("OutboundLink")],1),t._v("，创建一个"),s("code",[t._v("GitHub OAuth App")]),t._v("。或者不用看官方文档，直接看如下两个步骤。")]),t._v(" "),s("p",[s("a",{attrs:{href:"https://github.com/settings/applications/new",target:"_blank",rel:"noopener noreferrer"}},[t._v("点击此处"),s("OutboundLink")],1),t._v("，进入创建页面：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_155930.png",alt:"image_20220721_155930"}})]),t._v(" "),s("p",[t._v("点击注册之后，就进入到了详情页面，可以看到"),s("code",[t._v("Client ID")]),t._v("，点击 "),s("code",[t._v("Generate a new client secret")]),t._v(" 生成一个秘钥：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_160023.png",alt:"image_20220721_160023"}})])]),t._v(" "),s("li",[s("p",[t._v("第二步：将配置信息填写到 "),s("code",[t._v("docs/.vuepress/config.js")]),t._v(" 中。")]),t._v(" "),s("div",{staticClass:"language-yaml line-numbers-mode"},[s("pre",{pre:!0,attrs:{class:"language-yaml"}},[s("code",[t._v("// vssue 评论插件\n  "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("plugins")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("\n      "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"vuepress-plugin-vssue-global"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n      "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("platform")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"github"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("title")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"[Comment]<%- frontmatter.title %>"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("needComments")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token boolean important"}},[t._v("true")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        // 其他的 Vssue 配置\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("autoCreateIssue")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token boolean important"}},[t._v("true")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("clientId")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"d3ec4ca6363950ca41a2"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("clientSecret")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"897465b6393f1d663e6128d2fab6959a0c0333cc"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("owner")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"lql95"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token key atrule"}},[t._v("repo")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"lql-notes"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n      "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n  "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n")])]),t._v(" "),s("div",{staticClass:"line-numbers-wrapper"},[s("span",{staticClass:"line-number"},[t._v("1")]),s("br"),s("span",{staticClass:"line-number"},[t._v("2")]),s("br"),s("span",{staticClass:"line-number"},[t._v("3")]),s("br"),s("span",{staticClass:"line-number"},[t._v("4")]),s("br"),s("span",{staticClass:"line-number"},[t._v("5")]),s("br"),s("span",{staticClass:"line-number"},[t._v("6")]),s("br"),s("span",{staticClass:"line-number"},[t._v("7")]),s("br"),s("span",{staticClass:"line-number"},[t._v("8")]),s("br"),s("span",{staticClass:"line-number"},[t._v("9")]),s("br"),s("span",{staticClass:"line-number"},[t._v("10")]),s("br"),s("span",{staticClass:"line-number"},[t._v("11")]),s("br"),s("span",{staticClass:"line-number"},[t._v("12")]),s("br"),s("span",{staticClass:"line-number"},[t._v("13")]),s("br"),s("span",{staticClass:"line-number"},[t._v("14")]),s("br"),s("span",{staticClass:"line-number"},[t._v("15")]),s("br"),s("span",{staticClass:"line-number"},[t._v("16")]),s("br"),s("span",{staticClass:"line-number"},[t._v("17")]),s("br")])])])]),t._v(" "),s("p",[t._v("现在基本配置项都已经搞定，可以将代码提交上去，然后"),s("code",[t._v("GitHub Actions")]),t._v("会自动将代码部署到 "),s("code",[t._v("gh-pages")]),t._v(" 分支。")]),t._v(" "),s("h2",{attrs:{id:"终极配置"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#终极配置"}},[t._v("#")]),t._v(" 终极配置")]),t._v(" "),s("p",[t._v("终极配置就是等 GitHub Actions 跑完之后，我们能看到分支当中多了一个 "),s("code",[t._v("gh-pages")]),t._v(" 分支。")]),t._v(" "),s("p",[t._v("此时点击 "),s("code",[t._v("Settings")]),t._v(" ---\x3e "),s("code",[t._v("Pages")]),t._v("，进行如下配置：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_160920.png",alt:"image_20220721_160920"}})]),t._v(" "),s("p",[t._v("两个配置项，第一个表示选择哪个分支作为静态文件，第二个表示选择前边分支的哪个目录。")]),t._v(" "),s("p",[t._v("点击保存之后，静待一分钟，然后就可以访问上边提供的那个地址了。成果如下：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_161147.png",alt:"image_20220721_161147"}})]),t._v(" "),s("blockquote",[s("p",[t._v("如果你想配置个人自定义域名，可参考此文档："),s("a",{attrs:{href:"https://.github.io/HowToStartOpenSource/pages/06d15f/",target:"_blank",rel:"noopener noreferrer"}},[t._v("https://.github.io/HowToStartOpenSource/pages/06d15f/"),s("OutboundLink")],1)])]),t._v(" "),s("p",[t._v("如果一路配置没问题，那么文章也应该会自动加载评论功能：")]),t._v(" "),s("p",[s("img",{attrs:{src:"https://cdn.staticaly.com/gh//tu/main/img/image_20220721_165020.png",alt:"image_20220721_165020"}})]),t._v(" "),s("p",[t._v("剩下的就是一些细节的优化调整，稍微打磨之后，就可以愉快地撰写你的博客了。")])])}),[],!1,null,null,null);s.default=e.exports}}]);