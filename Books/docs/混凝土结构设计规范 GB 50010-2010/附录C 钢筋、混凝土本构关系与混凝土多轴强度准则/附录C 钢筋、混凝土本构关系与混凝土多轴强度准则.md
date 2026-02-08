# 附录 C 钢筋、混凝土本构关系与混凝土多轴强度准则

C.1 钢筋本构关系

C.1.1 普通钢筋的屈服强度及极限强度的平均值  $ f_{vm} $  、  $ f_{stm} $  可按下列公式计算：

 $$ f_{\mathrm{ym}}=f_{\mathrm{yk}}/(1-1.645\delta_{\mathrm{s}}) $$ 

 $$ f_{\mathrm{s t m}}=f_{\mathrm{s t k}}/(1-1.645\delta_{\mathrm{s}}) $$ 

式中： $ f_{yk} $ 、 $ f_{ym} $  ——钢筋屈服强度的标准值、平均值；

 $ f_{stk} $ 、 $ f_{stm} $  ——钢筋极限强度的标准值、平均值；

 $ \delta_{s} $ ——钢筋强度的变异系数，宜根据试验统计确定。

C.1.2 钢筋单调加载的应力-应变本构关系曲线（图 C.1.2）可按下列规定确定。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_5/imgs/img_in_chart_box_162_601_382_794.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A01Z%2F-1%2F%2F3135d8104439444d2fb599fdea28e0828353f8add2b780541861b681e157048a" alt="Image" width="28%" /></div>


<div style="text-align: center;">(a) 有屈服点钢筋</div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_5/imgs/img_in_chart_box_411_606_632_796.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A01Z%2F-1%2F%2Fea61536e39bde7310c6b5e06fda1542867fc1a944a7c1137dc4e93e27362e33d" alt="Image" width="28%" /></div>


<div style="text-align: center;">(b) 无屈服点钢筋</div>


<div style="text-align: center;">图 C.1.2 钢筋单调受拉应力-应变曲线</div>


