# Twelve-Tone Suite Architecture / 十二音工具代码架构

## English

The Mermaid diagram below shows the main runtime path. GitHub renders it as a diagram.

```mermaid
flowchart TD
    Main["main()\nCreate Tk root window"] --> UI["TwelveToneSuite\nMonochrome workspace"]

    UI --> Input["Tone-row input\nManual / Random / Default / Clear"]
    Input --> MatrixCore["TwelveToneMatrix\nGenerate P / I / R / RI"]
    MatrixCore --> Variants["Sequence variants\nP / I / R / RI"]
    MatrixCore --> MatrixView["Twelve-tone matrix\n12 × 12 grid"]
    MatrixView --> CurrentMatrix["current_matrix\ncurrent_matrix_data"]

    UI --> MusicPanel["Music generation panel\nInstruments / Tempo / Measures / Technique / Emotion"]
    CurrentMatrix --> MusicPanel
    MusicPanel --> Generate["start_workspace_generation()"]
    Generate --> Composer["AdvancedTwelveToneComposer\nrun_with_inputs()"]
    Composer --> Score["create_professional_score()"]
    Score --> Techniques["Emotion expression\nIntelligent phrasing\nNotation humanization"]
    Techniques --> MusicXML["generate_sibelius_files()"]
    MusicXML --> Optimizer["XMLOptimizer\nOptimize and save MusicXML"]
    Optimizer --> Desktop["User Desktop\nprofessional_score_*.xml"]
    Desktop --> OpenSibelius["open -a Sibelius\nOne-click open"]

    UI --> Result["Completion dialog\nShow path / Reveal file / Open in Sibelius"]
    Desktop --> Result

    Legacy["Legacy compatibility modules\nOlder classes retained later in the file"] -.-> MatrixCore
    Legacy -.-> Composer
```

### Main modules

| Module | Responsibility |
| --- | --- |
| `TwelveToneSuite` | Main window, input controls, matrix display, and music-generation entry point |
| `TwelveToneMatrix` | Twelve-tone row and P/I/R/RI transformations |
| `AdvancedTwelveToneComposer` | Creates a score from the matrix and composition settings |
| `EmotionExpressionSystem` | Dynamics and expressive shaping |
| `PhrasingIntelligence` | Phrase-level development and shaping |
| `HandwrittenNotationGenerator` | Humanizes notation details |
| `XMLOptimizer` | Optimizes and writes MusicXML |
| `open_in_sibelius()` | Passes the generated file to Sibelius through the operating system |

### Runtime flow

1. The user enters or randomizes a row in `TwelveToneSuite`.
2. `TwelveToneMatrix` calculates the transformations and matrix.
3. The music-generation panel reads the current matrix and composition settings.
4. `AdvancedTwelveToneComposer` creates a `music21` score.
5. `XMLOptimizer` saves the result to the Desktop.
6. The result dialog can open the XML file in Sibelius.

---

## 中文

下方 Mermaid 图展示桌面程序的主要运行链路，GitHub 会自动将其渲染成架构图。

```mermaid
flowchart TD
    Main["main()\n创建 Tk 根窗口"] --> UI["TwelveToneSuite\n黑白统一工作台"]

    UI --> Input["音列输入\n手动 / 随机 / 默认 / 清空"]
    Input --> MatrixCore["TwelveToneMatrix\n生成 P / I / R / RI"]
    MatrixCore --> Variants["序列变体\nP / I / R / RI"]
    MatrixCore --> MatrixView["十二音矩阵\n12 × 12 网格"]
    MatrixView --> CurrentMatrix["current_matrix\ncurrent_matrix_data"]

    UI --> MusicPanel["音乐生成区\n乐器 / 速度 / 小节 / 技法 / 情感"]
    CurrentMatrix --> MusicPanel
    MusicPanel --> Generate["start_workspace_generation()"]
    Generate --> Composer["AdvancedTwelveToneComposer\nrun_with_inputs()"]
    Composer --> Score["create_professional_score()"]
    Score --> Techniques["情感表达\n智能乐句\n谱面人性化"]
    Techniques --> MusicXML["generate_sibelius_files()"]
    MusicXML --> Optimizer["XMLOptimizer\n优化并保存 MusicXML"]
    Optimizer --> Desktop["用户桌面\nprofessional_score_*.xml"]
    Desktop --> OpenSibelius["open -a Sibelius\n一键打开"]

    UI --> Result["生成完成弹窗\n显示路径 / 桌面显示 / Sibelius"]
    Desktop --> Result

    Legacy["历史兼容模块\n文件后部保留的旧版本类"] -.-> MatrixCore
    Legacy -.-> Composer
```

### 主要模块

| 模块 | 作用 |
| --- | --- |
| `TwelveToneSuite` | 主窗口、输入控件、矩阵展示和音乐生成入口 |
| `TwelveToneMatrix` | 十二音序列与 P/I/R/RI 变换 |
| `AdvancedTwelveToneComposer` | 根据矩阵和作曲参数生成乐谱对象 |
| `EmotionExpressionSystem` | 力度与情感表达处理 |
| `PhrasingIntelligence` | 乐句级的发展与处理 |
| `HandwrittenNotationGenerator` | 谱面细节人性化处理 |
| `XMLOptimizer` | 优化并输出 MusicXML |
| `open_in_sibelius()` | 调用系统命令交给 Sibelius 打开 |

### 运行时数据流

1. 用户在 `TwelveToneSuite` 中输入或随机生成音列。
2. `TwelveToneMatrix` 计算序列变换和矩阵。
3. 音乐生成区读取当前矩阵和作曲参数。
4. `AdvancedTwelveToneComposer` 创建 `music21` 乐谱对象。
5. `XMLOptimizer` 将结果保存到桌面。
6. 用户可从结果窗口调用 Sibelius 打开 XML 文件。
