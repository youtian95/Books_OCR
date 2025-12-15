

## 附录 K 单层厂房纵向抗震验算

### K.1 单层钢筋混凝土柱厂房纵向抗震计算的修正刚度法

#### K.1.1 纵向基本自振周期的计算。

按本附录计算单跨或等高多跨的钢筋混凝土柱厂房纵向地震作用时，在柱顶标高不大于15m且平均跨度不大于30m时，纵向基本周期可按下列公式确定：

1 砖围护墙厂房，可按下式计算：

 $$ T_{1}=0.23+0.00025\psi_{1}l\sqrt{H^{3}} $$ 

式中： $ \psi_{1} $ ——屋盖类型系数，大型屋面板钢筋混凝土屋架可采用1.0，钢屋架采用0.85；

l——厂房跨度（m），多跨厂房可取各跨的平均值；

H——基础顶面至柱顶的高度（m）。

2 敞开、半敞开或墙板与柱子柔性连接的厂房，可按式（K.1.1-1）进行计算并乘以下列围护墙影响系数：

 $$ \psi_{2}=2.6-0.002l\sqrt{H^{3}} $$ 

式中： $ \psi_{2} $  ——围护墙影响系数，小于1.0时应采用1.0。

#### K.1.2 柱列地震作用的计算。

1 等高多跨钢筋混凝土屋盖的厂房，各纵向柱列的柱顶标高处的地震作用标准值，可按下列公式确定：

 $$ F_{i}=\alpha_{1}G_{eq}\frac{K_{ai}}{\sum K_{ai}} $$ 

 $$ K_{a i}=\psi_{3}\psi_{4}K_{i} $$ 

式中： $ F_{i} $  —— i 柱列柱顶标高处的纵向地震作用标准值；

 $ \alpha_{1} $  ——相应于厂房纵向基本自振周期的水平地震影响系数，应按本规范第5.1.5条确定；

 $ G_{eq} $  ——厂房单元柱列总等效重力荷载代表值，应包括按本规范第5.1.3条确定的屋盖重力荷载代表值、70%纵墙自重、50%横墙与山墙自重及折算的柱自重（有吊车时采用10%柱自重，无吊车时采用50%柱自重）；

 $ K_{i} $  —— i 柱列柱顶的总侧移刚度，应包括 i 柱列内柱子和上、下柱间支撑的侧移刚度及纵墙的折减侧移刚度的总和，贴砌的砖围护墙侧移刚度的折减系数，可根据柱列侧移值的大小，采用 0.2～0.6；

 $ K_{ai} $  —— i 柱列柱顶的调整侧移刚度；

 $ \psi_{3} $  ——柱列侧移刚度的围护墙影响系数，可按表 K.1.2-1 采用；有纵向砖围护墙的四跨或五跨厂房，由边柱列数起的第三柱列，可按表内相应数值的 1.15 倍采用；

 $ \psi_{t} $  ——柱列侧移刚度的柱间支撑影响系数，纵向为砖围护墙时，边柱列可采用1.0，中柱列可按表K.1.2-2采用。

<div style="text-align: center;">表 K.1.2-1 围护墙影响系数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2" colspan="2">围护墙类别和烈度</td><td colspan="5">柱列和屋盖类别</td></tr><tr><td rowspan="3">边柱列</td><td colspan="4">中柱列</td></tr><tr><td rowspan="2">240砖墙</td><td rowspan="2">370砖墙</td><td colspan="2">无檩屋盖</td><td colspan="2">有檩屋盖</td></tr><tr><td style='text-align: center;'>边跨无天窗</td><td style='text-align: center;'>边跨有天窗</td><td style='text-align: center;'>边跨无天窗</td><td style='text-align: center;'>边跨有天窗</td></tr><tr><td style='text-align: center;'></td><td style='text-align: center;'>7度</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.9</td></tr><tr><td style='text-align: center;'>7度</td><td style='text-align: center;'>8度</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>1.6</td><td style='text-align: center;'>1.7</td></tr><tr><td style='text-align: center;'>8度</td><td style='text-align: center;'>9度</td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>1.3</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>1.5</td></tr><tr><td style='text-align: center;'>9度</td><td style='text-align: center;'></td><td style='text-align: center;'>0.85</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.3</td><td style='text-align: center;'>1.3</td><td style='text-align: center;'>1.4</td></tr><tr><td colspan="2">无墙、石棉瓦或挂板</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>1.2</td><td style='text-align: center;'>1.2</td></tr></table>

