# Codex Plugin 使用与发布

这个仓库同时是一个 **skills-only Codex Plugin**。插件清单位于
`.codex-plugin/plugin.json`，当前包含一个 Skill：

```text
skills/adaptive-ml-coach/
```

安装插件或 Skill 不会包含尚未发布的下一版本内容，也不会打包学习者本地的
`.local/learner_profile.json`。

## 初学者：从 GitHub 直接安装 Skill

在 Codex 中输入：

```text
Use $skill-installer to install the skill from:
https://github.com/eliot127825-rgb/Adaptive-ml-code-gym/tree/main/skills/adaptive-ml-coach
```

安装完成后新建一个对话，然后输入：

```text
Use $adaptive-ml-coach to assess my level and start my first exercise.
```

如果 Codex 没有立即发现它，请重启 Codex 后再新建对话。

## 已克隆仓库：手动安装 Skill

当前 Codex 的个人 Skill 发现目录是 `$HOME/.agents/skills`。Windows PowerShell
示例：

```powershell
$skillHome = Join-Path $env:USERPROFILE ".agents\skills"
New-Item -ItemType Directory -Force -Path $skillHome
Copy-Item -Recurse -Force `
  .\skills\adaptive-ml-coach `
  (Join-Path $skillHome "adaptive-ml-coach")
```

复制后新建一个 Codex 对话；如果仍未发现，请重启 Codex。

## 维护者：构建 Plugin ZIP

在仓库根目录运行：

```powershell
python scripts/validate_repository.py
python scripts/build_plugin.py
```

产物默认写入：

```text
dist/adaptive-ml-code-gym-plugin-0.2.0.zip
```

ZIP 只包含 `.codex-plugin/` 和 `skills/`。题库由 Skill 发现现有仓库，或在用户
确认目录和网络访问后从公开 V1 仓库初始化。

正式发布前，还应使用官方 `plugin-creator` 的验证器检查仓库根目录或解压后的
插件目录，并在新的 Codex 对话中运行以下代表性请求：

```text
Assess my level before assigning an exercise.
Start me at Starter level without the assessment.
Help me understand the first failing test in my current kata.
```

GitHub Actions 会在每次推送和 Pull Request 时重复执行仓库验证、ZIP 构建和
压缩包完整性检查，并上传名为 `adaptive-ml-code-gym-plugin` 的构建产物。