1 有屈服点钢筋

 $$ \sigma_{s}=\left\{\begin{aligned}&E_{s}\epsilon_{s}&&\epsilon_{s}\leqslant\epsilon_{y}\\ &f_{y,r}&&\epsilon_{y}<\epsilon_{s}\leqslant\epsilon_{u y}\\ &f_{y,r}+k(\epsilon_{s}-\epsilon_{u y})&&\epsilon_{u y}<\epsilon_{s}\leqslant\epsilon_{u}\\ &0&&\epsilon_{s}>\epsilon_{u}\end{aligned}\right. $$ 

2 无屈服点钢筋

 $$ \sigma_{\mathrm{p}}=\left\{\begin{aligned}&E_{\mathrm{s}}\boldsymbol{\varepsilon}_{\mathrm{s}}&&\boldsymbol{\varepsilon}_{\mathrm{s}}\leqslant\boldsymbol{\varepsilon}_{\mathrm{y}}\\ &f_{\mathrm{y},\mathrm{r}}+k\left(\boldsymbol{\varepsilon}_{\mathrm{s}}-\boldsymbol{\varepsilon}_{\mathrm{y}}\right)&&\boldsymbol{\varepsilon}_{\mathrm{y}}<\boldsymbol{\varepsilon}_{\mathrm{s}}\leqslant\boldsymbol{\varepsilon}_{\mathrm{u}}\\ &0&&\boldsymbol{\varepsilon}_{\mathrm{s}}>\boldsymbol{\varepsilon}_{\mathrm{u}}\end{aligned}\right. $$ 

式中： $ E_{s} $  ——钢筋的弹性模量；

 $ \sigma_{s} $  ——钢筋应力；

 $ \varepsilon_{s} $  ——钢筋应变；

 $ f_{y,r} $  ——钢筋的屈服强度代表值，其值可根据实际结构分析需要分别取  $ f_{y} $ 、 $ f_{yk} $  或  $ f_{ym} $ ;

 $ f_{st,r} $  ——钢筋极限强度代表值，其值可根据实际结构分析需要分别取  $ f_{st} $  、  $ f_{stk} $  或  $ f_{stm} $  ；

 $ \varepsilon_{y} $  ——与  $ f_{y,r} $  相应的钢筋屈服应变，可取  $ f_{y,r}/E_{s} $ ;

 $ \varepsilon_{uy} $  ——钢筋硬化起点应变；

 $ \varepsilon_{u} $ ——与 $ f_{st,r} $ 相应的钢筋峰值应变；

k——钢筋硬化段斜率， $  k = \left( f_{\mathrm{st,r}} - f_{\mathrm{y,r}} \right) / \left( \varepsilon_{\mathrm{u}} - \varepsilon_{\mathrm{uy}} \right)  $ 

C.1.3 钢筋反复加载的应力-应变本构关系曲线（图 C.1.3）宜按下列公式确定，也可采用简化的折线形式表达。

 $$ \sigma_{\mathrm{s}}=E_{\mathrm{s}}(\varepsilon_{\mathrm{s}}-\varepsilon_{\mathrm{a}})-\left(\frac{\varepsilon_{\mathrm{s}}-\varepsilon_{\mathrm{a}}}{\varepsilon_{\mathrm{b}}-\varepsilon_{\mathrm{a}}}\right)^{\mathrm{p}}\left[E_{\mathrm{s}}(\varepsilon_{\mathrm{b}}-\varepsilon_{\mathrm{a}})-\sigma_{\mathrm{b}}\right] $$ 

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_6/imgs/img_in_image_box_258_739_551_988.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A01Z%2F-1%2F%2Fc5702ebbc30e7c876b087ef7eb2ffba08c79f0038783ee87253422e082da17c9" alt="Image" width="37%" /></div>


<div style="text-align: center;">图 C.1.3 钢筋反复加载应力-应变曲线</div>


 $$ p=\frac{(E_{\mathrm{s}}-k)(\varepsilon_{\mathrm{b}}-\varepsilon_{\mathrm{a}})}{E_{\mathrm{s}}(\varepsilon_{\mathrm{b}}-\varepsilon_{\mathrm{a}})-\sigma_{\mathrm{b}}} $$ 

式中：  $ \varepsilon_{a} $  ——再加载路径起点对应的应变；

 $ \sigma_{b} $ 、 $ \varepsilon_{b} $ ——再加载路径终点对应的应力和应变，如再加载方向钢筋未曾屈服过，则 $ \sigma_{b} $ 、 $ \varepsilon_{b} $ 取钢筋初始屈服点的应力和应变。如再加载方向钢筋已经屈服过，则取该方向钢筋历史最大应力和应变。

C.2 混凝土本构关系

C.2.1 混凝土的抗压强度及抗拉强度的平均值  $ f_{cm} $  、  $ f_{tm} $  可按下列公式计算：

 $$ f_{\mathrm{c m}}=f_{\mathrm{c k}}/(1-1.645\delta_{\mathrm{c}}) $$ 

 $$ f_{\mathrm{tm}}=f_{\mathrm{tk}}/(1-1.645\delta_{\mathrm{c}}) $$ 

式中： $ f_{cm} $ 、 $ f_{ck} $ ——混凝土抗压强度的平均值、标准值；

 $ f_{tm} $ 、 $ f_{tk} $ ——混凝土抗拉强度的平均值、标准值；

 $ \delta_{c} $ ——混凝土强度变异系数，宜根据试验统计确定。

C.2.2 本节规定的混凝土本构模型应适用于下列条件：

1 混凝土强度等级 C20～C80；

2 混凝土质量密度  $ 2200 ~kg/m^{3} \sim 2400 ~kg/m^{3} $ ;

3 正常温度、湿度环境；

4 正常加载速度。

C.2.3 混凝土单轴受拉的应力-应变曲线（图 C.2.3）可按下列公式确定：

 $$ \sigma=(1-d_{\mathrm{t}})E_{\mathrm{c}}\varepsilon $$ 

 $$ d_{\mathrm{t}}=\left\{\begin{aligned}&1-\rho_{\mathrm{t}}\left[1.2-0.2x^{5}\right]&x\leqslant1\\ &1-\frac{\rho_{\mathrm{t}}}{\alpha_{\mathrm{t}}\left(x-1\right)^{1.7}+x}&x>1\end{aligned}\right. $$ 

 $$ x=\frac{\varepsilon}{\varepsilon_{\mathrm{t,r}}} $$ 

 $$ \rho_{\mathrm{r}}=\frac{f_{\mathrm{t},\mathrm{r}}}{E_{\mathrm{c}}\varepsilon_{\mathrm{t},\mathrm{r}}} $$ 

式中： $ \alpha_{t} $  ——混凝土单轴受拉应力-应变曲线下降段的参数值，按表 C.2.3 取用；

 $ f_{t,r} $  ——混凝土的单轴抗拉强度代表值，其值可根据实际结构分析需要分别取  $ f_{t} $ 、 $ f_{tk} $  或  $ f_{tm} $ ;

 $ \varepsilon_{t,r} $  ——与单轴抗拉强度代表值  $ f_{t,r} $  相应的混凝土峰值拉应变，按表 C.2.3 取用；

 $ d_{t} $  ——混凝土单轴受拉损伤演化参数。

<div style="text-align: center;">表 C.2.3 混凝土单轴受拉应力-应变曲线的参数取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>ft,r(N/mm2)</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.5</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>2.5</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>3.5</td><td style='text-align: center;'>4.0</td></tr><tr><td style='text-align: center;'>εt,r(10-6)</td><td style='text-align: center;'>65</td><td style='text-align: center;'>81</td><td style='text-align: center;'>95</td><td style='text-align: center;'>107</td><td style='text-align: center;'>118</td><td style='text-align: center;'>128</td><td style='text-align: center;'>137</td></tr><tr><td style='text-align: center;'>αt</td><td style='text-align: center;'>0.31</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>1.95</td><td style='text-align: center;'>2.81</td><td style='text-align: center;'>3.82</td><td style='text-align: center;'>5.00</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_8/imgs/img_in_image_box_246_504_552_760.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A02Z%2F-1%2F%2Ff77dc24eebb4d97f9f0a8fee9e0bdc6e2086baa55c6305fe0be070ff01f27819" alt="Image" width="39%" /></div>


<div style="text-align: center;">图 C.2.3 混凝土单轴应力-应变曲线</div>


注：混凝土受拉、受压的应力-应变曲线示意图绘于同一坐标系中，但取不同的比例。符号取“受拉为负、受压为正”。

C.2.4 混凝土单轴受压的应力-应变曲线（图 C.2.3）可按下列公式确定：

 $$ \sigma=(1-d_{\mathrm{c}})E_{\mathrm{c}}\varepsilon $$ 

 $$ d_{c}=\left\{\begin{aligned}1-\frac{\rho_{c}n}{n-1+x^{n}}\quad&x\leqslant1\\ 1-\frac{\rho_{c}}{\alpha_{c}\left(x-1\right)^{2}+x}\quad&x>1\end{aligned}\right. $$ 

 $$ \rho_{\mathrm{c}}=\frac{f_{\mathrm{c},\mathrm{r}}}{E_{\mathrm{c}}\boldsymbol{\varepsilon}_{\mathrm{c},\mathrm{r}}} $$ 

 $$ n=\frac{E_{\mathrm{c}}\varepsilon_{\mathrm{c},\mathrm{r}}}{E_{\mathrm{c}}\varepsilon_{\mathrm{c},\mathrm{r}}-f_{\mathrm{c},\mathrm{r}}} $$ 

 $$ x=\frac{\varepsilon}{\varepsilon_{\mathrm{c,r}}} $$ 

式中： $ \alpha_{c} $  ——混凝土单轴受压应力-应变曲线下降段参数值，按表 C.2.4 取用；

 $ f_{c,r} $  ——混凝土单轴抗压强度代表值，其值可根据实际结构分析的需要分别取  $ f_{c} $  、 $ f_{ck} $  或  $ f_{cm} $  ；

 $ \varepsilon_{c,r} $  ——与单轴抗压强度  $ f_{c,r} $  相应的混凝土峰值压应变，按表 C.2.4 取用；

 $ d_{c} $  ——混凝土单轴受压损伤演化参数。

<div style="text-align: center;">表 C.2.4 混凝土单轴受压应力-应变曲线的参数取值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>f c,r(N/mm²)</td><td style='text-align: center;'>20</td><td style='text-align: center;'>25</td><td style='text-align: center;'>30</td><td style='text-align: center;'>35</td><td style='text-align: center;'>40</td><td style='text-align: center;'>45</td><td style='text-align: center;'>50</td><td style='text-align: center;'>55</td><td style='text-align: center;'>60</td><td style='text-align: center;'>65</td><td style='text-align: center;'>70</td><td style='text-align: center;'>75</td><td style='text-align: center;'>80</td></tr><tr><td style='text-align: center;'>εc,r(10⁻⁶)</td><td style='text-align: center;'>1470</td><td style='text-align: center;'>1560</td><td style='text-align: center;'>1640</td><td style='text-align: center;'>1720</td><td style='text-align: center;'>1790</td><td style='text-align: center;'>1850</td><td style='text-align: center;'>1920</td><td style='text-align: center;'>1980</td><td style='text-align: center;'>2030</td><td style='text-align: center;'>2080</td><td style='text-align: center;'>2130</td><td style='text-align: center;'>2190</td><td style='text-align: center;'>2240</td></tr><tr><td style='text-align: center;'>αc</td><td style='text-align: center;'>0.74</td><td style='text-align: center;'>1.06</td><td style='text-align: center;'>1.36</td><td style='text-align: center;'>1.65</td><td style='text-align: center;'>1.94</td><td style='text-align: center;'>2.21</td><td style='text-align: center;'>2.48</td><td style='text-align: center;'>2.74</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.25</td><td style='text-align: center;'>3.50</td><td style='text-align: center;'>3.75</td><td style='text-align: center;'>3.99</td></tr><tr><td style='text-align: center;'>εcu/εc,r</td><td style='text-align: center;'>3.0</td><td style='text-align: center;'>2.6</td><td style='text-align: center;'>2.3</td><td style='text-align: center;'>2.1</td><td style='text-align: center;'>2.0</td><td style='text-align: center;'>1.9</td><td style='text-align: center;'>1.9</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.8</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'>1.7</td><td style='text-align: center;'>1.6</td></tr></table>

注： $ \varepsilon_{cu} $  为应力应变曲线下降段应力等于  $ 0.5 f_{c,r} $  时的混凝土压应变。

C.2.5 在重复荷载作用下，受压混凝土卸载及再加载应力路径（图 C.2.5）可按下列公式确定：

 $$ \sigma=E_{r}(\varepsilon-\varepsilon_{z}) $$ 

 $$ E_{\mathrm{r}}=\frac{\sigma_{\mathrm{u n}}}{\varepsilon_{\mathrm{u n}}-\varepsilon_{\mathrm{z}}} $$ 

 $$ \varepsilon_{z}=\varepsilon_{\mathrm{u n}}-\left[\frac{(\varepsilon_{\mathrm{u n}}+\varepsilon_{\mathrm{c a}})\sigma_{\mathrm{u n}}}{\sigma_{\mathrm{u n}}+E_{\mathrm{c}}\varepsilon_{\mathrm{c a}}}\right] $$ 

 $$ \varepsilon_{\mathrm{c a}}=\operatorname*{m a x}\left(\frac{\varepsilon_{\mathrm{c}}}{\varepsilon_{\mathrm{c}}+\varepsilon_{\mathrm{u n}}},\frac{0.09\varepsilon_{\mathrm{u n}}}{\varepsilon_{\mathrm{c}}}\right)\sqrt{\varepsilon_{\mathrm{c}}\varepsilon_{\mathrm{u n}}} $$ 

式中：σ——受压混凝土的压应力；

ε——受压混凝土的压应变；

 $ \varepsilon_{z} $  ——受压混凝土卸载至零应力点时的残余应变；

 $ E_{r} $  ——受压混凝土卸载/再加载的变形模量；

 $ \sigma_{un} $ 、 $ \varepsilon_{un} $ ——分别为受压混凝土从骨架线开始卸载时的应力和应变；

 $ \varepsilon_{ca} $  ——附加应变；

 $ \varepsilon_{c} $ ——混凝土受压峰值应力对应的应变。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_10/imgs/img_in_chart_box_223_446_570_690.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A03Z%2F-1%2F%2Fe1bac6a9536d434cc562c97d71b1d83b630359c5469e92571dd7d9fad84dfded" alt="Image" width="44%" /></div>


<div style="text-align: center;">图 C.2.5 重复荷载作用下混凝土应力-应变曲线</div>


C.2.6 混凝土在双轴加载、卸载条件下的本构关系可采用损伤模型或弹塑性模型。弹塑性本构关系可采用弹塑性增量本构理论，损伤本构关系按下列公式确定：

1 双轴受拉区 $ \left(\sigma_{1}^{\prime}<0,\sigma_{2}^{\prime}<0\right) $ 

1）加载方程

 $$ \left\{\begin{aligned}\sigma_{1}\\ \sigma_{2}\end{aligned}\right\}=(1-d_{\mathrm{t}})\left\{\begin{aligned}\sigma_{1}^{\prime}\\ \sigma_{2}^{\prime}\end{aligned}\right\} $$ 

 $$ \varepsilon_{\mathrm{t,e}}=-\sqrt{\frac{1}{1-\nu^{2}}\left[(\varepsilon_{1})^{2}+(\varepsilon_{2})^{2}+2\nu\varepsilon_{1}\varepsilon_{2}\right]} $$ 

 $$ \left\{\begin{aligned}\sigma_{1}^{\prime}\\ \sigma_{2}^{\prime}\end{aligned}\right\}=\frac{E_{\mathrm{c}}}{1-\nu^{2}}\left[\begin{matrix}1&\nu\\ \nu&1\end{matrix}\right]\left\{\begin{aligned}\varepsilon_{1}\\ \varepsilon_{2}\end{aligned}\right\} $$ 

式中： $ d_{t} $  ——受拉损伤演化参数，可由式（C.2.3-2）计算，

其中  $ x = \frac{\varepsilon_{t,e}}{\varepsilon_{t}} $ ;

 $ \varepsilon_{t,e} $  ——受拉能量等效应变；

 $ \sigma_{1}^{\prime} $ ， $ \sigma_{2}^{\prime} $ ——有效应力；

 $ \nu $ ——混凝土泊松比，可取0.18～0.22。

2）卸载方程

 $$ \left\{\begin{aligned}\sigma_{1}-\sigma_{un,1}\\ \sigma_{2}-\sigma_{un,2}\end{aligned}\right\}=(1-d_{t})\frac{E_{c}}{1-\nu^{2}}\left[\begin{matrix}1&\nu\\ \nu&1\end{matrix}\right]\left\{\begin{aligned}\varepsilon_{1}-\varepsilon_{un,1}\\ \varepsilon_{2}-\varepsilon_{un,2}\end{aligned}\right\} $$ 

式中： $ \sigma_{un,1} $ 、 $ \sigma_{un,2} $ 、 $ \varepsilon_{un,1} $ 、 $ \varepsilon_{un,2} $  ——二维卸载点处的应力、应变。

在加载方程中，损伤演化参数应采用即时应变换算得到的能量等效应变计算；卸载方程中的损伤演化参数应采用卸载点处的应变换算的能量等效应变计算，并且在整个卸载和再加载过程中保持不变。

2 双轴受压区 $ \left(\sigma_{1}^{\prime}\geqslant0,\sigma_{2}^{\prime}\geqslant0\right) $ 

1）加载方程

 $$ \left\{\begin{aligned}\sigma_{1}\\ \sigma_{2}\end{aligned}\right\}=(1-d_{\mathrm{c}})\left\{\begin{aligned}\sigma_{1}^{\prime}\\ \sigma_{2}^{\prime}\end{aligned}\right\} $$ 

 $$ \begin{aligned}\varepsilon_{\mathrm{c},\mathrm{e}}&=\frac{1}{(1-\nu^{2})(1-\alpha_{\mathrm{s}})}\left[\alpha_{\mathrm{s}}(1+\nu)(\varepsilon_{1}+\varepsilon_{2})\right.\\&\left.+\sqrt{(\varepsilon_{1}+\nu\varepsilon_{2})^{2}+(\varepsilon_{2}+\nu\varepsilon_{1})^{2}-(\varepsilon_{1}+\nu\varepsilon_{2})(\varepsilon_{2}+\nu\varepsilon_{1})}\right]\end{aligned} $$ 

 $$ \alpha_{\mathrm{s}}=\frac{r-1}{2r-1} $$ 

式中： $ d_{c} $  ——受压损伤演化参数，可由公式（C.2.4-2）计算，

其中  $ x = \frac{\varepsilon_{c,e}}{\varepsilon_{c}} $ ;

 $ \varepsilon_{c,e} $  ——受压能量等效应变；

 $ \alpha_{s} $  ——受剪屈服参数；

r——双轴受压强度提高系数，取值范围1.15～1.30，可根据实验数据确定，在缺乏实验数据时可取1.2。

2）卸载方程

 $$ \left\{\begin{aligned}\sigma_{1}-\sigma_{un,1}\\ \sigma_{2}-\sigma_{un,2}\end{aligned}\right\}=(1-\eta_{d} d_{c})\frac{E_{c}}{1-\nu^{2}}\begin{bmatrix}1&\nu\\ \nu&1\end{bmatrix}\left\{\begin{aligned}\varepsilon_{1}-\varepsilon_{un,1}\\ \varepsilon_{2}-\varepsilon_{un,2}\end{aligned}\right\} $$ 

 $$ \eta_{\mathrm{d}}=\frac{\varepsilon_{\mathrm{c,e}}}{\varepsilon_{\mathrm{c,e}}+\varepsilon_{\mathrm{ca}}} $$ 

式中： $ \eta_{d} $  ——塑性因子；

 $ \varepsilon_{ca} $  ——附加应变，按公式（C.2.5-4）计算。

3 双轴拉压区 $ \left(\sigma_{1}^{\prime}<0,\sigma_{2}^{\prime}\geqslant0\right) $ 或 $ \left(\sigma_{1}^{\prime}\geqslant0,\sigma_{2}^{\prime}<0\right) $ 

1）加载方程

 $$ \left\{\begin{aligned}\sigma_{1}\\ \sigma_{2}\end{aligned}\right\}=\left[\begin{aligned}(1-d_{\mathrm{t}})&0\\ 0&(1-d_{\mathrm{c}})\end{aligned}\right]\left\{\begin{aligned}\sigma_{1}^{\prime}\\ \sigma_{2}^{\prime}\end{aligned}\right\} $$ 

 $$ \varepsilon_{\mathrm{t,e}}=-\sqrt{\frac{1}{(1-\nu^{2})}\varepsilon_{1}(\varepsilon_{1}+\gamma\varepsilon_{2})} $$ 

式中： $ d_{t} $  ——受拉损伤演化参数，可由式（C.2.3-2）计算，

其中  $ x = \frac{\varepsilon_{t,e}}{\varepsilon_{t}} $ ;

 $ d_{c} $  ——受压损伤演化参数，可由式（C.2.4-2）计算，

其中  $ x=\frac{\varepsilon_{c,e}}{\varepsilon_{c}} $ ;

 $ \varepsilon_{t,e} $ 、 $ \varepsilon_{c,e} $  ——能量等效应变，其中， $ \varepsilon_{c,e} $  按式（C.2.6-6）计算， $ \varepsilon_{t,e} $  可按式（C.2.6-11）计算。

2）卸载方程

 $$ \left\{\begin{aligned}\sigma_{1}-\sigma_{un,1}\\ \sigma_{2}-\sigma_{un,2}\end{aligned}\right\}=\frac{E_{c}}{1-\nu^{2}}\left[\begin{matrix}(1-d_{t})&(1-d_{t})\nu\\ (1-\eta_{d}d_{c})\nu&(1-\eta_{d}d_{c})\end{matrix}\right]\left\{\begin{aligned}\varepsilon_{1}-\varepsilon_{un,1}\\ \varepsilon_{2}-\varepsilon_{un,2}\end{aligned}\right\} $$ 

式中： $ \eta_{d} $  ——塑性因子。

C.3 钢筋-混凝土粘结滑移本构关系

C.3.1 混凝土与热轧带肋钢筋之间的粘结应力-滑移（ $ \tau-s $ ）本构关系曲线（图 C.3.1）可按下列规定确定，曲线特征点的参数值可按表 C.3.1 取用。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_13/imgs/img_in_chart_box_208_407_601_604.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A04Z%2F-1%2F%2F06e33113b21d455265ed8663e61d4c20292301498a611ef356e66cc84507698c" alt="Image" width="50%" /></div>


<div style="text-align: center;">图 C.3.1 混凝土与钢筋间的粘结应力-滑移曲线</div>


线性段

 $$ \tau=k_{1}s\quad0\leqslant s\leqslant s_{cr} $$ 

 $$  劈裂段 \quad\tau=\tau_{cr}+k_{2}\left(s-s_{cr}\right)\quad s_{cr}<s\leqslant s_{u} $$ 

 $$ \begin{aligned} 下降段 \quad&\tau=\tau_{u}+k_{3}(s-s_{u})\quad s_{u}<s\leqslant s_{r}\end{aligned} $$ 

残余段

 $$ \tau=\tau_{r}\quad s>s_{r} $$ 

卸载段

 $$ \tau=\tau_{\mathrm{u n}}+k_{1}(s-s_{\mathrm{u n}}) $$ 

式中： $ \tau $ ——混凝土与热轧带肋钢筋之间的粘结应力（N/mm $ ^{2} $ ）；

s——混凝土与热轧带肋钢筋之间的相对滑移（mm）；

 $ k_{1} $ ——线性段斜率， $ \tau_{cr}/s_{cr} $ ;

 $ k_{2} $ ——劈裂段斜率， $ \left(\tau_{\mathrm{u}}-\tau_{\mathrm{cr}}\right)/\left(s_{\mathrm{u}}-s_{\mathrm{cr}}\right) $ ;

 $ k_{3} $ ——下降段斜率， $ \left(\tau_{\mathrm{r}}-\tau_{\mathrm{u}}\right)/\left(s_{\mathrm{r}}-s_{\mathrm{u}}\right) $ ;

 $ \tau_{un} $ ——卸载点的粘结应力（N/mm $ ^{2} $ ）；

 $ s_{un} $  ——卸载点的相对滑移（mm）。

<div style="text-align: center;">表 C.3.1 混凝土与钢筋间粘结应力-滑移曲线的参数值</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>特征点</td><td colspan="2">劈裂（cr）</td><td colspan="2">峰值（u）</td><td colspan="2">残余（r）</td></tr><tr><td style='text-align: center;'>粘结应力（N/mm²）</td><td style='text-align: center;'>τcr</td><td style='text-align: center;'>2.5ft,r</td><td style='text-align: center;'>τu</td><td style='text-align: center;'>3ft,r</td><td style='text-align: center;'>τr</td><td style='text-align: center;'>ft,r</td></tr><tr><td style='text-align: center;'>相对滑移（mm）</td><td style='text-align: center;'>scr</td><td style='text-align: center;'>0.025d</td><td style='text-align: center;'>su</td><td style='text-align: center;'>0.04d</td><td style='text-align: center;'>sr</td><td style='text-align: center;'>0.55d</td></tr></table>

注：表中 d 为钢筋直径（mm）； $ f_{t,r} $  为混凝土的抗拉强度特征值（N/mm $ ^{2} $ ）。

C.3.2 除热轧带肋钢筋外，其余种类钢筋的粘结应力-滑移本构关系曲线的参数值可根据试验确定。

C.4 混凝土强度准则

C.4.1 当采用混凝土多轴强度准则进行承载力计算时，材料强度参数取值及抗力计算应符合下列原则：

1 当采用弹塑性方法确定作用效应时，混凝土强度指标宜取平均值；

2 当采用弹性方法或弹塑性方法分析结果进行构件承载力计算时，混凝土强度指标可根据需要，取其强度设计值（ $ f_{c} $  或  $ f_{t} $ ）或标准值（ $ f_{ck} $  或  $ f_{tk} $ ）。

3 采用弹性分析或弹塑性分析求得混凝土的应力分布和主应力值后，混凝土多轴强度验算应符合下列要求：

 $$ \left|\sigma_{i}\right|\leqslant\left|f_{i}\right|\quad(i=1,2,3) $$ 

式中： $ \sigma_{i} $ ——混凝土主应力值，受拉为负，受压为正，且 $ \sigma_{1}\geqslant\sigma_{2} $ 

 $ \geqslant\sigma_{3}; $ 

 $ f_{i} $ ——混凝土多轴强度代表值，受拉为负，受压为正，且

 $ f_{1}\geqslant f_{2}\geqslant f_{3} $ 

C. 4.2 在二轴应力状态下，混凝土的二轴强度由下列4条曲线连成的封闭曲线（图 C.4.2）确定；也可以根据表 C.4.2-1、表 C.4.2-2 和表 C.4.2-3 所列的数值内插取值。

强度包络曲线方程应符合下列公式的规定：

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_15/imgs/img_in_image_box_182_90_621_461.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A05Z%2F-1%2F%2F12601f1db77cbc144e23eee84c06ca3d65aad6f36c390bdf3c0c898a59ffcb67" alt="Image" width="56%" /></div>


<div style="text-align: center;">图 C.4.2 混凝土二轴应力的强度包络图</div>


 $$ \left\{\begin{aligned}L_{1}:\quad&f_{1}^{2}+f_{2}^{2}-2\nu f_{1}f_{2}=(f_{\mathrm{t},\mathrm{r}})^{2}\\ L_{2}:\quad\sqrt{f_{1}^{2}+f_{2}^{2}-f_{1}f_{2}}-\alpha_{\mathrm{s}}\left(f_{1}+f_{2}\right)=(1-\alpha_{\mathrm{s}})f_{\mathrm{c},\mathrm{r}}\\ L_{3}:\quad&\frac{f_{2}}{f_{\mathrm{c},\mathrm{r}}}-\frac{f_{1}}{f_{\mathrm{t},\mathrm{r}}}=1\\ L_{4}:\quad&\frac{f_{1}}{f_{\mathrm{c},\mathrm{r}}}-\frac{f_{2}}{f_{\mathrm{t},\mathrm{r}}}=1\end{aligned}\right. $$ 

式中： $ \alpha_{s} $  ——受剪屈服参数，由公式（C.2.6-7）确定。

<div style="text-align: center;">表 C.4.2-1 混凝土在二轴拉-压应力状态下的抗拉、抗压强度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>f2/ft,r</td><td style='text-align: center;'>0</td><td style='text-align: center;'>-0.1</td><td style='text-align: center;'>-0.2</td><td style='text-align: center;'>-0.3</td><td style='text-align: center;'>-0.4</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.6</td><td style='text-align: center;'>-0.7</td><td style='text-align: center;'>-0.8</td><td style='text-align: center;'>-0.9</td><td style='text-align: center;'>-1.0</td></tr><tr><td style='text-align: center;'>f1/fc,r</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0</td></tr></table>

<div style="text-align: center;">表 C.4.2-2 混凝土在二轴受压状态下的抗压强度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>f1/fc,r</td><td style='text-align: center;'>1.0</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.10</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>1.29</td><td style='text-align: center;'>1.25</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.16</td></tr><tr><td style='text-align: center;'>f2/fc,r</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.074</td><td style='text-align: center;'>0.16</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.88</td><td style='text-align: center;'>1.03</td><td style='text-align: center;'>1.11</td><td style='text-align: center;'>1.16</td></tr></table>

<div style="text-align: center;">表 C.4.2-3 混凝土在二轴受拉状态下的抗拉强度</div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>f1/ft,r</td><td style='text-align: center;'>-0.79</td><td style='text-align: center;'>-0.7</td><td style='text-align: center;'>-0.6</td><td style='text-align: center;'>-0.5</td><td style='text-align: center;'>-0.4</td><td style='text-align: center;'>-0.3</td><td style='text-align: center;'>-0.2</td><td style='text-align: center;'>-0.1</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>f2/ft,r</td><td style='text-align: center;'>-0.79</td><td style='text-align: center;'>-0.86</td><td style='text-align: center;'>-0.93</td><td style='text-align: center;'>-0.97</td><td style='text-align: center;'>-1.00</td><td style='text-align: center;'>-1.02</td><td style='text-align: center;'>-1.02</td><td style='text-align: center;'>-1.02</td><td style='text-align: center;'>-1.00</td></tr></table>

C. 4.3 混凝土在三轴应力状态下的强度可按下列规定确定：

1 在三轴受拉（拉-拉-拉）应力状态下，混凝土的三轴抗拉强度  $ f_{3} $  均可取单轴抗拉强度的 0.9 倍；

2 三轴拉压（拉-拉-压、拉-压-压）应力状态下混凝土的三轴抗压强度  $ f_{1} $  可根据应力比  $ \sigma_{3}/\sigma_{1} $  和  $ \sigma_{2}/\sigma_{1} $  按图 C.4.3-1 确定，或根据表 C.4.3-1 内插取值，其最高强度不宜超过单轴抗压强度的 1.2 倍；

<div style="text-align: center;">表 C.4.3-1 混凝土在三轴拉-压状态下抗压强度的调整系数  $ (f_{1}/f_{c,r}) $ </div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>$ \sigma_{2}/\sigma_{1} $</td><td style='text-align: center;'>-0.75</td><td style='text-align: center;'>-0.50</td><td style='text-align: center;'>-0.25</td><td style='text-align: center;'>-0.10</td><td style='text-align: center;'>-0.05</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0.25</td><td style='text-align: center;'>0.35</td><td style='text-align: center;'>0.36</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.75</td><td style='text-align: center;'>1.00</td></tr><tr><td style='text-align: center;'>$ \sigma_{3}/\sigma_{1} $</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>-1.00</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td><td style='text-align: center;'>0</td></tr><tr><td style='text-align: center;'>-0.75</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td><td style='text-align: center;'>0.05</td></tr><tr><td style='text-align: center;'>-0.50</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td><td style='text-align: center;'>0.10</td></tr><tr><td style='text-align: center;'>-0.25</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td><td style='text-align: center;'>0.20</td></tr><tr><td style='text-align: center;'>-0.12</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td><td style='text-align: center;'>0.30</td></tr><tr><td style='text-align: center;'>-0.10</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td><td style='text-align: center;'>0.40</td></tr><tr><td style='text-align: center;'>-0.08</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td><td style='text-align: center;'>0.50</td></tr><tr><td style='text-align: center;'>-0.05</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td><td style='text-align: center;'>0.60</td></tr><tr><td style='text-align: center;'>-0.04</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td><td style='text-align: center;'>0.70</td></tr><tr><td style='text-align: center;'>-0.02</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td><td style='text-align: center;'>0.80</td></tr><tr><td style='text-align: center;'>-0.01</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td><td style='text-align: center;'>0.90</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td></tr></table>

注：正值为压，负值为拉。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_17/imgs/img_in_chart_box_137_89_661_485.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A06Z%2F-1%2F%2F735cff0cd32e1a7b90fdcd1b550aaf3c8130c08cda07e3f190c2daab02a3364a" alt="Image" width="67%" /></div>


<div style="text-align: center;">图 C.4.3-1 三轴拉-压应力状态下混凝土的三轴抗压强度</div>


3 三轴受压（压-压-压）应力状态下混凝土的三轴抗压强度  $ f_{1} $  可根据应力比  $ \sigma_{3}/\sigma_{1} $  和  $ \sigma_{2}/\sigma_{1} $  按图 C.4.3-2 确定，或根据表 C.4.3-2 内插取值，其最高强度不宜超过单轴抗压强度的 3 倍。

<div style="text-align: center;">表 C.4.3-2 混凝土在三轴受压状态下抗压强度的提高系数  $ \left(f_{1}/f_{c,r}\right) $ </div>



<table border=1 style='margin: auto; width: max-content;'><tr><td style='text-align: center;'>$ \sigma_{2}/\sigma_{1} $</td><td rowspan="2">0</td><td rowspan="2">0.05</td><td rowspan="2">0.10</td><td rowspan="2">0.15</td><td rowspan="2">0.20</td><td rowspan="2">0.25</td><td rowspan="2">0.30</td><td rowspan="2">0.40</td><td rowspan="2">0.60</td><td rowspan="2">0.80</td><td rowspan="2">1.00</td></tr><tr><td style='text-align: center;'>$ \sigma_{3}/\sigma_{1} $</td></tr><tr><td style='text-align: center;'>0</td><td style='text-align: center;'>1.00</td><td style='text-align: center;'>1.05</td><td style='text-align: center;'>1.10</td><td style='text-align: center;'>1.15</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td><td style='text-align: center;'>1.20</td></tr><tr><td style='text-align: center;'>0.05</td><td style='text-align: center;'>—</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td><td style='text-align: center;'>1.40</td></tr><tr><td style='text-align: center;'>0.08</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td><td style='text-align: center;'>1.64</td></tr><tr><td style='text-align: center;'>0.10</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td><td style='text-align: center;'>1.80</td></tr><tr><td style='text-align: center;'>0.12</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td><td style='text-align: center;'>2.00</td></tr><tr><td style='text-align: center;'>0.15</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td><td style='text-align: center;'>2.30</td></tr><tr><td style='text-align: center;'>0.18</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td><td style='text-align: center;'>2.72</td></tr><tr><td style='text-align: center;'>0.20</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>—</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td><td style='text-align: center;'>3.00</td></tr></table>

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_18/imgs/img_in_chart_box_190_99_697_481.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A06Z%2F-1%2F%2F820cd2b71a306b72c19c74597e391260d75846bb59562a017f98912c3f9dac2c" alt="Image" width="64%" /></div>


<div style="text-align: center;">图 C.4.3-2 三轴受压状态下混凝土的三轴抗压强度</div>