<div style="text-align: center;">表 K.1.2-2 纵向采用砖围护墙的中柱列柱间支撑影响系数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">厂房单元内 设置下柱支 撑的柱间数</td><td colspan="5">中柱列下柱支撑斜杆的长细比</td><td rowspan="2">中柱列 无支撑</td></tr><tr><td style='text-align: center;'>≤40</td><td style='text-align: center;'>41~80</td><td style='text-align: center;'>81~120</td><td style='text-align: center;'>121~150</td><td style='text-align: center;'>&gt;150</td></tr><tr><td style='text-align: center;'>一柱间</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>1.25</td><td rowspan="2">1.4</td></tr><tr><td style='text-align: center;'>二柱间</td><td style='text-align: center;'>-</td><td style='text-align: center;'>-</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>1.0</td></tr></table>

2 等高多跨钢筋混凝土屋盖厂房，柱列各吊车梁顶标高处的纵向地震作用标准值，可按下式确定：

 $$ F_{\mathrm{c}i}=\alpha_{\mathrm{i}}G_{\mathrm{c}i}\frac{H_{\mathrm{c}i}}{H_{i}} $$ 

式中： $ F_{ci} $  —— i 柱列在吊车梁顶标高处的纵向地震作用标准值；

 $ G_{ci} $  ——集中于 i 柱列吊车梁顶标高处的等效重力荷载代表值，应包括按本规范第 5.1.3 条确定的吊车梁与悬吊物的重力荷载代表值和 40% 柱子自重；

 $ H_{ci} $  —— i 柱列吊车梁顶高度；

 $ H_{i} $  —— i 柱列柱顶高度。

### K.2 单层钢筋混凝土柱厂房柱间支撑地震作用效应及验算

K.2.1 斜杆长细比不大于 200 的柱间支撑在单位侧力作用下的水平位移，可按下式确定：

 $$ u=\sum\frac{1}{1+\varphi_{i}}u_{t i} $$ 

式中：u——单位侧力作用点的位移；

 $ \varphi_{i} $  —— i 节间斜杆轴心受压稳定系数，应按现行国家标准《钢结构设计规范》GB 50017 采用；

 $ u_{ti} $  ——单位侧力作用下 i 节间仅考虑拉杆受力的相对位移。

K.2.2 长细比不大于 200 的斜杆截面可仅按抗拉验算，但应考虑压杆的卸载影响，其拉力可按下式确定：

 $$ N_{\mathrm{t}}=\frac{l_{i}}{(1+\psi_{\mathrm{c}}\varphi_{i})s_{\mathrm{c}}}V_{\mathrm{b}i} $$ 

式中： $ N_{t} $  ——i 节间支撑斜杆抗拉验算时的轴向拉力设计值；

 $ l_{i} $  —— i 节间斜杆的全长；

 $ \psi_{c} $  ——压杆卸载系数，压杆长细比为60、100和200时，可分别采用0.7、0.6和0.5；

 $ V_{bi} $  —— i 节间支撑承受的地震剪力设计值；

 $ s_{c} $  ——支撑所在柱间的净距。

K.2.3 无贴砌墙的纵向柱列，上柱支撑与同列下柱支撑宜等强设计。

### K.3 单层钢筋混凝土柱厂房柱间支撑

## 端节点预埋件的截面抗震验算

K.3.1 柱间支撑与柱连接节点预埋件的锚件采用锚筋时，其截面抗震承载力宜按下列公式验算：

 $$ N\leqslant\frac{0.8f_{\mathrm{y}}A_{\mathrm{s}}}{\gamma_{\mathrm{RE}}\left(\frac{\cos\theta}{0.8\zeta_{\mathrm{m}}\psi}+\frac{\sin\theta}{\zeta_{\mathrm{r}}\zeta_{\mathrm{v}}}\right)} $$ 

 $$ \psi=\frac{1}{1+\frac{0.6e_{0}}{\zeta_{r}s}} $$ 

 $$ \zeta_{\mathrm{m}}=0.6+0.25t/d $$ 

 $$ \zeta_{v}=(4-0.08d)\sqrt{f_{c}/f_{y}} $$ 

式中： $ A_{s} $  ——锚筋总截面面积；

 $ \gamma_{RE} $  ——承载力抗震调整系数，可采用1.0；

N——预埋板的斜向拉力，可采用全截面屈服点强度计算的支撑斜杆轴向力的1.05倍；

 $ e_{0} $  ——斜向拉力对锚筋合力作用线的偏心距，应小于外排锚筋之间距离的 20%（mm）；

 $ \theta $ ——斜向拉力与其水平投影的夹角；

 $ \psi $ ——偏心影响系数；

s ——外排锚筋之间的距离（mm）；

 $ \zeta_{m} $  ——预埋板弯曲变形影响系数；

t ——预埋板厚度（mm）；

