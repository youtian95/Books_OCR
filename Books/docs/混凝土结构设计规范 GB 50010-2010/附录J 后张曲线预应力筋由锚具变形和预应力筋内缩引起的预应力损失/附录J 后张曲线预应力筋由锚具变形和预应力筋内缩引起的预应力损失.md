# 附录 J 后张曲线预应力筋由锚具变形和预应力筋内缩引起的预应力损失

J.0.1 在后张法构件中，应计算曲线预应力筋由锚具变形和预应力筋内缩引起的预应力损失。

1 反摩擦影响长度  $ l_{f} $ (mm)(图 J.0.1) 可按下列公式计算：

 $$ l_{\mathrm{f}}=\sqrt{\frac{a\cdot E_{\mathrm{p}}}{\Delta\sigma_{\mathrm{d}}}} $$ 

 $$ \Delta\sigma_{\mathrm{d}}=\frac{\sigma_{0}-\sigma_{l}}{l} $$ 

式中：a——张拉端锚具变形和预应力筋内缩值（mm），按本规范表10.2.2采用；

 $ \Delta\sigma_{d} $  ——单位长度由管道摩擦引起的预应力损失（MPa/mm）；

 $ \sigma_{0} $ ——张拉端锚下控制应力，按本规范第10.1.3条的规定采用；

 $ \sigma_{i} $ ——预应力筋扣除沿途摩擦损失后锚固端应力；

l——张拉端至锚固端的距离（mm）。

2 当  $ l_{f} \leqslant l $  时，预应力筋离张拉端 x 处考虑反摩擦后的预应力损失  $ \sigma_{l1} $ ，可按下列公式计算：

 $$ \sigma_{l1}=\Delta\sigma\frac{l_{\mathrm{f}}-x}{l_{\mathrm{f}}} $$ 

 $$ \Delta\sigma=2\Delta\sigma_{\mathrm{d}}l_{\mathrm{f}} $$ 

式中： $ \Delta\sigma $ ——预应力筋考虑反向摩擦后在张拉端锚下的预应力损失值。

3 当  $ l_{f} \geq l $  时，预应力筋离张拉端  $ x^{\prime} $  处考虑反向摩擦后的预应力损失  $ \sigma_{l1}^{\prime} $ ，可按下列公式计算：

 $$ \sigma_{l1}^{\prime}=\Delta\sigma^{\prime}-2x^{\prime}\Delta\sigma_{\mathrm{d}} $$ 

式中： $ \Delta\sigma^{\prime} $ ——预应力筋考虑反向摩擦后在张拉端锚下的预应力损失值，可按以下方法求得：在图J.0.1中设“ $ ca^{\prime}bd $ ”等腰梯形面积 $ A=a\cdot E_{p} $ ，试算得到cd，则 $ \Delta\sigma^{\prime}=cd $ 。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_50/imgs/img_in_image_box_184_216_611_502.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A18Z%2F-1%2F%2F9d13902e8a92a19b63dc576cf5b3105c2f1735f60603c1c09c33c639eabe50c8" alt="Image" width="54%" /></div>


<div style="text-align: center;">图 J.0.1 考虑反向摩擦后预应力损失计算</div>


注：1  $ caa' $  表示预应力筋扣除管道正摩擦损失后的应力分布线；

2 eaa' 表示  $ l_{1} \leqslant l $  时，预应力筋扣除管道正摩擦和内缩（考虑反摩擦）损失后的应力分布线；

3 db 表示  $ l_{f} > l $  时，预应力筋扣除管道正摩擦和内缩（考虑反摩擦）损失后的应力分布线。

J.0.2 两端张拉（分次张拉或同时张拉）且反摩擦损失影响长度有重叠时，在重叠范围内同一截面扣除正摩擦和回缩反摩擦损失后预应力筋的应力可取：两端分别张拉、锚固，分别计算正摩擦和回缩反摩擦损失，分别将张拉端锚下控制应力减去上述应力计算结果所得较大值。

