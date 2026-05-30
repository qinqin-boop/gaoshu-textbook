/* ============================================================
 *  concept-anim.js — 高数下册 概念动画库 (零依赖, canvas + rAF)
 *  用法: 在课文知识点旁放
 *      <figure class="concept-anim" data-anim="vector-add"></figure>
 *  本脚本自动挂载: 标题 + 画布 + 播放/暂停 + (可选)滑块 + 说明.
 *  仅在进入视口时运行, 离开即暂停, 省 CPU.
 * ============================================================ */
(function () {
  'use strict';
  const REG = {};
  function register(name, def) { REG[name] = def; }

  // ---------- 通用绘图助手 ----------
  const C = {
    navy: '#1a365d', gold: '#c9a227', rust: '#8b3a0a', green: '#2d6e2d',
    orange: '#c2410c', grey: '#94a3b8', faint: '#e5e5e0', bg: '#fff'
  };
  function arrow(ctx, x1, y1, x2, y2, color, w) {
    w = w || 2.5;
    const a = Math.atan2(y2 - y1, x2 - x1), h = 9 + w;
    ctx.strokeStyle = color; ctx.fillStyle = color; ctx.lineWidth = w;
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - h * Math.cos(a - 0.4), y2 - h * Math.sin(a - 0.4));
    ctx.lineTo(x2 - h * Math.cos(a + 0.4), y2 - h * Math.sin(a + 0.4));
    ctx.closePath(); ctx.fill();
  }
  function dline(ctx, x1, y1, x2, y2, color) {
    ctx.save(); ctx.strokeStyle = color || C.grey; ctx.lineWidth = 1.3;
    ctx.setLineDash([5, 4]);
    ctx.beginPath(); ctx.moveTo(x1, y1); ctx.lineTo(x2, y2); ctx.stroke();
    ctx.restore();
  }
  function label(ctx, txt, x, y, color, size) {
    ctx.fillStyle = color || C.navy;
    ctx.font = (size || 14) + 'px Georgia, serif';
    ctx.fillText(txt, x, y);
  }
  // 简易 3D -> 2D 等距投影 (绕 z 轴 yaw 旋转 + 固定俯仰)
  function proj(x, y, z, yaw, cx, cy, s) {
    const cosA = Math.cos(yaw), sinA = Math.sin(yaw);
    const X = x * cosA - y * sinA;          // 水平
    const Y = x * sinA + y * cosA;          // 进深
    const tilt = 0.5;
    return [cx + X * s, cy - z * s + Y * s * tilt];
  }

  // ================= 动画定义 =================

  // 1) 向量加法 · 平行四边形法则
  register('vector-add', {
    title: '向量加法 · 平行四边形法则',
    caption: '把 $\\vec b$ 平移到 $\\vec a$ 的终点, 首尾相接得和 $\\vec a+\\vec b$ (绿); 它正是平行四边形的对角线。',
    draw(ctx, e) {
      const { w, h, t } = e, ox = w * 0.18, oy = h * 0.82;
      const ax = 120, ay = -40, bx = 60, by = -90;
      // b 平移进度 0->1 循环
      const k = (Math.sin(t * 1.1) * 0.5 + 0.5);
      ctx.clearRect(0, 0, w, h);
      // 平行四边形虚线
      dline(ctx, ox + ax, oy + ay, ox + ax + bx, oy + ay + by, C.faint);
      dline(ctx, ox + bx, oy + by, ox + ax + bx, oy + ay + by, C.faint);
      arrow(ctx, ox, oy, ox + ax, oy + ay, C.navy);
      arrow(ctx, ox, oy, ox + bx, oy + by, C.rust);
      // 平移中的 b: 从原点滑向 a 的终点
      const sx = ox + ax * k, sy = oy + ay * k;
      arrow(ctx, sx, sy, sx + bx, sy + by, C.orange, 2);
      // 和向量
      arrow(ctx, ox, oy, ox + ax + bx, oy + ay + by, C.green, 3);
      label(ctx, 'a', ox + ax * 0.5 + 6, oy + ay * 0.5 - 4, C.navy);
      label(ctx, 'b', ox + bx * 0.5 - 16, oy + by * 0.5, C.rust);
      label(ctx, 'a+b', ox + (ax + bx) * 0.5 - 6, oy + (ay + by) * 0.5 + 18, C.green);
    }
  });

  // 2) 数量积 · 投影 (可拖角度)
  register('dot-product', {
    title: '数量积 · 投影几何意义',
    caption: '$\\vec a\\cdot\\vec b=|\\vec a||\\vec b|\\cos\\theta$ = ($\\vec a$ 在 $\\vec b$ 上的投影长) × $|\\vec b|$。拖滑块转 $\\vec a$: 钝角时投影为负 → 点乘变负。',
    slider: { label: '夹角 θ', min: 0, max: 180, value: 50, step: 1 },
    draw(ctx, e) {
      const { w, h } = e, ox = w * 0.5, oy = h * 0.78;
      const theta = (e.slider != null ? e.slider : 50) * Math.PI / 180;
      const La = 120, Lb = 150;
      ctx.clearRect(0, 0, w, h);
      // b 沿水平正方向
      const bx = ox + Lb, by = oy;
      arrow(ctx, ox, oy, bx, by, C.rust);
      // a 与 b 夹角 theta (逆时针向上)
      const ax = ox + La * Math.cos(theta), ay = oy - La * Math.sin(theta);
      arrow(ctx, ox, oy, ax, ay, C.navy);
      // a 在 b 上投影
      const projLen = La * Math.cos(theta);
      const px = ox + projLen, py = oy;
      dline(ctx, ax, ay, px, py, C.grey);
      ctx.strokeStyle = C.green; ctx.lineWidth = 5;
      ctx.beginPath(); ctx.moveTo(ox, oy + 0); ctx.lineTo(px, py); ctx.stroke();
      label(ctx, 'a', ax + 6, ay, C.navy);
      label(ctx, 'b', bx + 6, by + 4, C.rust);
      const dot = (La * Lb * Math.cos(theta) / 100).toFixed(0);
      label(ctx, '投影 = |a|cosθ ' + (projLen < 0 ? '< 0' : '≥ 0'), ox - 60, h - 10, C.green, 13);
      label(ctx, 'a·b ∝ ' + dot, w - 90, 22, dot < 0 ? C.orange : C.navy, 14);
    }
  });

  // 3) 向量积 · 右手定则 (3D 旋转)
  register('cross-product', {
    title: '向量积 · 右手定则',
    caption: '$\\vec a\\times\\vec b$ 垂直于 $\\vec a,\\vec b$ 所在平面, 模 = 平行四边形面积 $|\\vec a||\\vec b|\\sin\\theta$, 方向由右手定则定。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.56, s = Math.min(w, h) * 0.16;
      const yaw = t * 0.5;
      ctx.clearRect(0, 0, w, h);
      const O = proj(0, 0, 0, yaw, cx, cy, s);
      const A = proj(2, 0, 0, yaw, cx, cy, s);    // a
      const B = proj(0.6, 1.7, 0, yaw, cx, cy, s); // b
      const Ptip = proj(2.6, 1.7, 0, yaw, cx, cy, s); // a+b 角
      const Cr = proj(0, 0, 1.8, yaw, cx, cy, s);  // a×b 沿 +z
      // 平行四边形面 (半透明)
      ctx.fillStyle = 'rgba(201,162,39,0.18)';
      ctx.beginPath(); ctx.moveTo(O[0], O[1]); ctx.lineTo(A[0], A[1]);
      ctx.lineTo(Ptip[0], Ptip[1]); ctx.lineTo(B[0], B[1]); ctx.closePath(); ctx.fill();
      arrow(ctx, O[0], O[1], A[0], A[1], C.navy);
      arrow(ctx, O[0], O[1], B[0], B[1], C.rust);
      arrow(ctx, O[0], O[1], Cr[0], Cr[1], C.green, 3);
      label(ctx, 'a', A[0] + 6, A[1] + 4, C.navy);
      label(ctx, 'b', B[0] + 6, B[1] + 4, C.rust);
      label(ctx, 'a×b', Cr[0] + 6, Cr[1], C.green);
      label(ctx, '面积 = |a×b|', cx - 30, h - 8, C.gold, 12);
    }
  });

  // 4) 旋转曲面生成
  register('surface-revolution', {
    title: '旋转曲面的生成',
    caption: '一条母线绕轴旋转一周, 扫出旋转曲面。每个点的轨迹是一个垂直于轴的圆 (纬圆)。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.5, s = Math.min(w, h) * 0.22;
      ctx.clearRect(0, 0, w, h);
      // 旋转轴 (z)
      const axBot = proj(0, 0, -1.6, 0, cx, cy, s), axTop = proj(0, 0, 1.6, 0, cx, cy, s);
      dline(ctx, axBot[0], axBot[1], axTop[0], axTop[1], C.grey);
      // 母线: z 从 -1..1, 半径 r(z)=0.6+0.5*z^2 (类似抛物)
      const prof = z => 0.55 + 0.5 * z * z;
      const sweep = (Math.sin(t * 0.6) * 0.5 + 0.5) * 2 * Math.PI; // 当前已扫角度
      // 已扫出的纬圆 (淡)
      ctx.strokeStyle = 'rgba(26,54,93,0.18)'; ctx.lineWidth = 1;
      for (let zi = -1; zi <= 1.001; zi += 0.25) {
        const r = prof(zi);
        ctx.beginPath();
        for (let a = 0; a <= sweep + 0.001; a += 0.18) {
          const p = proj(r * Math.cos(a), r * Math.sin(a), zi, 0, cx, cy, s);
          a === 0 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
        }
        ctx.stroke();
      }
      // 当前母线位置 (旋转到 sweep)
      ctx.strokeStyle = C.rust; ctx.lineWidth = 2.5; ctx.beginPath();
      for (let zi = -1; zi <= 1.001; zi += 0.1) {
        const r = prof(zi);
        const p = proj(r * Math.cos(sweep), r * Math.sin(sweep), zi, 0, cx, cy, s);
        zi === -1 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();
      // 原始母线 (角度 0)
      ctx.strokeStyle = C.navy; ctx.lineWidth = 2; ctx.beginPath();
      for (let zi = -1; zi <= 1.001; zi += 0.1) {
        const r = prof(zi);
        const p = proj(r, 0, zi, 0, cx, cy, s);
        zi === -1 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();
      label(ctx, '母线', proj(prof(1), 0, 1, 0, cx, cy, s)[0] + 6, proj(prof(1), 0, 1, 0, cx, cy, s)[1], C.navy, 12);
    }
  });

  function fact(n) { let r = 1; for (let i = 2; i <= n; i++) r *= i; return r; }
  // 画椭圆等高线族 (世界系: cx,cy 中心, s 缩放, ax/ay 半轴比例)
  function ellipseContours(ctx, cx, cy, s, axf, ayf, cs) {
    ctx.strokeStyle = 'rgba(26,54,93,0.28)'; ctx.lineWidth = 1;
    cs.forEach(c => {
      ctx.beginPath();
      for (let a = 0; a <= 6.30; a += 0.12) {
        const x = axf(c) * Math.cos(a), y = ayf(c) * Math.sin(a);
        const px = cx + x * s, py = cy - y * s;
        a === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py);
      }
      ctx.closePath(); ctx.stroke();
    });
  }

  // ====== 第9章 多元微分 ======

  // 5) 偏导数 = 切片曲线的切线斜率
  register('partial-derivative', {
    title: '偏导数 · 切片求斜率',
    caption: '固定 $y=y_0$ 用平面切曲面, 得切片曲线 (红); 它在某点的切线斜率 (绿) 就是偏导数 $\\partial z/\\partial x$。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.6, s = Math.min(w, h) * 0.2;
      const yaw = 0.6 + 0.18 * Math.sin(t * 0.25);
      const f = (x, y) => 0.45 * (x * x - y * y);
      ctx.clearRect(0, 0, w, h);
      // 网格
      ctx.strokeStyle = 'rgba(148,163,184,0.5)'; ctx.lineWidth = 1;
      for (let yj = -1.5; yj <= 1.5001; yj += 0.5) {
        ctx.beginPath();
        for (let xi = -1.5; xi <= 1.5001; xi += 0.15) {
          const p = proj(xi, yj, f(xi, yj), yaw, cx, cy, s);
          xi === -1.5 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
        }
        ctx.stroke();
      }
      for (let xi = -1.5; xi <= 1.5001; xi += 0.5) {
        ctx.beginPath();
        for (let yj = -1.5; yj <= 1.5001; yj += 0.15) {
          const p = proj(xi, yj, f(xi, yj), yaw, cx, cy, s);
          yj === -1.5 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
        }
        ctx.stroke();
      }
      // 切片 y=y0 (扫动)
      const y0 = 1.2 * Math.sin(t * 0.7);
      ctx.strokeStyle = C.rust; ctx.lineWidth = 2.6; ctx.beginPath();
      for (let xi = -1.5; xi <= 1.5001; xi += 0.08) {
        const p = proj(xi, y0, f(xi, y0), yaw, cx, cy, s);
        xi === -1.5 ? ctx.moveTo(p[0], p[1]) : ctx.lineTo(p[0], p[1]);
      }
      ctx.stroke();
      // 切线 @ x0
      const x0 = 0.9 * Math.sin(t * 0.9), m = 0.9 * x0, d = 0.6;
      const z0 = f(x0, y0);
      const T1 = proj(x0 - d, y0, z0 - m * d, yaw, cx, cy, s);
      const T2 = proj(x0 + d, y0, z0 + m * d, yaw, cx, cy, s);
      arrow(ctx, T1[0], T1[1], T2[0], T2[1], C.green, 2.6);
      const P = proj(x0, y0, z0, yaw, cx, cy, s);
      ctx.fillStyle = C.green; ctx.beginPath(); ctx.arc(P[0], P[1], 4, 0, 6.3); ctx.fill();
      label(ctx, '∂z/∂x ≈ ' + m.toFixed(2), 12, 22, C.green, 14);
      label(ctx, '切片 y = ' + y0.toFixed(2), 12, h - 10, C.rust, 13);
    }
  });

  // 6) 梯度下降
  register('gradient-descent', {
    title: '梯度下降 · 滚向谷底',
    caption: '沿负梯度 $-\\nabla f$ 方向每步下降 (橙箭头), 小球逐步滚到最低点。这是 SGD 等优化算法的几何原型。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.52, s = Math.min(w, h) * 0.12;
      // f = x^2/4 + y^2, ∇f=(x/2, 2y)
      ctx.clearRect(0, 0, w, h);
      ellipseContours(ctx, cx, cy, s, c => 2 * Math.sqrt(c), c => Math.sqrt(c), [0.5, 1, 2, 4, 7]);
      const lr = 0.12, N = 26;
      const steps = Math.floor((t * 2) % (N + 8));
      let px = 3.6, py = 2.4;
      ctx.strokeStyle = C.navy; ctx.lineWidth = 1.6; ctx.beginPath();
      ctx.moveTo(cx + px * s, cy - py * s);
      let lastx = px, lasty = py;
      for (let i = 0; i < Math.min(steps, N); i++) {
        px -= lr * (px / 2) * 2; py -= lr * (2 * py) * 2;
        ctx.lineTo(cx + px * s, cy - py * s);
        lastx = px; lasty = py;
      }
      ctx.stroke();
      // 负梯度箭头
      const gx = lastx / 2, gy = 2 * lasty, gn = Math.hypot(gx, gy) || 1;
      arrow(ctx, cx + lastx * s, cy - lasty * s,
        cx + lastx * s - gx / gn * 34, cy - lasty * s + gy / gn * 34, C.orange, 2.4);
      ctx.fillStyle = C.rust; ctx.beginPath(); ctx.arc(cx + lastx * s, cy - lasty * s, 5.5, 0, 6.3); ctx.fill();
      label(ctx, '步 ' + Math.min(steps, N) + '/' + N, 12, 22, C.navy, 13);
      label(ctx, '−∇f', cx + lastx * s - gx / gn * 40, cy - lasty * s + gy / gn * 40, C.orange, 12);
    }
  });

  // 7) 方向导数与梯度
  register('directional-derivative', {
    title: '方向导数 · 梯度方向最陡',
    caption: '方向导数 $D_{\\vec u}f=\\nabla f\\cdot\\vec u$。转动 $\\vec u$: 与梯度 $\\nabla f$ (橙) 同向时值最大, 垂直时为 0。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.42, cy = h * 0.55, s = Math.min(w, h) * 0.13;
      ctx.clearRect(0, 0, w, h);
      ellipseContours(ctx, cx, cy, s, c => 2 * Math.sqrt(c), c => Math.sqrt(c), [0.5, 1, 2, 4, 7]);
      const x0 = 2.2, y0 = 1.0;              // 取值点
      const gx = x0 / 2, gy = 2 * y0, gn = Math.hypot(gx, gy);
      const ang = t * 0.9, ux = Math.cos(ang), uy = Math.sin(ang);
      const Dv = gx * ux + gy * uy;          // 方向导数
      // 梯度
      arrow(ctx, cx + x0 * s, cy - y0 * s, cx + x0 * s + gx / gn * 50, cy - y0 * s - gy / gn * 50, C.orange, 2.6);
      // 方向 u
      arrow(ctx, cx + x0 * s, cy - y0 * s, cx + x0 * s + ux * 46, cy - y0 * s - uy * 46, C.navy, 2.4);
      ctx.fillStyle = C.navy; ctx.beginPath(); ctx.arc(cx + x0 * s, cy - y0 * s, 4, 0, 6.3); ctx.fill();
      label(ctx, '∇f', cx + x0 * s + gx / gn * 56, cy - y0 * s - gy / gn * 56, C.orange, 12);
      label(ctx, 'u', cx + x0 * s + ux * 54, cy - y0 * s - uy * 54, C.navy, 12);
      // 数值条
      const bx = w - 60, by = h - 26, bh = (h - 50);
      ctx.fillStyle = '#eee'; ctx.fillRect(bx, 24, 26, bh);
      const frac = Math.max(0, Dv) / gn;
      ctx.fillStyle = Dv >= 0 ? C.green : C.orange;
      ctx.fillRect(bx, by - frac * bh, 26, frac * bh);
      label(ctx, 'Dᵤf=' + Dv.toFixed(2), bx - 36, 18, Dv >= 0 ? C.green : C.orange, 12);
    }
  });

  // ====== 第10章 重积分 ======

  // 8) 黎曼和逼近
  register('riemann-sum', {
    title: '积分 = 黎曼和的极限',
    caption: '小矩形求和逼近曲边面积, 分得越细越准。二重积分把这一思想推广到平面区域上的小块求和。',
    draw(ctx, e) {
      const { w, h, t } = e, pad = 30, x0 = pad, x1 = w - pad, y0 = h - 26, top = 18;
      const f = x => 0.55 + 0.32 * Math.sin(x * 2.2) + 0.18 * x; // x∈[0,1]
      ctx.clearRect(0, 0, w, h);
      const X = u => x0 + u * (x1 - x0), Y = v => y0 - v * (y0 - top);
      // 矩形
      const ns = [2, 4, 8, 16, 32, 64], n = ns[Math.floor(t / 1.2) % ns.length];
      ctx.fillStyle = 'rgba(45,110,45,0.22)'; ctx.strokeStyle = 'rgba(45,110,45,0.7)'; ctx.lineWidth = 1;
      for (let i = 0; i < n; i++) {
        const u = (i + 0.5) / n, hgt = f(u);
        const rx = X(i / n), rw = (x1 - x0) / n;
        ctx.fillRect(rx, Y(hgt), rw, y0 - Y(hgt));
        ctx.strokeRect(rx, Y(hgt), rw, y0 - Y(hgt));
      }
      // 曲线
      ctx.strokeStyle = C.navy; ctx.lineWidth = 2.4; ctx.beginPath();
      for (let u = 0; u <= 1.001; u += 0.02) { const px = X(u), py = Y(f(u)); u === 0 ? ctx.moveTo(px, py) : ctx.lineTo(px, py); }
      ctx.stroke();
      // 坐标轴
      ctx.strokeStyle = C.grey; ctx.lineWidth = 1; ctx.beginPath();
      ctx.moveTo(x0, y0); ctx.lineTo(x1, y0); ctx.moveTo(x0, y0); ctx.lineTo(x0, top); ctx.stroke();
      label(ctx, 'n = ' + n + ' 个小矩形', x0 + 4, 16, C.green, 14);
    }
  });

  // 9) 极坐标面积元 r dr dθ
  register('polar-element', {
    title: '极坐标面积元 dA = r·dr·dθ',
    caption: '极坐标下小块是扇环, 面积 $dA=r\\,dr\\,d\\theta$。离原点越远 (r 越大) 同样 $dr\\,d\\theta$ 的块越大 —— 这就是雅可比因子 $r$。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.92, s = Math.min(w * 0.5, h) * 0.95;
      ctx.clearRect(0, 0, w, h);
      // 极网格 (上半)
      ctx.strokeStyle = 'rgba(148,163,184,0.6)'; ctx.lineWidth = 1;
      for (let r = 0.2; r <= 1.001; r += 0.2) {
        ctx.beginPath(); ctx.arc(cx, cy, r * s, Math.PI, 2 * Math.PI); ctx.stroke();
      }
      for (let a = 0; a <= Math.PI + 0.01; a += Math.PI / 8) {
        ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(Math.PI + a) * s, cy - Math.sin(Math.PI + a) * 0);
        ctx.lineTo(cx - Math.cos(a) * s, cy - Math.sin(a) * s); ctx.stroke();
      }
      // 高亮一个扇环元 (θ 扫动, r 也变)
      const th = (t * 0.6) % Math.PI, dth = Math.PI / 8;
      const r = 0.4 + 0.4 * (Math.sin(t * 0.5) * 0.5 + 0.5), dr = 0.18;
      ctx.fillStyle = 'rgba(201,162,39,0.45)';
      ctx.beginPath();
      ctx.arc(cx, cy, r * s, Math.PI + th, Math.PI + th + dth);
      ctx.arc(cx, cy, (r + dr) * s, Math.PI + th + dth, Math.PI + th, true);
      ctx.closePath(); ctx.fill();
      ctx.strokeStyle = C.rust; ctx.lineWidth = 1.8; ctx.stroke();
      label(ctx, 'dA = r·dr·dθ', 12, 20, C.rust, 14);
      label(ctx, 'r = ' + r.toFixed(2), 12, 38, C.navy, 12);
    }
  });

  // ====== 第11章 曲线曲面积分 ======

  // 10) 向量场 + 沿路径环流
  register('vector-field-flow', {
    title: '向量场 · 沿路径做功',
    caption: '质点沿曲线移动, 每步累加 $\\vec F\\cdot d\\vec r$ (力在位移上的投影), 总和即曲线积分 $\\oint \\vec F\\cdot d\\vec r$。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.5, s = Math.min(w, h) * 0.16;
      // 旋转场 F=(-y, x)
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = 'rgba(148,163,184,0.8)'; ctx.fillStyle = 'rgba(148,163,184,0.8)';
      for (let gx = -2; gx <= 2.01; gx++) for (let gy = -1.4; gy <= 1.41; gy++) {
        const fx = -gy, fy = gx, n = Math.hypot(fx, fy) || 1, L = 14;
        const ox = cx + gx * s, oy = cy - gy * s;
        arrow(ctx, ox, oy, ox + fx / n * L, oy - fy / n * L, 'rgba(148,163,184,0.8)', 1.3);
      }
      // 路径: 半径 R 的圆
      const R = 1.4;
      ctx.strokeStyle = C.gold; ctx.lineWidth = 1.6; ctx.setLineDash([4, 3]);
      ctx.beginPath(); ctx.arc(cx, cy, R * s, 0, 6.3); ctx.stroke(); ctx.setLineDash([]);
      // 质点
      const ang = t * 0.8, qx = R * Math.cos(ang), qy = R * Math.sin(ang);
      const ox = cx + qx * s, oy = cy - qy * s;
      // F 与切向 dr
      const Fx = -qy, Fy = qx, dxr = -Math.sin(ang), dyr = Math.cos(ang);
      arrow(ctx, ox, oy, ox + Fx * s * 0.6, oy - Fy * s * 0.6, C.rust, 2.4);
      arrow(ctx, ox, oy, ox + dxr * 30, oy - dyr * 30, C.navy, 2);
      ctx.fillStyle = C.green; ctx.beginPath(); ctx.arc(ox, oy, 5, 0, 6.3); ctx.fill();
      label(ctx, 'F', ox + Fx * s * 0.6, oy - Fy * s * 0.6 - 4, C.rust, 12);
      label(ctx, 'dr', ox + dxr * 34, oy - dyr * 34, C.navy, 12);
      label(ctx, '∮ F·dr  (旋转场 → 环流 > 0)', 10, h - 10, C.green, 12);
    }
  });

  // ====== 第12章 无穷级数 ======

  // 11) 部分和收敛
  register('partial-sum', {
    title: '部分和收敛',
    caption: '几何级数 $\\sum 1/2^n = 1$。部分和 $S_n$ 随 n 增大越来越接近极限线 (虚线), 这就是"级数收敛"。',
    draw(ctx, e) {
      const { w, h, t } = e, pad = 34, x0 = pad, x1 = w - 14, yb = h - 24, top = 20;
      ctx.clearRect(0, 0, w, h);
      const N = 12, lim = 1;
      const X = i => x0 + (i / N) * (x1 - x0), Y = v => yb - v * (yb - top);
      // 极限线
      dline(ctx, x0, Y(lim), x1, Y(lim), C.rust);
      label(ctx, '极限 = 1', x1 - 64, Y(lim) - 6, C.rust, 12);
      // 轴
      ctx.strokeStyle = C.grey; ctx.lineWidth = 1; ctx.beginPath();
      ctx.moveTo(x0, yb); ctx.lineTo(x1, yb); ctx.moveTo(x0, yb); ctx.lineTo(x0, top); ctx.stroke();
      const shown = 1 + Math.floor((t * 1.5) % N);
      let S = 0;
      ctx.fillStyle = C.navy; ctx.strokeStyle = 'rgba(26,54,93,0.4)'; ctx.lineWidth = 1.4;
      ctx.beginPath();
      for (let n = 1; n <= shown; n++) {
        S += 1 / Math.pow(2, n);
        const px = X(n), py = Y(S);
        n === 1 ? ctx.moveTo(px, py) : ctx.lineTo(px, py);
      }
      ctx.stroke();
      S = 0;
      for (let n = 1; n <= shown; n++) {
        S += 1 / Math.pow(2, n);
        ctx.beginPath(); ctx.arc(X(n), Y(S), 3.5, 0, 6.3); ctx.fill();
      }
      label(ctx, 'S' + shown + ' = ' + S.toFixed(4), 10, 16, C.navy, 14);
    }
  });

  // 12) Taylor 多项式逼近
  register('taylor-approx', {
    title: 'Taylor 多项式逐阶逼近',
    caption: '$\\sin x$ 的 Taylor 多项式 (红) 随阶数升高, 在越来越宽的区间上贴合原函数 (蓝)。',
    draw(ctx, e) {
      const { w, h, t } = e, cx = w * 0.5, cy = h * 0.5, sx = w / 13, sy = h * 0.32;
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = C.grey; ctx.lineWidth = 1; ctx.beginPath();
      ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.moveTo(cx, 6); ctx.lineTo(cx, h - 6); ctx.stroke();
      // sin
      ctx.strokeStyle = C.navy; ctx.lineWidth = 2.4; ctx.beginPath();
      for (let px = 0; px <= w; px += 2) { const x = (px - cx) / sx, y = Math.sin(x); px === 0 ? ctx.moveTo(px, cy - y * sy) : ctx.lineTo(px, cy - y * sy); }
      ctx.stroke();
      // Taylor 至阶数
      const degs = [1, 3, 5, 7, 9, 11], deg = degs[Math.floor(t / 1.3) % degs.length];
      ctx.strokeStyle = C.rust; ctx.lineWidth = 2.2; ctx.beginPath();
      let started = false;
      for (let px = 0; px <= w; px += 2) {
        const x = (px - cx) / sx; let y = 0;
        for (let k = 0; 2 * k + 1 <= deg; k++) y += Math.pow(-1, k) * Math.pow(x, 2 * k + 1) / fact(2 * k + 1);
        if (Math.abs(y) > 3) { started = false; continue; }
        started ? ctx.lineTo(px, cy - y * sy) : (ctx.moveTo(px, cy - y * sy), started = true);
      }
      ctx.stroke();
      label(ctx, '阶数 = ' + deg, 12, 20, C.rust, 14);
    }
  });

  // 13) Fourier 级数逼近方波
  register('fourier-square', {
    title: 'Fourier 级数逼近方波',
    caption: '叠加越来越多正弦谐波 (红) 逼近方波 (灰)。谐波越多越像 —— 跳变处的小过冲即 Gibbs 现象。',
    draw(ctx, e) {
      const { w, h, t } = e, cy = h * 0.5, sy = h * 0.3, P = w;
      ctx.clearRect(0, 0, w, h);
      ctx.strokeStyle = C.grey; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(0, cy); ctx.lineTo(w, cy); ctx.stroke();
      // 目标方波
      ctx.strokeStyle = 'rgba(148,163,184,0.9)'; ctx.lineWidth = 1.6; ctx.beginPath();
      for (let px = 0; px <= w; px += 2) { const x = px / P * 4 * Math.PI; const sq = (Math.sin(x) >= 0 ? 1 : -1); ctx.lineTo(px, cy - sq * sy); }
      ctx.stroke();
      // 部分和
      const Ns = [1, 2, 3, 5, 8, 15], Nh = Ns[Math.floor(t / 1.3) % Ns.length];
      ctx.strokeStyle = C.rust; ctx.lineWidth = 2.2; ctx.beginPath();
      for (let px = 0; px <= w; px += 1) {
        const x = px / P * 4 * Math.PI; let y = 0;
        for (let k = 1; k <= 2 * Nh; k += 2) y += (4 / Math.PI) * Math.sin(k * x) / k;
        px === 0 ? ctx.moveTo(px, cy - y * sy) : ctx.lineTo(px, cy - y * sy);
      }
      ctx.stroke();
      label(ctx, '谐波数 = ' + Nh, 12, 20, C.rust, 14);
    }
  });

  // ---------- 挂载逻辑 ----------
  function mount(fig) {
    const name = fig.dataset.anim;
    const def = REG[name];
    if (!def) { fig.innerHTML = '<p style="color:#b91c1c">⚠ 未知动画: ' + name + '</p>'; return; }
    fig.classList.add('ca-ready');
    // 结构
    const bar = document.createElement('div'); bar.className = 'ca-bar';
    const ttl = document.createElement('span'); ttl.className = 'ca-title'; ttl.textContent = '🎬 ' + def.title;
    const btn = document.createElement('button'); btn.className = 'ca-btn'; btn.textContent = '⏸ 暂停';
    bar.appendChild(ttl); bar.appendChild(btn);
    const canvas = document.createElement('canvas'); canvas.className = 'ca-canvas';
    const cap = document.createElement('figcaption'); cap.className = 'ca-cap'; cap.innerHTML = def.caption || '';
    fig.appendChild(bar); fig.appendChild(canvas);

    let sliderEl = null;
    if (def.slider) {
      const wrap = document.createElement('div'); wrap.className = 'ca-slider';
      const lab = document.createElement('label'); lab.textContent = def.slider.label + ': ';
      const val = document.createElement('span'); val.className = 'ca-sval';
      sliderEl = document.createElement('input');
      sliderEl.type = 'range';
      sliderEl.min = def.slider.min; sliderEl.max = def.slider.max;
      sliderEl.step = def.slider.step || 1; sliderEl.value = def.slider.value;
      val.textContent = sliderEl.value;
      sliderEl.addEventListener('input', () => { val.textContent = sliderEl.value; });
      lab.appendChild(val);
      wrap.appendChild(lab); wrap.appendChild(sliderEl);
      fig.appendChild(wrap);
    }
    fig.appendChild(cap);

    const ctx = canvas.getContext('2d');
    let dpr = Math.min(window.devicePixelRatio || 1, 2);
    function resize() {
      const cw = fig.clientWidth || 320;
      const ch = Math.round(Math.min(cw * 0.62, 300));
      canvas.style.width = cw + 'px'; canvas.style.height = ch + 'px';
      canvas.width = cw * dpr; canvas.height = ch * dpr;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      canvas._w = cw; canvas._h = ch;
    }
    resize();
    window.addEventListener('resize', resize);

    let playing = false, raf = null, base = 0, acc = 0;
    function frame(now) {
      if (!playing) return;
      const tt = acc + (now - base) / 1000;
      def.draw(ctx, { w: canvas._w, h: canvas._h, t: tt,
        slider: sliderEl ? parseFloat(sliderEl.value) : null });
      raf = requestAnimationFrame(frame);
    }
    function play() {
      if (playing) return; playing = true; btn.textContent = '⏸ 暂停';
      base = performance.now(); raf = requestAnimationFrame(frame);
    }
    function pause() {
      if (!playing) return; playing = false; btn.textContent = '▶ 播放';
      acc += (performance.now() - base) / 1000; cancelAnimationFrame(raf);
    }
    btn.addEventListener('click', () => playing ? pause() : play());
    // 静态首帧
    def.draw(ctx, { w: canvas._w, h: canvas._h, t: 0, slider: sliderEl ? parseFloat(sliderEl.value) : null });
    // 滑块拖动时若暂停, 也重绘一帧
    if (sliderEl) sliderEl.addEventListener('input', () => {
      if (!playing) def.draw(ctx, { w: canvas._w, h: canvas._h, t: acc, slider: parseFloat(sliderEl.value) });
    });

    // 进视口才播, 离开就停
    const io = new IntersectionObserver(es => {
      es.forEach(en => en.isIntersecting ? play() : pause());
    }, { threshold: 0.15 });
    io.observe(fig);
  }

  function init() {
    document.querySelectorAll('figure.concept-anim:not(.ca-ready)').forEach(mount);
    // 若 KaTeX 在场, 渲染说明里的公式
    if (window.renderMathInElement) {
      document.querySelectorAll('figcaption.ca-cap').forEach(el => {
        try { window.renderMathInElement(el, { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false }); } catch (e) {}
      });
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