d ——锚筋直径（mm）;

 $ \zeta_{r} $  ——验算方向锚筋排数的影响系数，二、三和四排可分别采用1.0、0.9和0.85；

 $ \zeta_{v} $  ——锚筋的受剪影响系数，大于0.7时应采用0.7。

K.3.2 柱间支撑与柱连接节点预埋件的锚件采用角钢加端板时，其截面抗震承载力宜按下列公式验算：

 $$ N\leqslant\frac{0.7}{\gamma_{RE}\left(\frac{\cos\theta}{\psi N_{u0}}+\frac{\sin\theta}{V_{u0}}\right)} $$ 

 $$ V_{uo}=3n\zeta_{r}\sqrt{W_{\min}bf_{a}f_{c}} $$ 

 $$ N_{uo}=0.8nf_{a}A_{s} $$ 

式中：n —— 角钢根数；

b——角钢肢宽；

 $ W_{min} $  ——与剪力方向垂直的角钢最小截面模量；

 $ A_{s} $  ——根角钢的截面面积；

 $ f_{a} $  ——角钢抗拉强度设计值。

### K.4 单层砖柱厂房纵向抗震计算的修正刚度法

K.4.1 本节适用于钢筋混凝土无檩或有檩屋盖等高多跨单层砖柱厂房的纵向抗震验算。

K.4.2 单层砖柱厂房的纵向基本自振周期可按下式计算：

 $$ T_{1}=2\psi_{\mathrm{T}}\sqrt{\frac{\sum G_{s}}{\sum K_{s}}} $$ 

式中： $ \phi_{T} $  ——周期修正系数，按表 K.4.2 采用；

 $ G_{s} $  ——第 s 柱列的集中重力荷载，包括柱列左右各半跨的屋盖和山墙重力荷载，及按动能等效原则换算集中到柱顶或墙顶处的墙、柱重力荷载；

 $ K_{s} $  ——第 s 柱列的侧移刚度。

<div style="text-align: center;">表 K.4.2 厂房纵向基本自振周期修正系数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="2">屋盖类型</td><td colspan="2">钢筋混凝土无檩屋盖</td><td colspan="2">钢筋混凝土有檩屋盖</td></tr><tr><td style='text-align: center;'>边跨无天窗</td><td style='text-align: center;'>边跨有天窗</td><td style='text-align: center;'>边跨无天窗</td><td style='text-align: center;'>边跨有天窗</td></tr><tr><td style='text-align: center;'>周期修正系数</td><td style='text-align: center;'>1.3</td><td style='text-align: center;'>1.35</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>1.45</td></tr></table>

K.4.3 单层砖柱厂房纵向总水平地震作用标准值可按下式计算：

 $$ F_{\mathrm{E k}}=\alpha_{1}\sum G_{s} $$ 

式中： $ \alpha_{1} $  ——相应于单层砖柱厂房纵向基本自振周期  $ T_{1} $  的地震影响系数；

 $ G_{s} $  ——按照柱列底部剪力相等原则，第 s 柱列换算集中到墙顶处的重力荷载代表值。

K.4.4 沿厂房纵向第 s 柱列上端的水平地震作用可按下式计算：

 $$ F_{s}=\frac{\psi_{s}K_{s}}{\sum\psi_{s}K_{s}}F_{\mathrm{E k}} $$ 

式中： $ \psi_{s} $  ——反映屋盖水平变形影响的柱列刚度调整系数，根据屋盖类型和各柱列的纵墙设置情况，按表 K.4.4 采用。

<div style="text-align: center;">表 K.4.4 柱列刚度调整系数</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td rowspan="3" colspan="2">纵墙设置情况</td><td colspan="4">屋盖类型</td></tr><tr><td colspan="2">钢筋混凝土无檩屋盖</td><td colspan="2">钢筋混凝土有檩屋盖</td></tr><tr><td style='text-align: center;'>边柱列</td><td style='text-align: center;'>中柱列</td><td style='text-align: center;'>边柱列</td><td style='text-align: center;'>中柱列</td></tr><tr><td colspan="2">砖柱敞棚</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.6</td></tr><tr><td colspan="2">各柱列均为带壁柱砖墙</td><td style='text-align: center;'>0.95</td><td style='text-align: center;'>1.1</td><td style='text-align: center;'>0.9</td><td style='text-align: center;'>1.2</td></tr><tr><td rowspan="2">边柱列为带壁柱砖墙</td><td style='text-align: center;'>中柱列的纵墙不少于4开间</td><td style='text-align: center;'>0.7</td><td style='text-align: center;'>1.4</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>1.5</td></tr><tr><td style='text-align: center;'>中柱列的纵墙少于4开间</td><td style='text-align: center;'>0.6</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>0.65</td><td style='text-align: center;'>1.9</td></tr></table>