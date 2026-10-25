# 单文件版本迁移说明 / Migration from the single-file version

## 保留的使用方式

- `python 十二音.py` 继续启动原来的黑白统一工作台。
- 新入口为 `python -m twelve_tone`，安装包后也可运行 `twelve-tone`。
- 保留六种既有作曲策略、钢琴双声部、音域处理和 MusicXML 导出。
- `AdvancedTwelveToneComposer` 的新导入位置为 `twelve_tone.composition.engine`。
- 引擎保留 `generate_matrix()`、`create_professional_score()`、`run_with_inputs()`、`generate_sibelius_files()`；原构造配置属性改由 `composer.settings` 读取。
- 原脚本没有声明稳定的 Python 库 API。内部技法、节奏和乐器法方法现分别位于 `composer.techniques`、`composer.rhythm`、`composer.instrumentation`。

## 拆分与清理

旧实现为 7019 行单文件，多个版本和启动段落交错。当前运行包保留实际主工作台及其生成链路，并按职责拆分。

移除的旧内容：

- 重复的 `TwelveToneAIArchitect` 及开发提示词/路线图窗口；这些文本不等于已实现功能。
- `main()` 之后的多套 `ModernTwelveToneWorkstation`、嵌套启动逻辑及方法热替换。
- 未被主工作台使用的旧 `TwelveToneMatrix` 独立窗口及重复的参数弹窗。
- 未接入主流程的实验性后处理和物理修正片段。
- 仅包含 `pass` 的 `HandwrittenNotationGenerator`。

原文仍可在 [重构前的提交](https://github.com/xudongdai-ai/twelve-tone-suite/tree/2937178daf521ad18ae110762ef273f8be66e404) 中查看；不再将这些片段作为运行依赖加载。

## 明确的行为修正

1. **矩阵完整性**：旧算法强制把逆行写入末行、逆行倒影写入末列，破坏行列完整性。改为统一的矩阵公式；首行始终等于输入音列，每行每列各包含十二个音级。
2. **矩阵标签**：行列按其真实 P/I 移位编号显示，支持首音不是 C 的输入。
3. **输入校验**：导入的 48 种序列必须齐全且各含十二个不同音级；不再静默跳过缺失序列。生成前重新解析当前输入，避免使用修改前的旧矩阵。
4. **演奏法兼容**：旧映射引用了不存在的 `music21.articulations.Fermata` 等类，导致连有效演奏法也无法构造。演奏法放入 `articulations`，装饰音放入 `expressions`，需跨音符的复杂技法暂保留为文本标记。
5. **线程边界**：后台线程只生成乐谱并写入队列；所有 Tk 操作由主线程完成。
6. **文件名**：时间戳增加微秒，减少同一秒内重复导出覆盖文件的情况。
7. **明确输出目录**：API 可传 `output_dir`。用户指定目录失败时直接报告错误；仅默认桌面目录保留回退当前目录的行为。

MusicXML 文件仍需由乐谱软件导入；没有接入远程 AI 服务，也没有实现手写谱面渲染。

## 验证范围

- 标准库 `unittest` 覆盖输入校验、随机矩阵行列完整性、变体、缺失依赖、启动入口、后台任务和系统命令参数。
- 安装 music21 后，测试全部六种策略的总谱生成、每小节时值、MusicXML 解析及回读。
- 可选真实 Tk 测试验证输入、清空、随机、默认、矩阵标签、自定义速度、后台生成和结果状态。
- 重构时额外对比了原主流程与新引擎：六种策略各使用三个随机种子，长笛与钢琴四小节的音高、时值、偏移和休止事件一致。矩阵显示、演奏法及呼吸记号的修正不属于这一等价比较。
- 文件打开命令通过参数测试验证；自动测试不启动或操控 Sibelius。

## English

The original launcher remains supported. Implementation now lives in the `twelve_tone` package, with separate matrix, composition, notation, export and UI modules. Composer configuration is available through `composer.settings`; internal strategy methods have moved to their corresponding services.

Obsolete workstations, developer prompt text, nested startup patches and no-op handwriting code are retained in Git history rather than imported at runtime. Deliberate fixes cover matrix integrity and labels, imported-row validation, correct music21 notation classes, main-thread Tk updates and more precise export filenames. The test suite checks both dependency-free matrix use and MusicXML generation; the real Tk smoke test is opt-in.
