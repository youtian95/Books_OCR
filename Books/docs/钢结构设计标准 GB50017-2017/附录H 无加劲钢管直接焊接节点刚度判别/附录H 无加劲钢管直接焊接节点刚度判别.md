

## 附录 H 无加劲钢管直接焊接节点刚度判别

H.0.1 空腹桁架、单层网格结构中无加劲圆钢管直接焊接节点的刚度应按下列规定计算。

1 平面 T 形（或 Y 形）节点：

1) 支管轴力作用下的节点刚度  $ K_{nT}^{j} $  应按下式计算（图 13.3.2-2 和图 13.3.2-3）：

 $$ K_{\mathrm{n T}}^{\mathrm{j}}=0.105E D\big(\sin\theta\big)^{-2.36}\gamma^{-1.90}\tau^{-0.12}e^{2.44\beta} $$ 

2) 支管平面内弯矩作用下的节点刚度  $ K_{mT}^{j} $  应按下式计算（图 13.3.3-1）：

 $$ K_{\mathrm{m T}}^{\mathrm{j}}=0.362E D^{3}\left(\sin\theta\right)^{-1.47}\gamma^{-1.79}\tau^{-0.08}\beta^{2.29} $$ 

其中， $ 30^{\circ}\leq\theta\leq90^{\circ},0.2\leq\beta\leq1.0,10\leq\gamma\leq50,0.2\leq\tau\leq1.0 $ 。

2 平面/微曲面 X 形节点：

1) 支管轴力作用下的节点刚度  $ K_{nX}^{j} $  应按下式计算（图 13.3.2-1）：

 $$ K_{\mathrm{nX}}^{\mathrm{j}}=0.952ED\big(\sin\theta\big)^{-1.74}\gamma^{0.97\beta^{2.58}-2.65}\exp\big(1.16\beta\big) $$ 

其中， $ 60^{\circ}\leq\theta\leq90^{\circ},0^{\circ}\leq\varphi\leq10^{\circ},0.5\leq\beta\leq0.9,5\leq\gamma\leq25,0.5\leq\tau\leq1.0 $ 。

2) 支管平面内弯矩作用下的节点刚度  $ K_{mX}^{j} $  应按下式计算（图 13.3.3-2）：

 $$ K_{\mathrm{m X}}^{\mathrm{j}}=0.303E D\beta^{2.35}\gamma^{0.3\beta^{13.62}-1.75}\left(\sin\theta\right)^{2.89\beta-2.52} $$ 

3) 支管平面外弯矩作用下的节点刚度  $ K_{mox}^{j} $  应按下式计算（图 13.3.3-2）：

 $$ K_{\mathrm{m o X}}^{\mathrm{j}}=2.083E D^{3}\left(\sin\theta\right)^{-1.23}\left(\cos\theta\right)^{6.85}\gamma^{-2.44}\beta^{2.27} $$ 

其中， $ 30^{\circ}<\theta<90^{\circ},0^{\circ}<\varphi<30^{\circ},0.2\leq\beta\leq0.9,5\leq\gamma\leq50,0.2\leq\tau\leq0.8 $ 。

式中：E ——弹性模量（N/mm $ ^{2} $ ）；

D——主管的外径（mm）;

 $ \beta $ ——支管和主管的外径比值；

γ——主管的半径和壁厚的比值；

 $ \tau $ ——支管和主管的壁厚比值；

 $ \theta $ ——主支管轴线间小于直角的夹角；

 $ \varphi $ ——空间管节点支管的横向夹角，即支管轴线在主管横截面所在平面投影的夹角。

H.0.2 空腹桁架中无加劲方管直接焊接节点的刚度计算宜符合下列规定。

当  $ \beta \leq 0.85 $  时，T 形节点的轴向刚度  $ K_{n} $  可按下列公式计算：

 $$ K_{\mathrm{n}}=\frac{2Et^{3}}{b^{2}\left(1-\beta\right)^{3}}\left[\left(1+\beta\right)\left(1-\beta\right)^{3/2}+2\eta+\sqrt{1-\beta}\right]\mu_{1} $$ 

 $$ \mu_{1}=\left(2.06-1.75\beta\right)\left(1.09\eta^{2}-1.37\eta+1.43\right) $$ 

当 $ \beta\leq0.85 $ 时，T形节点的弯曲刚度 $ K_{m} $ 可按下式计算：

 $$ K_{\mathrm{m}}=5.49\big(\beta^{3}-1.298\beta^{2}+0.59\beta-0.073\big)\big(\eta^{2}+0.066\eta+0.1\big)\big(t^{2}-1.659t+0.711\big) $$ 

式中：t ——矩形主管的壁厚（mm）；

b——矩形主管的宽度（mm）；

 $ \beta $ ——支管截面宽度与主管截面宽度的比值；

 $ \eta $ ——支管截面高度宽与主管截面宽度的比值。

H.0.3 空腹桁架采用无加劲钢管直接焊接节点时的应按下列规定进行刚度判别：

1 符合 T 形节点相应的几何参数的适用范围。

2 当空腹桁架跨数为偶数时，在节点平面内弯曲刚度与支管线刚度之比不小于 $ \frac{60}{1+G} $ 时，可将节点视为刚接，否则应视为半刚接；其中G为该节点相邻的支管线刚度与主管线刚度的比值。

3 当空腹桁架跨数为奇数时，在与跨中相邻节点的平面内弯曲刚度与支管线刚度之比不小于 $ \frac{1080G}{(3G+1)(3G+4)} $ 时，可将该节点视为刚接；在除与跨中相邻节点以外的其他节点的平面内弯曲刚度与支管线刚度之比不小于 $ \frac{60}{1+G} $ 时，可将该节点视为刚接。