J.0.3 常用束形的后张曲线预应力筋或折线预应力筋，由于锚具变形和预应力筋内缩在反向摩擦影响长度  $ l_{f} $  范围内的预应力损失值  $ \sigma_{l1} $ ，可按下列公式计算：

1 抛物线形预应力筋可近似按圆弧形曲线预应力筋考虑（图 J.0.3-1）。当其对应的圆心角  $ \theta \leqslant 45^{\circ} $  时（对无粘结预应力筋  $ \theta \leqslant 90^{\circ} $ ），预应力损失值  $ \sigma_{1} $  可按下列公式计算：

 $$ \sigma_{l1}=2\sigma_{\mathrm{c o n}}l_{\mathrm{f}}\Big(\frac{\mu}{r_{\mathrm{c}}}+\kappa\Big)\Big(1-\frac{x}{l_{\mathrm{f}}}\Big) $$ 

反向摩擦影响长度  $ l_{f} $  （m）可按下列公式计算：

 $$ l_{\mathrm{f}}=\sqrt{\frac{aE_{\mathrm{s}}}{1000\sigma_{\mathrm{con}}(\mu/r_{\mathrm{c}}+\kappa)}} $$ 

式中： $ r_{c} $  ——圆弧形曲线预应力筋的曲率半径（m）；

 $ \mu $ ——预应力筋与孔道壁之间的摩擦系数，按本规范表10.2.4采用；

 $ \kappa $ ——考虑孔道每米长度局部偏差的摩擦系数，按本规范表10.2.4采用；

x——张拉端至计算截面的距离（m）；

a——张拉端锚具变形和预应力筋内缩值（mm），按本规范表 10.2.2 采用；

 $ E_{s} $ ——预应力筋弹性模量。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_51/imgs/img_in_image_box_260_529_546_639.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A19Z%2F-1%2F%2Fae764ffb198831d168524f46f3e7e6a8ea94d1b2d48922b59a2a225ee840e140" alt="Image" width="36%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_51/imgs/img_in_image_box_252_652_546_821.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A19Z%2F-1%2F%2Fbde0c65b02a93592fbfbfe407f95e02ab05e2e21bfeab26f1dab2a004880382b" alt="Image" width="37%" /></div>


<div style="text-align: center;">图 J.0.3-1 圆弧形曲线预应力筋的预应力损失  $ \sigma_{l1} $ </div>


2 端部为直线（直线长度为  $ l_{0} $ ），而后由两条圆弧形曲线（圆弧对应的圆心角  $ \theta \leqslant 45^{\circ} $ ，对无粘结预应力筋取  $ \theta \leqslant 90^{\circ} $ ）组成的预应力筋（图 J.0.3-2），预应力损失值  $ \sigma_{l1} $  可按下列公式计算：

当 $ x \leqslant l_{0} $ 时

 $$ \sigma_{l1}=2i_{1}(l_{1}-l_{0})+2i_{2}(l_{f}-l_{1}) $$ 

当  $ l_{0}<x\leq l_{1} $  时

 $$ \sigma_{l1}=2i_{1}(l_{1}-x)+2i_{2}(l_{\mathrm{f}}-l_{1}) $$ 

当  $ l_{1}<x\leq l_{f} $  时

 $$ \sigma_{l1}=2i_{2}(l_{\mathrm{f}}-x) $$ 

反向摩擦影响长度  $ l_{f}(m) $  可按下列公式计算：

 $$ l_{\mathrm{f}}=\sqrt{\frac{aE_{\mathrm{s}}}{1000i_{2}}-\frac{i_{1}(l_{1}^{2}-l_{0}^{2})}{i_{2}}+l_{1}^{2}} $$ 

 $$ i_{\mathrm{1}}=\sigma_{\mathrm{a}}(\kappa+\mu/r_{\mathrm{c1}}) $$ 

 $$ i_{2}=\sigma_{\mathrm{b}}(\kappa+\mu/r_{\mathrm{c2}}) $$ 

