# React Link Demo1

一个使用 React 和 Ink 构建的命令行界面(CLI)应用演示项目。

## 项目简介

本项目展示了如何在命令行环境中使用 React 和 Ink 库创建交互式终端用户界面。主要功能包括：

- 使用 React 组件化方式构建 CLI 应用
- 利用 Ink 提供的终端渲染能力
- 实现动态计数器功能，展示状态管理和副作用处理

## 技术栈

- **React** (v19.2.6): 用于构建用户界面的 JavaScript 库
- **Ink** (v7.0.3): 用于在终端中渲染 React 组件的库
- **Babel**: JavaScript 编译器，支持 JSX 语法转换
  - @babel/cli
  - @babel/core
  - @babel/preset-react


```
npm install -D @babel/core @babel/cli
npm install --save-dev @babel/preset-react
```
## 项目结构

```
React-link-demo1/
├── index.js          # 主入口文件，包含 Counter 组件
├── cli.js            # Babel 编译后的输出文件
├── babel.config.json # Babel 配置文件
├── package.json      # 项目依赖和脚本配置
└── node_modules/     # 项目依赖包
```

## 安装与运行

### 前置条件

确保已安装 Node.js 和 npm

### 安装依赖

```bash
npm install
```

### 运行应用

```bash
node index.js
```

或者运行编译后的版本：

```bash
node cli.js
```

## 功能说明

### Counter 组件

应用核心是一个计数器组件，具有以下特性：

- **自动递增**: 每 100 毫秒自动增加计数值
- **彩色输出**: 使用绿色文本显示计数结果
- **资源清理**: 组件卸载时正确清除定时器，避免内存泄漏

## 开发说明

### Babel 配置

项目使用 `@babel/preset-react` 来支持 JSX 语法，配置文件位于 `babel.config.json`。

### 编译代码

如果需要手动编译 JSX 代码：

```bash
npx babel index.js --out-file cli.js
```

## 注意事项

- 本示例主要用于学习目的，展示 React + Ink 在 CLI 应用中的基本用法
- 当前没有配置测试脚本，可根据需要添加单元测试

## 许可证

ISC License


