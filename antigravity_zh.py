#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Antigravity zh-CN - lightweight translation-only patch.

Appends a DOM translator to dist/preload.js and a native-menu translator to
dist/menu.js. Does not touch app.asar, does not package an exe.

Usage:
    python antigravity_zh.py                 # apply
    python antigravity_zh.py --update        # after an Antigravity update: re-extract asar, then apply
    python antigravity_zh.py --restore       # remove the injected blocks
    python antigravity_zh.py --dry-run       # show what would change
    python antigravity_zh.py --dist "D:\\path\\to\\resources\\app\\dist"
"""
import argparse
import json
import os
import shutil
import struct
import subprocess
import sys

BEGIN = "/* >>> antigravity-zh-cn (begin) */"
END = "/* <<< antigravity-zh-cn (end) */"

DOM_JS = r"""
// Antigravity zh-CN DOM translator
(function() {
  if (globalThis.__antigravityZhDom) return;
  globalThis.__antigravityZhDom = true;

  const dictionary = {
    "(tell the agent what to do instead)": "(告诉智能体接下来该做什么)",
    "+ Add Folder": "+ 添加文件夹",
    "+ Add folder": "+ 添加文件夹",
    "+ New Conversation": "+ 新建对话",
    "A Google Cloud project is required to use Antigravity.": "使用 Antigravity 需要 Google Cloud 项目。",
    "A copy of the workspace snapshot recorded at this step.": "此步骤记录的工作区快照副本。",
    "A full copy of this workspace, uncommitted changes included.": "此工作区的完整副本，包含未提交的更改。",
    "A label for this computer when you connect from another device. Changing it reconnects.": "当从其他设备连接时用于标识此计算机的标签。更改该标签将重新连接。",
    "A license or project selection is required to use Antigravity.": "使用 Antigravity 需要许可证或项目选择。",
    "A shell setup script run before every command the agent executes.": "在智能体执行每条命令前运行的 Shell 初始化脚本。",
    "API Configuration": "API 配置",
    "API Key": "API 密钥",
    "About": "关于",
    "Accent": "强调色",
    "Accept Step": "接受步骤",
    "Access grants": "访问授权",
    "Account": "账号",
    "Account Settings": "账号设置",
    "Account connected.": "账户已连接。",
    "Action": "操作",
    "Action required": "需要处理",
    "Actions": "操作",
    "Active": "进行中",
    "Activity": "活动",
    "Actual behavior": "实际行为",
    "Actuation Permissions": "操作权限",
    "Add": "添加",
    "Add Context": "添加上下文",
    "Add Folder": "添加文件夹",
    "Add Hook Card": "添加钩子卡片",
    "Add MCP": "添加 MCP",
    "Add MCP +": "添加 MCP +",
    "Add MCP Server": "添加 MCP 服务器",
    "Add MCP Servers": "添加 MCP 服务器",
    "Add Terminal": "添加终端",
    "Add Workspace": "添加工作区",
    "Add folder": "添加文件夹",
    "Add inline comment": "添加行内评论",
    "Add terminal": "添加终端",
    "Add to Chat": "添加到对话",
    "Add to Chat/Quote": "添加到对话/引用",
    "Added (Staged)": "已添加 (已暂存)",
    "Address CLs needing attention": "处理需要关注的修改列表 (CL)",
    "Advanced": "高级",
    "Advanced Settings": "高级设置",
    "Agent Behavior": "智能体行为",
    "Agent Edits": "智能体编辑",
    "Agent Host Address": "智能体主机地址",
    "Agent Non-Workspace File Access": "智能体非工作区文件访问",
    "Agent Script": "智能体脚本",
    "Agent Settings": "智能体设置",
    "Agent always asks for review.": "智能体始终请求审阅。",
    "Agent can scroll on browser pages to access more content.": "智能体可以滚动浏览器页面以访问更多内容。",
    "Agent encountered an internal error.": "智能体遇到内部错误。",
    "Agent execution terminated due to error": "智能体执行因错误而终止",
    "Agent execution terminated due to error.": "智能体执行因错误而终止。",
    "Agent is thinking...": "智能体正在思考...",
    "Agent settings and permissions for conversations outside of projects.": "针对项目外对话的智能体设置和权限。",
    "Agent terminated due to error": "智能体因错误而终止",
    "Agents": "智能体",
    "All changes since": "所有更改自",
    "All terminal commands require review. The agent can read or write to any file in the machine.": "所有终端命令均需审阅。智能体可以读取或写入机器上的任何文件。",
    "All time": "全部时间",
    "Allow": "允许",
    "Allow List Terminal Commands": "终端命令允许列表",
    "Allow Once": "仅允许一次",
    "Allow execution of this command?": "允许执行此命令吗？",
    "Allow full browser script execution without prompting.": "允许执行完整的浏览器脚本而不提示。",
    "Allow read access to this path?": "允许读取此路径吗？",
    "Allow sandboxed commands to make network requests.": "允许沙盒中的命令发起网络请求。",
    "Allow write access to this path?": "允许写入此路径吗？",
    "Allow/deny": "允许/拒绝",
    "Allow/deny agent browser actuation access to specific URLs": "允许/拒绝智能体对特定 URL 的浏览器操作访问",
    "Allow/deny agent browser actuation access to specific URLs.": "允许/拒绝智能体对特定 URL 的浏览器操作权限。",
    "Allow/deny agent command execution outside the sandbox": "允许/拒绝智能体在沙盒外执行命令",
    "Allow/deny agent command execution outside the sandbox.": "允许/拒绝智能体在沙盒外部执行命令。",
    "Allow/deny agent read access to specific URLs or domains.": "允许/拒绝智能体对特定 URL 或域名的读取权限。",
    "Allow/deny agent read access to specific URLs.": "允许/拒绝智能体对特定 URL 的读取权限。",
    "Allow/deny agent read access to specific files or directories.": "允许/拒绝智能体对特定文件或目录的读取权限。",
    "Allow/deny agent write access to specific files or directories.": "允许/拒绝智能体对特定文件或目录的写入权限。",
    "Allow/deny specific commands outside the sandbox.": "允许/拒绝沙盒外的特定命令。",
    "Allow/deny specific terminal commands.": "允许/拒绝特定的终端命令。",
    "Alphabetical (A-Z)": "字母顺序 (A-Z)",
    "Alphabetical (Z-A)": "字母倒序 (Z-A)",
    "Also includes": "还包括",
    "Alt+Enter On empty prompt, sends next in queue": "Alt+Enter 键：在输入为空时，发送队列中的下一条",
    "Alt+Enter Sends immediately": "Alt+Enter 键：立即发送",
    "Always": "始终",
    "Always Allow": "始终允许",
    "Always Ask": "总是询问",
    "Always Proceed": "自动执行",
    "An error occurred while submitting your feedback. Please try again.": "提交反馈时出错，请重试。",
    "An unexpected bug occurred.": "发生了意外错误。",
    "Analyzed": "已分析",
    "Android CLI": "Android CLI",
    "Antigravity Interactive HTML": "Antigravity 交互式 HTML",
    "Any error messages": "任何错误消息",
    "Any relevant information": "任何相关信息",
    "App": "应用",
    "App Settings": "应用设置",
    "App Shortcuts": "应用快捷键",
    "App Version": "应用版本",
    "App version": "应用版本",
    "Appearance": "外观",
    "Application": "应用",
    "Applications": "应用",
    "Apply": "应用",
    "Archive": "归档",
    "Archive Conversation": "归档对话",
    "Archive This Conversation": "归档此对话",
    "Archive Workspace": "归档工作区",
    "Archive project": "归档项目",
    "Are you sure you want to delete": "您确定要删除",
    "Are you sure you want to delete the": "您确定要删除",
    "Are you sure you want to delete the project": "您确定要删除项目",
    "Are you sure you want to delete this conversation? This action cannot be undone.": "您确定要删除此对话吗？此操作无法撤销。",
    "Are you sure you want to delete this handler?": "您确定要删除此处理器吗？",
    "Are you sure you want to delete this hook card?": "您确定要删除此钩子卡片吗？",
    "Artifact": "产物",
    "Artifact Review Policy": "产物审阅策略",
    "Artifacts": "产物",
    "Ask": "询问",
    "Ask a quick question without interrupting the main conversation.": "快速提问而不打断主对话。",
    "Ask anything, @ to mention, / for actions": "输入任何问题，使用 @ 提及，使用 / 执行操作",
    "Ask before sensitive operations.": "敏感操作前询问。",
    "Attach Antigravity server logs": "附加 Antigravity 服务器日志",
    "Attach a screenshot (optional)": "附加截图（可选）",
    "Auth and Billing": "认证与计费",
    "Auto (Preview)": "自动（预览）",
    "Auto (detected)": "自动 (已检测)",
    "Auto-Updater": "自动更新程序",
    "Auto-start": "开机自启",
    "Automatic Check for Updates": "自动检查更新",
    "Automatically decide if commands run.": "自动决定是否运行命令。",
    "Automatically prompt you to restart the app when a new update is available.": "有新更新可用时自动提示您重启应用。",
    "Automatically prompt you to restart the app when a new update is available. When disabled, you can check for updates manually from the app menu.": "当有新更新可用时自动提示您重启应用。禁用后，您可以从应用菜单中手动检查更新。",
    "Automation": "自动化",
    "Automations": "自动化",
    "Available AI Credits:": "可用 AI 积分：",
    "Avatar URL": "头像 URL",
    "Back": "返回",
    "Background": "背景颜色",
    "Background Task": "后台任务",
    "Background Tasks": "后台任务",
    "Background tasks": "后台任务",
    "Bad response": "差的回答",
    "Baseline model quota reached": "已达到基础模型配额",
    "Best of N": "N 选优",
    "Best-of-N Ended": "N 选优已结束",
    "Best-of-N Started": "Best-of-N 已启动",
    "Block all browser JavaScript execution.": "阻止所有浏览器 JavaScript 执行。",
    "Bot Name": "机器人名称",
    "Branch": "分支",
    "Branch Changes": "分支变更",
    "Browse and enable plugins from the Build With Google catalog": "从 Build With Google 目录浏览并启用插件",
    "Browse and enable plugins from the Build With Google catalog.": "浏览并启用“使用 Google 构建”目录中的插件。",
    "Browse and enable plugins from the Build with Antigravity catalog": "从 Build with Antigravity 目录浏览并启用插件",
    "Browse the Marketplace": "浏览插件市场",
    "Browser": "浏览器",
    "Browser Actuation Permissions": "浏览器操作权限",
    "Browser Actuation Rules": "浏览器操作规则",
    "Browser CDP Port": "浏览器 CDP 端口",
    "Browser Javascript Execution Policy": "浏览器 JavaScript 执行策略",
    "Browser Settings": "浏览器设置",
    "Browser Subagent": "浏览器子智能体",
    "Browser User Profile Path": "浏览器用户配置文件路径",
    "Browsing History": "浏览历史",
    "Bug Report": "错误报告",
    "Build With Google Plugins": "使用 Google 插件构建",
    "Build with Antigravity Plugins": "使用 Antigravity 插件构建",
    "Build with Google": "使用 Google 构建",
    "Built In": "内置",
    "Built-in Browser": "内置浏览器",
    "By using this app, you agree to its": "使用本应用即表示您同意其",
    "By using this app, you agree to its ": "使用本应用即表示您同意其 ",
    "Cancel": "取消",
    "Cancel All Tasks": "取消所有任务",
    "Cannot parse folder URI.": "无法解析文件夹 URI。",
    "Change": "更改",
    "Change...": "更改...",
    "Changes": "更改",
    "Change…": "更改…",
    "Chat": "对话",
    "Chat Settings": "聊天设置",
    "Chat Shortcuts": "对话快捷键",
    "Check for Updates": "检查更新",
    "Check for update": "检查更新",
    "Choose a predefined security preset for the agent. This controls terminal auto-execution policy, and file access policy.": "为智能体选择一个预定义的安全预设。这将控制终端自动执行策略和文件访问策略。",
    "Choose between the Default and Project 4K experience.": "在默认体验和 Project 4K 体验之间选择。",
    "Choose how much detail is shown during a conversation.": "选择对话过程中显示多少细节。",
    "Choose the experience that fits how you work.": "选择适合您工作方式的体验。",
    "Choose where links open by default when clicked.": "选择点击链接时的默认打开位置。",
    "Choose where terminal sessions appear.": "选择终端会话的显示位置。",
    "Chrome Binary Path": "Chrome 可执行文件路径",
    "Chrome DevTools": "Chrome 开发者工具",
    "Claude and GPT models": "Claude 和 GPT 模型",
    "Clear": "清除",
    "Clear History": "清除历史记录",
    "Clear visited URLs and autocomplete suggestions from the built-in browser.": "清除内置浏览器的访问记录和自动补全建议。",
    "Click to copy URL": "点击复制 URL",
    "Click to respond to the question.": "点击以回答问题。",
    "Click to respond to the questions.": "点击以回答问题。",
    "Clone current workspace into a new independent workspace": "克隆当前工作区为一个新的独立工作区",
    "Close All": "全部关闭",
    "Close Others": "关闭其他",
    "Close Saved": "关闭已保存",
    "Close Settings": "关闭设置",
    "Close Tab": "关闭标签页",
    "Close Terminal Tab": "关闭终端标签页",
    "Close split view and go to forked conversation": "关闭分屏视图并前往分支对话",
    "Close to the Right": "关闭右侧",
    "Cloud CLI MCP Server provides tools to run gcloud and bq CLIcommands in a remote sandbox environment": "Cloud CLI MCP 服务器提供了在远程沙盒环境中运行 gcloud 和 bq CLI 命令的工具。",
    "Code Font": "代码字体",
    "Code Search": "代码搜索",
    "Collapse All": "全部折叠",
    "Collapse All Folders": "折叠所有文件夹",
    "Command": "命令",
    "Command Palette": "命令面板",
    "Command Setup Script": "命令设置脚本",
    "Commands": "命令",
    "Commands Outside Sandbox": "沙盒外命令",
    "Commands and files these agents can use.": "这些智能体可使用的命令和文件。",
    "Commit": "提交",
    "Commit succeeded": "提交成功",
    "Complete Onboarding Step": "完成新手入门引导步骤",
    "Complete verification": "完成验证",
    "Completed": "已完成",
    "Configuration saved successfully!": "配置保存成功！",
    "Configure Branches": "配置分支",
    "Configure GitHub access policies.": "配置 GitHub 访问策略。",
    "Configure agent execution, queued message delivery, and permissions.": "配置智能体执行、排队消息发送以及权限。",
    "Configure allowed and denied URLs for browser actuation.": "配置允许和拒绝进行浏览器操作的 URL。",
    "Configure allowed and denied URLs for reading": "配置允许和拒绝读取的 URL",
    "Configure allowed and denied URLs for reading.": "配置允许和拒绝读取的 URL。",
    "Configure allowed and denied paths for file reads and writes.": "配置允许和拒绝的文件读取和写入路径。",
    "Configure allowed commands outside the sandbox.": "配置允许在沙盒外执行的命令。",
    "Configure allowed terminal commands.": "配置允许执行的终端命令。",
    "Configure default behaviors, skills, and MCP servers.": "配置默认行为、技能和 MCP 服务器。",
    "Configure external tools via Model Context Protocol.": "通过模型上下文协议配置外部工具。",
    "Configure global allowed and denied resource permissions": "配置全局允许和拒绝的资源权限",
    "Configure global allowed and denied resource permissions.": "配置全局允许和拒绝的资源权限。",
    "Configure hooks that run on agent lifecycle events.": "配置在智能体生命周期事件中触发的钩子。",
    "Configure keyboard shortcuts.": "配置键盘快捷键。",
    "Configure link opening and built-in browser preferences.": "配置链接打开方式和内置浏览器偏好。",
    "Configure link opening and side panel preview preferences.": "配置链接打开方式和侧边栏预览偏好。",
    "Configure the agent's visual theme and display preferences.": "配置智能体的视觉主题和显示偏好。",
    "Configure the browser subagent. It requires": "配置浏览器子智能体。需要安装",
    "Configure the default width of markdown artifacts.": "配置 Markdown 工件的默认宽度。",
    "Configure the maximum width of the conversation panel.": "配置对话面板的最大宽度。",
    "Configure what the agent can do in local and remote conversations.": "配置智能体在本地和远程对话中可执行的操作。",
    "Configure when follow-up messages are sent.": "配置发送后续消息的时机。",
    "Configure workspace-specific permissions, resources, and customizations.": "配置特定工作区的权限、资源及自定义项。",
    "Configures how the agent tries to access files outside of its working folders.": "配置智能体如何尝试访问工作文件夹以外的文件。",
    "Confirm Redo": "确认重做",
    "Confirm Undo": "确认撤销",
    "Confirming this redo action will make the following changes:": "确认此重做操作将做出以下更改：",
    "Confirming this redo action will not make any code changes.": "确认此重做操作不会做出任何代码更改。",
    "Confirming this undo action will make the following changes:": "确认此撤销操作将做出以下更改：",
    "Confirming this undo action will not make any code changes.": "确认此撤销操作不会做出任何代码更改。",
    "Connect": "连接",
    "Connect an account so the agent can run automations.": "连接账户，以便智能体运行自动化。",
    "Connecting to language server...": "正在连接语言服务器...",
    "Context": "上下文",
    "Continue Response": "继续回答",
    "Continue your work from another device with Remote Control. Scan the QR code or open the link below.": "通过远程控制在其他设备上继续您的工作。请扫描二维码或打开下方链接。",
    "Contrast": "对比度",
    "Controls the actions the agent can take": "控制智能体可以执行的操作",
    "Controls the actions the agent can take.": "控制智能体可以执行的操作。",
    "Controls whether terminal commands require your approval before running.": "控制终端命令在运行前是否需要您的批准。",
    "Controls whether the agent can run custom JavaScript to automate complex browser actions.": "控制智能体是否可以运行自定义 JavaScript 来自动化复杂的浏览器操作。",
    "Conversation": "对话",
    "Conversation Archived": "对话已归档",
    "Conversation History": "历史对话",
    "Conversation ID": "对话 ID",
    "Conversation Name": "对话名称",
    "Conversation Steps": "对话步骤",
    "Conversation Width": "对话宽度",
    "Conversation copied as Markdown to clipboard": "对话已作为 Markdown 复制到剪贴板",
    "Conversation unavailable": "对话不可用",
    "Conversations": "对话",
    "Copied": "已复制",
    "Copy Config File Path": "复制配置文件路径",
    "Copy Content": "复制内容",
    "Copy Conversation ID": "复制对话 ID",
    "Copy Conversation Link": "复制对话链接",
    "Copy File Name": "复制文件名",
    "Copy File Path": "复制文件路径",
    "Copy ID": "复制 ID",
    "Copy Image": "复制图片",
    "Copy Link": "复制链接",
    "Copy Path": "复制路径",
    "Copy Project ID": "复制项目 ID",
    "Copy Project Name": "复制项目名称",
    "Copy debug info": "复制调试信息",
    "Copy email address": "复制电子邮箱",
    "Copy error to clipboard": "复制错误到剪贴板",
    "Copy full URL to clipboard": "复制完整 URL 到剪贴板",
    "Copy id": "复制 ID",
    "Copy link": "复制链接",
    "Copy output": "复制输出",
    "Copy path": "复制路径",
    "Core tools and knowledge required to develop for Android": "开发 Android 所需的核心工具和知识",
    "Could not create project": "无法创建项目",
    "Create New Project": "创建新项目",
    "Create Project": "创建项目",
    "Create a Plugin with the Agent": "使用智能体创建插件",
    "Create a new workspace from your first message.": "从第一条消息创建新工作区。",
    "Create a project first.": "请先创建项目。",
    "Create with Prompt": "用提示词创建",
    "Created": "已创建",
    "Created Date": "创建日期",
    "Creating Chat Bot": "正在创建对话机器人",
    "Creating Cloud Project": "正在创建云项目",
    "Creating Fork...": "正在创建分叉...",
    "Creating Sidecar": "正在创建 Sidecar",
    "Creating the forked conversation...": "正在创建分叉对话...",
    "Creating workspace for the forked conversation...": "正在为分叉对话创建工作区...",
    "Creating worktree for the forked conversation...": "正在为分叉对话创建工作树...",
    "Creation Date": "创建日期",
    "Curated collection of agent skills for science.": "精选的科学领域智能体技能集合。",
    "Curated sets of plugins for common workflows and roles.": "为常见工作流和角色精选的插件集合。",
    "Current Version": "当前版本",
    "Current Workspace": "当前工作区",
    "Current workspace": "当前工作区",
    "Custom": "自定义配置",
    "Custom Agents": "自定义智能体",
    "Custom View": "自定义视图",
    "Custom agents are not available in Best of N mode.": "自定义智能体在 Best of N 模式下不可用。",
    "Custom...": "自定义...",
    "Customizations": "自定义",
    "Customize": "自定义",
    "Customize Global Skills": "自定义全局技能",
    "Custom…": "自定义…",
    "Daily": "每天",
    "Danger Zone": "危险区域",
    "Dark": "深色",
    "Dark Theme": "深色主题",
    "Dart and Flutter": "Dart 和 Flutter",
    "Data Agent Kit": "Data Agent Kit",
    "Date Added": "添加日期",
    "Default": "默认",
    "Default Customizations": "默认自定义项",
    "Default Dark": "默认深色",
    "Default Light": "默认浅色",
    "Default Model": "默认模型",
    "Delete": "删除",
    "Delete All": "全部删除",
    "Delete All Remote Agents Data?": "删除所有远程智能体数据？",
    "Delete Conversation": "删除对话",
    "Delete Handler": "删除处理器",
    "Delete Hook": "删除钩子",
    "Delete MCP Server": "删除 MCP 服务器",
    "Delete Permanently": "永久删除",
    "Delete Project": "删除项目",
    "Delete Task": "删除任务",
    "Delete Terminal": "删除终端",
    "Delete all recordings?": "删除所有录音？",
    "Delete comment": "删除评论",
    "Deleted": "已删除",
    "Deny": "拒绝",
    "Deny List Terminal Commands": "终端命令拒绝列表",
    "Describe the bug you encountered...": "描述您遇到的错误...",
    "Describe the feature you would like to see...": "描述您希望看到的功能...",
    "Describe your Remote Control issue...": "描述您的远程控制问题...",
    "Describe your auth or billing issue...": "描述您的认证或计费问题...",
    "Describe your issue or idea...": "描述您的问题或想法...",
    "Description": "描述",
    "Determines the markup language of the output.": "决定输出的标记语言。",
    "Dev mode: Localhost server automatically detected": "开发者模式：已自动检测到本地服务器",
    "Developer Tools": "开发者工具",
    "Device Name": "设备名称",
    "Did restarting the desktop app help?": "重启桌面应用是否有帮助？",
    "Diff contents are no longer available.": "差异内容已不可用。",
    "Disable": "禁用",
    "Disabled": "已禁用",
    "Disabled. Open Details to finish setup or enable.": "已禁用。打开详情完成设置或启用。",
    "Disabled. Open the plugin page to finish setup.": "已禁用。打开插件页面完成设置。",
    "Disables all safety barriers for maximal iteration velocity.": "禁用所有安全屏障，以获得最快的迭代速度。",
    "Discard": "放弃",
    "Discard unstaged changes": "放弃未暂存的更改",
    "Dismiss": "忽略",
    "Display Options": "显示选项",
    "Display and preserve intermediate thinking steps.": "显示并保留中间思考过程。",
    "Don't show this for 2 days": "两天内不再显示",
    "Download": "下载",
    "Download Diagnostics": "下载诊断数据",
    "Download Location": "下载位置",
    "Download feature is not available.": "下载功能不可用。",
    "Downloading": "下载中...",
    "Drag to resize, double-click to reset": "拖拽调整大小，双击重置",
    "Draws from your organization's pooled Gemini Enterprise usage.": "使用您组织的 Gemini Enterprise 共享用量。",
    "Duplicate": "制作副本",
    "Duplicate Conversation": "复制对话",
    "Edit": "编辑",
    "Edit comment": "编辑评论",
    "Edited": "已编辑",
    "Editor Font": "编辑器字体",
    "Editor Shortcuts": "编辑器快捷键",
    "Email": "电子邮箱",
    "Embedded web preview": "内嵌 Web 预览",
    "Enable": "启用",
    "Enable AI Credit Overages": "启用 AI 积分超额使用",
    "Enable Browser Tools": "启用浏览器工具",
    "Enable Chat": "启用对话",
    "Enable Demo Mode (Beta)": "启用演示模式 (测试版)",
    "Enable Notifications": "启用通知",
    "Enable Notifications for Agent": "为智能体启用通知",
    "Enable Overages": "启用超额积分",
    "Enable Proxy": "启用代理",
    "Enable Remote Control": "启用远程控制",
    "Enable Sandbox Mode (Preview)": "启用沙盒模式 (预览版)",
    "Enable Sounds for Agent": "为智能体启用提示音",
    "Enable Telemetry": "启用遥测",
    "Enable Terminal Sandbox": "启用终端沙盒",
    "Enable Web Access": "启用网络访问",
    "Enter Queues after the turn": "Enter 键：在当前轮次后排队",
    "Enter a prompt for the agent to run...": "输入提示词以供智能体运行...",
    "Enter avatar URL (optional)": "输入头像 URL (可选)",
    "Enter bot name (optional)": "输入机器人名称 (可选)",
    "Enter command...": "输入命令...",
    "Enter device name...": "输入设备名称...",
    "Enter project name...": "输入项目名称...",
    "Enter target...": "输入目标...",
    "Enter the required configuration values to install this MCP server.": "输入安装此 MCP 服务器所需的配置值。",
    "Enter tool name or server...": "输入工具名称或服务器...",
    "Enter workspace name": "输入工作区名称",
    "Enter workspace name (e.g., my-feature)": "输入工作区名称 (例如 my-feature)",
    "Enter your feedback here...": "在此输入您的反馈...",
    "Environment": "环境",
    "Equalize Split Panes": "平分分屏面板",
    "Error ID:": "错误 ID：",
    "Error Loading Models": "加载模型时出错",
    "Error fetching MCP prompt": "获取 MCP 提示词出错",
    "Error occurred during import.": "导入时出错。",
    "Every command requires approval.": "每条命令都需要批准。",
    "Every day": "每天",
    "Every hour": "每小时",
    "Every week": "每周",
    "Every weekday": "每个工作日",
    "Execute URLs": "URL 执行",
    "Executed": "已执行",
    "Execution": "执行",
    "Expand All Folders": "展开所有文件夹",
    "Expected behavior": "预期行为",
    "Experimental Features": "实验性功能",
    "Experimental features": "实验性功能",
    "Exploring file, editing file": "浏览文件、编辑文件",
    "Export": "导出",
    "Extensions": "扩展",
    "External Browser": "外部浏览器",
    "External tools the agent can call via Model Context Protocol": "智能体可通过模型上下文协议调用的外部工具",
    "External tools the agent can call via Model Context Protocol.": "智能体可通过模型上下文协议 (MCP) 调用的外部工具。",
    "Failed": "已失败",
    "Failed to Commit": "提交失败",
    "Failed to Generate Commit Message": "生成提交信息失败",
    "Failed to Push": "推送失败",
    "Failed to add plugin.": "添加插件失败。",
    "Failed to add plugin. Please try again.": "添加插件失败，请重试。",
    "Failed to continue": "继续执行失败",
    "Failed to create terminal": "创建终端失败",
    "Failed to create workspace": "创建工作区失败",
    "Failed to create worktree": "创建工作树失败",
    "Failed to delete conversation": "删除对话失败",
    "Failed to delete plugin.": "删除插件失败。",
    "Failed to delete plugin. Please try again.": "删除插件失败，请重试。",
    "Failed to delete skill.": "删除技能失败。",
    "Failed to delete skill. Please try again.": "删除技能失败，请重试。",
    "Failed to fork conversation": "分支对话失败",
    "Failed to load diff contents.": "加载差异内容失败。",
    "Failed to load diff.": "加载差异失败。",
    "Failed to load plugins. Please try again.": "加载插件失败，请重试。",
    "Failed to proceed": "继续失败",
    "Failed to rename conversation": "重命名对话失败",
    "Failed to resolve permissions. Please try again.": "解析权限失败，请重试。",
    "Failed to save project": "保存项目失败",
    "Failed to start Best of N mode": "启动 Best of N 模式失败",
    "Failed to start conversation": "开启对话失败",
    "Failed to stop agent": "停止智能体失败",
    "Failed to stop conversation": "停止对话失败",
    "Failed to toggle plugin. Please try again.": "切换插件失败，请重试。",
    "Failed to unarchive project": "取消归档项目失败",
    "Failed to update permissions. Please try again.": "更新权限失败，请重试。",
    "Fast": "快速",
    "Feature Request": "功能请求",
    "Features": "功能",
    "Feedback": "反馈",
    "Feedback Type": "反馈类型",
    "File Access Rules": "文件访问规则",
    "File Changed": "已修改文件",
    "File Permissions": "文件权限",
    "File Picker": "文件选择器",
    "File Reads": "文件读取",
    "File Writes": "文件写入",
    "Files Changed": "已修改文件",
    "Files changed": "已修改文件",
    "Files modified by the agent in this conversation": "智能体在此对话中修改的文件",
    "Filter": "筛选",
    "Filter resources...": "筛选资源...",
    "Find in Pane": "在面板中查找",
    "Find skills, agents, and more in the Marketplace.": "在插件市场中发现技能、智能体及更多内容。",
    "Firebase": "Firebase",
    "Fires after a tool step completes.": "在工具步骤完成后触发。",
    "Fires after tool calls finish.": "在工具调用完成后触发。",
    "Fires before a tool step executes.": "在工具步骤执行前触发。",
    "Fires before the model is called.": "在调用模型前触发。",
    "Fires when the execution loop terminates.": "在执行循环终止时触发。",
    "Five Hour Limit": "五小时限额",
    "Five Hour Limit Remaining": "五小时限额剩余",
    "Focus Input": "聚焦输入框",
    "Folder": "文件夹",
    "Folder where files downloaded in the built-in browser are saved.": "内置浏览器下载文件保存的文件夹。",
    "Folders": "文件夹",
    "Folders these agents can access.": "这些智能体可访问的文件夹。",
    "Font": "字体",
    "Font Size": "字体大小",
    "For any feedback that does not fit into the above categories.": "适用于不属于上述类别的任何反馈。",
    "Foreground": "前景颜色",
    "Fork": "分支",
    "Friday": "星期五",
    "Full Error": "完整错误信息",
    "Full machine": "完整机器访问",
    "Gemini API": "Gemini API",
    "Gemini Models": "Gemini 模型",
    "General": "常规",
    "General Feedback": "常规反馈",
    "Generate personalized rules": "生成个性化规则",
    "Generating...": "生成中...",
    "Generations": "生成历史",
    "Get More AI Credits": "获取更多 AI 积分",
    "Getting scripts...": "正在获取脚本...",
    "Getting started with a Project": "开始使用项目",
    "GitHub Permissions": "GitHub 权限",
    "GitHub Personal Access Token": "GitHub 个人访问令牌",
    "GitHub Policies": "GitHub 策略",
    "Give Feedback": "提供反馈",
    "Global Permissions": "全局权限",
    "Global Shortcut": "全局快捷键",
    "Global Shortcuts": "全局快捷键",
    "Global permissions": "全局权限",
    "Go Back": "后退",
    "Go Back in Pane": "在面板中后退",
    "Go Forward": "前进",
    "Go Forward in Pane": "在面板中前进",
    "Goals": "目标",
    "Good response": "好的回答",
    "Google Antigravity SDK": "Google Antigravity SDK",
    "Google Calendar": "Google 日历",
    "Google Docs": "Google 文档",
    "Google Drive": "Google 云端硬盘",
    "Google Kubernetes Engine (Remote)": "Google Kubernetes Engine (远程)",
    "Google Maps Platform": "Google Maps Platform",
    "Google Sheets": "Google 表格",
    "Google Slides": "Google 幻灯片",
    "Google Workspace": "Google Workspace",
    "Got it": "知道了",
    "Group By": "分组方式",
    "Group By Project": "按项目分组",
    "Group By Workspace": "按工作区分组",
    "Group name": "分组名称",
    "Hardware Acceleration": "硬件加速",
    "Having trouble signing in?": "登录遇到问题？",
    "Hide breakdown": "隐藏明细",
    "Hide thought process": "隐藏思考过程",
    "High": "高",
    "History": "历史记录",
    "Hook will only trigger if the tool name matches run_command or view_file.": "钩子仅在工具名称匹配 run_command 或 view_file 时触发。",
    "Hook will only trigger if the tool name matches run_command.": "钩子仅在工具名称匹配 run_command 时触发。",
    "Hook will only trigger if the tool name starts with browser_.": "钩子仅在工具名称以 browser_ 开头时触发。",
    "Hook will trigger if any tool is executed.": "钩子将在执行任何工具时触发。",
    "Hooks": "钩子",
    "Host Environment": "主机环境",
    "Hourly": "每小时",
    "How can we improve?": "我们该如何改进？",
    "How loud Antigravity's voice is.": "Antigravity 语音的音量。",
    "How loud Jetski's voice is.": "Jetski 的音量。",
    "I prefer an immediate single response to prioritize productivity right now.": "我希望立即得到单次回复以提高当前的效率。",
    "Import": "导入",
    "Import AI Studio Project": "导入 AI Studio 项目",
    "In Progress": "进行中",
    "In a rush": "快速响应",
    "Inactive": "未激活",
    "Include app logs": "包含应用日志",
    "Include default customizations, such as default skills.": "包含默认自定义项，例如默认技能。",
    "Include diagnostic data": "包含诊断数据",
    "Include unstaged changes": "包含未暂存的更改",
    "Inherit General": "继承全局设置",
    "Inherit Global": "继承全局",
    "Inherits Global": "继承全局",
    "Inherits your General settings when working in this project.": "在此项目中工作时继承您的全局设置。",
    "Inherits your Global Permissions": "继承您的全局权限",
    "Inherits your Global Permissions when working in this project": "在此项目中工作时继承您的全局权限",
    "Inherits your Global Permissions when working in this project.": "在此项目中工作时继承您的全局权限。",
    "Inline Actions": "行内操作",
    "Inline Widget": "行内小部件",
    "Input device for voice mode and dictation.": "语音模式和听写使用的输入设备。",
    "Input device for voice mode.": "语音模式的输入设备。",
    "Input required": "需要输入",
    "Installed": "已安装",
    "Installed MCP Servers": "已安装的 MCP 服务器",
    "Installed Skills": "已安装技能",
    "Instructions": "指令",
    "Insufficient AI Credits": "AI 积分不足",
    "Interrupt the agent and send immediately.": "中断智能体并立即发送。",
    "Invalid Media": "无效媒体",
    "Invocation": "调用",
    "Issue Type": "问题类型",
    "Jetski Chat": "智能对话",
    "Just now": "刚刚",
    "Keep In Menu Bar": "保留在系统托盘",
    "Keep the app accessible from the menu bar and running in the background when all windows are closed.": "应用将可以从系统托盘访问，并在所有窗口关闭时继续在后台运行。",
    "Keep your coding agent up to date with the latest web best practices.": "让您的编程智能体掌握最新的 Web 最佳实践。",
    "Keeps working in this workspace. Nothing is copied.": "继续在此工作区中工作，不复制任何内容。",
    "Keybindings": "快捷键绑定",
    "Keyboard Shortcuts": "键盘快捷键",
    "Keyboard shortcuts": "键盘快捷键",
    "Keyboard shortcuts for quick navigation and control.": "用于快速导航和控制的键盘快捷键。",
    "Kick off work on your computer and continue working with your agents from your phone or another device.": "在电脑上启动工作，并可以通过手机或其他设备继续与智能体协同工作。",
    "Kick off work on your computer and continue working with your agents from your phone or another device. Turn on Remote Control in app settings.": "在电脑上启动工作，并可以通过手机或其他设备继续与智能体协同工作。请在应用设置中开启“远程控制”。",
    "Knowledge": "知识库",
    "LAYOUT CONTROLS": "布局控制",
    "Labs": "实验室",
    "Language": "语言",
    "Large": "大",
    "Last 24 hours": "最近 24 小时",
    "Last 3 months": "最近 3 个月",
    "Last 30 days": "最近 30 天",
    "Last 7 days": "最近 7 天",
    "Last Prompt": "最新提示词",
    "Last Updated": "最后更新",
    "Last prompt": "最新提示词",
    "Launch at login": "登录时自动启动",
    "Launch on startup": "开机时启动",
    "Layout Controls": "布局控制",
    "Layout controls": "布局控制",
    "Learn more": "了解更多",
    "Learn more about": "了解更多关于",
    "Learn more.": "了解更多。",
    "Leaving Soon": "即将下线",
    "Leaving soon": "即将下线",
    "Legal Help": "法律帮助",
    "Light": "浅色",
    "Light Theme": "浅色主题",
    "Limited time": "限时",
    "Loading": "正在加载",
    "Loading Antigravity": "正在加载 Antigravity",
    "Loading MCP servers...": "正在加载 MCP 服务器...",
    "Loading Notebook View...": "正在加载 Notebook 视图...",
    "Loading hooks...": "正在加载钩子...",
    "Loading licenses...": "正在加载许可证...",
    "Loading media...": "正在加载媒体...",
    "Loading plugins...": "正在加载插件...",
    "Loading token usage...": "正在加载 Token 使用量...",
    "Loading workspace customizations...": "正在加载工作区自定义项...",
    "Local": "本地",
    "Local Permissions": "本地权限",
    "Logout": "退出登录",
    "Logs": "日志",
    "Low": "低",
    "MCP Configuration Error:": "MCP 配置错误：",
    "MCP Install Error:": "MCP 安装错误：",
    "MCP Servers": "MCP 服务器",
    "MCP Tools": "MCP 工具",
    "MCP servers": "MCP 服务器",
    "MCP tool": "MCP 工具",
    "Main Agent": "主智能体",
    "Manage Antigravity app settings.": "管理 Antigravity 应用设置。",
    "Manage Hooks": "管理钩子",
    "Manage Projects": "管理项目",
    "Manage application settings.": "管理应用设置。",
    "Manage fine-grained permissions for GitHub.": "管理 GitHub 的细粒度权限。",
    "Manage project folders, agent settings, and permissions.": "管理项目文件夹、智能体设置和权限。",
    "Manage your conversations from the companion website.": "在配套网站上管理您的对话。",
    "Manage your model quota and credits.": "管理您的模型配额和积分额度。",
    "Manage your notification preferences.": "管理您的通知偏好设置。",
    "Manage your plan, credentials, and general preferences.": "管理您的套餐、凭据和常规偏好设置。",
    "Manifest Changes": "清单变更",
    "Manually customize individual settings.": "手动自定义各项设置。",
    "Mark Read": "标记为已读",
    "Mark Unread": "标记为未读",
    "Mark as Read": "标记为已读",
    "Mark as Unread": "标记为未读",
    "Marketing Emails": "营销邮件",
    "Marketplace": "插件市场",
    "Maximize": "最大化",
    "Maximize Pane": "最大化面板",
    "Maximum number of attachments reached": "已达到附件数量上限",
    "Maximum number of attachments reached.": "已达到附件数量上限。",
    "Media": "媒体",
    "Medium": "中",
    "Memory": "记忆",
    "Mention Page": "提及页面",
    "Mentions": "提及",
    "Message input": "消息输入框",
    "Microphone": "麦克风",
    "Microphone blocked. Allow mic access.": "麦克风被阻止，请允许麦克风访问。",
    "Minimize": "最小化",
    "Minimize Pane": "最小化面板",
    "Model": "模型",
    "Model Credits": "模型积分",
    "Model Quota": "模型配额",
    "Model quota reached": "已达模型配额",
    "Models": "模型",
    "Models & Usage": "模型与用量",
    "Modern Web Guidance": "现代 Web 开发指南",
    "Modified": "已修改",
    "Modified in": "修改于",
    "Modify permissions for file and terminal tools.": "修改文件和终端工具的权限。",
    "Modify permissions for file, terminal, and MCP tools": "修改文件、终端和 MCP 工具的权限",
    "Modify permissions for file, terminal, and MCP tools.": "修改文件、终端和 MCP 工具的权限。",
    "Monday": "星期一",
    "Monthly Limit": "每月限额",
    "More Actions": "更多操作",
    "More actions": "更多操作",
    "Move Conversation Down": "下移对话",
    "Move Conversation Up": "上移对话",
    "Move to Group": "移动到分组",
    "NAVIGATION": "导航",
    "Narrow": "较窄",
    "Navigation": "导航",
    "Network": "网络",
    "Network Access Rules": "网络访问规则",
    "Network Permissions": "网络权限",
    "Network Reads": "网络读取",
    "Never": "从不",
    "New Agent Script": "新建智能体脚本",
    "New Conversation": "新建对话",
    "New Group": "新建分组",
    "New Project": "新建项目",
    "New Tab": "新建标签页",
    "New Terminal": "新建终端",
    "New Terminal Tab": "新建终端标签页",
    "New Workspace": "新建工作区",
    "New Worktree": "新建工作树",
    "New chats will be grouped by workspace.": "新对话将按工作区分组。",
    "New hook name": "新钩子名称",
    "Next Aux Pane Tab": "下一个辅助面板标签",
    "Next Pane Tab": "下一个面板标签",
    "Next Side Panel Tab": "下一个侧边栏标签",
    "Next question": "下一个问题",
    "No (tell the agent what to do instead)": "否 (告诉智能体改做什么)",
    "No MCP Servers": "无 MCP 服务器",
    "No MCP servers installed": "未安装任何 MCP 服务器",
    "No MCP servers yet. Use Add to browse the store.": "暂无 MCP 服务器。请使用“添加”浏览商店。",
    "No Model Selected": "未选择模型",
    "No Models Available": "无可用模型",
    "No Project": "无项目",
    "No Subtitle": "无副标题",
    "No active terminals": "无活动终端",
    "No artifacts": "暂无产物",
    "No artifacts generated": "暂无生成的产物",
    "No automations yet": "暂无自动化",
    "No background tasks": "无后台任务",
    "No changes to review": "无可审阅的更改",
    "No conversations yet": "暂无对话",
    "No custom agents yet.": "暂无自定义智能体。",
    "No description available.": "暂无描述。",
    "No file changes": "无文件更改",
    "No folders added yet.": "尚未添加文件夹。",
    "No keyboard shortcuts found matching your filter.": "未找到与筛选条件匹配的键盘快捷键。",
    "No matching resources found.": "未找到匹配的资源。",
    "No plugins available.": "暂无可用插件。",
    "No project": "无项目",
    "No project found": "暂无项目",
    "No project found.": "暂无项目",
    "No project selected or project management not available.": "未选择项目或项目管理不可用。",
    "No projects found": "暂无项目",
    "No projects found.": "暂无项目",
    "No quota information available.": "暂无配额信息。",
    "No resources added yet.": "尚未添加资源。",
    "No subagent": "暂无子智能体",
    "No subagents": "暂无子智能体",
    "No subagents running": "暂无运行中的子智能体",
    "No token data available.": "暂无 Token 数据。",
    "None": "无",
    "Not Signed In": "未登录",
    "Not found": "未找到",
    "Not in Project": "未分组项目",
    "Not set": "未设置",
    "Notice": "提示",
    "Notification Preferences": "通知偏好设置",
    "Notification Settings": "通知设置",
    "Notifications": "通知",
    "Now that you've created a project, configure your project's agent settings or start a conversation.": "现在您已经创建了一个项目，接下来请配置该项目的智能体设置，或者直接开始对话。",
    "OK": "确定",
    "Only stored on your machine.": "仅存储在本机。",
    "Only the conversation will be rewound; your files will be left as-is.": "仅回退对话，文件保持不变。",
    "Open Antigravity IDE": "打开 Antigravity IDE",
    "Open Command Palette": "打开命令面板",
    "Open Commit Graph": "打开提交图谱",
    "Open Conversation": "打开对话",
    "Open Conversation History": "打开历史对话",
    "Open Conversation Picker": "打开对话选择器",
    "Open File": "打开文件",
    "Open File Search": "打开文件搜索",
    "Open Folder": "打开文件夹",
    "Open IDE": "打开 IDE",
    "Open Keyboard Shortcuts": "打开快捷键设置",
    "Open Links In": "在以下位置打开链接",
    "Open Logs": "打开日志",
    "Open MCP Config": "打开 MCP 配置",
    "Open Preferences": "打开偏好设置",
    "Open Project Settings": "打开项目设置",
    "Open Settings": "打开设置",
    "Open System Preferences": "打开系统偏好设置",
    "Open Workspace": "打开工作区",
    "Open Workspace Selector": "打开工作区选择器",
    "Open in Code Search": "在代码搜索中打开",
    "Open in Notebook View": "在笔记本视图中打开",
    "Open in Remote Control": "在远程控制中打开",
    "Open in new tab": "在新标签页中打开",
    "Open project settings": "打开项目设置",
    "Open side-by-side view": "打开并排视图",
    "Operating System": "操作系统",
    "Optimize the interface and terminal output for screen readers.": "为屏幕阅读器优化界面和终端输出。",
    "Options": "选项",
    "Organization Allowed Domains (Read-Only)": "组织允许的域名 (只读)",
    "Other (write your answer)": "其他 (填写您的回答)",
    "Our servers are experiencing high traffic right now, please try again in a minute.": "我们的服务器当前负载较高，请稍后重试。",
    "Output": "输出",
    "Outside of folders file access policy": "工作文件夹以外的文件访问策略",
    "Override feature environment": "覆盖功能特性环境",
    "Overview": "概览",
    "Parent conversation ID is required to fork.": "分叉需要父对话 ID。",
    "Paste auth code": "粘贴认证代码",
    "Paste code here": "在此粘贴代码",
    "Pay only for the tokens you use, billed through Gemini platform.": "仅为使用的 Token 付费，通过 Gemini 平台计费。",
    "Permanently delete": "永久删除",
    "Permission Preset": "权限预设",
    "Permission Settings": "权限设置",
    "Permissions": "权限",
    "Pin": "置顶",
    "Pinned Conversations": "置顶对话",
    "Plan": "订阅计划",
    "Plan Review Policy": "计划审阅策略",
    "Planning...": "计划中...",
    "Play a sound when your action is needed or the agent finishes.": "需要您操作或智能体完成时播放声音。",
    "Please describe the issue in detail. The more actionable your feedback, the quicker our team can address your request. Some helpful information includes:": "请详细描述您的问题。您的反馈越具体，我们的团队就能越快处理您的请求。一些有用的信息包括：",
    "Please fill out all required values to continue.": "请填写所有必填值以继续。",
    "Please list the steps to reproduce the issue": "请列出重现问题的步骤",
    "Please list the steps to reproduce the issue...": "请列出重现问题的步骤...",
    "Please provide a more detailed description (at least 10 characters).": "请提供更详细的描述（至少 10 个字符）。",
    "Please provide details...": "请提供详细信息...",
    "Plugin": "插件",
    "Plugin Operation Error:": "插件操作错误：",
    "Plugin details": "插件详情",
    "Plugins": "插件",
    "Port number for Chrome DevTools Protocol remote debugging. Leave empty for default (9222).": "Chrome DevTools 协议远程调试端口。留空为默认 (9222)。",
    "Preset": "预设",
    "Press desired key combination": "按下所需的组合键",
    "Prevent Sleep": "阻止睡眠",
    "Prevent the computer from sleeping while the app is running.": "在应用运行时阻止计算机进入睡眠状态。",
    "Preview is not available for this file type.": "此文件类型不支持预览。",
    "Previous Aux Pane Tab": "上一个辅助面板标签",
    "Previous Pane Tab": "上一个面板标签",
    "Previous Side Panel Tab": "上一个侧边栏标签",
    "Previous question": "上一个问题",
    "Privacy": "隐私",
    "Proceed with Plan": "继续执行计划",
    "Profile": "个人资料",
    "Profile Settings": "个人资料",
    "Project": "项目",
    "Project 4K interface without developer tooling.": "不含开发者工具的 Project 4K 界面。",
    "Project Folders": "项目文件夹",
    "Project Name": "项目名称",
    "Project Settings": "项目设置",
    "Projects": "项目",
    "Prompt for approval before running browser scripts.": "在运行浏览器脚本前提示批准。",
    "Prompt to execute on schedule...": "按计划执行的提示词...",
    "Prompt too simple": "提示词过于简单",
    "Prototype, build & run modern apps users love with Firebase's backend, AI, and operational infrastructure.": "借助 Firebase 的后端、AI 和运营基础设施，设计原型、构建并运行深受用户喜爱的现代应用。",
    "Provide Feedback": "提供反馈",
    "Proxy": "代理",
    "Proxy Server": "代理服务器",
    "Purchase Credits": "购买积分",
    "Push": "推送",
    "Push succeeded": "推送成功",
    "Queue": "排队",
    "Queue until after the current turn.": "排队至当前轮次结束后。",
    "Queued Messages": "排队消息",
    "Quick Start": "快速开始",
    "Quota": "配额",
    "Quote Selection": "引用所选文本",
    "RECOMMENDED": "推荐",
    "Read": "读取",
    "Read URL": "读取 URL",
    "Read URLs": "URL 读取",
    "Receive product updates, tips, and promotions from Google Antigravity via email.": "通过电子邮件接收来自 Google Antigravity 的产品更新、提示和促销信息。",
    "Recent Files": "最近打开的文件",
    "Recommended": "推荐",
    "Record Audio": "录制音频",
    "Record Audio Ctrl+M": "录制音频 Ctrl+M",
    "Record voice memo": "录制语音备忘",
    "Redo changes": "重做更改",
    "Redo changes up to this point": "重做更改至此处",
    "Refresh": "刷新",
    "Refresh MCP servers": "刷新 MCP 服务器",
    "Refresh quota and credits data": "刷新配额和积分数据",
    "Refreshed credentials for all automations.": "已刷新所有自动化的凭据。",
    "Refreshing": "刷新中",
    "Refreshing credentials...": "正在刷新凭据...",
    "Refreshing...": "刷新中...",
    "Regroup Google3 Chats": "重新对对话进行分组",
    "Reject Step": "拒绝步骤",
    "Reliable automation, in-depth debugging, and performance analysis in Chrome using Chrome DevTools and Puppeteer": "使用 Chrome DevTools 和 Puppeteer 在 Chrome 中实现可靠的自动化、深度调试和性能分析",
    "Reload": "重新加载",
    "Remote": "远程",
    "Remote Control": "远程控制",
    "Remote Control Issue": "远程控制问题",
    "Remote control issue": "远程控制问题",
    "Remove": "移除",
    "Remove From Split": "从分屏中移除",
    "Rename": "重命名",
    "Rename Group": "重命名分组",
    "Renamed": "已重命名",
    "Render display math flush left.": "块级公式左对齐渲染。",
    "Render display math in leqno style (left-justified tags).": "使用 leqno 风格 (编号左对齐) 渲染块级公式。",
    "Reopen Closed Tab": "重新打开已关闭的标签页",
    "Replace With New": "替换为新建",
    "Replace the default browser right-click menu with quick actions.": "用快捷操作替换浏览器默认右键菜单。",
    "Replace with New": "替换为新建",
    "Replace with new": "替换为新建",
    "Request Review": "请求审阅",
    "Requires manual review for all terminal commands and file accesses outside of the working folders.": "要求对所有终端命令和工作文件夹之外的文件访问进行手动审阅。",
    "Reset State": "重置状态",
    "Reset Zoom": "重置缩放",
    "Reset to Default": "恢复默认设置",
    "Reset to default": "恢复默认",
    "Restart Main Language Server": "重启主语言服务器",
    "Restart to update": "重启以更新",
    "Restore": "还原",
    "Restore Defaults": "恢复默认设置",
    "Restore Pane": "还原面板",
    "Restore defaults": "恢复默认设置",
    "Restricts agent tools to a secure, isolated local sandbox.": "将智能体工具限制在安全隔离的本地沙盒中。",
    "Reuse your last workspace.": "复用上次使用的工作区。",
    "Reveal in Finder": "在访达中显示",
    "Review": "审阅",
    "Review Policy": "审阅策略",
    "Review pending conversations": "审阅待处理对话",
    "Rules": "规则",
    "Run": "运行",
    "Run (unsandboxed)": "运行 (非沙盒)",
    "Run a prompt on a schedule, like a morning summary of yesterday's changes. Runs show up here.": "按计划运行提示词，例如每天早上汇总昨天的变更。运行记录会显示在这里。",
    "Run all commands without restrictions.": "无限制地运行所有命令。",
    "Run command": "运行命令",
    "Run in a new worktree": "在新的工作树中运行",
    "Run in your current workspace": "在当前工作区中运行",
    "Run terminal commands with sandbox restrictions.": "在沙盒限制下运行终端命令。",
    "Run the app against a Linux environment. Connecting relaunches the app into the selected WSL distro.": "在 Linux 环境中运行应用。连接后将重启应用并切换至所选的 WSL 分发版。",
    "Running": "运行中",
    "Sample GDoc": "示例 Google 文档",
    "Sandbox Allow Network": "沙盒允许网络访问",
    "Saturday": "星期六",
    "Save": "保存",
    "Save changes": "保存更改",
    "Save rule to always allow execution of this command?": "保存规则以始终允许执行此命令吗？",
    "Save rule to always allow read access to this path?": "保存规则以始终允许读取此路径吗？",
    "Save rule to always allow write access to this path?": "保存规则以始终允许写入此路径吗？",
    "Scheduled": "已计划",
    "Scheduled Tasks": "计划任务",
    "Science": "科学",
    "Scratch": "草稿",
    "Screen Recording": "屏幕录制",
    "Screenshot": "屏幕截图",
    "Search": "搜索",
    "Search Engine": "搜索引擎",
    "Search GoB repositories...": "搜索代码仓库...",
    "Search MCP servers by name": "按名称搜索 MCP 服务器",
    "Search across files...": "跨文件搜索...",
    "Search conversations, commands, and code...": "搜索对话、命令和代码...",
    "Search conversations...": "搜索对话...",
    "Search customizations...": "搜索自定义项...",
    "Search file contents...": "搜索文件内容...",
    "Search files...": "搜索文件...",
    "Search flags": "搜索功能开关",
    "Search for commands...": "搜索命令...",
    "Search for conversations...": "搜索对话...",
    "Search for files in the project...": "在项目中搜索文件...",
    "Search projects": "搜索项目",
    "Search projects...": "搜索项目...",
    "Search shortcuts...": "搜索快捷键...",
    "Search workspaces...": "搜索工作区...",
    "Security Preset": "安全预设",
    "See Activity": "查看活动",
    "See All": "查看全部",
    "See Plans": "查看套餐方案",
    "See all": "查看全部",
    "See less": "收起",
    "See more": "查看更多",
    "See our": "查看我们的",
    "See our troubleshooting guide for more help": "查看我们的排查指南以获取更多帮助",
    "See our troubleshooting guide for more help.": "查看我们的排查指南以获取更多帮助。",
    "Select Model": "选择模型",
    "Select Model to Send Message": "选择发送消息的模型",
    "Select Next Conversation": "选择下一个对话",
    "Select Previous Conversation": "选择上一个对话",
    "Select a model": "选择一个模型",
    "Select a workspace to save agent scripts to your workspace.": "选择一个工作区以将智能体脚本保存到您的工作区。",
    "Select another model": "选择其他模型",
    "Select branch": "选择分支",
    "Select category to search...": "选择要搜索的类别...",
    "Select light, dark, or inherit system settings.": "选择浅色、深色，或跟随系统设置。",
    "Select model": "选择模型",
    "Select your license": "选择您的许可证",
    "Send Feedback": "发送反馈",
    "Send Immediately": "立即发送",
    "Send Now": "立即发送",
    "Send command input?": "发送命令输入？",
    "Send message": "发送消息",
    "Send message Enter": "发送消息 Enter",
    "Set the volume of agent sounds.": "设置智能体音效的音量。",
    "Settings": "设置",
    "Setup": "设置",
    "Setup script failed.": "设置脚本失败。",
    "Setup script ran successfully.": "设置脚本运行成功。",
    "Share Conversation (Preview)": "分享对话 (预览版)",
    "Shortcut": "快捷键",
    "Shortcuts": "快捷键",
    "Show All": "显示全部",
    "Show in File Explorer": "在文件资源管理器中显示",
    "Show more results": "显示更多结果",
    "Show system notifications when your action is needed or the agent finishes.": "当需要您操作或智能体完成时显示系统通知。",
    "Show thought process": "显示思考过程",
    "Sidebar": "侧边栏",
    "Sidebar grouped by project": "侧边栏按项目分组",
    "Sidebar grouped by workspace": "侧边栏按工作区分组",
    "Sign Out": "退出登录",
    "Sign in to finish setting up this plugin.": "登录以完成此插件的设置。",
    "Sign out of this server?": "要退出此服务器吗？",
    "Signing Out...": "正在退出登录...",
    "Skill deletion is not available.": "技能删除不可用。",
    "Skills": "技能",
    "Skills & Rules": "技能与规则",
    "Skip": "跳过",
    "Small": "小",
    "Something went wrong!": "出错了！",
    "Sonnet 5.5 is now available on paid Pro and Ultra plans. Third-party model access will no longer be available on your current plan starting on November 2, 2026.": "Sonnet 5.5 现已在付费的 Pro 和 Ultra 方案中提供。从 2026 年 11 月 2 日起，您当前的方案将不再支持访问第三方模型。",
    "Sort Conversations": "对话排序",
    "Sound": "声音",
    "Specifies Agent's behavior when asking for review on artifacts, which are documents it creates to enable a richer conversation experience.": "指定智能体在请求审阅产物时的行为。产物是指其为提供更丰富对话体验而创建的各类文档与生成物。",
    "Split": "分屏",
    "Split Conversation Horizontally": "水平拆分对话",
    "Split Conversation Vertically": "垂直拆分对话",
    "Split Down": "向下分屏",
    "Split Left": "向左分屏",
    "Split Right": "向右分屏",
    "Split Terminal": "拆分终端",
    "Split Up": "向上分屏",
    "Stage change": "暂存更改",
    "Staged Changes": "已暂存的更改",
    "Staged index changes and working tree changes": "暂存区更改与工作树更改",
    "Standalone": "独立",
    "Standalone Terminals": "独立终端",
    "Start Voice Recording": "开始语音录制",
    "Start first conversation": "开始首次对话",
    "Start using Gemini 3.8 Flash, our best Flash model.": "开始使用 Gemini 3.8 Flash，我们最强大的 Flash 模型。",
    "Start without a workspace, for general questions.": "不选择工作区，直接进行一般性提问。",
    "Starting": "启动中",
    "Startup": "启动",
    "Status": "状态",
    "Step": "步骤",
    "Step Type": "步骤类型",
    "Steps": "步骤",
    "Steps to Reproduce": "重现步骤",
    "Steps to reproduce the issue": "重现问题的步骤",
    "Stop": "停止",
    "Stop All Subagents": "停止所有子智能体",
    "Stop Recording": "停止录制",
    "Stop Subagent": "停止子智能体",
    "Stop Voice Recording": "停止语音录制",
    "Stopped": "已停止",
    "Strict Mode": "严格模式",
    "Strong": "强",
    "Subagents": "子智能体",
    "Submit": "提交",
    "Subtitles": "副标题",
    "Suggestions": "建议",
    "Sunday": "星期日",
    "Switch Roles": "切换角色",
    "Sync newly created JJ worktrees to head when starting a conversation.": "开始对话时将新建的 JJ 工作树同步到 head。",
    "System": "系统",
    "System Default": "跟随系统",
    "System Prompt": "系统提示词",
    "System default": "系统默认",
    "Table options": "表格选项",
    "Tasks": "任务",
    "Team of subagents to do long running work": "由子智能体团队执行长时间运行的工作",
    "Temperature": "温度",
    "Terminal & Tooling Permissions": "终端与工具权限",
    "Terminal Command Auto Execution": "终端命令自动执行",
    "Terminal Commands": "终端命令",
    "Terminal Shortcuts": "终端快捷键",
    "Terminal: Add to Chat": "终端：添加到对话",
    "Terminals": "终端",
    "Termination": "终止",
    "Terms": "条款",
    "Terms of Service": "服务条款",
    "Thank you! Your feedback has been submitted successfully.": "谢谢！您的反馈已成功提交。",
    "Thanks for your feedback!": "感谢您的反馈！",
    "The agent always asks for review.": "智能体始终请求审阅。",
    "The agent asks for permission before executing commands matched by a deny list entry.": "智能体在执行匹配拒绝列表的命令前会请求许可。",
    "The agent auto-executes commands matched by an allow list entry.": "智能体自动执行匹配允许列表的命令。",
    "The agent has encountered an internal error.": "智能体遇到内部错误。",
    "The agent is waiting for your input.": "智能体正在等待您的输入。",
    "The app will be accessible from the menu bar and will keep running in the background when all windows are closed.": "应用将可以从系统托盘访问，并在所有窗口关闭时继续在后台运行。",
    "The breakdown below shows token usage from customizations like rules, skills, and MCP. If a budget is exceeded, large rules are demoted to path pointers and large customizations are excluded automatically.": "下方的明细展示了来自规则、技能和 MCP 等自定义项的 Token 使用情况。如果超出预算，大型规则将降级为路径指针，大型自定义项将被自动排除。",
    "The breakdown below shows token usage from customizations like skills, rules, and MCP. If the budget is exceeded, large customizations will be truncated automatically.": "下方的明细展示了来自技能、规则和 MCP 等自定义项的 Token 使用情况。如果超出预算，大型规则将降级为路径指针，大型自定义项将被自动排除。",
    "The conversation could not be loaded because its data was not found.": "无法加载对话，因为未找到其数据。",
    "The conversation was compacted to fit within the context window.": "对话已压缩以适配上下文窗口。",
    "The conversation was compacted while generating this response.": "生成此回复时对话已被压缩。",
    "The current trigger rate is too high.": "当前触发频率过高。",
    "The full developer experience.": "完整的开发者体验。",
    "The server returned no conversation to fork into.": "服务器未返回可分叉的对话。",
    "The voice Jetski speaks with.": "Jetski 使用的语音。",
    "The voice used in Voice mode. Powered by Gemini Live.": "语音模式使用的语音，由 Gemini Live 提供。",
    "Theme": "主题",
    "There are no customizations enabled": "当前未启用任何自定义项",
    "There are no customizations enabled.": "当前未启用任何自定义项。",
    "Thinking...": "思考中...",
    "This action cannot be undone": "此操作无法撤销",
    "This action cannot be undone.": "此操作无法撤销。",
    "This command ran in the sandbox.": "此命令在沙盒中运行。",
    "This computer": "此计算机",
    "This migration may mess up your settings, chats, and sidebar.": "此迁移可能会打乱您的设置、对话和侧边栏。",
    "This month": "本月",
    "This prompt is straightforward and does not need alternative comparisons.": "此提示词很直接，不需要多模型候选对比。",
    "This redo action will not make any code changes.": "此重做操作不会对代码做出任何更改。",
    "This request is not well-suited for parallel Best-of-N generation.": "此请求不适合进行并行的 Best-of-N 候选生成。",
    "This undo action will not make any code changes.": "此撤销操作不会对代码做出任何更改。",
    "This week": "本周",
    "This will permanently delete": "这将永久删除包含在其中的",
    "Thought": "思考过程",
    "Thursday": "星期四",
    "Tip": "提示",
    "To modify notification settings, open your operating system's system preferences.": "要修改通知设置，请打开操作系统的系统偏好设置。",
    "Today": "今天",
    "Toggle Auxiliary Pane": "切换辅助面板",
    "Toggle Developer Tools": "切换开发者工具",
    "Toggle Environment Selector": "切换环境选择器",
    "Toggle File Viewer": "切换文件查看器",
    "Toggle Maximize Auxiliary Pane": "切换最大化辅助面板",
    "Toggle Maximize Side Panel": "切换最大化侧边栏",
    "Toggle Model Selector": "切换模型选择器",
    "Toggle Overview Panel": "切换概览面板",
    "Toggle Project Selector": "切换项目选择器",
    "Toggle Side Panel": "切换侧边栏",
    "Toggle Sidebar": "切换侧边栏",
    "Toggle Terminal": "切换终端",
    "Toggle Visibility": "切换显示/隐藏",
    "Toggle Voice Recording": "切换语音录制",
    "Token Usage": "Token 使用量",
    "Tokens": "Token 数",
    "Too many requests, please try again in a bit!": "请求过多，请稍后重试！",
    "Too many surveys": "问卷调查过多",
    "Tool Permissions": "工具权限",
    "Tool permissions": "工具权限",
    "Tools": "工具",
    "Trajectory Debug View": "运行轨迹调试视图",
    "Trajectory ID": "轨迹 ID",
    "Trigger": "触发器",
    "Trigger multiple response variants from the same prompt.": "从同一提示触发多个回答变体。",
    "True changes vs the parent workspace": "相对于父工作区的实际变更",
    "Try Remote Control": "尝试远程控制",
    "Tuesday": "星期二",
    "Turbo": "极速",
    "Turbo mode": "极速模式",
    "Turn on Remote Control in app settings": "请在应用设置中开启“远程控制”",
    "Turn on Remote Control in app settings.": "请在应用设置中开启“远程控制”。",
    "Turn on a flag you don't have": "开启尚未获得的功能开关",
    "Type / and select plan to have the agent generate a plan": "输入 / 并选择 plan 即可让智能体生成计划",
    "Type / and select plan to have the agent generate a plan.": "输入 / 并选择 plan 即可让智能体生成计划。",
    "Type absolute path or navigate folders...": "输入绝对路径或浏览文件夹...",
    "Typeahead menu": "预输入菜单",
    "Typing your corp password here may trigger a Password Alert reset.": "在此输入企业密码可能会触发密码警报重置。",
    "UI Extensions": "界面扩展",
    "Unable to resolve platform.": "无法解析平台。",
    "Uncommitted": "未提交",
    "Undo": "撤销",
    "Undo changes": "撤销更改",
    "Undo changes up to this point": "撤销更改至此处",
    "Undo restores your entire workspace to its state at this point.": "撤销会将整个工作区恢复到此时的状态。",
    "Unstage change": "取消暂存更改",
    "Untitled": "未命名",
    "Untracked (Unstaged)": "未跟踪 (未暂存)",
    "Up to date": "已是最新版本",
    "Update": "更新",
    "Update Available": "有可用更新",
    "Updated sidebar grouping": "已更新侧边栏分组",
    "Updater": "更新程序",
    "Updates": "更新",
    "Updates to your sidebar": "侧边栏更新",
    "Upgrade": "升级",
    "Uploads": "已上传文件",
    "Uptime": "运行时间",
    "Usage": "用量",
    "Use": "使用",
    "Use Add MCP to browse the store, or add a custom server via the MCP config": "使用“添加 MCP”浏览商店，或通过 MCP 配置添加自定义服务器",
    "Use Add MCP to browse the store, or add a custom server via the MCP config.": "使用“添加 MCP”浏览商店，或通过 MCP 配置添加自定义服务器。",
    "Use Add MCP to browse the store.": "使用“添加 MCP”浏览商店。",
    "Use Antigravity through your Gemini subscription.": "通过 Gemini 订阅使用 Antigravity。",
    "Use full Git clones for Best of N": "在 Best of N 中使用完整 Git 克隆",
    "Use full VCS clones for Best of N": "在 Best of N 中使用完整 VCS 克隆",
    "Use theme to be imported with settings": "使用随设置导入的主题",
    "Useful for typical development with an emphasis on security. It prioritizes safety over speed by requiring manual approval for all terminal commands and files outside the project directory.": "适用于注重安全的典型开发场景。它将安全性置于速度之上，要求对所有终端命令和项目目录之外的文件访问进行手动批准。",
    "User Type": "用户类型",
    "User cancelled agent execution.": "用户取消了智能体执行。",
    "Uses your local files and tools. Schedules only.": "使用本地文件和工具，仅按计划运行。",
    "Using the Antigravity Python SDK to build AI agents": "使用 Antigravity Python SDK 构建 AI 智能体",
    "Validation timed out.": "验证超时。",
    "Verbose": "详细",
    "Verbose Agent Chat": "详细的智能体对话",
    "Verification required": "需要验证",
    "Version": "版本",
    "View Page": "查看页面",
    "View Split Diff": "分屏查看差异",
    "View Usage": "查看用量",
    "View archived in the sidebar (Display options menu).": "在侧边栏查看已归档项目（显示选项菜单）。",
    "Viewed": "已查看",
    "Visit Legal Help to ask for content changes for legal reasons": "访问法律帮助以出于法律原因请求更改内容",
    "Visit Legal Help to ask for content changes for legal reasons.": "访问法律帮助以出于法律原因请求更改内容。",
    "Voice": "语音",
    "Voice mode": "语音模式",
    "Volume": "音量",
    "We'd love to hear from you.": "我们期待您的反馈。",
    "Web (desktop)": "Web (桌面端)",
    "Web (desktop, remote control)": "Web (桌面端，远程控制)",
    "Web (mobile)": "Web (移动端)",
    "Web (mobile, remote control)": "Web (移动端，远程控制)",
    "Web Search": "网络搜索",
    "Wednesday": "星期三",
    "Weekly Limit": "每周限额",
    "Weekly Limit Remaining": "每周限额剩余",
    "Welcome to Cider with Jetski": "欢迎使用配备智能助手的编辑器",
    "What should the agent do on each run? For example: summarize new bugs assigned to me and anything that changed overnight.": "智能体每次运行时应做什么？例如：汇总分配给我的新 Bug 以及夜间发生的变更。",
    "When disabled, you can check for updates manually from the app menu.": "禁用后，您可以从应用菜单手动检查更新。",
    "When enabled, the agent will include default customizations, including default skills.": "启用后，智能体将包含默认自定义项（包括默认技能）。",
    "When toggled on, Antigravity collects usage data to help Google enhance performance and features.": "开启后，Antigravity 将收集使用数据，以帮助 Google 提升性能和功能。",
    "When toggled on, Antigravity will use your AI credits to fulfill model requests once you're out of model quota. Antigravity will always use your model quota first before using AI credits.": "启用后，当您的模型配额用尽时，Antigravity 将使用您的 AI 积分来完成模型请求。Antigravity 将始终优先使用模型配额。",
    "Whether the agent asks you to review its documents": "智能体是否要求您审阅其文档",
    "Whether the agent asks you to review its documents.": "智能体是否要求您审阅其文档。",
    "Wide": "较宽",
    "Window": "窗口",
    "Windows Subsystem for Linux": "适用于 Linux 的 Windows 子系统 (WSL)",
    "Work with local agents from another device": "从另一台设备与本地智能体协同工作",
    "Work with local agents from another device.": "在其他设备上与本地智能体协同工作。",
    "Working.": "运行中。",
    "Working...": "运行中...",
    "Workspace": "工作区",
    "Workspace File Access": "工作区文件访问",
    "Workspace Settings": "工作区设置",
    "Workspace setup warning": "工作区配置警告",
    "Workspaces": "工作区",
    "Worktree": "工作区树",
    "Worktrees": "工作区树",
    "Write": "写入",
    "Yes, allow this time": "是，仅本次允许",
    "Yes, and always allow": "是，始终允许",
    "Yes, and always allow in this conversation": "是，在本次对话中始终允许",
    "Yes, and always allow when not in a project": "是，在未分组项目中始终允许",
    "Yes, save rule globally": "是，全局保存规则",
    "Yes, save rule in this conversation": "是，在本次对话中保存规则",
    "Yes, save rule when not in a project": "是，在未分组项目中保存规则",
    "Yesterday": "昨天",
    "You can prompt the model to try again or start a new conversation if the error persists.": "您可以提示模型重试，或者如果错误仍然存在，可以开启新的对话。",
    "You can upgrade to a Google AI Ultra plan to receive higher rate limits.": "您可以升级至 Google AI Ultra 套餐以获得更高的使用限额。",
    "You currently don't have any MCP Servers installed. Add an MCP server above or add a custom one via the MCP Config.": "您目前尚未安装任何 MCP 服务器。请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。",
    "Your Antigravity use will be associated with provided project.": "您的 Antigravity 使用将关联到提供的项目。",
    "Your Plan:": "当前计划：",
    "Your Plan: Google AI Pro": "当前计划：Google AI Pro",
    "Your administrator has disabled MCP servers for this workspace.": "您的管理员已为此工作区禁用 MCP 服务器。",
    "Your changes were not saved. Please try again.": "更改未保存，请重试。",
    "Your quota for this model is running low": "您对此模型的配额即将用尽",
    "Your quota for this model is running low.": "您对此模型的配额即将用尽。",
    "Zoom In": "放大",
    "Zoom Level": "缩放比例",
    "Zoom Out": "缩小",
    "Zoom in": "放大",
    "Zoom out": "缩小",
    "active conversation": "个进行中的对话",
    "active conversations": "个进行中的对话",
    "add": "添加",
    "agent": "智能体",
    "agents": "智能体",
    "allow": "允许",
    "analyzed": "已分析",
    "and select": "并选择",
    "application": "应用",
    "ask": "询问",
    "at": "于",
    "branch": "分支",
    "branches": "分支",
    "cancel": "取消",
    "clear": "清除",
    "close": "关闭",
    "coding agent": "编程智能体",
    "command": "命令",
    "commands": "命令",
    "confirm": "确认",
    "connect": "连接",
    "console": "控制台",
    "contrast": "对比度",
    "control": "控制",
    "conversation": "对话",
    "copy": "复制",
    "create": "创建",
    "cut": "剪切",
    "delete": "删除",
    "deny": "拒绝",
    "directory": "目录",
    "disable": "禁用",
    "dismiss": "忽略",
    "download": "下载",
    "duplicate": "制作副本",
    "e.g., curl": "例如：curl",
    "e.g., npm test": "例如：npm test",
    "edit": "编辑",
    "enable": "启用",
    "error": "错误",
    "failed": "失败",
    "false": "假",
    "file": "文件",
    "files": "文件",
    "find": "查找",
    "folder": "文件夹",
    "folders": "文件夹",
    "for more help": "以获取更多帮助",
    "for more help.": "以获取更多帮助。",
    "found": "找到",
    "global": "全局",
    "global settings": "全局设置",
    "hide": "隐藏",
    "hourly": "每小时",
    "including": "包括",
    "info": "信息",
    "inherit": "继承",
    "inherit global": "继承全局",
    "inherits": "继承",
    "input": "输入",
    "invalid media": "无效媒体",
    "just now": "刚刚",
    "legal help": "法律帮助",
    "limit": "限额",
    "limits": "限额",
    "local": "本地",
    "new": "新建",
    "no": "否",
    "no project": "无项目",
    "not found": "未找到",
    "notice": "提示",
    "now": "刚刚",
    "off": "关",
    "on": "开",
    "open": "打开",
    "output": "输出",
    "paste": "粘贴",
    "path": "路径",
    "paths": "路径",
    "pending": "等待中",
    "permanently delete": "永久删除",
    "plugin": "插件",
    "plugins": "插件",
    "project": "项目",
    "projects": "项目",
    "read": "读取",
    "reads": "读取",
    "remote": "远程",
    "remote control": "远程控制",
    "remove": "移除",
    "rename": "重命名",
    "retry": "重试",
    "run": "运行",
    "running": "运行中",
    "save": "保存",
    "search": "搜索",
    "select": "选择",
    "show": "显示",
    "start": "启动",
    "stop": "停止",
    "strong": "强",
    "subagent": "子智能体",
    "subagents": "子智能体",
    "success": "成功",
    "task": "任务",
    "tasks": "任务",
    "tell the agent what to do instead": "告诉智能体接下来该做什么",
    "terminal": "终端",
    "terminals": "终端",
    "to ask for content changes for legal reasons": "以出于法律原因请求更改内容",
    "to ask for content changes for legal reasons.": "以出于法律原因请求更改内容。",
    "to be installed. The browser subagent can be invoked by typing /browser in the conversation input box.": "。您可以在对话输入框中输入 /browser 来调用浏览器子智能体。",
    "to have the agent generate a plan": "即可让智能体生成计划",
    "to have the agent generate a plan.": "即可让智能体生成计划。",
    "troubleshooting guide": "排查指南",
    "troubleshooting_guide": "排查指南",
    "true": "真",
    "uncommitted": "未提交",
    "update": "更新",
    "uploads": "已上传文件",
    "view": "查看",
    "warning": "警告",
    "weekly": "每周",
    "when working in this project": "（当在此项目中工作时）",
    "when working in this project.": "（当在此项目中工作时）。",
    "workspace": "工作区",
    "workspaces": "工作区",
    "worktree": "工作区树",
    "worktrees": "工作区树",
    "write": "写入",
    "writes": "写入",
    "yes": "是",
  };

  const coreWords = {
    "add": "添加",
    "agent": "智能体",
    "agents": "智能体",
    "allow": "允许",
    "ask": "询问",
    "cancel": "取消",
    "clear": "清除",
    "close": "关闭",
    "command": "命令",
    "commands": "命令",
    "confirm": "确认",
    "console": "控制台",
    "copy": "复制",
    "create": "创建",
    "cut": "剪切",
    "delete": "删除",
    "deny": "拒绝",
    "directory": "目录",
    "disable": "禁用",
    "dismiss": "忽略",
    "download": "下载",
    "duplicate": "制作副本",
    "edit": "编辑",
    "enable": "启用",
    "error": "错误",
    "failed": "失败",
    "false": "假",
    "file": "文件",
    "files": "文件",
    "find": "查找",
    "folder": "文件夹",
    "global": "全局",
    "hide": "隐藏",
    "info": "信息",
    "input": "输入",
    "new": "新建",
    "no": "否",
    "notice": "提示",
    "off": "关",
    "on": "开",
    "open": "打开",
    "output": "输出",
    "paste": "粘贴",
    "pending": "等待中",
    "regenerate": "重新生成",
    "remove": "移除",
    "rename": "重命名",
    "retry": "重试",
    "run": "运行",
    "running": "运行中",
    "save": "保存",
    "search": "搜索",
    "select": "选择",
    "show": "显示",
    "split": "分屏",
    "start": "启动",
    "stop": "停止",
    "subagent": "子智能体",
    "subagents": "子智能体",
    "success": "成功",
    "task": "任务",
    "tasks": "任务",
    "terminal": "终端",
    "true": "真",
    "update": "更新",
    "view": "查看",
    "warning": "警告",
    "workspace": "工作区",
    "workspaces": "工作区",
    "yes": "是",
  };

  // Structured Prefix & Content Match Rules for Complex / Truncated Text
  const textPrefixRules = [
    // Plugins & Customizations
    ["Plugins are packaged collections of skills and MCPs to help the Agent in", "插件是技能和 MCP 的打包集合，用于帮助 "],
    ["Plugins are packaged collections of skills and MCPs", "插件是技能和 MCP 的打包集合，用于帮助 "],
    ["work with Google developer products. You can always change your choices in Settings.", " 中的智能体与 Google 开发者产品协同工作。您可以随时在“设置”中更改您的选择。"],
    ["Provides a comprehensive guide", "提供 Google Antigravity (AGY) 的综合指南、快速参考和站点地图，包括 Antigravity CLI、Antigravity 2.0、IDE、Python SDK、斜杠命令、快捷键和自定义项。"],
    ["How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill", "如何在对话中内联或作为独立产物渲染丰富的交互式 HTML 小部件。当您想要向用户显示图表、数据可视化或交互式控件时，请使用此技能。"],
    ["Automatically migrate legacy workflows", "自动将旧版工作流迁移到技能目录。它会扫描现有工作流，并创建目标..."],
    ["Guidelines for interacting with GitHub and request permissions", "关于与 GitHub 交互的指南，并在智能体环境中由于限制导致命令失败时向用户请求相应的权限。"],
    ["Comprehensive guide and reference for the Antigravity Customization System", "Antigravity 自定义系统的综合指南和参考。用于解释自定义项的工作原理、加载优先级、发现机制，并指导创建技能、规则、插件、钩子和 MCP 服务器。"],
    ["Skills providing tailored instructions for happy path", "提供 Dart 和 Flutter 开发主流程定制化指南的技能。"],
    ["Interactive guide to design and create a scheduled background automation", "设计和创建计划后台自动化的交互式指南。当用户想要创建自动化或周期性计划任务时（例如“总结我的邮件”），请使用此技能。"],
    ["How to manage and create plugins", "如何管理和创建插件——作为单一单元安装、启用和禁用的命名空间技能、智能体、规则、MCP 服务器和钩子捆绑包。"],
    ["Build, package, run, and debug UI extensions for Antigravity", "为 Antigravity 构建、打包、运行和调试 UI 扩展：在侧边面板中渲染的交互式 Web 面板，由使用内置 Sidecar SDK 的 Node.js sidecar 提供服务。"],
    ["Discover UI plugin panels relevant to the current task", "发现与当前任务相关的 UI 插件面板，并在对话中显示一键式快捷胶囊以在侧边面板中打开（切换）它们。"],
    ["Build and prototype location-aware applications with Google Maps Platform", "使用 Google Maps Platform 构建具有位置感知能力的应用并设计原型。"],
    ["Specialized suite of skills for data engineers and database", "专为 Google Cloud 上的数据工程师和数据库从业人员打造的专业技能套件。"],
    ["Build applications with the Gemini Interactions API and Live API", "使用 Gemini Interactions API 和 Live API 构建应用，包括文本生成、多轮对话等功能。"],
    ["Build on Google's developer platforms, including Android, Chrome, Gemini, and Google Cloud.", "基于 Google 开发者平台（包括 Android、Chrome、Gemini 和 Google Cloud）构建。"],
    ["Prototype, build & run modern apps that user", "原型设计、构建和运行现代应用程序..."],
    ["Curated collection of agent skills for science t", "为科学任务精心挑选的智能体技能集合。"],
    ["Using the Google Antigravity Python SDK to b", "使用 Google Antigravity Python SDK 构建自定义智能体..."],
    ["Search and retrieve official documentation acr", "搜索和检索官方开发者文档..."],
    ["Integration skill and tools for Google Maps Pl", "适用于 Google Maps Platform 的集成技能和工具。"],
    ["Official plugin for Dart and Flutter that installs", "Dart 和 Flutter 官方插件，提供相关工具安装和开发支持。"],
    ["This plugin provides a specialized suite of skill", "此插件提供一套专为数据处理打造的专业技能..."],
    ["Connect to Google Workspace, including Docs, Sheets, Slides, Drive, and Calendar.", "连接到 Google Workspace，包括文档、表格、幻灯片、云端硬盘和日历。"],
    ["Read, draft, and edit docs.", "读取、起草和编辑文档。"],
    ["Read, write, and format spreadsheets.", "读取、写入和格式化电子表格。"],
    ["Read, edit, and export presentations.", "读取、编辑和导出演示文稿。"],
    ["Search, upload, download, and share files.", "搜索、上传、下载和共享文件。"],
    ["Check availability, schedule events, and RSVP.", "查看空闲时间、安排活动并回复邀请。"],

    // MCP Servers Descriptions
    ["Investigate and fix software issues using AI-powered root cause analysis", "使用 AI 驱动的根本原因分析来调查和修复软件问题。此 MCP 服务器连接到您的 Antimetal 账户..."],
    ["Query and act on your marketing, analytics, CRM, e-commerce", "跨 325 多个连接器查询并处理您的营销、分析、CRM、电子商务和仓库数据..."],
    ["Query your GitLab SDLC as a knowledge graph", "将您的 GitLab SDLC 作为知识图谱进行查询。Orbit 会建立相关索引..."],
    ["Enable Antigravity to deploy apps to Google Cloud Run", "使 Antigravity 能够将应用部署到 Google Cloud Run。"],
    ["Search and reference over 600,000 real-world app screens", "搜索并参考超过 600,000 个真实的应用程序屏幕、用户流程和 UI 模式..."],
    ["Build, edit, deploy, and manage full-stack web apps with Lovable", "使用自然语言，通过 Lovable 构建、编辑、部署和管理全栈 Web 应用..."],
    ["The GKE remote MCP server provides read write access to your GKE", "GKE 远程 MCP 服务器提供对您的 GKE Kubernetes 资源的读写访问权限。"],
    ["The Dart and Flutter MCP server exposes Dart (and Flutter)", "Dart 和 Flutter MCP 服务器向兼容的 AI 助手客户端公开相关开发工具操作。"],
    ["The Firebase Model Context Protocol (MCP) Server gives AI-powered", "Firebase MCP 服务器使 AI 工具能够处理您的 Firebase 项目和应用程序代码库。"],
    ["The Genkit Model Context Protocol (MCP) Server gives AI-powered", "Genkit MCP 服务器使 AI 工具能够构建、调试和检查您的 Genkit 应用。"],
    ["The gopls Model Context Protocol (MCP) server provides tools", "gopls MCP 服务器为您的 Go 代码库提供语义代码分析、实时诊断和转换工具。"],
    ["Interact with your BigQuery data using natural language", "使用自然语言与您的 BigQuery 数据交互。允许您安全地连接到您的数据集..."],
    ["The AlloyDB for PostgreSQL remote MCP server lets you access", "AlloyDB for PostgreSQL 远程 MCP 服务器允许您访问和运行 AlloyDB 工具..."],
    ["The Bigtable Admin remote MCP server lets you manage Bigtable", "Bigtable Admin 远程 MCP 服务器允许您管理 Bigtable 资源。"],
    ["The Cloud SQL remote MCP server lets you access and run Cloud SQL", "Cloud SQL 远程 MCP 服务器允许您访问和运行 Cloud SQL 工具..."],
    ["The Spanner remote MCP server lets you access and run Spanner", "Spanner 远程 MCP 服务器允许您访问和运行 Spanner 工具..."],
    ["The Apigee API hub remote MCP server lets you manage", "Apigee API hub 远程 MCP 服务器允许您管理 API、版本、规范、操作等。"],
    ["Connect your AI assistants to Looker business intelligence", "将您的 AI 助手连接到 Looker 商业智能，通过自然语言查询实现数据探索。"],
    ["Connect your AI assistants to the Knowledge Catalog", "将您的 AI 助手连接到 Knowledge Catalog，实现数据发现和治理。"],
    ["The MCP Toolbox for Databases is an open-source MCP server", "MCP Toolbox for Databases 是一个开源 MCP 服务器，旨在简化和保护用于与数据库交互的工具的开发。"],
    ["Interact with your Oracle Database data using natural language", "使用自然语言与您的 Oracle 数据库交互。此 MCP 服务器允许您安全地连接到您的数据库以执行 SQL 查询..."],
    ["The Dev Mode MCP Server brings Figma directly into your workflow", "Dev Mode MCP 服务器通过向从 Figma 生成代码的 AI 智能体提供重要的设计信息和上下文，将 Figma 直接带入您的工作流..."],
    ["The GitHub MCP Server is a Model Context Protocol (MCP) server", "GitHub MCP 服务器提供与 GitHub API 的无缝集成，从而实现高级自动化和..."],
    ["The Google Home Developer MCP server allows you to search", "Google Home Developer MCP 服务器允许您搜索 Google Home 文档、OpenThread 和 Matter 规范文档。"],
    ["Neon MCP Server is an open-source tool that lets you interact", "Neon MCP 服务器是一个开源工具，允许您使用自然语言与您的 Neon Postgres 数据库交互。"],
    ["The Stripe Model Context Protocol server allows you to integrate", "Stripe MCP 服务器允许您通过函数调用与 Stripe API 集成。该协议支持各种交互工具..."],
    ["Interact with Redis key-value stores", "与 Redis 键值存储交互。"],
    ["A Model Context Protocol server for interacting with MongoDB", "用于与 MongoDB Atlas 交互的模型上下文协议服务器。"],
    ["Official Notion MCP Server that allows interaction with Notion", "官方 Notion MCP 服务器，允许通过 Notion API 与 Notion 工作区、页面、数据库和评论进行交互。"],
    ["Official Linear.app MCP Server for interacting with Linear", "官方 Linear.app MCP 服务器，用于与 Linear 项目、议题和工作流进行交互。"],
    ["An MCP server implementation that integrates the Perplexity", "一个集成了 Perplexity Sonar API 的 MCP 服务器实现，以提供实时的、全网范围的研究能力。"],
    ["Official PayPal MCP Server that allows integration with PayPal", "官方 PayPal MCP 服务器，允许与 PayPal API 集成，用于支付处理、交易管理和账户操作。"],
    ["The Heroku Platform MCP Server enables seamless interaction", "Heroku Platform MCP 服务器可实现与 Heroku 平台资源的无缝交互，允许 LLM 读取、管理和操作应用程序..."],
    ["The Pinecone MCP Server enables AI tools to search Pinecone", "Pinecone MCP 服务器使 AI 工具能够搜索 Pinecone 文档、配置索引、根据索引配置生成代码..."],
    ["Connect your Supabase projects to AI assistants.", "将您的 Supabase 项目连接到 AI 助手。此 MCP 服务器允许管理表、获取配置、执行 SQL 查询、管理边缘函数等..."],
    ["The Prisma MCP Server enables AI tools to interact with Prisma", "Prisma MCP 服务器使 AI 工具能够与 Prisma 交互，从而轻松创建和管理 Postgres 数据库。"],
    ["The Locofy MCP Server", "Locofy MCP 服务器使 Locofy.ai 代码能够与您的 IDE 集成并进行扩展。"],
    ["Locofy MCP Server enables Locofy.ai code", "Locofy MCP 服务器使 Locofy.ai 代码能够与您的 IDE 集成并进行扩展。"],
    ["Airweave lets agents search any app.", "Airweave 允许智能体搜索任何应用程序。"],
    ["Atlassian MCP Server for interacting with Atlassian", "用于与 Atlassian 产品交互的 Atlassian MCP 服务器。"],
    ["Interact with your Harness account using natural language", "使用自然语言与您的 Harness 账户交互。此 MCP 服务器允许 AI 智能体检查和管理 CI/CD 流水线、执行、服务..."],
    ["SonarQube MCP Server enables AI assistants to interact", "SonarQube MCP 服务器使 AI 助手能够与 SonarQube 实例交互，进行代码质量分析、项目管理和质量门限操作。"],
    ["Perform searches on ingested data in Google-owned data stores", "在 Google 拥有的数据存储中，对已摄取的数据执行搜索。"],
    ["Interact with documents stored in a Firestore database", "使用自然语言与存储在 Firestore 数据库中的文档进行交互。"],
    ["Access resources in the Cloud Logging platform using natural", "使用自然语言访问 Cloud Logging 平台中的资源。"],
    ["Manage clusters for Managed Service for Apache Kafka", "使用自然语言管理 Apache Kafka 托管服务和 Kafka Connect 的集群。"],
    ["Access resources in the Cloud Monitoring platform using natural", "使用自然语言访问 Cloud Monitoring 平台中的资源。"],
    ["Manage Pub/Sub resources and publish messages. Create, list,", "管理 Pub/Sub 资源并发布消息。创建、列出、获取、更新和删除 Pub/Sub 主题、订阅和快照，以及发布消息..."],
    ["The Cloud Quotas MCP server allows you to view quota allocations", "Cloud Quotas MCP 服务器允许您查看配额分配、请求增加配额以及管理配额调整器配置。"],
    ["Enable Antigravity to control and inspect a live Chrome browser", "使 Antigravity 能够控制和检查实时 Chrome 浏览器，利用 Chrome DevTools 的强大功能进行可靠的自动化、深度调试..."],
    ["Netlify MCP Server enables AI assistants to interact", "Netlify MCP 服务器使 AI 助手能够与 Netlify 平台交互，以管理站点、部署、域名和其他 Web 开发工作流。"],
    ["A Model Context Protocol server that provides structured thinking", "一个模型上下文协议服务器，为 LLM 对话提供结构化思考和推理能力。"],
    ["Sonatype MCP server for interacting with our dependency management", "用于与我们的依赖项管理和安全情报平台交互的 Sonatype MCP 服务器。"],
    ["The Google Maps Platform Code Assist MCP server provides", "Google Maps Platform Code Assist MCP 服务器为您喜爱的 AI 编程助手提供最新、官方的 Google Maps Platform 文档、代码..."],
    ["This MCP server provides your LLM with docs and examples to instrument your AI apps with Arize AX", "此 MCP 服务器为您的 LLM 提供文档和示例，以便使用 Arize AX 检测您的 AI 应用。它还提供对 Arize 支持的访问。将其连接到您的 IDE..."],
    ["The Postman MCP Server connects Postman to AI tools", "Postman MCP 服务器将 Postman 连接到 AI 工具，使 AI 智能体和助手能够访问工作区、管理集合和环境..."],
    ["The Stitch MCP server enables AI assistants to interact with Stitch", "Stitch MCP 服务器使 AI 助手能够与 Stitch 交互以进行设计：从文本和图像生成 UI 设计，以及访问项目和屏幕..."],
    ["The ClickHouse MCP server enables agents to securely interact", "ClickHouse MCP 服务器使智能体能够安全地与 ClickHouse 数据库交互。它提供了一个通用接口来执行 SQL、探索数据和查看..."],
    ["Perform a range of infrastructure management tasks, including: manage virtual machine", "执行一系列基础设施管理任务，包括：管理虚拟机 (VM) 实例、管理实例组管理器和实例模板..."],
    ["Access enterprise mobility data using natural language queries", "使用关于设备队列的自然语言查询、策略合规性的自动审计以及设备集成来访问企业移动数据..."],
    ["Search your Google Cloud projects using natural language", "使用自然语言搜索您的 Google Cloud 项目。"],

    // Error and Fallback Links
    ["Kick off work on your computer and continue working", "在电脑上启动工作，并可以通过手机或其他设备继续与智能体协同工作。请在应用设置中开启“远程控制”。"],
    ["Turn on Remote Control in app settings", "请在应用设置中开启“远程控制”。"],
    ["Try Remote Control", "尝试远程控制"],
    ["Agent execution terminated due to error", "智能体执行因错误而终止。"],
    ["Confirming this undo action will make the following changes", "确认此撤销操作将做出以下更改："],
    ["Confirming this undo action will not make any code changes", "确认此撤销操作不会做出任何代码更改。"],
    ["Confirming this redo action will make the following changes", "确认此重做操作将做出以下更改："],
    ["Confirming this redo action will not make any code changes", "确认此重做操作不会做出任何代码更改。"],
    ["Undo changes up to this point", "撤销更改至此处"],
    ["Redo changes up to this point", "重做更改至此处"],
    ["Our servers are experiencing high traffic", "我们的服务器当前负载较高，请稍后重试。"],
    ["Agent terminated due to error", "智能体因错误而终止"],
    ["You can prompt the model to try again", "您可以提示模型重试，或者如果错误仍然存在，可以开启新的对话。"],
    ["for more help", " 以获取更多帮助。"],
    ["See our", "查看我们的 "]
  ];
  textPrefixRules.sort(function(a, b) { return b[0].length - a[0].length; });

  function translateText(text) {
    if (!text || typeof text !== 'string') return text;
    let trimmed = text.trim();
    if (!trimmed) return text;

    if (dictionary[trimmed]) {
      return text.replace(trimmed, dictionary[trimmed]);
    }
    
    // Dynamic Regex Translations
    let m;
    if (text.indexOf("of the customization budget is available") !== -1) {
      text = text.replace(/(\d+(?:\.\d+)?)% of the customization budget is available\.?/g, "自定义项预算可用额度为 $1%。");
      text = text.replace(/%\s*of the customization budget is available\.?/g, "% 的自定义项预算可用额度。");
      text = text.replace(/(^\s*)of the customization budget is available\.?/g, "$1的自定义项预算可用额度。");
    }
    if ((m = trimmed.match(/^Show (\d+) breakdowns?$/))) {
      return text.replace(trimmed, "显示 " + m[1] + " 项明细");
    }
    if ((m = trimmed.match(/^Explored (\d+) files? >$/))) {
      return text.replace(trimmed, "已浏览 " + m[1] + " 个文件 >");
    }
    if ((m = trimmed.match(/^Editing (.+) \+(\d+) -(\d+)$/))) {
      return text.replace(trimmed, "正在编辑 " + m[1] + " +" + m[2] + " -" + m[3]);
    }
    if (trimmed === "Waiting for user input") {
      return text.replace(trimmed, "等待用户输入");
    }
    if ((m = trimmed.match(/^Artifacts?\s*(\d+)$/i))) {
      return text.replace(trimmed, "产物 " + m[1]);
    }
    if ((m = trimmed.match(/^No artifacts generated\.?$/i))) {
      return text.replace(trimmed, "未生成任何产物");
    }
    if (/(?:No|否)\s*(?:projects?|项目)?\s*found/i.test(text) || text.indexOf("No projects found") !== -1 || text.indexOf("No project found") !== -1) {
      return text.replace(/(?:No|否)\s*(?:projects?|项目)?\s*found\.?|No projects found\.?|No project found\.?/gi, "暂无项目");
    }
    if ((m = trimmed.match(/^(?:No|否)\s*projects?\s*found\.?$/i))) {
      return text.replace(trimmed, "暂无项目");
    }
    if ((m = trimmed.match(/^No\s+Project$/i))) {
      return text.replace(trimmed, "无项目");
    }
    if (trimmed === "Type") return text.replace(trimmed, "输入");
    if (trimmed === "and select") return text.replace(trimmed, "并选择");
    if (trimmed === "to have the agent generate a plan." || trimmed === "to have the agent generate a plan") {
      return text.replace(trimmed, "即可让智能体生成计划。");
    }
    if (trimmed === "Visit") return text.replace(trimmed, "访问");
    if (trimmed === "Legal Help") return text.replace(trimmed, "法律帮助");
    if (trimmed === "to ask for content changes for legal reasons." || trimmed === "to ask for content changes for legal reasons") {
      return text.replace(trimmed, "以出于法律原因请求更改内容。");
    }
    if ((m = trimmed.match(/^Learn more about (.+)$/))) {
      return text.replace(trimmed, "了解更多关于 " + (dictionary[m[1]] || m[1]) + " 的信息");
    }
    if ((m = trimmed.match(/^You have used some of your weekly limit, it will fully refresh in (.*)\.$/))) {
      let timeStr = m[1].replace(/days?/g, "天").replace(/hours?/g, "小时").replace(/minutes?/g, "分钟").replace(/,/g, "");
      return text.replace(trimmed, "您已使用部分每周限额，它将在 " + timeStr + " 后完全重置。");
    }
    if ((m = trimmed.match(/^You have used some of your 5-hour limit, it will fully refresh in (.*)\.$/))) {
      let timeStr = m[1].replace(/days?/g, "天").replace(/hours?/g, "小时").replace(/minutes?/g, "分钟").replace(/,/g, "");
      return text.replace(trimmed, "您已使用部分五小时限额，它将在 " + timeStr + " 后完全重置。");
    }
    if ((m = trimmed.match(/^Resets? in\s+(.+)$/i))) {
      let timeStr = m[1]
        .replace(/(\d+)\s*d(?:ays?)?/gi, "$1天 ")
        .replace(/(\d+)\s*h(?:ours?)?/gi, "$1小时 ")
        .replace(/(\d+)\s*m(?:inutes?|ins?)?/gi, "$1分钟 ")
        .replace(/(\d+)\s*s(?:econds?|ecs?)?/gi, "$1秒 ")
        .replace(/,\s*/g, " ")
        .trim();
      return text.replace(trimmed, "将在 " + timeStr + " 后重置");
    }
    if (/^Exploring\b/i.test(trimmed) || /running command/i.test(trimmed)) {
      let translatedActions = trimmed
        .replace(/Exploring file/gi, "浏览文件")
        .replace(/running command/gi, "运行命令")
        .replace(/editing file/gi, "编辑文件")
        .replace(/,\s*/g, "、");
      return text.replace(trimmed, translatedActions);
    }
    if ((m = trimmed.match(/^Files? Changed\s*(\d+)$/i))) return text.replace(trimmed, "已修改文件 " + m[1]);
    if ((m = trimmed.match(/^Uploads?\s*(\d+)$/i))) return text.replace(trimmed, "已上传文件 " + m[1]);
    if ((m = trimmed.match(/^See all\s*\((.+?)\)$/i))) return text.replace(trimmed, "查看全部 (" + m[1] + ")");
    if ((m = trimmed.match(/^Background Tasks?\s*(\d+)$/i))) return text.replace(trimmed, "后台任务 " + m[1]);
    if ((m = trimmed.match(/^Terminals?\s*(\d+)$/i))) return text.replace(trimmed, "终端 " + m[1]);
    if ((m = trimmed.match(/^No subagents?(?:\s*running)?\.?$/i))) return text.replace(trimmed, "暂无子智能体");
    if ((m = trimmed.match(/^Available AI Credits: ([\d,]+)$/))) {
      return text.replace(trimmed, "可用 AI 积分: " + m[1]);
    }
    if ((m = trimmed.match(/^Send feedback as (.+)$/))) {
      return text.replace(trimmed, "以 " + m[1] + " 的身份发送反馈");
    }
    if ((m = trimmed.match(/^(\+?\d+) more lines$/))) {
      return text.replace(trimmed, "更多 " + m[1] + " 行");
    }
    if ((m = trimmed.match(/^(\d+) files? changed$/))) {
      return text.replace(trimmed, m[1] + " 个文件已修改");
    }
    if ((m = trimmed.match(/^See (\d+) more$/i))) return text.replace(trimmed, "查看更多 " + m[1] + " 项");
    if ((m = trimmed.match(/^Last (\d+) days?$/i))) return text.replace(trimmed, "最近 " + m[1] + " 天");
    if ((m = trimmed.match(/^Last (\d+) hours?$/i))) return text.replace(trimmed, "最近 " + m[1] + " 小时");
    if ((m = trimmed.match(/^Last (\d+) months?$/i))) return text.replace(trimmed, "最近 " + m[1] + " 个月");
    if ((m = trimmed.match(/^Version ([\d\.]+(-\w+)?)$/))) {
      return text.replace(trimmed, "版本 v" + m[1]);
    }
    if ((m = trimmed.match(/^Start using (.+?), our best (.+?) model\.?$/i))) {
      return text.replace(trimmed, "开始使用 " + m[1] + "，我们最强大的 " + m[2] + " 模型。");
    }
    if (text.indexOf("is now available on paid Pro and Ultra plans") !== -1 || text.indexOf("Third-party model access will no longer be available") !== -1) {
      return "Sonnet 5.5 现已在付费的 Pro 和 Ultra 方案中提供。从 2026 年 11 月 2 日起，您当前的方案将不再支持访问第三方模型。";
    }
    if ((m = trimmed.match(/^(\d+)\s*s(?:\s*ago)?$/i))) return text.replace(trimmed, m[1] + "秒前");
    if ((m = trimmed.match(/^(\d+)\s*m(?:\s*ago)?$/i))) return text.replace(trimmed, m[1] + "分钟前");
    if ((m = trimmed.match(/^(\d+)\s*h(?:\s*ago)?$/i))) return text.replace(trimmed, m[1] + "小时前");
    if ((m = trimmed.match(/^(\d+)\s*d(?:\s*ago)?$/i))) return text.replace(trimmed, m[1] + "天前");

    // Dynamic Time Formatter
    if (text.indexOf("Worked for") !== -1) {
      return text.replace(/Worked for ([\d\.a-z ]+)/gi, function(_, timeStr) {
        let t = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "运行耗时 " + t;
      });
    }
    if (text.indexOf("Thought for") !== -1) {
      return text.replace(/Thought for ([\d\.a-z ]+)/gi, function(_, timeStr) {
        let t = timeStr.replace(/ms/g, "毫秒").replace(/s/g, "秒").replace(/m/g, "分").replace(/h/g, "小时");
        return "思考耗时 " + t;
      });
    }

    // Special Multi-segment Matches
    if (text.indexOf("Google Developer Knowledge") !== -1 || text.indexOf("official developer documentation and retrieve") !== -1) {
      return "Google Developer Knowledge MCP 服务器使 AI 驱动的开发工具能够搜索 Google 的官方开发者文档并检索相关内容...";
    }
    if (text.indexOf("Ask questions. Get answers") !== -1) {
      if (text.indexOf("PostHog") !== -1) {
        return "提出问题。获取答案。该 MCP 是您的编程智能体与之对话的服务器。用英语提问，它会针对您的 PostHog 数据运行查询并返回结果。";
      }
      return "提出问题。获取答案。该 MCP 是您的 ";
    }
    if (text.indexOf("talks to. Ask a question in English") !== -1 || text.indexOf("runs the query against your") !== -1) {
      return " 与之对话的服务器。用英语提问，它会针对您的 ";
    }
    if (text.indexOf("The answer lands") !== -1 || text.indexOf("data. The answer") !== -1) {
      return " 数据运行查询并返回结果。";
    }

    if (text.indexOf("Configure the browser subagent") !== -1) {
      text = text.replace(/Configure the browser subagent\.?/g, "配置浏览器子智能体。");
    }
    if (text.indexOf("to be installed.") !== -1) {
      text = text.replace(/\s?to be installed\./g, "");
    }
    if (text.indexOf("The browser subagent can be invoked by typing") !== -1) {
      text = text.replace(/The browser subagent can be invoked by typing \/browser in the conversation input box\./g, "您可以在对话输入框中输入 /browser 来调用浏览器子智能体。");
    }

    if (text.indexOf("You currently don't have any MCP Servers installed.") !== -1) {
      text = text.replace(/You currently don't have any MCP Servers installed\./g, "您目前尚未安装任何 MCP 服务器。");
    }
    if (text.indexOf("Add an MCP server above") !== -1) {
      text = text.replace(/Add an MCP server above or add a custom one via the MCP Config\./g, "请在上方添加 MCP 服务器，或通过 MCP 配置添加自定义服务器。");
    }

    // Prefix Rules Matching
    for (let i = 0; i < textPrefixRules.length; i++) {
      if (text.indexOf(textPrefixRules[i][0]) !== -1) {
        return textPrefixRules[i][1];
      }
    }

    // Short Word Exact Replacement
    let wordsCount = trimmed.split(/\s+/).length;
    if (wordsCount <= 3) {
      let lowerText = trimmed.toLowerCase();
      if (coreWords[lowerText]) {
        return text.replace(trimmed, coreWords[lowerText]);
      }
    }
    
    return text;
  }

  // ----- protection & attribute handling ---------------------------------
  var PROTECTED_SELECTOR = [
    "pre", "code", "kbd", "samp", "textarea",
    ".monaco-editor", ".xterm", ".terminal", ".diff-editor", ".diff-view",
    ".markdown-body", "[contenteditable=\"true\"]",
    "[data-message-author-role]", "[data-lexical-editor]", "[role=\"textbox\"]"
  ].join(",");

  function isProtected(el) {
    if (!el || !el.closest) return false;
    try { return !!el.closest(PROTECTED_SELECTOR); } catch (e) { return false; }
  }

  var ATTRS = ["title", "placeholder", "aria-label", "data-tooltip", "alt", "value"];

  var EMPTY_STATES = {
    "No automations yet": "暂无自动化",
    "否 automations yet": "暂无自动化",
    "No projects yet": "暂无项目",
    "否 projects yet": "暂无项目",
    "No conversations yet": "暂无对话",
    "否 conversations yet": "暂无对话"
  };

  var FULL_PHRASES = {
    "Type / and select plan to have the agent generate a plan.": "输入 / 并选择 plan，让智能体生成计划。"
  };

  var CONSERVATIVE = true;

  function normalizeText(value) {
    return (value || "").replace(/\s+/g, " ").trim();
  }

  function fragmentCoverage(el) {
    var nodes = [];
    (function collect(node) {
      if (!node || !node.childNodes) return;
      for (var i = 0; i < node.childNodes.length; i++) {
        var child = node.childNodes[i];
        if (child.nodeType === Node.TEXT_NODE) nodes.push(child);
        else if (child.nodeType === Node.ELEMENT_NODE) collect(child);
      }
    })(el);
    for (var j = 0; j < nodes.length; j++) {
      var text = nodes[j].textContent;
      if (!text || !/[A-Za-z]/.test(text)) continue;
      if (translateText(text) !== text) continue;
      var parent = nodes[j].parentElement;
      if (parent && parent.closest && parent.closest("a, code, kbd, samp")) continue;
      return false;
    }
    return true;
  }

  function hasBlockChild(el) {
    if (!el || !el.children) return false;
    for (var i = 0; i < el.children.length; i++) {
      var t = el.children[i].tagName;
      if (t === "P" || t === "DIV" || t === "LI" || t === "UL" || t === "OL" ||
          t === "SECTION" || t === "ARTICLE" || t === "HEADER" || t === "FOOTER" ||
          t === "TABLE" || t === "TR" || t === "TD") return true;
    }
    return false;
  }

  function shouldSkipSubtree(el) {
    if (!CONSERVATIVE || !el || !el.textContent) return false;
    var full = normalizeText(el.textContent);
    if (full.length < 12 || full.length > 300) return false;
    if (!/[.!?]$/.test(full)) return false;
    if (dictionary[full]) return false;
    var tag = el.tagName;
    if (tag !== "P" && tag !== "DIV" && tag !== "SPAN" && tag !== "LI" && tag !== "LABEL" && tag !== "TD") return false;
    if (el.children && el.children.length > 8) return false;
    if (hasBlockChild(el)) return false;
    if (el.querySelector && el.querySelector("button, input, select, textarea, [role=\"button\"]")) return false;
    return !fragmentCoverage(el);
  }

  function translateAttrs(el) {
    if (!el || !el.getAttribute) return;
    for (var i = 0; i < ATTRS.length; i++) {
      var name = ATTRS[i];
      var value = el.getAttribute(name);
      if (!value) continue;
      if (name === "value" && el.tagName === "INPUT") {
        var type = (el.getAttribute("type") || "").toLowerCase();
        if (type !== "button" && type !== "submit" && type !== "reset") continue;
      }
      var translated = translateText(value);
      if (translated !== value) el.setAttribute(name, translated);
    }
  }

  function processNode(node) {
    if (!node) return;
    if (node.nodeType === Node.TEXT_NODE) {
      var parent = node.parentElement;
      if (parent) {
        var full = normalizeText(parent.textContent);
        if (EMPTY_STATES[full]) {
          parent.textContent = EMPTY_STATES[full];
          return;
        }
        if (CONSERVATIVE && full !== normalizeText(node.textContent) && /[.!?]$/.test(full)) {
          if (full.length <= 300 && !hasBlockChild(parent) && !fragmentCoverage(parent)) {
            return;
          }
        }
      }
      if (isProtected(parent)) return;
      var original = node.textContent;
      var translated = translateText(original);
      if (translated !== original) node.textContent = translated;
      return;
    }
    if (node.nodeType !== Node.ELEMENT_NODE) return;
    var tag = node.tagName;
    if (tag === "SCRIPT" || tag === "STYLE" || tag === "NOSCRIPT" || tag === "TEMPLATE") return;
    translateAttrs(node);
    if (isProtected(node)) return;
    var fullPhrase = normalizeText(node.textContent);
    if (FULL_PHRASES[fullPhrase]) {
      node.textContent = FULL_PHRASES[fullPhrase];
      return;
    }
    if (shouldSkipSubtree(node)) return;
    if (tag === "SVG" || tag === "CANVAS") return;
    var children = Array.from(node.childNodes);
    for (var i = 0; i < children.length; i++) processNode(children[i]);
  }

  var observer = new MutationObserver(function(mutations) {
    for (var i = 0; i < mutations.length; i++) {
      var mutation = mutations[i];
      if (mutation.type === "childList") {
        mutation.addedNodes.forEach(processNode);
      } else if (mutation.type === "characterData") {
        processNode(mutation.target);
      } else if (mutation.type === "attributes") {
        translateAttrs(mutation.target);
      }
    }
  });

  function start() {
    if (!document.documentElement) return;
    processNode(document.documentElement);
    observer.observe(document.documentElement, {
      childList: true,
      subtree: true,
      characterData: true,
      attributes: true,
      attributeFilter: ATTRS
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start, { once: true });
  } else {
    start();
  }
})();
"""

MENU_JS = r"""// Antigravity zh-CN menu translator
(function() {
  if (globalThis.__antigravityZhMenu) return;
  globalThis.__antigravityZhMenu = true;

  var menuTranslationMap = {"About Antigravity": "关于 Antigravity", "Actual Size": "实际大小", "Add inline comment": "添加行内评论", "Add to Chat": "添加到对话", "Add to Chat/Quote": "添加到对话/引用", "Archive": "归档", "Archive This Conversation": "归档此对话", "Ask before sensitive operations.": "敏感操作前询问。", "Auto (Preview)": "自动（预览）", "Automatically decide if commands run.": "自动决定是否运行命令。", "Back": "返回", "Check for Updates": "检查更新", "Checking for Updates...": "正在检查更新...", "Close": "关闭", "Close Other Tabs": "关闭其他标签页", "Close Tab": "关闭标签页", "Close Tabs to the Right": "关闭右侧标签页", "Close Window": "关闭窗口", "Collapse All": "全部折叠", "Command Palette": "命令面板", "Connect to WSL": "连接到 WSL", "Copy": "复制", "Copy Content": "复制内容", "Copy File Path": "复制文件路径", "Copy Image": "复制图片", "Copy Image Address": "复制图片地址", "Copy Link": "复制链接", "Copy Path": "复制路径", "Copy Project ID": "复制项目 ID", "Copy Project Name": "复制项目名称", "Copy Relative Path": "复制相对路径", "Cut": "剪切", "Default": "默认", "Delete": "删除", "Delete Project": "删除项目", "Docs": "文档", "Documentation": "文档", "Download": "下载", "Downloading Update...": "正在下载更新...", "Edit": "编辑", "Every command requires approval.": "每条命令都需要批准。", "Expand All": "全部展开", "Extensions": "扩展", "File": "文件", "Find in Pane": "在面板中查找", "Force Reload": "强制重新加载", "Forward": "前进", "Give Feedback": "提供反馈", "Help": "帮助", "Hide Antigravity": "隐藏 Antigravity", "Hide Others": "隐藏其他", "Inspect Element": "检查元素", "Keyboard Shortcuts": "键盘快捷键", "Mark as Read": "标记为已读", "Mark as Unread": "标记为未读", "Maximize": "最大化", "Minimize": "最小化", "Move Conversation Down": "下移对话", "Move Conversation Up": "上移对话", "Move to New Window": "移动到新窗口", "New Conversation": "新建对话", "New File": "新建文件", "New Folder": "新建文件夹", "New Tab": "新建标签页", "New Window": "新建窗口", "Next Side Panel Tab": "下一个侧边栏标签", "Open": "打开", "Open Containing Folder": "打开所在文件夹", "Open Link in New Tab": "在新标签页中打开链接", "Open Settings": "打开设置", "Open in Integrated Terminal": "在集成终端中打开", "Open in New Window": "在新窗口中打开", "Paste": "粘贴", "Pin": "置顶", "Previous Side Panel Tab": "上一个侧边栏标签", "Project Settings": "项目设置", "Quit": "退出", "Quit Antigravity": "退出 Antigravity", "Redo": "重做", "Refresh": "刷新", "Relaunch in WSL": "在 WSL 中重新启动", "Reload": "重新加载", "Rename": "重命名", "Reopen Closed Tab": "重新打开已关闭的标签页", "Reopen Locally": "在本地重新打开", "Replace With New": "替换为新建", "Report Issue": "报告问题", "Request Review": "请求审阅", "Reset Zoom": "重置缩放", "Restart to Update": "重启以应用更新", "Reveal in Explorer": "在资源管理器中显示", "Reveal in File Explorer": "在文件资源管理器中显示", "Run all commands without restrictions.": "无限制地运行所有命令。", "Save As": "另存为", "Select All": "全选", "Send Feedback": "发送反馈", "Services": "服务", "Settings": "设置", "Show All": "显示全部", "Show Antigravity": "显示 Antigravity", "Show in File Explorer": "在文件资源管理器中显示", "Show in Folder": "在文件夹中显示", "Split": "分屏", "Split Down": "向下分屏", "Split Right": "向右分屏", "Toggle Developer Tools": "切换开发者工具", "Toggle Full Screen": "切换全屏", "Toggle Maximize Auxiliary Pane": "切换最大化辅助面板", "Toggle Maximize Side Panel": "切换最大化侧边栏", "Toggle Overview Panel": "切换概览面板", "Toggle Side Panel": "切换侧边栏", "Toggle Terminal": "切换终端", "Turbo": "极速", "Turbo mode": "极速模式", "Undo": "撤销", "Unpin": "取消置顶", "Use Global": "使用全局设置", "Use global": "使用全局设置", "View": "视图", "Window": "窗口", "Zoom In": "放大", "Zoom Out": "缩小"};

  function tr(value) {
    if (typeof value !== 'string' || !value) return value;
    if (menuTranslationMap[value]) return menuTranslationMap[value];
    var trimmed = value.trim();
    if (trimmed !== value && menuTranslationMap[trimmed]) return menuTranslationMap[trimmed];
    return value;
  }

  function walkTemplate(items) {
    if (!Array.isArray(items)) return;
    for (var i = 0; i < items.length; i++) {
      var item = items[i];
      if (!item || typeof item !== 'object') continue;
      if (typeof item.label === 'string') item.label = tr(item.label);
      if (typeof item.sublabel === 'string') item.sublabel = tr(item.sublabel);
      if (typeof item.toolTip === 'string') item.toolTip = tr(item.toolTip);
      if (Array.isArray(item.submenu)) walkTemplate(item.submenu);
    }
  }

  function walkMenuItem(item) {
    if (!item || typeof item !== 'object') return;
    if (typeof item.label === 'string') item.label = tr(item.label);
    if (typeof item.sublabel === 'string') item.sublabel = tr(item.sublabel);
    if (typeof item.toolTip === 'string') item.toolTip = tr(item.toolTip);
    if (item.submenu && Array.isArray(item.submenu.items)) {
      item.submenu.items.forEach(walkMenuItem);
    }
  }

  try {
    var electron = require('electron');
    var Menu = electron && electron.Menu;
    if (Menu && Menu.buildFromTemplate && !Menu.__antigravityZh) {
      var originalBuild = Menu.buildFromTemplate;
      Menu.buildFromTemplate = function(template) {
        walkTemplate(template);
        return originalBuild.call(this, template);
      };
      Menu.__antigravityZh = true;
    }
    if (Menu && Menu.setApplicationMenu && !Menu.__antigravityZhSet) {
      var originalSet = Menu.setApplicationMenu;
      Menu.setApplicationMenu = function(menu) {
        if (menu && Array.isArray(menu.items)) menu.items.forEach(walkMenuItem);
        return originalSet.call(this, menu);
      };
      Menu.__antigravityZhSet = true;
    }
    if (Menu && Menu.getApplicationMenu) {
      var current = Menu.getApplicationMenu();
      if (current && Array.isArray(current.items)) current.items.forEach(walkMenuItem);
    }
  } catch (e) {
    console.error('Antigravity zh-CN menu hook failed:', e);
  }
})();
"""


def _clean_install_value(value):
    text = str(value).strip()
    if not text:
        return ""
    if "," in text and text.lower().endswith((",0", ",1")):
        text = text.rsplit(",", 1)[0]
    if text.startswith('"'):
        end = text.find('"', 1)
        if end != -1:
            text = text[1:end]
    elif " /" in text:
        text = text.split(" /", 1)[0]
    text = text.strip().strip('"')
    if os.path.isfile(text):
        return os.path.dirname(text)
    if os.path.isdir(text):
        return text
    return ""


def find_install_root():
    local = os.environ.get("LOCALAPPDATA") or ""
    program_files = os.environ.get("ProgramFiles") or ""
    program_files_x86 = os.environ.get("ProgramFiles(x86)") or ""
    candidates = []
    for base in (
        os.path.join(local, "Programs", "antigravity") if local else "",
        os.path.join(program_files, "Antigravity") if program_files else "",
        os.path.join(program_files_x86, "Antigravity") if program_files_x86 else "",
        os.path.join(local, "Programs", "Antigravity") if local else "",
    ):
        if base:
            candidates.append(base)
    if os.name == "nt":
        try:
            import winreg
            keys = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
            ]
            for hive, path in keys:
                try:
                    with winreg.OpenKey(hive, path) as root:
                        for i in range(winreg.QueryInfoKey(root)[0]):
                            try:
                                name = winreg.EnumKey(root, i)
                                with winreg.OpenKey(root, name) as sub:
                                    try:
                                        display, _ = winreg.QueryValueEx(sub, "DisplayName")
                                    except OSError:
                                        continue
                                    if "antigravity" not in str(display).lower():
                                        continue
                                    for value in ("InstallLocation", "DisplayIcon", "UninstallString"):
                                        try:
                                            raw, _ = winreg.QueryValueEx(sub, value)
                                        except OSError:
                                            continue
                                        candidate = _clean_install_value(raw)
                                        if candidate:
                                            candidates.append(candidate)
                            except OSError:
                                continue
                except OSError:
                    continue
        except ImportError:
            pass
    for candidate in candidates:
        if candidate and os.path.isdir(os.path.join(candidate, "resources")):
            return candidate
    for candidate in candidates:
        if candidate and os.path.isfile(os.path.join(candidate, "Antigravity.exe")):
            return candidate
    return None


def default_dist():
    root = find_install_root()
    if root:
        return os.path.join(root, "resources", "app", "dist")
    local = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return os.path.join(local, "Programs", "antigravity", "resources", "app", "dist")


def is_app_running():
    if os.name != "nt":
        return False
    try:
        out = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq Antigravity.exe"],
            capture_output=True, text=True, timeout=10,
        ).stdout
        return "Antigravity.exe" in out
    except Exception:
        return False


def extract_asar(asar_path, dest_dir):
    with open(asar_path, "rb") as f:
        magic, size, _u1, header_size = struct.unpack("<4I", f.read(16))
        header = json.loads(f.read(header_size).decode("utf-8"))
        base_offset = 8 + size

        def extract_node(node, current_path):
            if not os.path.exists(current_path):
                os.makedirs(current_path)
            for name, info in node.items():
                path = os.path.join(current_path, name)
                if "files" in info:
                    extract_node(info["files"], path)
                elif "offset" in info:
                    f.seek(base_offset + int(info["offset"]))
                    with open(path, "wb") as out:
                        out.write(f.read(int(info["size"])))

        extract_node(header.get("files", {}), dest_dir)


def refresh_app(dist, dry_run):
    app_dir = os.path.dirname(dist)
    resources = os.path.dirname(app_dir)
    asar = os.path.join(resources, "app.asar")
    disabled = asar + ".disabled"
    if not os.path.isfile(asar):
        print("[skip] app.asar not found; using existing extracted app")
        return True
    if dry_run:
        print(f"[dry-run] would move {app_dir}, extract {asar}, then rename it to .disabled")
        return True
    if is_app_running():
        print("[error] Antigravity is running. Quit it completely (including tray), then retry.")
        return False
    old = app_dir + ".old"
    print(f"[update] extracting {asar} -> {app_dir}")
    try:
        if os.path.isdir(old):
            shutil.rmtree(old, ignore_errors=True)
        if os.path.isdir(app_dir):
            os.rename(app_dir, old)
        os.makedirs(app_dir)
        extract_asar(asar, app_dir)
        if not os.path.isfile(os.path.join(app_dir, "dist", "preload.js")):
            raise RuntimeError("preload.js missing after extraction")
        if os.path.exists(disabled):
            os.remove(disabled)
        os.rename(asar, disabled)
        shutil.rmtree(old, ignore_errors=True)
        print("[update] extraction complete")
        return True
    except Exception as e:
        print(f"[error] update failed: {e}")
        if os.path.isdir(old):
            if os.path.isdir(app_dir):
                shutil.rmtree(app_dir, ignore_errors=True)
            try:
                os.rename(old, app_dir)
            except Exception:
                pass
        return False


def read_text(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        return f.read()


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def block_for(js, newline):
    return (BEGIN + newline + js.replace("\n", newline) + newline + END + newline)


def strip_legacy(path, marker, dry_run):
    text = read_text(path)
    if marker not in text:
        return False
    newline = "\r\n" if "\r\n" in text else "\n"
    begin = text.find(BEGIN)
    if begin != -1:
        end = text.find(END, begin)
        if end == -1:
            return False
        end += len(END)
        head, tail = text[:end], text[end:]
    else:
        head, tail = "", text
    removed = 0
    while True:
        index = tail.rfind(marker)
        if index == -1:
            break
        line_start = tail.rfind(newline, 0, index) + 1
        if tail[line_start:index].strip():
            break
        tail = tail[:line_start]
        removed += 1
    if not removed:
        return False
    text = (head + tail).rstrip("\r\n") + newline
    if not dry_run:
        write_text(path, text)
    return True


def apply_block(path, js, dry_run, legacy_marker=""):
    if legacy_marker and strip_legacy(path, legacy_marker, dry_run):
        print(f"[removed legacy] {path}")
    text = read_text(path)
    newline = "\r\n" if "\r\n" in text else "\n"
    block = block_for(js, newline)
    if BEGIN in text:
        start = text.index(BEGIN)
        end = text.find(END, start)
        if end == -1:
            raise RuntimeError("found begin marker but no end marker")
        after = end + len(END)
        while after < len(text) and text[after] in "\r\n":
            after += 1
        text = text[:start] + block + text[after:]
        action = "updated"
    else:
        text = text + newline + newline + block
        action = "appended"
    if not dry_run:
        write_text(path, text)
    return action


def restore_block(path, dry_run):
    text = read_text(path)
    if BEGIN not in text:
        return "clean"
    start = text.index(BEGIN)
    end = text.find(END, start)
    if end == -1:
        raise RuntimeError("found begin marker but no end marker")
    end += len(END)
    while end < len(text) and text[end] in "\r\n":
        end += 1
    newline = "\r\n" if "\r\n" in text else "\n"
    prefix = text[:start]
    removed = 0
    while removed < 2 * len(newline) and prefix.endswith(newline):
        prefix = prefix[:-len(newline)]
        removed += len(newline)
    text = prefix
    if not dry_run:
        write_text(path, text)
    return "restored"


def main():
    parser = argparse.ArgumentParser(description="Antigravity zh-CN translation-only patch")
    parser.add_argument("--dist", default=default_dist(), help="path to resources/app/dist")
    parser.add_argument("--update", action="store_true", help="re-extract app.asar after an Antigravity update")
    parser.add_argument("--restore", action="store_true", help="remove injected translation blocks")
    parser.add_argument("--dry-run", action="store_true", help="show actions without writing")
    parser.add_argument("--print-dist", action="store_true", help="print the detected dist path and exit")
    args = parser.parse_args()

    if args.print_dist:
        print(args.dist)
        return 0

    if args.restore and args.update:
        print("[error] --restore and --update cannot be combined")
        return 2

    print(f"[info] dist: {args.dist}")

    if args.update:
        if not refresh_app(args.dist, args.dry_run):
            return 1
        if not os.path.isdir(args.dist):
            if args.dry_run:
                print("[dry-run] dist does not exist yet; extraction would create it.")
                return 0
            print(f"[error] dist directory not found after update: {args.dist}")
            return 2
    elif not os.path.isdir(args.dist):
        print(f"[error] dist directory not found: {args.dist}")
        print("        Pass --dist, or run --update once Antigravity is installed.")
        return 2
    elif not args.restore:
        asar = os.path.join(os.path.dirname(os.path.dirname(args.dist)), "app.asar")
        if os.path.isfile(asar):
            print("[warn] app.asar exists, which usually means Antigravity was updated.")
            print("       Run with --update to re-extract and re-apply.")
            return 3

    targets = [
        ("preload.js", DOM_JS, "// Antigravity Chinese Localization Engine"),
        ("menu.js", MENU_JS, "// Antigravity Chinese Localization Engine - Menu"),
    ]
    if args.restore:
        for name, _, _ in targets:
            path = os.path.join(args.dist, name)
            if not os.path.isfile(path):
                print(f"[skip] {name} not found")
                continue
            print(f"[{restore_block(path, args.dry_run)}] {path}")
        print("Restart Antigravity to take effect.")
        return 0

    changed = 0
    for name, js, legacy in targets:
        path = os.path.join(args.dist, name)
        if not os.path.isfile(path):
            print(f"[skip] {name} not found: {path}")
            continue
        action = apply_block(path, js, args.dry_run, legacy)
        print(f"[{action}] {path}")
        changed += 1

    if not changed:
        print("[error] neither preload.js nor menu.js found")
        return 1
    if args.dry_run:
        print("Dry run: no files written.")
    else:
        print("Done. Restart Antigravity to apply.")
        print("Rollback: python antigravity_zh.py --restore")
    return 0


if __name__ == "__main__":
    sys.exit(main())