式中： $ l_{1} $  ——预应力筋张拉端起点至反弯点的水平投影长度；

 $ i_{1} $ 、 $ i_{2} $ ——第一、二段圆弧形曲线预应力筋中应力近似直线变化的斜率；

 $ r_{c1} $ 、 $ r_{c2} $ ——第一、二段圆弧形曲线预应力筋的曲率半径；

 $ \sigma_{a} $ 、 $ \sigma_{b} $ ——预应力筋在a、b点的应力。

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_52/imgs/img_in_image_box_216_537_575_882.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A19Z%2F-1%2F%2Fc6129f7a69b7073e7e5a8dab530878941093dff5452686da9dfe8695a3a8a9a1" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 J.0.3-2 两条圆弧形曲线组成的预应力筋的预应力损失  $ \sigma_{11} $ </div>


3 当折线形预应力筋的锚固损失消失于折点 c 之外时（图 J.0.3-3），预应力损失值  $ \sigma_{1} $  可按下列公式计算：

当 $ x \leqslant l_{0} $ 时

<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_53/imgs/img_in_image_box_219_96_578_236.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A19Z%2F-1%2F%2F65702e4a09ffec18b5f41b3b1f160e9a4a40128812d45f93b935530e23060fd2" alt="Image" width="46%" /></div>


<div style="text-align: center;"><img src="https://pplines-online.bj.bcebos.com/deploy/official/paddleocr/pp-ocr-vl//6505bc93-8679-48a1-8b0a-c3e0c67d1bed/markdown_53/imgs/img_in_image_box_217_245_577_463.jpg?authorization=bce-auth-v1%2FALTAKzReLNvew3ySINYJ0fuAMN%2F2026-01-11T12%3A59%3A20Z%2F-1%2F%2F67b3bdc465a4b6a6692b35e77a55de53833cce32fd6a63360acbc9822fa3f429" alt="Image" width="46%" /></div>


<div style="text-align: center;">图 J.0.3-3 折线形预应力筋的预应力损失  $ \sigma_{l1} $ </div>


 $$ \sigma_{l1}=2\sigma_{1}+2i_{1}(l_{1}-l_{0})+2\sigma_{2}+2i_{2}(l_{\mathrm{f}}-l_{1})\mathrm{(J.0.3-9)} $$ 

当  $ l_{0}<x\leqslant l_{1} $  时

 $$ \sigma_{l1}=2i_{1}(l_{1}-x)+2\sigma_{2}+2i_{2}(l_{\mathrm{f}}-l_{1}) $$ 

当  $ l_{1}<x\leqslant l_{f} $  时

 $$ \sigma_{l1}=2i_{2}(l_{\mathrm{f}}-x) $$ 

反向摩擦影响长度  $ l_{f}(m) $  可按下列公式计算：

 $$ l_{f}=\sqrt{\frac{aE_{s}}{1000i_{2}}-\frac{i_{1}(l_{1}-l_{0})^{2}+2i_{1}l_{0}(l_{1}-l_{0})+2\sigma_{1}l_{0}+2\sigma_{2}l_{1}}{i_{2}}+l_{1}^{2}} $$ 

 $$ i_{1}=\sigma_{\mathrm{c o n}}(1-\mu\theta)\kappa $$ 

 $$ i_{2}=\sigma_{\mathrm{c o n}}\left[1-\kappa(l_{1}-l_{0})\right]\, (1 - \mu\theta)^{2}\kappa $$ 

 $$ \sigma_{1}=\sigma_{\mathrm{c o n}}\mu\theta $$ 

 $$ \sigma_{2}=\sigma_{\mathrm{c o n}}\big[1-\kappa(l_{1}-l_{0})\big]\, (1 - \mu\theta)\mu\theta $$ 

式中： $ i_{1} $  ——预应力筋 bc 段中应力近似直线变化的斜率；

 $ i_{2} $ ——预应力筋在折点 c 以外应力近似直线变化的斜率；

 $ l_{1} $ ——张拉端起点至预应力筋折点c的水平投影长度。
