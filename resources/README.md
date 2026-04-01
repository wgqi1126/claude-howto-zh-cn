<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 品牌素材

Claude How To 项目的完整 Logo、图标与网站图标（favicon）集合。所有素材均采用 V3.0 设计：指南针与代码括号（`>`）符号，象征在代码中的引导式导航——采用黑/白/灰配色，并以亮绿色（#22C55E）作为强调色。

## 目录结构

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 Logo - 浅色模式 (520×120px)
│   └── claude-howto-logo-dark.svg  # 主 Logo - 深色模式 (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # 应用图标 - 浅色模式 (256×256px)
│   └── claude-howto-icon-dark.svg  # 应用图标 - 深色模式 (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px（主用）
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 中的补充素材：
```
assets/logo/
├── logo-full.svg       # 图形 + 文字标（横向）
├── logo-mark.svg       # 仅指南针符号 (120×120px)
├── logo-wordmark.svg   # 仅文字
├── logo-icon.svg       # 应用图标 (512×512，圆角)
├── favicon.svg         # 16×16 优化版
├── logo-white.svg      # 深色背景用白色版
└── logo-black.svg      # 黑色单色版
```

## 素材概览

### 设计理念（V3.0）

**指南针与代码括号** —— 引导与代码的结合：
- **指南针外环** = 导航、辨明方向
- **北针（绿色）** = 方向、学习路径上的进展
- **南针（黑色）** = 扎根、扎实基础
- **`>` 括号** = 终端提示符、代码、CLI 语境
- **刻度线** = 精确、结构化学习

### Logo

**文件**：
- `logos/claude-howto-logo.svg`（浅色模式）
- `logos/claude-howto-logo-dark.svg`（深色模式）

**规格**：
- **尺寸**：520×120 px
- **用途**：带文字标的主品牌 Logo
- **使用场景**：
  - 网站页眉
  - README 徽章
  - 营销物料
  - 印刷品
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白底）与深色（#0A0A0A 背景）

### 图标

**文件**：
- `icons/claude-howto-icon.svg`（浅色模式）
- `icons/claude-howto-icon-dark.svg`（深色模式）

**规格**：
- **尺寸**：256×256 px
- **用途**：应用图标、头像、缩略图
- **使用场景**：
  - 应用图标
  - 个人资料头像
  - 社交媒体缩略图
  - 文档页眉
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白底）与深色（#0A0A0A 背景）

**设计元素**：
- 带方位与间方位刻度的指南针外环
- 绿色北针（方向/引导）
- 黑色南针（基础）
- 居中的 `>` 代码括号（终端/CLI）
- 绿色中心点强调

### Favicon

针对网页使用优化的多种尺寸：

| 文件 | 尺寸 | DPI | 用途 |
|------|------|-----|------|
| `favicon-16.svg` | 16×16 px | 1x | 浏览器标签页（旧版浏览器） |
| `favicon-32.svg` | 32×32 px | 1x | 标准浏览器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 屏幕 |
| `favicon-128.svg` | 128×128 px | 2x | Apple 触摸图标、书签 |
| `favicon-256.svg` | 256×256 px | 4x | 现代浏览器、PWA 图标 |

**优化说明**：
- 16px：极简几何——仅外环、指针与 V 形饰线
- 32px：增加方位刻度
- 64px 及以上：含间方位刻度的完整细节
- 各尺寸与主图标视觉一致
- SVG 格式可在任意尺寸下保持清晰

## HTML 集成

### 基础 Favicon 配置

```html
<!-- 浏览器 favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple 触摸图标（移动设备主屏幕） -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA 与现代浏览器 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整配置

```html
<head>
  <!-- 主 favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple 触摸图标 -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA 图标 -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest 引用（若使用 manifest.json） -->
  <meta name="theme-color" content="#000000">
</head>
```

## 配色

### 主色
- **黑色**：`#000000`（主文案、描边、南针）
- **白色**：`#FFFFFF`（浅色背景）
- **灰色**：`#6B7280`（次要文字、细小刻度）

### 强调色
- **亮绿色**：`#22C55E`（北针、中心点、强调线——仅作点缀，勿作大面积背景）

### 深色模式
- **背景**：`#0A0A0A`（近黑）

### CSS 变量
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 配置
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用建议
- 主文案与结构元素使用黑色
- 次要/辅助元素使用灰色
- 绿色**仅**用于强调——指针、圆点、强调线
- 勿将绿色用作背景色
- 保持 WCAG AA 对比度（最低 4.5:1）

## 设计规范

### Logo 使用
- 置于白色或深色（#0A0A0A）背景上
- 等比缩放
- Logo 周围保留净空（至少为 Logo 高度的一半）
- 按背景选用提供的浅色/深色变体

### Icon 使用
- 使用标准尺寸：16、32、64、128、256px
- 保持指南针比例
- 等比缩放

### Favicon 使用
- 按场景选用合适尺寸
- 16–32px：浏览器标签、书签
- 64px：站点图标等
- 128px 及以上：Apple/Android 主屏幕

## SVG 优化

所有 SVG 均为扁平设计，无渐变或滤镜：
- 干净的描边几何
- 无嵌入位图
- 路径已优化
- 响应式 viewBox

网页优化示例：
```bash
# 在保持质量的前提下压缩 SVG
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG 转换

将 SVG 转为 PNG 以兼容旧浏览器：

```bash
# 使用 ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# 使用 Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 无障碍

- 高对比度（符合 WCAG AA——最低 4.5:1）
- 简洁几何形状，各尺寸均可辨识
- 可缩放矢量格式
- 图标内不含文字（文字单独置于文字标）
- 含义不依赖红绿配色区分

## 署名

这些素材属于 Claude How To 项目。

**许可**：MIT（见项目 LICENSE 文件）

## 版本历史

- **v3.0**（2026 年 2 月）：指南针 + 括号设计，黑/白/灰 + 绿色强调配色
- **v2.0**（2026 年 1 月）：受 Claude 启发的 12 射线星爆设计，翡翠色系
- **v1.0**（2026 年 1 月）：基于六边形的进阶图标初版

---

**最近更新**：2026 年 2 月  
**当前版本**：3.0（指南针-括号）  
**全部素材**：可用于生产的 SVG，完全可缩放，符合 WCAG AA 可访问性
