(window.webpackJsonp=window.webpackJsonp||[]).push([[34],{432:function(v,_,t){"use strict";t.r(_);var a=t(5),s=Object(a.a)({},(function(){var v=this,_=v._self._c;return _("ContentSlotsDistributor",{attrs:{"slot-key":v.$parent.slotKey}},[_("h3",{attrs:{id:"analyses-jepsen"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#analyses-jepsen"}},[v._v("#")]),v._v(" Analyses-jepsen")]),v._v(" "),_("p",[_("a",{attrs:{href:"https://jepsen.io/analyses",target:"_blank",rel:"noopener noreferrer"}},[v._v("https://jepsen.io/analyses"),_("OutboundLink")],1)]),v._v(" "),_("h3",{attrs:{id:"分区"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#分区"}},[v._v("#")]),v._v(" 分区")]),v._v(" "),_("p",[v._v("有垂直分区和水平分区，垂直分区是指将表按列分开，水平分区是指将表按行分开。")]),v._v(" "),_("p",[v._v("OLTP： 水平分区\nOLAP： 垂直分区")]),v._v(" "),_("p",[v._v("水平分区的扩展性更强；")]),v._v(" "),_("p",[v._v("partition,shard,region,tablet,vnode.")]),v._v(" "),_("h4",{attrs:{id:"水平分区算法"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#水平分区算法"}},[v._v("#")]),v._v(" 水平分区算法")]),v._v(" "),_("ul",[_("li",[_("p",[v._v("范围分区")]),v._v(" "),_("ul",[_("li",[v._v("优势\n"),_("ul",[_("li",[v._v("分区键")]),v._v(" "),_("li",[v._v("简单")]),v._v(" "),_("li",[v._v("范围容易调整")]),v._v(" "),_("li",[v._v("同一节点速度快")])])]),v._v(" "),_("li",[v._v("缺点\n"),_("ul",[_("li",[v._v("无法使用分区键之外的关键字进行范围查询")]),v._v(" "),_("li",[v._v("跨节点慢")]),v._v(" "),_("li",[v._v("热点、不均匀")])])]),v._v(" "),_("li",[v._v("例子\n"),_("ul",[_("li",[v._v("Bigtable")]),v._v(" "),_("li",[v._v("Hbase")]),v._v(" "),_("li",[v._v("tikv")])])])])]),v._v(" "),_("li",[_("p",[v._v("哈希分区")]),v._v(" "),_("ul",[_("li",[v._v("优势\n"),_("ul",[_("li",[v._v("均匀")])])]),v._v(" "),_("li",[v._v("缺点\n"),_("ul",[_("li",[_("strong",[v._v("范围查询需要额外数据")])]),v._v(" "),_("li",[v._v("节点扩容、缩容需要大量数据迁移")])])])])]),v._v(" "),_("li",[_("p",[v._v("一致性哈希")]),v._v(" "),_("ul",[_("li",[v._v("优势\n"),_("ul",[_("li",[v._v("缓解了节点扩容、缩容需要大量数据迁移的问题")])])]),v._v(" "),_("li",[v._v("缺点\n"),_("ul",[_("li",[v._v("节点多时优势才明显")]),v._v(" "),_("li",[v._v("不带虚拟节点的情况下，节点下线会引起大范围的数据迁移")]),v._v(" "),_("li",[_("strong",[v._v("范围查询需要额外数据")])])])])])])]),v._v(" "),_("h4",{attrs:{id:"分区的挑战"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#分区的挑战"}},[v._v("#")]),v._v(" 分区的挑战")]),v._v(" "),_("ul",[_("li",[v._v("垂直分区中的多表查询")]),v._v(" "),_("li",[v._v("水平分区的范围查询")])]),v._v(" "),_("h3",{attrs:{id:"复制"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#复制"}},[v._v("#")]),v._v(" 复制")]),v._v(" "),_("ul",[_("li",[v._v("增强数据可用性和安全性")]),v._v(" "),_("li",[v._v("减少往返时间\n"),_("ul",[_("li",[v._v("Round-Trip Time RTT")])])]),v._v(" "),_("li",[v._v("增加吞吐量")])]),v._v(" "),_("h4",{attrs:{id:"单主复制"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#单主复制"}},[v._v("#")]),v._v(" 单主复制")]),v._v(" "),_("p",[v._v("主从复制、主从复制")]),v._v(" "),_("ul",[_("li",[v._v("同步复制：所有节点确认\n"),_("ul",[_("li",[v._v("优点：\n"),_("ul",[_("li",[v._v("简单")]),v._v(" "),_("li",[v._v("并发写在主节点")]),v._v(" "),_("li",[v._v("读负载均衡")])])]),v._v(" "),_("li",[v._v("缺点：\n"),_("ul",[_("li",[v._v("主从切换慢")]),v._v(" "),_("li",[v._v("主从切换不正常 -> 脑裂 🧠")]),v._v(" "),_("li",[v._v("写请求负载均衡？")]),v._v(" "),_("li",[v._v("性能差")])])])])]),v._v(" "),_("li",[v._v("异步复制：主节点确认")]),v._v(" "),_("li",[v._v("半同步复制：部分节点")])]),v._v(" "),_("h4",{attrs:{id:"多主复制"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#多主复制"}},[v._v("#")]),v._v(" 多主复制")]),v._v(" "),_("ul",[_("li",[v._v("多个主节点")]),v._v(" "),_("li",[v._v("可用性提高")]),v._v(" "),_("li",[v._v("一致性变差")])]),v._v(" "),_("p",[v._v("一般多个数据中心，且避免请求跨数据中心")]),v._v(" "),_("p",[v._v("需要处理数据冲突问题：\n特点账号特定节点？")]),v._v(" "),_("p",[v._v("应对冲突最好的方法就是避免冲突？")]),v._v(" "),_("ul",[_("li",[v._v("客户端解决\n"),_("ul",[_("li",[v._v("购物车")])])]),v._v(" "),_("li",[v._v("Last-Write-Wins\n"),_("ul",[_("li",[v._v("时间如何同步")])])]),v._v(" "),_("li",[v._v("因果关系跟踪")]),v._v(" "),_("li",[v._v("Conflict-Free Replicated Type CRDT")])]),v._v(" "),_("h4",{attrs:{id:"无主复制"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#无主复制"}},[v._v("#")]),v._v(" 无主复制")]),v._v(" "),_("p",[v._v("完全没有主节点")]),v._v(" "),_("p",[_("strong",[v._v("亚马逊 Dynamo 架构")])]),v._v(" "),_("p",[v._v("Apache Cassandra、Riak")]),v._v(" "),_("p",[v._v("客户端同时发送给多个节点，满足一定数量确认就可以认为成功了；\n冲突更多了；\n客户端会读到旧的数据；")]),v._v(" "),_("p",[v._v("修复：")]),v._v(" "),_("ul",[_("li",[v._v("读修复（Read Repair）：知道旧的数据，让节点更新；")]),v._v(" "),_("li",[_("strong",[v._v("反熵过程（Anti-Entropy Process）")]),v._v("：后台进程处理；\n"),_("ul",[_("li",[v._v("比较 Merkle Tree  而非一个个具体的数据；")])])])]),v._v(" "),_("p",[v._v("基于Quorum 的数据冗余机制")]),v._v(" "),_("ul",[_("li",[v._v("客户端向服务端发送请求；")]),v._v(" "),_("li",[v._v("需要决定到底要多少个节点才足够、增加或减少读写请求的节点的数量系统会发生什么变化；")])]),v._v(" "),_("div",{staticClass:"language-shell line-numbers-mode"},[_("pre",{pre:!0,attrs:{class:"language-shell"}},[_("code",[v._v("N 个节点\nW 个写入数据\nR 个节点读出数据\n\n需要\n  W+R "),_("span",{pre:!0,attrs:{class:"token operator"}},[v._v(">")]),v._v(" N\n  R "),_("span",{pre:!0,attrs:{class:"token operator"}},[v._v(">")]),v._v(" N - W \n这个情况下，必然读到成功写入的数据。\n\n当\n  W  "),_("span",{pre:!0,attrs:{class:"token operator"}},[v._v(">")]),v._v(" N /2 的时候\n两个不同写请求不能同时修改同一份数据\n\n最多可以设定  "),_("span",{pre:!0,attrs:{class:"token assign-left variable"}},[v._v("W")]),_("span",{pre:!0,attrs:{class:"token operator"}},[v._v("=")]),v._v("N "),_("span",{pre:!0,attrs:{class:"token assign-left variable"}},[v._v("R")]),_("span",{pre:!0,attrs:{class:"token operator"}},[v._v("=")]),v._v("N；\n\nW、R 可以配置。\n\n")])]),v._v(" "),_("div",{staticClass:"line-numbers-wrapper"},[_("span",{staticClass:"line-number"},[v._v("1")]),_("br"),_("span",{staticClass:"line-number"},[v._v("2")]),_("br"),_("span",{staticClass:"line-number"},[v._v("3")]),_("br"),_("span",{staticClass:"line-number"},[v._v("4")]),_("br"),_("span",{staticClass:"line-number"},[v._v("5")]),_("br"),_("span",{staticClass:"line-number"},[v._v("6")]),_("br"),_("span",{staticClass:"line-number"},[v._v("7")]),_("br"),_("span",{staticClass:"line-number"},[v._v("8")]),_("br"),_("span",{staticClass:"line-number"},[v._v("9")]),_("br"),_("span",{staticClass:"line-number"},[v._v("10")]),_("br"),_("span",{staticClass:"line-number"},[v._v("11")]),_("br"),_("span",{staticClass:"line-number"},[v._v("12")]),_("br"),_("span",{staticClass:"line-number"},[v._v("13")]),_("br"),_("span",{staticClass:"line-number"},[v._v("14")]),_("br"),_("span",{staticClass:"line-number"},[v._v("15")]),_("br"),_("span",{staticClass:"line-number"},[v._v("16")]),_("br"),_("span",{staticClass:"line-number"},[v._v("17")]),_("br")])]),_("p",[v._v("怎么确认哪个是需要的呢？")]),v._v(" "),_("h3",{attrs:{id:"cap-定理"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#cap-定理"}},[v._v("#")]),v._v(" CAP 定理")]),v._v(" "),_("p",[v._v("布鲁尔定理")]),v._v(" "),_("ul",[_("li",[v._v("一致性（Consistency）")]),v._v(" "),_("li",[v._v("可用性（Availability）")]),v._v(" "),_("li",[v._v("分区容错性（Partition Tolerance）")])]),v._v(" "),_("p",[v._v("网络问题决定了分区容错性是基本需求，然后在一致性和可用性之间进行选择：CP 或 AP")]),v._v(" "),_("ul",[_("li",[v._v("只在网络分区的时候选择，其他时候尽量满足所有；")]),v._v(" "),_("li")]),v._v(" "),_("h4",{attrs:{id:"pacelc-定理"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#pacelc-定理"}},[v._v("#")]),v._v(" PACELC 定理")]),v._v(" "),_("p",[v._v("延迟一直存在，网络分区不会一直存在。")]),v._v(" "),_("p",[v._v("PACELC 定理指出，")]),v._v(" "),_("p",[v._v("在分布式系统存在网络分区（P）的情况下，必须在可用性（A）和一致致性（C）之间做出选择；")]),v._v(" "),_("p",[v._v("否则（Else, E）系统在没有网络分区且正常运行的情况下，必须在\n延迟（L）和一致性（C）之间做出选择。")]),v._v(" "),_("table",[_("thead",[_("tr",[_("th",[v._v("DDBS")]),v._v(" "),_("th",[v._v("PA")]),v._v(" "),_("th",[v._v("PC")]),v._v(" "),_("th",[v._v("EL")]),v._v(" "),_("th",[v._v("EC")])])]),v._v(" "),_("tbody",[_("tr",[_("td",[v._v("MySQL Cluster")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")])]),v._v(" "),_("tr",[_("td",[v._v("BigTable/Hbase")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")])]),v._v(" "),_("tr",[_("td",[v._v("DynamoDB")]),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td")]),v._v(" "),_("tr",[_("td",[v._v("Cassandra")]),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td")]),v._v(" "),_("tr",[_("td",[v._v("MongoDB")]),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")])]),v._v(" "),_("tr",[_("td",[v._v("MetaStore")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")])]),v._v(" "),_("tr",[_("td",[v._v("VoltDB/H-Store")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")])]),v._v(" "),_("tr",[_("td",[v._v("Riak")]),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td"),v._v(" "),_("td",[v._v("X")]),v._v(" "),_("td")])])]),v._v(" "),_("h4",{attrs:{id:"base-理论"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#base-理论"}},[v._v("#")]),v._v(" BASE 理论")]),v._v(" "),_("p",[v._v("Basically Available, Soft State, Eventually Consistent")]),v._v(" "),_("p",[v._v("基本可用、软状态、最终一致性")]),v._v(" "),_("h3",{attrs:{id:"一致性模型"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#一致性模型"}},[v._v("#")]),v._v(" 一致性模型")]),v._v(" "),_("p",[v._v("三个“一致性”\n分布式共识算法：Consensus Algorithm\n线性一致性：Linearizable Consistency 行为\nACID：Consistency 数据库领域，数据")]),v._v(" "),_("p",[_("img",{attrs:{src:"https://jepsen.io/consistency/models/map.svg",alt:"https://jepsen.io/consistency/models/map.svg"}})]),v._v(" "),_("h4",{attrs:{id:"线性一致性"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#线性一致性"}},[v._v("#")]),v._v(" 线性一致性")]),v._v(" "),_("p",[_("strong",[v._v("非严格定义")]),v._v("：线性一致性意味着分布式系统的所有操作看起来的都是原子的，整个分布式系统看起来好像只有一个节点。")]),v._v(" "),_("p",[_("strong",[v._v("严格定义")]),v._v("：给定一个执行历史，执行历史根据并发操作可以扩展为多个顺序历史（Sequential History），只要从中找到一个合法的顺序历史，那么该历史就是线性一致性的。")]),v._v(" "),_("p",[v._v("并发操作的可能：")]),v._v(" "),_("ul",[_("li",[v._v("一个在另一个之前完成，顺序关系")]),v._v(" "),_("li",[v._v("两个有重叠")]),v._v(" "),_("li",[v._v("一个操作跨度包含了另一个，并发关系")])]),v._v(" "),_("p",[v._v("？？？")]),v._v(" "),_("p",[v._v("第一：顺序记录中的任何一次读必须读到最近一次写入的数据；\n第二：顺序记录要和全局时钟下的顺序一致；")]),v._v(" "),_("p",[v._v("实现：通过共识算法实现线性一致性；")]),v._v(" "),_("p",[v._v("代价：同步原语和原子变量都会增加开销，全局时钟难以实现；")]),v._v(" "),_("h4",{attrs:{id:"顺序一致性"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#顺序一致性"}},[v._v("#")]),v._v(" 顺序一致性")]),v._v(" "),_("p",[v._v("同一个客户端的操作顺序一致，不同客户端的操作顺序可以不一致；")]),v._v(" "),_("p",[v._v("只关注局部的顺序；")]),v._v(" "),_("h4",{attrs:{id:"因果一致性"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#因果一致性"}},[v._v("#")]),v._v(" 因果一致性")]),v._v(" "),_("p",[v._v("相同的顺序看到因果相关的操作，而没有因果关系的并发操作可以被不同的进程以不同的顺序看到；")]),v._v(" "),_("h4",{attrs:{id:"最终一致性"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#最终一致性"}},[v._v("#")]),v._v(" 最终一致性")]),v._v(" "),_("p",[v._v("在没有写操作的情况下，所有的读操作最终都会返回最近写入的值；")]),v._v(" "),_("h4",{attrs:{id:"以客户端为中心的一致性模型"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#以客户端为中心的一致性模型"}},[v._v("#")]),v._v(" 以客户端为中心的一致性模型")]),v._v(" "),_("p",[v._v("前面的一致性模型都是以数据为中心的，而以客户端为中心的一致性模型则是以客户端为中心的。")]),v._v(" "),_("p",[v._v("聚焦单个客户端观察到的系统状态。")]),v._v(" "),_("ul",[_("li",[v._v("单调读：读原来或比原来更新；")]),v._v(" "),_("li",[v._v("单调写：同一客户端的写操作在所有副本上都以同样的顺序执行；")]),v._v(" "),_("li",[v._v("读己之所写：同一客户端，写操作完成后，在同一副本或其他副本上的读操作必须返回写入的值；")])]),v._v(" "),_("p",[_("strong",[v._v("PRAM（Pipelined RAM）一致性")])]),v._v(" "),_("p",[v._v("FIFO 一致性")]),v._v(" "),_("p",[v._v("同一个客户端的多个写操作，将被"),_("strong",[v._v("所有的")]),v._v("副本按照同样的顺序执行，当不同的客户端的写操作并发时，系统不保证顺序；")]),v._v(" "),_("p",[v._v("读后写：会话因果？")]),v._v(" "),_("h3",{attrs:{id:"隔离级别"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#隔离级别"}},[v._v("#")]),v._v(" 隔离级别")]),v._v(" "),_("ul",[_("li",[v._v("串行化")]),v._v(" "),_("li",[v._v("可重复读")]),v._v(" "),_("li",[v._v("快照隔离")]),v._v(" "),_("li",[v._v("读已提交")]),v._v(" "),_("li",[v._v("读未提交")])]),v._v(" "),_("p",[v._v("脏写：一个事务覆盖了另一个正在执行的事务的未提交的数据；破坏数据完整性，无法正确回滚；")]),v._v(" "),_("p",[v._v("脏读：一个事务读取了另一个事务未提交的数据；这个读到的数据并不是最终的；")]),v._v(" "),_("p",[v._v("不可重复读：一个事务中查询一个值两次不同；")]),v._v(" "),_("p",[v._v("幻读：条件查询时，两次查询的结果不一致；")]),v._v(" "),_("p",[v._v("更新丢失：两个事务同时更新同一行数据，其中一个事务的更新被另一个事务覆盖，只有一个生效；")]),v._v(" "),_("p",[v._v("读偏斜：？")]),v._v(" "),_("p",[v._v("写偏斜：？")]),v._v(" "),_("h3",{attrs:{id:"一致性和隔离级别的对比"}},[_("a",{staticClass:"header-anchor",attrs:{href:"#一致性和隔离级别的对比"}},[v._v("#")]),v._v(" "),_("strong",[v._v("一致性和隔离级别的对比")])]),v._v(" "),_("ul",[_("li",[v._v("都是描述系统能够容忍的哪些行为；")]),v._v(" "),_("li",[v._v("一致性适用单个操作对象，隔离级别涉及多个操作对象；")]),v._v(" "),_("li",[v._v("线性一致性保证实时，串行化保证并发的效果和顺序；")]),v._v(" "),_("li",[v._v("单机单线程 -> 严格串行化？")])])])}),[],!1,null,null,null);_.default=s.exports}}]);