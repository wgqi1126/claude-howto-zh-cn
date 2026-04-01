# Claude How To - 设计系统

## 视觉识别

### 图标设计理念：指南针与代码尖括号

Claude How To 图标采用 **指南针与 `>` 代码尖括号**，象征在代码中的引导式导航：

```
     N (绿色)
     ▲
     │
W ───>─── E     指南针 = 引导/方向
     │          > 尖括号 = 代码/终端/CLI
     ▼
     S (黑色)
```

由此带来：
- **视觉清晰**：一眼传达「代码导航指南」
- **符号含义**：指南针 = 辨向；`>` = 代码/终端
- **可缩放性**：从 16px 到 512px 任意尺寸均可用
- **品牌一致**：极简配色，契合开发者工具气质

---

## 色彩系统

### 色板

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Black (Primary) | `#000000` | 0, 0, 0 | 主描边、正文、南端指针 |
| White (Background) | `#FFFFFF` | 255, 255, 255 | 浅色背景 |
| Gray (Secondary) | `#6B7280` | 107, 114, 128 | 次要刻度、次要文字 |
| Bright Green (Accent) | `#22C55E` | 34, 197, 94 | 北端指针、中心点、强调线 |
| Near Black (Dark BG) | `#0A0A0A` | 10, 10, 10 | 深色模式背景 |

### 对比度（WCAG）

- Black on White（白底黑字）：**21:1** AAA
- Gray on White（白底灰字）：**4.6:1** AA
- Green on White（白底绿色）：**3.2:1**（仅作装饰，不用于正文）
- White on Dark（深色底白字）：**19.5:1** AAA

### 强调色规则

**亮绿（#22C55E）仅用于高亮：**
- 指南针北针
- 中心点
- 强调下划线/边框
- 不得用作背景色
- 不得用于正文

---

## 字体

### Logo 字体
- **Family**：Inter, SF Pro Display, -apple-system, Segoe UI, sans-serif
- **「Claude」**：42px，字重 700（粗体），黑色
- **「How-To」**：32px，字重 500（中等），灰色（#6B7280）
- **副标题**：10px，字重 500，灰色，字间距 1.5px，大写

### 界面字体
- **Family**：Inter, SF Pro，系统字体（sans-serif）
- **Weight**：400-600
- **Style**：简洁、易读

---

## 图标细节

### 指南针规格

指南针标识由以下几何元素构成：

```
Element             | Stroke/Fill    | Color
--------------------|----------------|------------------
Outer ring          | 3px stroke     | Black / White (dark mode)
North tick          | 2.5px stroke   | Black / White (dark mode)
Other cardinal ticks| 2px stroke     | Gray / White 50% (dark mode)
Intercardinal ticks | 1.5px stroke   | Gray / White 40% (dark mode)
North needle        | filled polygon | #22C55E (always green)
South needle        | filled polygon | Black / White (dark mode)
> bracket           | 3px stroke     | Black / White (dark mode)
Center dot          | filled circle  | #22C55E (always green)
```

### 尺寸递进

```
16px  → 仅外环、指针与尖括号（最简）
32px  → 增加正方位刻度
64px  → 增加间方位刻度
128px → 完整细节，各元素清晰
256px → 细节最丰富，线宽更粗
```

---

## 尺寸规范

### Logo 尺寸

- **最小**：宽度 200px（网页）
- **推荐**：520px（设计稿原始尺寸）
- **最大**：无上限（矢量格式）
- **宽高比**：约 4.3:1（宽:高）

### 图标尺寸

- **最小**：16px（favicon）
- **推荐**：64–256px（应用、头像）
- **最大**：无上限（矢量格式）
- **宽高比**：1:1（正方形）

---

## 间距与对齐

### Logo 留白

```
┌─────────────────────────────────────┐
│                                     │
│        最小安全留白                  │
│         (logo 高度 / 2)            │
│                                     │
│    [COMPASS]  Claude                │
│               How-To                │
│                                     │
└─────────────────────────────────────┘
```

### 图标中心点

所有图标以其画布中心为对齐基准：
- 256px 画布：中心在 128×128
- 128px 画布：中心在 64×64
- 与其他 UI 元素对齐一致

---

## 可访问性

### 色彩对比
- 所有文字满足 WCAG AA（最低 4.5:1）
- 绿色强调为装饰性，不承担信息传达
- 不依赖红绿区分信息

### 可缩放性
- 矢量格式保证任意尺寸清晰
- 几何图形在 16px 仍可辨识
- 按可用尺寸递进细节

---

## 应用示例

### 网页页头
- 尺寸：520×120px logo
- 文件：`logos/claude-howto-logo.svg`
- 背景：白色或深色（#0A0A0A）
- 内边距：最少 20px

### 应用图标
- 尺寸：256×256px
- 文件：`icons/claude-howto-icon.svg`
- 背景：白色或深色
- 用途：应用快捷方式、头像

### 浏览器 Favicon
- 尺寸：主用 32px，备用 16px
- 文件：`favicons/favicon-32.svg`
- 格式：SVG，显示清晰

### 社交媒体
- 头像：256×256px 图标
- 横幅：520×120px logo（居中）

### 文档
- 章标题：Logo 按比例缩放适配
- 节图标：64×64px favicon
- 行内：32×32px favicon

---

## 文件格式说明

### SVG 结构

所有 SVG 为扁平化设计：
- 无渐变（仅纯色）
- 无滤镜效果（无模糊、发光或阴影）
- 清晰的描边与填充几何
- 使用 viewBox 实现响应式缩放
- 代码可读、含注释

### 跨浏览器兼容性

- Chrome/Edge：完全支持
- Firefox：完全支持
- Safari：完全支持
- iOS Safari：完全支持
- 所有现代浏览器：完全支持

---

## 自定义

### 更换强调色

若要使用其他强调色做变体：

1. 将所有 `#22C55E` 替换为你的强调色
2. 装饰元素对比度保持高于 3:1
3. 黑/白/灰结构保持不变

### 缩放

```css
svg {
  width: 256px;
  height: 256px;
}
```

SVG 通过 viewBox 自动缩放 — 无需额外 transform。

---

## 版本控制

在 git 中跟踪设计变更：
- 正常版本管理 SVG 文件（文本格式）
- 有重大设计变更时打 tag 发布
- 提交时包含 DESIGN-SYSTEM.md

---

**最后更新**：2026 年 2 月  
**设计系统版本**：3.0
