# Problem-Set TA

A source-grounded, plainspoken office-hours assistant for quantitative coursework.

Problem-Set TA supports two explicit modes:

| Mode | What it does |
| --- | --- |
| **Assist mode** | Uses Socratic prompts, checks each step, and withholds the final answer while the student works. |
| **Answer mode** | Gives a complete worked solution, including reasoning and a sanity check. |

The skill is designed for probability and statistics, statistical inference, linear algebra, and quantitative finance. It prefers the student's course materials, then a named textbook, then cited web sources. Its tone is concise and specific: no praise padding or generic chatbot preamble.

## Quick start

1. Install the skill for your AI tool using one of the options below.
2. Start a new conversation and initialize it:

   ```text
   /problem-set-ta initialize
   ```

3. Provide the course, level, and lecture notes or textbook when prompted.
4. For each problem, choose `assist mode` or `answer mode`.

Example:

```text
Assist mode. Using my uploaded lecture notes, help me work through question 3.
```

## Install

Download the latest packaged files from [Releases](https://github.com/nandanna1r/problem-set-ta/releases), or clone the repository:

```bash
git clone https://github.com/nandanna1r/problem-set-ta.git
cd problem-set-ta
```

### ChatGPT and Codex

The repository is an OpenAI plugin as well as a standalone skill.

- **ChatGPT:** once the plugin is published or added to your available plugin directory, install **Problem-Set TA** from the Plugins tab. Invoke it with `@problem-set-ta`, or describe a matching problem and let ChatGPT select it.
- **ChatGPT desktop / Codex:** import the release bundle from the Skills interface where standalone skill import is available.
- **Codex CLI or IDE extension:** copy `skills/problem-set-ta` into a personal or repository skill directory:

  ```bash
  # Personal: available in every repository
  mkdir -p ~/.agents/skills
  cp -R skills/problem-set-ta ~/.agents/skills/problem-set-ta

  # Or repository-scoped
  mkdir -p .agents/skills
  cp -R skills/problem-set-ta .agents/skills/problem-set-ta
  ```

  Invoke it with `$problem-set-ta` or let Codex select it from the description.

See OpenAI's current [skill documentation](https://developers.openai.com/codex/skills) and [plugin documentation](https://developers.openai.com/codex/plugins).

### Claude.ai

1. Download `problem-set-ta.zip` from the latest release.
2. In Claude, go to **Customize > Skills**.
3. Choose **+ Create skill > Upload a skill**, then select the ZIP file.
4. Enable the skill and invoke `/problem-set-ta`, or ask for help with a matching quantitative problem.

Custom skill upload requires code execution and file creation to be enabled. See Anthropic's [custom skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

### Claude Code

Install the same canonical folder as a personal skill:

```bash
mkdir -p ~/.claude/skills
cp -R skills/problem-set-ta ~/.claude/skills/problem-set-ta
```

For a single project, copy it to `.claude/skills/problem-set-ta` instead. Invoke it with `/problem-set-ta`. See the [Claude Code skills documentation](https://code.claude.com/docs/en/slash-commands).

### Other Agent Skills-compatible tools

Point the tool at [`skills/problem-set-ta/SKILL.md`](skills/problem-set-ta/SKILL.md), following that tool's skill installation convention. The skill uses standard `name` and `description` frontmatter and has no runtime dependencies.

## What to expect

The initialization interview asks for:

- subject and course;
- level (introductory, intermediate, or graduate);
- course materials or a named textbook;
- an optional default mode for the session.

If you skip initialization and paste a problem directly, the skill performs a lightweight setup from the available context. It still requires an explicit mode before substantive work.

The host AI needs access to the cited materials. Web search is useful when neither course materials nor a textbook cover a method.

## Repository layout

```text
.
|-- .codex-plugin/plugin.json        OpenAI plugin manifest
|-- skills/problem-set-ta/SKILL.md  Canonical skill source
|-- scripts/package_skill.py        Reproducible release packager
|-- .github/workflows/validate.yml  Validation and release artifacts
`-- README.md
```

There is one canonical `SKILL.md`. Platform packages are generated from it so Claude, ChatGPT, and Codex do not drift apart.

## Build release bundles

Python 3.9 or later is sufficient; there are no third-party dependencies.

```bash
python scripts/package_skill.py
```

This validates the skill and plugin metadata, then writes:

- `dist/problem-set-ta.skill` for skill-aware clients;
- `dist/problem-set-ta.zip` for Claude upload;
- `dist/problem-set-ta-plugin.zip` for the OpenAI plugin package.

## Contributing

Issues and focused pull requests are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing behavior. In particular, preserve the explicit mode boundary and source-grounding requirement unless the proposal deliberately revises the product design.

## Academic use

This tool can explain or solve coursework when asked. Students remain responsible for following their course's collaboration and AI-use policies.

## License

[MIT](LICENSE)
