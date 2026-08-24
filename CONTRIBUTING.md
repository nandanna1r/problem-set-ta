# Contributing

Thanks for improving Problem-Set TA.

## Before opening a change

Use an issue for behavior changes that affect the core contract: source grounding, mode selection, answer withholding in assist mode, or subject scope. Small wording fixes can go directly to a pull request.

## Development

The canonical source is `skills/problem-set-ta/SKILL.md`. Do not maintain separate Claude and OpenAI variants unless a platform incompatibility makes that unavoidable.

After editing, run:

```bash
python scripts/package_skill.py
```

The command validates the required metadata and builds all distribution archives. Do not commit the generated `dist/` directory.

## Behavioral checks

Test at least these prompts in one supported host:

1. A new student invokes initialization without a problem.
2. A student supplies a problem but omits the mode.
3. In assist mode, the student makes a correct step, then an incorrect step.
4. In answer mode, the assistant gives a complete solution with a cited method and sanity check.
5. A request outside the intended quantitative scope does not force an awkward step-checking workflow.

Pull requests should explain which behavior changed and include the prompts used for testing.
